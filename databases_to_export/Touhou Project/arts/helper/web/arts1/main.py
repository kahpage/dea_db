from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json
import openpyxl

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    for file in sorted(PATH_CURRENT.glob("*.htm"), key=lambda p: p.name):
        print(f"Processing {file.name} ...")
        with file.open("r", encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')

        div = soup.find("div", class_="article_contents")
        current_category = ""

        # iterate over all tags directly under div
        for tag in div.find_all(recursive=False):
            if tag.name == "h3":
                current_category = tag.get_text(strip=True)
            elif tag.name == "table":
                for row in tag.find_all("tr"):
                    cols = row.find_all("td")
                    if len(cols) < 3:
                        continue
                    position = cols[0].get_text(strip=True)
                    circle_name = cols[1].get_text(strip=True)
                    circle_penname = cols[2].get_text(strip=True)
                    circle_url_tags = cols[3].find_all("a")
                    circle_urls = [circle_url_tag['href'].replace("https://web.archive.org/web/20141024075725/","") for circle_url_tag in circle_url_tags if 'href' in circle_url_tag.attrs]

                    circle = Circle(
                        position=position,
                        aliases=[circle_name],
                        pen_names=[circle_penname],
                        links=circle_urls if is_to_add(circle_urls) else None,
                        comments=f"Category: {current_category}"
                    )
                    circles.append(circle)
    
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        