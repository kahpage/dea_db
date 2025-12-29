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
                if len(cols) < 4:
                    print(len(cols), cols)
                    continue
            
                position = cols[0].get_text(strip=True)
                name = cols[1].get_text(strip=True)
                penname = cols[2].get_text(strip=True)

                links = []
                web_tag = cols[3].find("a")
                if web_tag and web_tag.has_attr("href"):
                    url = web_tag["href"]
                    # regex: if starts with ./, replace with http://vocaloid-fantasia.com/
                    url = re.sub(r'^\.\/', 'http://vocaloid-fantasia.com/', url)
                    links.append(url)

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


        