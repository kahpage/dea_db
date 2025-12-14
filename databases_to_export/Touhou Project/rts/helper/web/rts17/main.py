from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    with (PATH_CURRENT / "rts17.htm").open("r", encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')

    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 2:
            continue

        circle_name = cols[0].text.strip()
        circle_penname = cols[1].text.strip()

        circle = Circle(
            aliases=[circle_name],
            pen_names=[circle_penname] if is_to_add(circle_penname) else None,
        )
        circles.append(circle)
    
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        