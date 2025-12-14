from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    with (PATH_CURRENT / "rts7.htm").open("r", encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')

    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            if not cols:
                continue
            if len(cols) < 2:
                print(cols)
                continue
            # if len(cols) != 2:
            #     continue

            position = cols[0].text.strip()
            if "配置" in position:
                continue    
            circle_name = cols[1].text.strip()
            circle_penname = cols[2].text.strip()
            url_tag = cols[3].find('a')
            if url_tag:
                url = url_tag.get('href').strip().replace('https://web.archive.org/web/20060423161331/', '')
            else:
                url = None
            circle = Circle(
                links = [url] if is_to_add(url) else None,
                position=position,
                aliases=[circle_name],
                pen_names=[circle_penname] if is_to_add(circle_penname) else None,
            )
            circles.append(circle)
    
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        