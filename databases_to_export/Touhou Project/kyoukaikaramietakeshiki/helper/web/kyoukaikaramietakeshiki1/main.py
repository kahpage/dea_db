from pathlib import Path
from db_structs import Circle, is_to_add, Source, Medium, ReliabilityTypes, OriginTypes
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
# Manually from https://web.archive.org/web/20250112160330/http://www.green.dti.ne.jp/maisan/gensoukyou/image/kyoukaikaramietakeshiki.pdf

    circles_dict: dict[str, dict[str, str]] = {} # Section: {pos_num: circle_name}

    # === 部 ===
    circles_dict["部"] = {
        "01": "honey blue",
        "02": "負け橙組",
        "03": "東ガル会",
        "04": "彼之庵",
        "05": "しめさばダイナミック",
        "06": "schwarzwald",
        "07": "ナナシノ十字星団",
        "08": "e-Paranoia",
        "09": "電派絵師団",
        "10": "Lapin Asile",
        "11": "Quarter Iceshop",
        "12": "TUNA-3d",
        "13": "たんしょくごろも",
        "14": "結神亭",
        "15": "匿名天体",
        # "16": "実行委員会用予備スペース"
        "17,18": "冷たい人比良が直せない予感。",
        # "19": "実行委員会用予備スペース"
        "20": "赤色バニラ",
        "21": "ギロチン銀座",
        "22": "8bit canvas",
        "23": "四方山",
        "24": "airdrop",
        "25": "アトリエ桃源郷",
        "26": "sugilight",
        "27": "小豆粥",
        "28": "鏡花水月",
        "29": "RED-SIGHT",
        "30": "アンニュイ赤蛸",
        "31,32": "世界秘封病学会",
    }
    
    # === 楽 ===
    circles_dict["楽"] = {
        "01": "snowfield",
        "02": "あとカフェラテ",
        "03": "アルフ·ライラ",
        "04": "漁火狐火",
        "05": "直VI-DAZE",
        "06": "オリエント鈍行",
        "07": "オレンジペコ",
        "08": "五花八門",
        "09": "Grass Doll",
        "10": "少女リップルズ",
        "11": "ひゃほい帝国",
        "12": "中規模夢想",
        "13": "からしめんたいこ",
        "14": "雪月華",
        "15": "HurrySense",
        "16": "ぐちょまぜ猫貴族",
        # "17": "実行委員会用予備スペース"
        "18": "りべるて",
        "19": "するめぇか。",
        "20": "ペーたんずラボ",
        "21": "二丁目租界",
        "22": "世田谷ボロ市",
        "23": "YUGUPETTI＊",
        "24": "Tsubame yado",
        "25": "SnowGale",
        "26": "Atmosphere theory",
        "27": "豆屋",
        "28": "MEMENT MORI",
        "29": "ハテノハテ星雲",
        "30": "ICBM",
        "31": "桔梗の花の咲くところ",
        "32": "わすれな部屋",
    }
    
    # === 倶 ===
    circles_dict["倶"] = {
        "01": "サクサク",
        "02": "ジョナサン",
        "03": "桜花月間",
        "04": "優戯",
        "05": "海豚の猫拳",
        "06": "春日郷想",
        "07": "無音工房",
        "08": "青茶會談",
        "09": "久幸繙文&幻想ノ郷茶",
        "10": "星空亭",
        "11": "偽薬籠中之月",
        "12": "七月のむじな",
        "13": "卵たつぷり",
        "14": "暮れ雨。",
        "15": "遊星",
        # "16": "準備会スペース",
        "17": "Imitation Room",
        "18": "遙かなる根の国",
        "19": "Wildish...",
        "20": "ラストオーダーはとつ",
        "21": "ネクロユニオン",
        "22": "電気は送れません。",
        "23": "三食角砂糖",
        "24": "とある荒野の休憩所。",
        "25": "アイネクライネ",
        "26": "ぴぽいこしっと",
        "27": "石薔薇十字団",
        "28": "Magic Melancholy",
        "29": "またぽとうほうしぶ",
        "30": "コ館★",
        "31": "ちょこびるる",
        "32": "明日やろう。",
    }
    
    # === 封 ===
    circles_dict["封"] = {
        "01": "天気輪の柱",
        "02": "へひゃい!!",
        "03": "CRiMary",
        "04": "256Diver",
        "05": "まくろびおていか",
        "06": "GKW",
        "07": "Nerd-Goods.com",
        "08": "k@!",
        "09": "草枕文庫",
        "10": "櫻川",
        "11": "ジャム工房",
        "12": "てきとーに",
        "13": "残酷綿棒",
        "14": "RIGHT+LIGHT",
        "15": "零式エルゴ領域",
        "16": "火照るパン",
        "17": "御祭長屋",
        "18": "Rhythm Five",
        "19": "夏色緑茶",
        "20": "雨具文庫",
        "21": "書肆「鰻」",
        "22": "乱蹴ハンス島",
        "23": "つくね書房",
        "24": "川の流れに身を任せ",
        "25": "和服亭",
        "26": "PALMLAP",
        "27": "142本目の紅いリアト",
        "28": "雨降らしの竜",
        "29": "ハスミ書房",
        "30": "あかれんが",
        "31": "BYKエンタープライズ",
        "32": "姫上家",
    }

    # === 秘 ===
    circles_dict["秘"] = {
        "01": "ゴツまさ倶楽部",
        "02": "Forest306 & Sing, R.S",
        "03": "荒御霊",
        "04": "UnLimited Questions",
        "05": "天狗ノ舞",
        "06": "Siestail",
        "07": "まかろに☆けちゃっぷ",
        "08": "Alice Music",
        "09": "UNVALANCE",
        "10": "KARASHIC RECORDS",
        "11": "桃のカンツメ",
        "12": "乃藤悟志",
        "13": "秋の七草",
        "14": "ふじつぼ",
        "15": "トップ派のハット卿",
        "16": "折葉坂三番地",
        "17": "NORTH LEAVE",
        "18": "碧礫亭",
        "19": "極彩色",
        "20": "友毒屋",
        "21": "sweater-girl",
        "22": "THE WATER DUCTS",
        "23": "ゐた·せくすありす",
        "24": "妹音〜Poteto Sou",
        "25": "有限産業すきま風",
        "26": "軍手艦隊",
        "27": "にゃんこの目",
        # "28": "実行委員会用予備スペース"
        # "29": "実行委員会用予備スペース"
        # "30": "実行委員会用予備スペース"
        "31": "うんちく商事",
        "32": "Water.Club.",
        "33": "Ennui Girl's Talk",
        "34": "命の限り好き勝手。",
        "35": "華胥の永眠",
        "36": "ちょいむつ",
        "37": "街角麻婆豆",
        "38": "onionclub",
        "39": "Lunatico",
        "40": "やぁい!",
    }

    circles: list[Circle] = []
    for section in circles_dict:
        for pos_num in circles_dict[section]:
            circle_name = circles_dict[section][pos_num]
            position = f"{section}{pos_num}"

            circles.append(
                Circle(
                    aliases=[circle_name],
                    position=position,
                )
            )


    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        