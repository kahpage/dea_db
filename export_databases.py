# =====================================================================
# Export the databases
# =====================================================================

import shutil
import json
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field
from db_structs import is_eg_db

# =========== User variable definitions ===========

PATH_CURRENT_DIR = Path(__file__).parent
PATH_ROOT = PATH_CURRENT_DIR.parent
PATH_exported = PATH_CURRENT_DIR / "databases_exported"
PATH_databases_to_export = PATH_CURRENT_DIR / "databases_to_export" # databases_to_export/ folder                                 -> Input

DB_FILE_ENCODING = "utf-8"

STATIC_JSON_INDENT: int | None = None # None to remove indent, int otherwise (e.g. 4)

def clean_database_to_event_group(content: dict[str, Any]) -> dict[str, Any]:
    """Retrieve only content relevant to the event list."""
    out_dict: dict[str, Any] = {}
    out_dict["aliases"] = content["aliases"]
    out_dict["events"] = content.get("events", [])
    
    return out_dict

if __name__ == '__main__':
    print("======= EXPORTING DATABASES... =======")
    print(f"{PATH_databases_to_export=}")
    print(f"{PATH_exported=}")

    # ============================================================
    #  Cleaning old exports 
    # ============================================================
    if not PATH_databases_to_export.is_dir():
        print("WARNING: Invalid paths. Please create an empty databases_served/ folder if it is missing.")
        print("Aborted !")
        exit()

    exists_folders: list[Path] = []
    if PATH_exported.is_dir():
        exists_folders.append(PATH_exported)
    
    if exists_folders:
        print(f"====== Clearing old {', '.join(f.stem for f in exists_folders)} folder{'s' if len(exists_folders)>2 else ''}... ======")
        ans = input(f"The content of the following folders will be deleted:\n{'\n'.join(str(folder) for folder in exists_folders)}\nEnter YES to confirm:\n")
        if ans != "YES":
            print("Aborted !")
            exit()
        for folder in exists_folders:
            shutil.rmtree(folder)
            
    PATH_exported.mkdir(parents=True, exist_ok=True)


    # ============================================================
    #  Database indexing
    # ============================================================
    def recursive_database_indexing(folder: Path) -> tuple[dict[str, Any], dict[str, Any]]:
        """Recursive search and database indexer.
        ret[0] = { "@databases": [], "@count": n, subcategory1: {}, subcategory2: {},...}
        ret[1] = { "@databases": {eg1: {eg_db_1}, ...}, "@count": n, subcategory1: {}, subcategory2: {},...}
        """
        index_this_folder: dict[str, Any] = {"@databases": [], "@count": 0}
        eg_db_this_folder: dict[str, Any] = {"@databases": {}, "@count": 0}
        for dir in (dir for dir in folder.iterdir() if dir.is_dir()):
            folder_name = dir.name
            if not is_eg_db(dir): # Normal folder
                index_this_folder[folder_name], eg_db_this_folder[folder_name] = recursive_database_indexing(dir)
                index_this_folder["@count"] += index_this_folder[folder_name]["@count"] # Increase count
                eg_db_this_folder["@count"] += index_this_folder[folder_name]["@count"]
            else: # Database folder
                # try opening eg
                db_file_path = dir / 'event_group.json'
                try:
                    with db_file_path.open("r", encoding="utf-8") as f:
                        content = json.load(f)
                    if not isinstance(content, dict):
                        raise ValueError(f"WARNING: invalid format, invalid described structure in {db_file_path}")
                    if "aliases" not in content:
                        raise ValueError(f"WARNING: invalid format, 'aliases' should be in json file in {db_file_path}")
                    index_this_folder["@databases"].append(dir.name)
                    index_this_folder["@count"] += 1
                    eg_db_this_folder["@databases"][dir.name] = clean_database_to_event_group(content)
                    eg_db_this_folder["@count"] += 1
                    print(f"db file found at {db_file_path}")
                except Exception as ex:
                    print(f"WARNING: json file {db_file_path} 's format is invalid ! ({ex})")
        return index_this_folder, eg_db_this_folder

    def recursive_copy_from_database_index(index: dict[str, Any], root_path_list: list[str] = []) -> None:
        """Copies the databases to databases_served/ and public/databases/ while preserving the folder structure, using the database index"""
        for db_name in index.get("@databases", []):
            # For databases of current folder
            db_folder_path = PATH_databases_to_export / "/".join(root_path_list) / db_name
            db_file_path = db_folder_path / "event_group.json"
            # new_db_file_path = PATH_public_databases  / "/".join(root_path_list) / db_name / "event_group.json" # new path
            new_db_file_path = PATH_exported  / "/".join(root_path_list) / db_name / "event_group.json" # new path
            
            print(f"mkdir {new_db_file_path.parent} for json database ...")
            new_db_file_path.parent.mkdir(parents=True, exist_ok=True)

            # Open event_group.json
            with db_file_path.open("r", encoding="utf-8") as f:
                old_content = json.load(f)
            # Export event_group.json
            with new_db_file_path.open("w+", encoding="utf-8") as f:
                json.dump(old_content, f, ensure_ascii=False, indent=STATIC_JSON_INDENT) # remove indent
            # Export the events too
            for event_alias0 in old_content.get("events", {}):
                with (db_folder_path / f"{event_alias0}.json").open("r", encoding="utf-8") as f:
                    event_content = json.load(f)
                with (new_db_file_path.parent / f"{event_alias0}.json").open("w+", encoding="utf-8") as f:
                    json.dump(event_content, f, ensure_ascii=False, indent=STATIC_JSON_INDENT)

            # # Copy media folder if exists # DEPRECATED
            # new_media_path = PATH_exported  / "/".join(root_path_list) / db_name / "media" # new media path
            # # new_media_path = PATH_served_databases / "/".join(root_path_list) / db_name / "media" # new media path
            # print(f"mkdir {new_media_path} ...")
            # new_media_path.mkdir(parents=True, exist_ok=True)
            # old_media_folder_path = db_folder_path / "media"
            # if old_media_folder_path.exists() and old_media_folder_path.is_dir():
            #     print(f"Running shutil.copytree({old_media_folder_path}, {new_media_path})...")
            #     shutil.copytree(old_media_folder_path, new_media_path, dirs_exist_ok=True)
        
        for subfolder_name in index:
            if subfolder_name not in ["@databases", "@count"]:
                recursive_copy_from_database_index(index[subfolder_name], root_path_list + [subfolder_name])

    print("====== Finding all databases in databases_to_export ... ======")    
    database_index, event_list_index = recursive_database_indexing(PATH_databases_to_export)

    print("====== Copying found databases to databases_served/ ... ======")
    recursive_copy_from_database_index(database_index)
    
    # index_file_path = PATH_static_databases / "database_file_index.json"
    index_file_path = PATH_exported / "database_file_index.json"
    index_file_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Saving index file at {index_file_path}...")
    with index_file_path.open("w+", encoding="utf-8") as f:
        json.dump(database_index, f, ensure_ascii=False, indent=STATIC_JSON_INDENT)
        
    # eg_db_file_path = PATH_static_databases / "event_list_index.json"
    eg_db_file_path = PATH_exported / "event_list_index.json"
    eg_db_file_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Saving event groups database file at {eg_db_file_path}...")
    with eg_db_file_path.open("w+", encoding="utf-8") as f:
        json.dump(event_list_index, f, ensure_ascii=False, indent=STATIC_JSON_INDENT)
    
    # ============================================================
    #  Circle participation index
    # ============================================================
    print("====== Indexing circles ... ======")
    @dataclass
    class ParticipatingCircle: # Circle for that index
        names: list[str] = field(default_factory=list) # aliases & pen_names
        misc: list[str] = field(default_factory=list) # Other fields to search in, e.g. comments

        def get_json(self) -> dict[str, Any]:
            out_dict = {
                "names": self.names,
            }
            if self.misc:
                out_dict["misc"] = self.misc
            return out_dict
        
        def get_compact_json(self) -> list[str]:
            """Returns a compact version of the circle, with only names and event_name."""
            return self.names
    
    # circle_index: list[ParticipatingCircle] = []
    def recursive_circle_index(index: dict[str, Any], root_path_list: list[str] = []) -> tuple[dict[str,Any], dict[str,Any]]:
        """Indexes all participating circles for events, using the database index. Makes a complete and a compacted (only limited fields) index"""
        this_circle_index: dict[str,Any] = {}
        this_circle_compact_index: dict[str,Any] = {}
        for db_name in index.get("@databases", []): # db_name is the eg
            # For databases of current folder
            db_folder_path = PATH_databases_to_export / "/".join(root_path_list) / db_name
            db_file_path = db_folder_path / "event_group.json"

            with db_file_path.open("r+", encoding="utf-8") as f:
                eg_content = json.load(f)

            if "events" not in eg_content or not eg_content["events"]:
                continue
            
            this_circle_index[db_name] = {} # if dict: event_group, if list: event and elems are circles
            this_circle_compact_index[db_name] = {}

            for event_alias0 in eg_content["events"]:
                with (db_folder_path / f"{event_alias0}.json").open("r+", encoding="utf-8") as ef:
                    event = json.load(ef)

                if "aliases" not in event or not event["aliases"]:
                    continue
                if "circles" not in event or not event['circles']:
                    continue
                
                event_circle_index = []
                event_circle_compact_index = []
                for circle in event['circles']:
                    names = []
                    if "aliases" in circle:
                        names.extend(circle["aliases"])
                    if "pen_names" in circle:
                        names.extend(circle["pen_names"])
                    misc = []
                    if "comments" in circle:
                        misc.append(circle["comments"])
                    if "links" in circle and circle["links"]:
                        misc.extend(circle["links"])
                    pc = ParticipatingCircle(names=names,misc=misc)
                    event_circle_index.append(pc.get_json())
                    event_circle_compact_index.append(pc.get_compact_json()) # just a list of names

                    this_circle_index[db_name][ event['aliases'][0] ] = event_circle_index
                    this_circle_compact_index[db_name][ event['aliases'][0] ] = event_circle_compact_index

        for subfolder_name in index:
            if subfolder_name not in ["@databases", "@count"]:
                this_circle_index[subfolder_name], this_circle_compact_index[subfolder_name] = recursive_circle_index(index[subfolder_name], root_path_list + [subfolder_name])
        return this_circle_index, this_circle_compact_index

    circle_index, circle_compact_index = recursive_circle_index(database_index)

    
    def split_json_tree(data, max_items):
        file_index = 1
        item_count = 0
        current_root = {}

        def flush():
            """Yield the current root as a JSON string and reset counters"""
            nonlocal file_index, current_root, item_count
            if item_count == 0:
                return
            yield json.dumps(current_root, ensure_ascii=False, indent=None)
            file_index += 1
            current_root = {}
            item_count = 0

        def ensure_path(path_keys):
            """Ensure nested dicts exist in current_root for the given path, rebuild the path if necessary"""
            node = current_root
            for k in path_keys:
                if k not in node:
                    node[k] = {}
                node = node[k]
            return node

        def traverse(node, path_keys):
            nonlocal item_count
            nonlocal current_root

            if isinstance(node, list): # Circle list i.e. event
                out_list = []
                parent = ensure_path(path_keys[:-1])
                parent[path_keys[-1]] = out_list

                for item in node:
                    if item_count >= max_items:
                        # yield current and reset
                        yield from flush()
                        parent = ensure_path(path_keys[:-1])
                        out_list = []
                        parent[path_keys[-1]] = out_list

                    out_list.append(item)
                    item_count += 1

                    if item_count >= max_items:
                        yield from flush()
                        parent = ensure_path(path_keys[:-1])
                        out_list = []
                        parent[path_keys[-1]] = out_list

            elif isinstance(node, dict): # Subcategory
                for k, v in node.items():
                    yield from traverse(v, path_keys + [k])

            else: # leaf value (not list/dict)
                raise ValueError("Invalid structure: leaf value encountered")

        # Traverse the whole tree
        yield from traverse(data, [])
        yield from flush()

    # === Extensive circle index ===
    CIRCLES_PER_FILE = 10_000 # 10k circles per file
    circle_extensive_index_folder = PATH_exported # in databases_served/
    circle_extensive_index_folder.mkdir(parents=True, exist_ok=True)
    print(f"Saving extensive circle database files in {circle_extensive_index_folder}...")
    extensive_chunk_count = 0
    for i, chunk in enumerate(split_json_tree(circle_index, CIRCLES_PER_FILE)):
        chunk_file_path = circle_extensive_index_folder / f"circle_participation_extensive_index_{i}.json"
        print(f"Writing chunk {i} of size {len(chunk)} characters to {chunk_file_path}...")
        with chunk_file_path.open("w+", encoding="utf-8") as f:
            f.write(chunk)
        extensive_chunk_count += 1
    
    # === Compact circle index ===
    CIRCLES_PER_FILE = 40_000 # 40k circles per file
    circle_compact_index_folder = PATH_exported # in databases_served/
    circle_compact_index_folder.mkdir(parents=True, exist_ok=True)
    print(f"Saving compact circle database files in {circle_compact_index_folder}...")
    compact_chunk_count = 0
    for i, chunk in enumerate(split_json_tree(circle_compact_index, CIRCLES_PER_FILE)):
        chunk_file_path = circle_compact_index_folder / f"circle_participation_compact_index_{i}.json"
        print(f"Writing chunk {i} of size {len(chunk)} characters to {chunk_file_path}...")
        with chunk_file_path.open("w+", encoding="utf-8") as f:
            f.write(chunk)
        compact_chunk_count += 1

    # === Circle index metadata ===
    # Get file sizes
    extensive_total_size = 0
    compact_total_size = 0
    for i in range(0, extensive_chunk_count):
        chunk_file_path = circle_extensive_index_folder / f"circle_participation_extensive_index_{i}.json"
        size = chunk_file_path.stat().st_size
        extensive_total_size += size

    for i in range(0, compact_chunk_count):
        chunk_file_path = circle_compact_index_folder / f"circle_participation_compact_index_{i}.json"
        size = chunk_file_path.stat().st_size
        compact_total_size += size
        
    out_metadata = {
        "extensive_index_chunk_count": extensive_chunk_count,
        "compact_index_chunk_count": compact_chunk_count,
        "extensive_total_size": extensive_total_size,
        "compact_total_size": compact_total_size,
    }

    circle_index_metadata_file_path = PATH_exported / "circle_index_metadata.json"
    print(f"Saving circle index metadata file at {circle_index_metadata_file_path}...")
    with circle_index_metadata_file_path.open("w+", encoding="utf-8") as f:
        json.dump(out_metadata, f, ensure_ascii=False, indent=STATIC_JSON_INDENT)
