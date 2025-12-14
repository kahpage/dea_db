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
    
        table = soup.find('table', class_='wikitable doujininfo')
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) < 4:
                print(f"  Skipping row with insufficient cells {cols=}")
                continue
            if "摊位编号" in cols[0].text:
                print("  Skipping header row")
                continue
            position = cols[0].text.strip()
            circle_name = cols[1].text.strip()
            link_tags = cols[2].find_all('a')
            circle_links = [a['href'] for a in link_tags if 'href' in a.attrs]
            
            circle = Circle(
                position=position,
                aliases=[circle_name],
                links=circle_links if is_to_add(circle_links) else None
            )
            circles.append(circle)
        
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        