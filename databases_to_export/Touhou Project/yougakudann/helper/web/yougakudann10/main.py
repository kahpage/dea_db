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
    circles_raw: list[tuple[str, str, str]] = [
        ("幺01", "テレピン1000ml", "蒲谷カバヂ"),
        ("幺02", "屑鉄おきば。", "黝無ニッケル"),
        ("幺03", "ゆめうるえ", "空ノ夢子"),
        ("幺04", "月桃プラネタリウム", "宵やま"),
        ("幺05", "as Qool as Qucumber", "瑞々"),
        ("幺06", "七色快男児", "仁科将人"),
        ("幺07", "伊予弁普及之会", "伊予弁"),
        ("幺08", "四葉挿話", "かむいこたん"),
        ("幺09", "れいんぼうてぃー", "ちびねこ"),
        ("幺10", "さかな店", "カジキオニオン"),
        ("樂01", "シャレコーベ草原", "donjuan"),
        ("樂02", "Narcissus", "片岡昴"),
        ("樂03", "土曜日の眠り姫", "神依巫女"),
        ("樂04", "鎖付鉄球工房", "スペキュラム合金"),
        ("樂05", "ちょこふぁん", "すばる"),
        ("樂06", "夢想夏月郷", "翡翠"),
        ("樂07", "みちく茶話会", "茶野みの"),
        ("樂08", "五花八門", "上條紗智"),
        ("樂09", "24G", "おそがみ なぎさ"),
        ("樂10", "メアリアンブルー", "イオ"),
        ("団01", "放課後日和", "ちるろり。"),
        ("団02", "insky.", "鈴けいか"),
        ("団03", "柳瀬川", "ミルキャラ"),
        ("団04", "大盛二丁", "木ノ下さく夜"),
        ("団05", "Sugar and Salt", "しおしお"),
        ("団06", "抹茶雲越パフェ", "つませう"),
        ("団07", "下り安全側線", "赤束子"),
        ("団08", "型K式", "カタケイ"),
    ]
    for position, name, penname in circles_raw:
        circle = Circle(
            position=position,
            aliases=[name],
            pen_names=[penname],
        )
        circles.append(circle)

    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        