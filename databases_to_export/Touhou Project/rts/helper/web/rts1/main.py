from pathlib import Path
from db_structs import Circle, is_to_add
from bs4 import BeautifulSoup
import lxml
import json

PATH_CURRENT = Path(__file__).parent


FULLWIDTH = {
 '０': '0','１': '1','２': '2','３': '3','４': '4','５': '5','６': '6','７': '7','８': '8','９': '9','Ａ': 'A','Ｂ': 'B','Ｃ': 'C','Ｄ': 'D','Ｅ': 'E','Ｆ': 'F','Ｇ': 'G','Ｈ': 'H','Ｉ': 'I','Ｊ': 'J','Ｋ': 'K','Ｌ': 'L','Ｍ': 'M','Ｎ': 'N','Ｏ': 'O','Ｐ': 'P','Ｑ': 'Q','Ｒ': 'R','Ｓ': 'S','Ｔ': 'T','Ｕ': 'U','Ｖ': 'V','Ｗ': 'W','Ｘ': 'X','Ｙ': 'Y','Ｚ': 'Z','ａ': 'a','ｂ': 'b','ｃ': 'c','ｄ': 'd','ｅ': 'e','ｆ': 'f','ｇ': 'g','ｈ': 'h','ｉ': 'i','ｊ': 'j','ｋ': 'k','ｌ': 'l','ｍ': 'm','ｎ': 'n','ｏ': 'o','ｐ': 'p','ｑ': 'q','ｒ': 'r','ｓ': 's','ｔ': 't','ｕ': 'u','ｖ': 'v','ｗ': 'w','ｘ': 'x','ｙ': 'y','ｚ': 'z',
}
SUBSTITUTIONS = {
    '～': '〜',
    'ー': '-',
    '－': '-',
    '　': ' ',
    '-': '-',
    '\\u3000': ' ',
    '！': '!',
    '．': '.',
    '·': '.',
}
SUBSTITUTIONS_ALL = {}
SUBSTITUTIONS_ALL.update(FULLWIDTH)
SUBSTITUTIONS_ALL.update(SUBSTITUTIONS)

def is_in_with_subst(str1: str, bigstr: str) -> bool:
    for key, value in SUBSTITUTIONS_ALL.items():
        str1 = str1.replace(key, value)
        bigstr = bigstr.replace(key, value)
    return str1.lower() in bigstr.lower()

if __name__ == '__main__':
    circles: list[Circle] = []

    # Official source
    with (PATH_CURRENT / "rts1.html").open("r", encoding='shift_jis') as f:
        soup = BeautifulSoup(f, 'lxml')

    circles_info = []
    circles_info_used_indices = []
    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows[1:]:
        cols = row.find_all('td') #TODO: rows of different length
        
        circle_name = cols[0].text.strip() if len(cols) > 0 else None
        circle_penname = cols[1].text.strip() if len(cols) > 1 else None
        booth_name = cols[2].text.strip() if len(cols) > 2 else None
        link = cols[3].text.strip() if len(cols) > 3 else None
        comments = cols[4].text.strip() if len(cols) > 4 else None

        if booth_name and "みょふ～会" in booth_name:
            print(f"Found special case circle: {circle_name} booth={booth_name}")
        
        circle_info = {
            "circle_name": circle_name,
            "circle_penname": circle_penname,
            "booth_name": booth_name,
            "links": [link] if is_to_add(link) else [],
            "comments": [comments] if comments else [],
        }

        circle_info["combined"] = f"{circle_info}"
        circles_info.append(circle_info)

        # if "ＭＡＮＩＡ" in circle_info["combined"]:
        #     print(circle_info["combined"])

    # Secondary source
    with (PATH_CURRENT / "rts1_ext.htm").open("r", encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
    table = soup.find_all('table')[-1]
    rows = table.find_all('tr')
    print(f"Found {len(rows)} rows in secondary source")

    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 5:
            continue

        position = cols[0].text.strip()
        circle_name = cols[1].text.strip()
        link_tags = cols[2].find_all('a')
        links = []
        if link_tags:
            links = [a['href'] for a in link_tags if 'href' in a.attrs]
        # Find matching circle in primary source
        circle_info = None
        circle_additional_alias = None
        for index, info in enumerate(circles_info):
            if is_in_with_subst(circle_name, info["combined"]):
                circle_info = info
                circles_info_used_indices.append(index)
                if circle_name not in info["combined"]:
                    circle_additional_alias = circle_name
                break
            
        if circle_info is None:
            # Special cases
            if circle_name == "DRAGIN":
                for index, info in enumerate(circles_info):
                    if is_in_with_subst("ＤＯＲＡＧＩＮ'", info["combined"]):
                        circle_info = info
                        circles_info_used_indices.append(index)
                        circle_additional_alias = circle_name
                        break
            elif circle_name == "twirl-look":
                for index, info in enumerate(circles_info):
                    if is_in_with_subst("twirl-lock", info["combined"]):
                        circle_info = info
                        circles_info_used_indices.append(index)
                        circle_additional_alias = circle_name
                        break
            elif circle_name == 'SeaFox':
                for index, info in enumerate(circles_info):
                    if is_in_with_subst("Sea Fox", info["combined"]):
                        circle_info = info
                        circles_info_used_indices.append(index)
                        circle_additional_alias = circle_name
                        break
            elif circle_name == 'P-MANIA':
                for index, info in enumerate(circles_info):
                    if is_in_with_subst("丁稚↑", info["combined"]):
                        circle_info = info
                        circles_info_used_indices.append(index)
                        circle_additional_alias = circle_name
                        break
            elif circle_name == 'FelisOvum':
                for index, info in enumerate(circles_info):
                    if is_in_with_subst("Felis Ovum", info["combined"]):
                        circle_info = info
                        circles_info_used_indices.append(index)
                        circle_additional_alias = circle_name
                        break
            elif circle_name == 'mistbell':
                for index, info in enumerate(circles_info):
                    if is_in_with_subst("mist bell", info["combined"]):
                        circle_info = info
                        circles_info_used_indices.append(index)
                        circle_additional_alias = circle_name
                        break
            elif circle_name == 'Twinkle Snows':
                # Was not in primary source
                circle_info = {
                    "circle_name": "Twinkle Snows",
                    "circle_penname": "",
                    "booth_name": "",
                    "links": [],
                    "comments": [],
                }
                circle_additional_alias = "Ｔｗｉｎｋｌｅ　Ｓｎｏｗｓ"
            elif circle_name == 'まりおねっと装甲猟兵':
                # Was not in primary source
                circle_info = {
                    "circle_name": "まりおねっと装甲猟兵",
                    "circle_penname": "",
                    "booth_name": "",
                    "links": [],
                    "comments": [],
                }
            elif circle_name == '月黄泉の街':
                # Was not in primary source
                circle_info = {
                    "circle_name": "月黄泉の街",
                    "circle_penname": "",
                    "booth_name": "",
                    "links": [],
                    "comments": [],
                }

        if circle_info is None: # No match found
            print(f"Circle from secondary source not found in primary: {circle_name}")
            break
            continue
        
        circle_links = circle_info["links"]
        if is_to_add(links):
            circle_links.extend(links)
        booth_name = circle_info["booth_name"]
        aliases = [circle_name]
        if is_to_add(booth_name):
            aliases.append(booth_name)
        circle_penname = circle_info["circle_penname"]
            
        comments = circle_info["comments"]
        circle = Circle(
            position=position if is_to_add(position) else None,
            comments=comments if is_to_add(comments) else None,
            links=circle_links if is_to_add(circle_links) else None,
            aliases=aliases,
            pen_names=[circle_penname] if is_to_add(circle_penname) else None,
        )
        circles.append(circle)
    
    # circles.sort(key=lambda c: c.position)
    # List all indices not used from primary source
    unused_indices = [i for i in range(len(circles_info)) if circles_info[i]["circle_name"] and i not in circles_info_used_indices]
    print(f"Unused: {unused_indices}")
    for i in unused_indices:
        info = circles_info[i]
        print(f"Unused circle: {info['combined']}")
    # This revealed some not found circles, let's add them too
    circles.append(Circle(
            position=None,
            aliases=["マリオネット装甲猟兵"],
    ))
    circles.append(Circle(
            position=None,
            aliases=["ＮＥＫＯＧＯＹＡ"],
    ))

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")

        