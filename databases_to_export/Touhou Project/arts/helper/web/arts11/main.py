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
            raw = f.read()
        
        m = re.search(r'const data = (\[[^\[]+?\])', raw, re.DOTALL | re.MULTILINE)
        data = json.loads(m.group(1))
        print(f"  Found {len(data)} circles in data.")

        for entry in data:
            position_raw = remove_span(str(entry['space']))
            circle_name_raw = remove_span(str(entry['circlename']))
            circle_penname_raw = remove_span(str(entry['penname']))
            circle_namekana_raw = remove_span(str(entry['circlenamekana']))
            circle_pennamekana_raw = remove_span(str(entry['pennamekana']))

            position = position_raw.strip()
            circle_name = circle_name_raw.strip()
            circle_namekana = circle_namekana_raw.strip()
            circle_penname = circle_penname_raw.strip()
            circle_pennamekana = circle_pennamekana_raw.strip()
            circle_links = []
            web_raw = str(entry['web']).strip()
            pixiv_raw = str(entry['pixiv']).strip()
            twitter_raw = str(entry['twitter']).strip()
            if is_to_add(web_raw):
                circle_links.append(web_raw)
            if is_to_add(pixiv_raw):
                circle_links.append(f"https://www.pixiv.net/en/users/{pixiv_raw}")
            if is_to_add(twitter_raw):
                circle_links.append(f"https://twitter.com/{twitter_raw}")
            circle = Circle(
                position=position,
                aliases=[circle_name],
                pen_names=[circle_penname] if is_to_add(circle_penname) else None,
                links=circle_links,
                comments=f"Name Kana: {circle_namekana}" + (f", Pen Name Kana: {circle_pennamekana}" if is_to_add(circle_pennamekana) else "")
            )
            circles.append(circle)
        
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        