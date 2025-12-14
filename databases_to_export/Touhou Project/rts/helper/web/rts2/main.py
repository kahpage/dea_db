from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    with (PATH_CURRENT / "rts2.html").open("r", encoding='shift-jis') as f:
        soup = BeautifulSoup(f, 'lxml')

    table = soup.find_all('table')[-1]
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        if not cols:
            continue
        print(cols)
        # if len(cols) != 2:
        #     continue

        position_group = cols[0].text.strip()
        position_num = cols[1].text.strip()
        circle_name = cols[2].text.strip()
        if len(cols) > 3:
            circle_penname = cols[3].text.strip()
        else:
            circle_penname = None

        circle = Circle(
            position=f"{position_group}{position_num}",
            aliases=[circle_name],
            pen_names=[circle_penname] if is_to_add(circle_penname) else None,
        )
        circles.append(circle)
    
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        