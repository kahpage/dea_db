from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json
import openpyxl
import re

def remove_span(string: str) -> str:
    # use re
    return re.sub(r'<span[^>]*>.*?</span>', r'', string)

def clean_link(link: str) -> str:
    # remove web.archive.org prefix if exists
    return re.sub(r'^https?://web\.archive\.org/web/\d+/', '', link)

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    for file in PATH_CURRENT.glob("*.htm"):
        print(f"Processing {file.name} ...")
        with file.open("rb") as f:
            soup = BeautifulSoup(f, 'lxml')
            
            # div id="post-body-2507171588164250193"
            div = soup.find("div", id="post-body-3830865112486359638")
            tables = div.find_all("table")
            print(f"  Found {len(tables)} tables.")
            for table in tables:
                rows = table.find_all("tr")
                print(f"  Found {len(rows)} rows.")
                for row in rows:
                    cols = row.find_all("td")
                    if len(cols) < 5:
                        print(f"    Skipping row: {row}")
                        continue

                    event = cols[0].get_text(strip=True)
                    if event != "幻想人形祭":
                        print(f"    Skipping row: {row}")
                        continue

                    name = cols[1].get_text(strip=True)
                    block = cols[2].get_text(strip=True)
                    number = cols[3].get_text(strip=True)
                    number_extra = cols[4].get_text(strip=True)
                    position = f"{block}{number}"
                    if number_extra:
                        position += f",{number_extra}"
                    if name:
                        circle = Circle(
                            position=position,
                            aliases=[name],
                        )
                        circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        