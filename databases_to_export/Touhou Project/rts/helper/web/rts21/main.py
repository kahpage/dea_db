from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json
import re

PATH_CURRENT = Path(__file__).parent

def remove_span(txt: str) -> str:
    """Remove <span> tags from the text."""
    txt = re.sub(r"<span class='is-hidden'>\d*</span>", '', txt)
    return txt

if __name__ == '__main__':
    circles: list[Circle] = []

    with (PATH_CURRENT / "rts21.htm").open("r", encoding='utf-8') as f:
        raw_content = f.read()

    re_data = re.compile(r'const data = (\[.*?\}\])', re.DOTALL + re.MULTILINE)
    match = re_data.findall(raw_content)
    if match:
        data_json = match[0]
        data = json.loads(data_json)
        for entry in data:
            circle_name = remove_span(entry.get("circlename", "").strip())
            circle_penname = remove_span(entry.get("penname", "").strip())
            circle_namekana = remove_span(entry.get("circlenamekana", "").strip())
            circle_pennamekana = remove_span(entry.get("pennamekana", "").strip())
            position = remove_span(entry.get("space", "").strip())
            website = remove_span(entry.get("web", "").strip())
            pixiv = remove_span(str(entry.get("pixiv", "")).strip())
            twitter = remove_span(str(entry.get("twitter", "")).strip())

            comments_list = []
            if circle_namekana:
                comments_list.append(f"Name kana: {circle_namekana}. ")
            if circle_pennamekana:
                comments_list.append(f"Pen name kana: {circle_pennamekana}. ")
            
            links = []
            if website:
                links.append(website)
            if pixiv:
                links.append(f"https://www.pixiv.net/en/users/{pixiv}")
            if twitter:
                links.append(f"https://x.com/{twitter}")

            circle = Circle(
                aliases=[circle_name] if is_to_add(circle_name) else [],
                pen_names=[circle_penname] if is_to_add(circle_penname) else None,
                comments="\n".join(comments_list) if comments_list else None,
                links=links if links else None,
            )
            circles.append(circle)
                
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        