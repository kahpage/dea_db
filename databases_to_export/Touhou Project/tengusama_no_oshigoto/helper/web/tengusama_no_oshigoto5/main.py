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

        enabled: bool = False

        tables = soup.find_all("table")
        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 6 or "サークル名" in cols[0].get_text() or not cols[0].get_text(strip=True):
                    print(len(cols), cols)
                    continue

                name = cols[0].get_text(strip=True)
                if name == "天狗様のお仕事５":
                    enabled = True
                    continue
                elif name == "諏訪子ランド２":
                    enabled = False
                    continue
                if not enabled:
                    continue         

                penname = cols[1].get_text(strip=True)
                position = cols[2].get_text(strip=True)

                links = []
                web_tag = cols[3].find("a")
                if web_tag and web_tag.has_attr("href"):
                    links.append(web_tag["href"])
                pixiv_tag = cols[4].find("a")
                if pixiv_tag and pixiv_tag.has_attr("href"):
                    links.append(pixiv_tag["href"])
                twitter_tag = cols[5].find("a")
                if twitter_tag and twitter_tag.has_attr("href"):
                    links.append(twitter_tag["href"])

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
