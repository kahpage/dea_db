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
        tables = soup.find_all("table", attrs={"border": "0"})
        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 4 or "サークル名" in cols[0].get_text() or not cols[3].get_text().strip():
                    print(len(cols), cols)
                    continue
            
                name = cols[0].get_text(strip=True)
                penname = cols[1].get_text(strip=True)
                position = cols[3].get_text(strip=True)

                links = []
                web_tag = cols[2].find("a")
                if web_tag and web_tag.has_attr("href"):
                    links.append(web_tag["href"])

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
