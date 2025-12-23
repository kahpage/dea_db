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


PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    # koromu10_1.htm
    for file in sorted(PATH_CURRENT.glob("koromu10_*.htm"), key=lambda p: p.name):
        print(f"Processing {file.name} ...")
        with file.open("r", encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')
        
        table = soup.find("table", attrs={"border": "0"})
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) not in [10, 6]:
                continue
            name = cols[2].get_text(strip=True)
            if "サークル名" in name or name == "":
                continue  # header row

            position = cols[1].get_text(strip=True)
            penname = cols[3].get_text(strip=True)
            links = []
            web_tag = cols[4].find("a")
            if web_tag and web_tag.has_attr("href"):
                links.append(web_tag["href"])
            pixiv_tag = cols[5].find("a")
            if pixiv_tag and pixiv_tag.has_attr("href"):
                links.append(pixiv_tag["href"])
            
            circle = Circle(
                position=position,
                aliases=[name],
                pen_names=[penname] if is_to_add(penname) else None,
                links=links
            )
            circles.append(circle)

    # koromu10other.htm
    print("Processing koromu10other.htm ...")
    with (PATH_CURRENT / "koromu10other.htm").open("r", encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
    table = soup.find("table", attrs={"border": "0"})
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) != 4:
            continue
        position = cols[1].get_text(strip=True)
        if not position.startswith("企業"):
            continue

        name = cols[2].get_text(strip=True)
        links = []
        link_tag = cols[3].find("a")
        if link_tag and link_tag.has_attr("href"):
            links.append(link_tag["href"])
        circle = Circle(
            position=position,
            aliases=[name],
            links=links
        )
        circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        