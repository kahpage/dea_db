from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json
import openpyxl

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    for file in sorted(PATH_CURRENT.glob("*.htm"), key=lambda p: p.name):
        print(f"Processing {file.name} ...")
        with file.open("r", encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')
        # table is table with id=circlelist
        table = soup.find('table', id='circlelist')
        if not table:
            raise RuntimeError(f"No table with id=circlelist found in {file.name}")

        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) < 3:
                print(f"  Skipping row with insufficient cells {cells=}")
                continue
            if "配置SP" in cells[0].text:
                print("  Skipping header row")
                continue
            position = cells[0].text.strip()
            circle_name = cells[1].text.strip()
            circle_penname = cells[2].text.strip()
            link_tag = cells[1].find('a')
            circle_links = [link_tag['href'].replace("https://web.archive.org/web/20130727035307/", "")] if link_tag and 'href' in link_tag.attrs else None
            circle = Circle(
                position=position,
                aliases=[circle_name],
                pen_names=[circle_penname] if is_to_add(circle_penname) else None,
                links=circle_links
            )
            circles.append(circle)
    
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        