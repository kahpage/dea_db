from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json
import openpyxl

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    # Import and read the Excel file
    wb = openpyxl.load_workbook(PATH_CURRENT / "reitaisai9_poslist.xlsx")
    sheet = wb.active
    if not sheet:
        raise RuntimeError("No active sheet found in the Excel file.")

    for row in sheet.iter_rows(min_row=1):
        position = row[0].value
        if not position or "配置" in position:
            continue
        circle_name = row[1].value
        circle_penname = row[2].value
        circle = Circle(
            position=position,
            aliases=[circle_name],
            pen_names=[circle_penname] if is_to_add(circle_penname) else None,
        )
        circles.append(circle)
    
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        