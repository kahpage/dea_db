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
            
            # div id="post-body-2507171588164250193"
            div = soup.find("div", id="post-body-2507171588164250193")
            # Split by <br> tags
            contents_html = div.encode_contents().decode('utf-8')
            parts = re.split(r'<br\s*/?>', contents_html, flags=re.IGNORECASE)
            contents_cleaned = [c.strip() for c in parts if c.strip()]
            print(f"  Found {len(contents_cleaned)} contents.")

            regex = re.compile(r"^(.[\d,]+) (.+)$", re.UNICODE)

            for content in contents_cleaned:
                match = regex.match(content)
                if not match:
                    print(f"    Skipping content: {content}")
                    continue
                position = match.group(1).strip()
                name = match.group(2).strip()

                circle = Circle(
                    position=position,
                    aliases=[name],
                )
                circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        