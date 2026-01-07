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
        tables = soup.find_all("table")
        print(f"Found {len(tables)} tables.")

        for table in tables:
            rows = table.find_all("tr")
            print(f" Found {len(rows)} rows.")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 5 or "サークル名" in cols[0].get_text() or not cols[1].get_text().strip():
                    print(len(cols), cols)
                    continue
                event = cols[4].get_text(strip=True)
                if event != "3:　ようせいげんき！６":
                    print(event)
                    continue
                name = cols[0].get_text(strip=True).replace("\r", "").replace("\n", "")
                if not name or "サークル名" in name or name == "（五十音順、敬称略）":
                    continue
            
                penname = cols[1].get_text(strip=True).replace("\r", "").replace("\n", "")
                position = cols[2].get_text(strip=True)

                links = []
                web = cols[3].get_text(strip=True)
                if web:
                    links.append(web)

                circle = Circle(
                    position=position,
                    pen_names=[penname],
                    aliases=[name],
                    links=[clean_link(link) for link in links],
                )
                circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        