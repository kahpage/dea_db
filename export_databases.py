# =====================================================================
#  Export the databases
# =====================================================================

import shutil
import json
from pathlib import Path
from typing import Any, TypedDict
from dataclasses import dataclass, field
from db_structs import is_eg_db

PATH_CURRENT_DIR = Path(__file__).parent
PATH_ROOT = PATH_CURRENT_DIR.parent

# =====================================================================
#  User-defined variables
# =====================================================================
PATH_exported = PATH_CURRENT_DIR / "databases_exported"
PATH_databases_to_export = PATH_CURRENT_DIR / "databases_to_export" # databases_to_export/ folder                                 -> Input

DB_FILE_ENCODING = "utf-8"
STATIC_JSON_INDENT: int | None = None # None to remove indent, int otherwise (e.g. 4)

CIRCLE_INDEX_CIRCLES_PER_FILE = 10_000 # 10k circles per file
CIRCLE_COMPACT_INDEX_CIRCLES_PER_FILE = 40_000 # 40k circles per file

# =====================================================================
#  Utilities
# =====================================================================
class RecurIndexResult(TypedDict):
    """Used for typing in recursive_indexing."""
    circle_index: dict[str, Any]         # Circles
    circle_compact_index: dict[str, Any] # Circles (compact)
    event_list_index: dict[str, Any]     # For Event List
    verify_index: dict[str, Any]         # For Verify, event_index but more exhaustive

@dataclass
class ParticipatingCircle: # Circle for that index
    names: list[str] = field(default_factory=list) # aliases & pen_names
    misc: list[str] = field(default_factory=list) # Other fields to search in, e.g. comments

    def get_json(self) -> dict[str, Any]:
        out_dict = {"names": self.names}
        if self.misc:
            out_dict["misc"] = self.misc
        return out_dict
    
    def get_compact_json(self) -> list[str]:
        """Returns a compact version of the circle, with only names and event_name."""
        return self.names
    
    
def split_json_tree(data: dict[str, Any], max_items: int) -> Any:
    """Splits a nested JSON tree into multiple JSON strings, each with up to max_items items in lists.
    Yields JSON strings."""
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

# =====================================================================
#  Step functions
# =====================================================================
def recursive_indexing(folder: Path) -> RecurIndexResult:
    """Recursive search and database indexer."""
    # ===== Initialize indexes =====
    circle_index_here: dict[str, Any] = {}
    circle_compact_index_here: dict[str, Any] = {}
    event_list_index_here: dict[str, Any] = {"@databases": {}, "@count": 0}
    verify_index_here: dict[str, Any] = {"@databases": {}, "@count": 0}

    # ===== Process subfolders =====
    for i, dir in enumerate(dir for dir in folder.iterdir() if dir.is_dir()): # For all dirs
        dirname = dir.name
        if not is_eg_db(dir): # ==== Normal folder ====
            recur_result = recursive_indexing(dir)

            # === Circle indexes (compact and normal) ===
            circle_index_here[dirname] = recur_result["circle_index"]
            circle_compact_index_here[dirname] = recur_result["circle_compact_index"]

            # === Event index ===
            event_list_index_here[dirname] = recur_result["event_list_index"]
            event_list_index_here["@count"] += recur_result["event_list_index"]["@count"] # Increase count
            
            # === Verify index ===
            verify_index_here[dirname] = recur_result["verify_index"]
            verify_index_here["@count"] += recur_result["verify_index"]["@count"] # Increase count
        
        else: # ==== Database folder ====
            print("==== Processing database:", dir)
            path_eg_db = dir / 'event_group.json'
            eg_data: dict[str, Any]
            with path_eg_db.open("r", encoding=DB_FILE_ENCODING) as f:
                eg_data = json.load(f)
            eg_events = eg_data.get("events", [])
            
            # ==== Prepare/eg ====
            # === Circle indexes (compact and normal) ===
            circle_index_events: dict[str, list[Any]] = {}
            circle_compact_index_events: dict[str, list[Any]] = {}
            
            # === Event index ===
            event_list_event_objects: dict[str, dict[str, Any]] = {} # {index:, dates:, circle_count:}
            
            # === Verify index ===
            verify_event_objects: dict[str, dict[str, Any]] = {}

            # ==== Event details ====
            for j, event_name in enumerate(eg_events):
                print("  - Event:", event_name)
                path_event = dir / f"{event_name}.json"
                event_data: dict[str, Any]
                with path_event.open("r", encoding=DB_FILE_ENCODING) as ef:
                    event_data = json.load(ef)
                circles = event_data.get("circles", [])

                # === Circle indexes (compact and normal) ===
                if circles:
                    circle_list_here: list[Any] = []
                    circle_compact_list_here: list[Any] = []
                    for circle in circles:
                        names = []
                        names.extend(circle.get("aliases", []))
                        names.extend(circle.get("pen_names", []))
                        misc = []
                        misc.append(circle.get("comments", ""))
                        misc.extend(circle.get("links", []))

                        pc = ParticipatingCircle(names=names, misc=misc)
                        circle_list_here.append(pc.get_json())
                        circle_compact_list_here.append(pc.get_compact_json())

                    circle_index_events[event_name] = circle_list_here
                    circle_compact_index_events[event_name] = circle_compact_list_here
                    
                # === Event index ===
                circle_count = len(circles) if circles else None
                new_event = {
                    "index": j,
                    "dates": event_data.get("dates", ""),
                    "circle_count": circle_count,
                }
                event_list_event_objects[event_name] = new_event

                # === Verify index ===
                media_raw = event_data.get("media", [])
                media: list[str] = [] # Path only
                for m in media_raw:
                    media.append(m.get("path", ""))
                circles = event_data.get("circles", [])
                location = event_data.get("locations", [None])[0] # First location only
                last_edited = event_data.get("last_edited", None)
                new_event = {
                    "name": event_data["aliases"][0], # First alias
                    "dates": event_data.get("dates", ""),
                }
                if media:
                    new_event["media"] = media 
                if location:
                    new_event["location"] = location
                if circles:
                    new_event["circle_count"] = len(circles)
                if last_edited:
                    new_event["last_edited"] = last_edited
                verify_event_objects[event_name] = new_event

            # ==== Post process ====
            # === Circle indexes (compact and normal) ===
            circle_index_here[dir.name] = circle_index_events
            circle_compact_index_here[dir.name] = circle_compact_index_events

            # === Event index ===
            eg_object = {
                "aliases": eg_data.get("aliases", []),
                "events": event_list_event_objects,
            }
            # Last edited
            eg_last_edited = eg_data.get("last_edited", None)
            if eg_last_edited:
                eg_object["last_edited"] = eg_last_edited
            
            event_list_index_here["@databases"][dir.name] = eg_object
            event_list_index_here["@count"] += len(eg_events)

            # === Verify index ===
            verify_eg_media = []
            for m in eg_data.get("media", []):
                media_path = m.get("path", "")
                if media_path:
                    verify_eg_media.append(media_path)
            eg_object = {
                "name": eg_data["aliases"][0], # First alias
                "events": verify_event_objects,
                "media": verify_eg_media, # Path only
                "links": eg_data.get("links", []),
            }
            verify_index_here["@databases"][dir.name] = eg_object
            verify_index_here["@count"] += 1

    # ===== Return =====
    result = RecurIndexResult(
        circle_index=circle_index_here,
        circle_compact_index=circle_compact_index_here,
        event_list_index=event_list_index_here,
        verify_index=verify_index_here,
    )
    return result

# =====================================================================
#  Main script
# =====================================================================
if __name__ == '__main__':
    # ===== Main execution =====
    print("======= EXPORTING DATABASES... =======")
    print(f"{PATH_databases_to_export=}")
    print(f"{PATH_exported=}")

    # ===== Cleaning old exports =====
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
            
    # ===== Create folders =====
    PATH_exported.mkdir(parents=True, exist_ok=True)

    # ===== Indexes =====
    print("====== Generating indexes... ======")
    recur_indexes = recursive_indexing(PATH_databases_to_export)

    circle_index = recur_indexes["circle_index"]
    circle_compact_index = recur_indexes["circle_compact_index"]
    event_list_index = recur_indexes["event_list_index"]
    verify_index = recur_indexes["verify_index"]

    # ===== Export indexes =====
    print("====== Exporting indexes... ======")
    # === Circle indexes (compact and normal) ===
    print("Exporting circle index...")
    circle_extensive_index_folder = PATH_exported # in databases_exported/
    circle_extensive_index_folder.mkdir(parents=True, exist_ok=True)
    print(f"Saving extensive circle database files in {circle_extensive_index_folder}...")
    extensive_chunk_count = 0
    for i, chunk in enumerate(split_json_tree(circle_index, CIRCLE_INDEX_CIRCLES_PER_FILE)):
        chunk_file_path = circle_extensive_index_folder / f"circle_participation_extensive_index_{i}.json"
        print(f"Writing chunk {i} of size {len(chunk)} characters to {chunk_file_path}...")
        with chunk_file_path.open("w+", encoding="utf-8") as f:
            f.write(chunk)
        extensive_chunk_count += 1
    
    print("Exporting compact circle index...")
    circle_compact_index_folder = PATH_exported # in databases_exported/
    circle_compact_index_folder.mkdir(parents=True, exist_ok=True)
    print(f"Saving compact circle database files in {circle_compact_index_folder}...")
    compact_chunk_count = 0
    for i, chunk in enumerate(split_json_tree(circle_compact_index, CIRCLE_COMPACT_INDEX_CIRCLES_PER_FILE)):
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

    # === Event index ===
    print("Exporting event list index...")
    path_event_list_index = PATH_exported / "event_list_index.json"
    with path_event_list_index.open("w", encoding=DB_FILE_ENCODING) as ef:
        json.dump(event_list_index, ef, indent=STATIC_JSON_INDENT, ensure_ascii=False)
    # === Verify index ===
    print("Exporting verify index...")
    path_verify_index = PATH_exported / "verify_index.json"
    with path_verify_index.open("w", encoding=DB_FILE_ENCODING) as vf:
        json.dump(verify_index, vf, indent=STATIC_JSON_INDENT, ensure_ascii=False)
    
    print("======= EXPORT COMPLETE =======")