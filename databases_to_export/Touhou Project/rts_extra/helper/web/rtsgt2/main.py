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
        
        # Find all tables where <table cellspacing="0">
        tables = soup.find_all("table", attrs={"cellspacing": "0"})
        for table in tables:
            rows = table.find_all("tr") 
            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 4:
                    print(f"  Skipping row with insufficient columns {cols=}")
                    continue

                circle_name = cols[0].get_text(strip=True)
                genre = cols[1].get_text(strip=True)
                circle_penname = cols[2].get_text(strip=True)
                position = cols[3].get_text(strip=True)
                link_tag = cols[0].find("a")
                links = [link_tag['href']] if link_tag else ""
                name_kana = cols[0].get("title", "").strip()                    
                
                comments = []
                if is_to_add(name_kana):
                    comments.append(f"Name Kana: {name_kana}")
                if is_to_add(genre):
                    comments.append(f"Genre: {genre}")
                circle = Circle(
                    position=position,
                    aliases=[circle_name],
                    links=links if is_to_add(links) else None,
                    pen_names=[circle_penname] if is_to_add(circle_penname) else None,
                    comments="\n".join(comments) if comments else None,
                )
                circles.append(circle)
        
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        