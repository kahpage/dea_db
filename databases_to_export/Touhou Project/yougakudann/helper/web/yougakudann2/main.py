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
            
            container = soup.find_all("div", class_="date-outer")[1]
            divs = container.find_all("div", class_="post-body entry-content")
            print(f"  Found {len(divs)} divs.")
            for div in divs:
                # Split div content between <br> tags (handle <br>, <br/> and <br />)
                contents_html = div.encode_contents().decode('utf-8')
                parts = re.split(r'<br\s*/?>', contents_html, flags=re.IGNORECASE)
                contents_cleaned = [c.strip() for c in parts if c.strip()]
                print(contents_cleaned)
                # Allow an optional non-digit marker (e.g. 幺 or 団) before the position
                regex = re.compile(
                    r"^(?P<position>\s*(?:[^\d\s\u3000]+)?\s*\d+(?:\.\d+)?)[\s\u3000]+"
                    r"(?:<a[^>]*href=[\'\"](?P<href>[^\'\"]+)[\'\"][^>]*>"
                    r"(?P<name>.*?)</a>|(?P<name_plain>[^<\r\n]+))",
                    re.UNICODE | re.DOTALL,
                )
                for content in contents_cleaned:
                    match = regex.match(content)
                    if not match:
                        print(f"    Skipping content: {content}")
                        continue
                    position = match.group("position").strip()
                    name = match.group("name") or match.group("name_plain")
                    name = remove_span(name).strip()
                    link = match.group("href")
                    links = [link] if link else []
                    circle = Circle(
                        position=position,
                        aliases=[name],
                        links=[clean_link(link) for link in links],
                    )
                    circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        