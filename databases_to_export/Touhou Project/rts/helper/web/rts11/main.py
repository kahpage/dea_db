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
        tables = soup.find_all('table', class_='circlelist')
        if not tables:
            raise RuntimeError(f"No table with id=circlelist found in {file.name}")

        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) < 4:
                    print(f"  Skipping row with insufficient cells {cells=}")
                    continue
                if "配置SP" in cells[0].text:
                    print("  Skipping header row")
                    continue
                position = cells[0].text.strip()
                circle_name = cells[1].text.strip()
                circle_penname = cells[2].text.strip()
                link_tags = cells[3].find_all('a')
                circle_links = [a['href'].replace("https://web.archive.org/web/20170708043332/", "").replace("https://web.archive.org/web/20150316084312/", "")  for a in link_tags if 'href' in a.attrs]
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

        