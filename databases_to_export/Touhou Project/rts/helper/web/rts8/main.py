from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    for p in sorted(PATH_CURRENT.glob("rts8_*.htm"), key=lambda x: x.name):
        print(f"Processing file {p.name} ...")
        circles_in_file: list[Circle] = []
        with p.open("r", encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')
        
        found_サークルスペース = False
        divs_space = soup.find_all('div', class_='space_01')
        divs_circle = soup.find_all('div', class_='circle_01')
        divs_penname = soup.find_all('div', class_='pn_01')

        print(f"Found {len(divs_space)} spaces, {len(divs_circle)} circles, {len(divs_penname)} pennames.")
        
        for space_div, circle_div, penname_div in zip(divs_space, divs_circle, divs_penname):
            position = space_div.text.strip()
            if "サークルスペース" in position:
                continue

            circle_name = circle_div.text.strip()
            circle_penname = penname_div.text.strip()
            url_tag = circle_div.find('a')
            if url_tag:
                url = url_tag.get('href').strip().replace('https://web.archive.org/web/20110510123421/http://www.reitaisai.com/circlelists/', '')
            else:
                url = None
            circle = Circle(
                links = [url.replace("https://web.archive.org/web/20110123213147/", "")] if is_to_add(url) else None,
                position=position,
                aliases=[circle_name],
                pen_names=[circle_penname] if is_to_add(circle_penname) else None,
            )
            circles_in_file.append(circle)
        circles.extend(circles_in_file)
        print(f"  -> Found {len(circles_in_file)} circles in this file.")
        
    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        