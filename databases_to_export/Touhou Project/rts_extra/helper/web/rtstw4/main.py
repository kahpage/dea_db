from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json
import openpyxl

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    for file in sorted(PATH_CURRENT.glob("*.htm"), key=lambda p: p.name):
        print(f"Processing {file.name} ...")
        with file.open("r", encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')
            
        table = soup.find_all("table")[-1]
        rows = table.find_all("tr")[1:]  # Skip header row
        for row in rows:
            cols = row.find_all("td")
            position = cols[0].get_text(strip=True)
            circle_name = cols[1].get_text(strip=True)
            link_tag = cols[2].find("a")
            links = [link_tag['href']] if link_tag else ""
            
            circle = Circle(
                position=position,
                aliases=[circle_name],
                links=links if is_to_add(links) else None,
            )
            circles.append(circle)
        
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        