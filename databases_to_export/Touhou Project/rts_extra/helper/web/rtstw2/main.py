from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json
import openpyxl

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    for file in sorted(PATH_CURRENT.glob("*.csv"), key=lambda p: p.name):
        print(f"Processing {file.name} ...")
        with file.open("r", encoding='utf-8') as f:
            lines = f.readlines()
            
        for line in lines:
            cols = line.strip().split("\t")
            position, circle_name, circle_penname = cols

            circle = Circle(
                position=position,
                aliases=[circle_name],
                pen_names=[circle_penname] if is_to_add(circle_penname) else None,
            )
            circles.append(circle)
        
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        