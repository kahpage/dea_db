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

def clean_link(link: str) -> str:
    # remove web.archive.org prefix if exists
    return re.sub(r'^https?://web\.archive\.org/web/\d+/', '', link)

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = []

    circles_raw = [
        ("G-33","ネガティブフィードバック","CHI-TA/arctan_P","1"),
        ("G-34","【O/N/E/A】-オネア-","いっさん","1"),
        ("G-35","M31","ヤミ","1"),
        ("G-36","在名古屋極東ローマ帝国総領事館","手布部","1"),
        ("G-37","Silent-Jadeite*Crown","音無乖 水無月燐","1"),
    ]
    for i in range(len(circles_raw)):
        position, name, penname, _ = circles_raw[i]
        circle = Circle(
            position=position,
            aliases=[name],
            pen_names=[penname] if is_to_add(penname) else None,
            links=[]
        )
        circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        