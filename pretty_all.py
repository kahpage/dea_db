import json
from pathlib import Path

def pretty_print_json(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    json_files = Path(__file__).parent.glob('*.json')
    for json_file in json_files:
        pretty_print_json(json_file)