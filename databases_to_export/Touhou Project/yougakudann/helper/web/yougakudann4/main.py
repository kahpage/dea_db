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
            div = soup.find("div", id="post-body-3414980858187852494")
            table = div.find("table")
            rows = table.find_all("tr")
            print(f"  Found {len(rows)} rows.")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 3:
                    print(f"    Skipping row with insufficient columns: {row}")
                    continue
                position = cols[0].get_text(strip=True)
                name = cols[1].get_text(strip=True)
                if not name:
                    print(f"    Skipping row with empty name: {row}")
                    continue

                links = []
                web = cols[2].get_text(strip=True)
                if web:
                    links.append(clean_link(web))
                circle = Circle(
                    position=position,
                    aliases=[name],
                    links=links if is_to_add(links) else None,
                )
                circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        