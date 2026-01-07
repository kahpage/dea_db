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
                if len(cols) < 4 or "サークル名" in cols[0].get_text():
                    print(len(cols), cols)
                    continue
            
                name = cols[0].get_text(strip=True)
                if not name:
                    continue
                penname = cols[1].get_text(strip=True)
                position = cols[2].get_text(strip=True)

                links = []
                web_tag = cols[3].find("a")
                if web_tag and "href" in web_tag.attrs:
                    links.append(web_tag.get("href"))

                circle = Circle(
                    position=position,
                    pen_names=[penname],
                    aliases=[name],
                    links=[clean_link(link) for link in links] if is_to_add(links) else None,
                )
                circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        