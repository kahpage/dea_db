from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    with (PATH_CURRENT / "rts16.htm").open("r", encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')

    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 4:
            continue
        if "配置番号" in cols[0].text:
            continue

        position = cols[0].text.strip()
        circle_name = cols[1].text.strip()
        circle_penname = cols[2].text.strip()

        link_tags = cols[3].find_all('a')
        circle_urls: list[str] = []
        if link_tags:
            circle_urls = [a['href'] for a in link_tags if 'href' in a.attrs]

        circle = Circle(
            aliases=[circle_name],
            pen_names=[circle_penname] if is_to_add(circle_penname) else None,
            links=circle_urls if is_to_add(circle_urls) else None,
            position=position if is_to_add(position) else None,
        )
        circles.append(circle)
    
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        