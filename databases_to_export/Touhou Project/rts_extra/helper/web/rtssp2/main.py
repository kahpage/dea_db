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
        
        space_tags = soup.find_all('div', class_='space_01')
        circle_tags = soup.find_all('div', class_='circle_01')
        pen_tags = soup.find_all('div', class_='pn_01')

        for space_tag, circle_tag, pen_tag in zip(space_tags, circle_tags, pen_tags):
            position = space_tag.text.strip()
            circle_name = circle_tag.text.strip()
            circle_penname = pen_tag.text.strip()
            link_tag = circle_tag.find('a')
            circle_links = []
            if link_tag and 'href' in link_tag.attrs:
                link = link_tag['href']
                link = re.sub(r'https://web\.archive\.org/web/\d+/', '', link)
                circle_links = [link]

            circle = Circle(
                position=position,
                aliases=[circle_name],
                pen_names=[circle_penname] if is_to_add(circle_penname) else None,
                links=circle_links if is_to_add(circle_links) else None
            )
            circles.append(circle)
        
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        