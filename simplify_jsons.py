# =====================================================================
# Simplify all JSON files under directory tree.
# =====================================================================

import json
from pathlib import Path
import sys
from typing import Any
from collections.abc import Collection

def RED(text: str) -> str: # AINSI red
    return f"\033[91m{text}\033[0m"
def GREEN(text: str) -> str: # AINSI green
    return f"\033[92m{text}\033[0m"

def recursive_simplify_structure(data: Any) -> Any:
    """Recursively simplify the data structure."""
    if (data is None or 
        isinstance(data, str) or 
        not isinstance(data, Collection)
    ): # Constants
        return data
    else: # Collection
        if len(data) == 0:
            pass
        # Recursion
        if isinstance(data, list):
            new_list = []
            for item in data:
                simplified_item = recursive_simplify_structure(item)
                if simplified_item:
                    new_list.append(simplified_item)
            return new_list
        elif isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                simplified_value = recursive_simplify_structure(value)
                if simplified_value:
                    new_dict[key] = simplified_value
            return new_dict
        else:
            raise ValueError(f"Unsupported data type: {type(data)}")

def simplify_json(path: Path) -> None:
    """Simplify the JSON file at the given path."""
    # Load JSON
    old_size = path.stat().st_size
    with path.open("r", encoding="utf-8") as f:
        data: Any = json.load(f)

    # Simplify data structure
    data_simplified = recursive_simplify_structure(data)

    # Save simplified JSON
    with path.open("w", encoding="utf-8") as f:
        json.dump(data_simplified, f, ensure_ascii=False, indent=None)
    new_size = path.stat().st_size
    if new_size != old_size:
        if new_size < old_size:
            print(GREEN(f"  {old_size} -> {new_size} bytes"))
        else:
            print(RED(f"  {old_size} -> {new_size} bytes"))

if __name__ == '__main__':
    # If path provided in args, use it; otherwise, use current directory
    base_path: Path
    if len(sys.argv) > 1:
        base_path = Path(sys.argv[1])
        if not base_path.is_dir():
            print(f"Provided path {base_path} is not a directory.")
            sys.exit(1)
    else:
        base_path = Path.cwd() / "databases_to_export"

    # Process all JSON files in the directory
    for json_file in base_path.rglob("*.json"):
        print(f"Simplifying {json_file} ...")
        try:
            simplify_json(json_file)
        except Exception as e:
            print(RED(f"  Error: {e}"))
    print("Done.")