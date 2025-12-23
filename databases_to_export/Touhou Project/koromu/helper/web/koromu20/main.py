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

    for file in sorted(PATH_CURRENT.glob("*.htm"), key=lambda p: p.name):
        print(f"Processing {file.name} ...")
        with file.open("r", encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')

        table = soup.find("table", class_="table table-bordered table-hover table-striped")
        rows = table.find_all("tr")[1:]  # skip header row
        for row in rows:
            cols = row.find_all("td")

            hall = cols[0].get_text(strip=True)
            booth = cols[1].get_text(strip=True)
            position = f"{hall} {booth}"

            name = cols[2].get_text(strip=True)
            penname = cols[3].get_text(strip=True)

            links = []
            web_tag = cols[4].find("a")
            if web_tag and web_tag.has_attr("href"):
                links.append(web_tag["href"])
            x_tag = cols[5].find("a")
            if x_tag and x_tag.has_attr("href"):
                links.append(x_tag["href"])
            instagram_tag = cols[6].find("a")
            if instagram_tag and instagram_tag.has_attr("href"):
                links.append(instagram_tag["href"])
            misskey_tag = cols[7].find("a")
            if misskey_tag and misskey_tag.has_attr("href"):
                links.append(misskey_tag["href"])
            bluesky_tag = cols[8].find("a")
            if bluesky_tag and bluesky_tag.has_attr("href"):
                links.append(bluesky_tag["href"])
            pixiv_tag = cols[9].find("a")
            if pixiv_tag and pixiv_tag.has_attr("href"):
                links.append(pixiv_tag["href"])
            skeb_tag = cols[10].find("a")
            if skeb_tag and skeb_tag.has_attr("href"):
                links.append(skeb_tag["href"])

            circle = Circle(
                position=position,
                aliases=[name],
                pen_names=[penname] if is_to_add(penname) else None,
                links=links
            )
            circles.append(circle)
            
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        