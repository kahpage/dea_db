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

    for file in sorted(PATH_CURRENT.glob("*.htm"), key=lambda p: p.name):
        print(f"Processing {file.name} ...")

        with file.open("r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, 'lxml')
        # table with border="1"
        table = soup.find_all("table")[-1]
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 3:
                print(len(cols), cols)
                continue  # skip invalid rows

            name = cols[0].get_text(strip=True)
            penname = cols[1].get_text(strip=True)

            links = []
            web_tag = cols[2].find("a")
            if web_tag and web_tag.has_attr("href"):
                links.append(web_tag["href"])
            twitter_tag = cols[3].find("a")
            if twitter_tag and twitter_tag.has_attr("href"):
                links.append(twitter_tag["href"])
                
            links_cleaned = [clean_link(link) for link in links]
            circle = Circle(
                aliases=[name],
                pen_names=[penname] if is_to_add(penname) else None,
                links=links_cleaned
            )
            circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        