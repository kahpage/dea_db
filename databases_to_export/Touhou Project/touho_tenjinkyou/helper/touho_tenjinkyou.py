# Notes:
#

from db_structs import Medium, Circle, Event, EventGroup, Source, ReliabilityTypes, OriginTypes, Location
from pathlib import Path
import json
# from bs4 import BeautifulSoup, Comment
# import re
# import requests
from typing import Any

if __name__ == '__main__':
    save_folder_path = Path(__file__).parent.parent
    events_raw: list[Any] = []

    thwikicc = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E5%A4%A9%E7%A5%9E%E5%93%8D"

    if True: # ==== touho_tenjinkyou 0 ====
        i = 0
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("0_东方天神响0.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20090622084715/http://www.aoboo.jp/tohotenjinkyo/circle.html#", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第0回 東方天神響 前夜祭", "Touhou Tenjinkyou 0 Zenyasai",
                "東方天神響0", "Touhou Tenjinkyou 0"
            ],
            dates="2009.08.30",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20090622084715/http://www.aoboo.jp/tohotenjinkyo/circle.html#", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20100508095604/http://aoboo.jp/tohotenjinkyo/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡21."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 1 ====
        i = 1
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("1_东方天神响1插画2.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("1_top_image.jpg",
                   [Source("https://web.archive.org/web/20090719070410/http://aoboo.jp/tohotenjinkyo/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="illustrated by 美月めいあ（ARANCIO TELA）"),
            Medium("Catalog: https://web.archive.org/web/20100407062254/http://www.aoboo.jp/tohotenjinkyo/tenjinkyo01.html",
                   [Source("https://web.archive.org/web/20100407062254/http://www.aoboo.jp/tohotenjinkyo/tenjinkyo01.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20090622084715/http://www.aoboo.jp/tohotenjinkyo/circle.html#", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第1回 東方天神響", "Touhou Tenjinkyou 1",
                "東方天神響1"
            ],
            dates="2010.01.24",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20090622084715/http://www.aoboo.jp/tohotenjinkyo/circle.html#", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20100508095604/http://aoboo.jp/tohotenjinkyo/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡22."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 2 ====
        i = 2
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("2_542px-东方天神响2插画2.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External)),
                    Source("Credits: https://web.archive.org/web/20100324124013/http://aoboo.jp/tohotenjinkyo/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                    comments="illustrated by CPU（HEXIVISION）"),
            Medium("2_536px-东方天神响2插画1.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20100407162905/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第2回 東方天神響", "Touhou Tenjinkyou 2",
                "東方天神響2"
            ],
            dates="2010.05.23",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20100407162905/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20100612123712/http://aoboo.jp/tohotenjinkyo/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡23."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 3 ====
        i = 3
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("3_top_image_03th.jpg",
                   [Source("https://web.archive.org/web/20100907195136/http://www.aoboo.jp/tohotenjinkyo/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="illustrated by 莞唯カズヒロ （pixyhat）"),
            Medium("3_03th_b02.jpg",
                   [Source("https://web.archive.org/web/20100917081354/http://aoboo.jp/tohotenjinkyo/images/03th_b02.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_03th_b03.jpg",
                   [Source("https://web.archive.org/web/20100917081300/http://aoboo.jp/tohotenjinkyo/images/03th_b03.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_03th_b01.jpg",
                   [Source("https://web.archive.org/web/20100917081248/http://aoboo.jp/tohotenjinkyo/images/03th_b01.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_top_frame.png",
                   [Source("https://web.archive.org/web/20090622084715/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20100917134210/http://aoboo.jp/tohotenjinkyo/images/3th_tenjinkyo_logo.pdf",
                   [Source("https://web.archive.org/web/20100917134210/http://aoboo.jp/tohotenjinkyo/images/3th_tenjinkyo_logo.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20100620092442/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第3回 東方天神響", "Touhou Tenjinkyou 3",
                "東方天神響3"
            ],
            dates="2010.09.05",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20100620092442/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20101213022016/http://aoboo.jp/tohotenjinkyo/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡24."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 4 ====
        i = 4
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("4_top_frame.png",
                   [Source("https://web.archive.org/web/20101019171543/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_4th_top_illust.jpg",
                   [Source("https://web.archive.org/web/20101213014139/http://aoboo.jp/tohotenjinkyo/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="illustrated by りべり・ちよこ （ ありぃすいべりぃ ）"),
            Medium("4_3_pad.jpg",
                [Source("https://web.archive.org/web/20110810113343/http://aoboo.jp/tohotenjinkyo/images/3_pad.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_1_deskmat.jpg",
                [Source("https://web.archive.org/web/20110810113235/http://aoboo.jp/tohotenjinkyo/images/1_deskmat.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20101019171543/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第4回 東方天神響", "Touhou Tenjinkyou 4",
                "東方天神響4"
            ],
            dates="2011.01.23",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20101019171543/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡25."
        )
        event_raw = event.get_json() # TODO: weird offset, but I think 4th is missing indeed. see here https://web.archive.org/web/20110514182830/http://aoboo.jp/tohotenjinkyo/circle_list.html
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 5 ====
        i = 5
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("5_top_frame.png",
                   [Source("https://web.archive.org/web/20110515071514/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("5_5th_top_illust.jpg",
                   [Source("https://web.archive.org/web/20110504022259/http://aoboo.jp/tohotenjinkyo/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20110515071514/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第5回 東方天神響", "Touhou Tenjinkyou 5",
                "東方天神響5"
            ],
            dates="2011.05.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20110515071514/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110514182830/http://aoboo.jp/tohotenjinkyo/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡26."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 6 ====
        i = 6
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("6_top_frame.png",
                   [Source("https://web.archive.org/web/20110718130225/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("6_6th_top_illust.jpg",
                   [Source("https://web.archive.org/web/20110824101702/http://aoboo.jp/tohotenjinkyo/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="illustrated byりべり・ちよこ（ありすぃべりぃ）"),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20110718130225/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第6回 東方天神響", "Touhou Tenjinkyou 6",
                "東方天神響6"
            ],
            dates="2011.09.04",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20110718130225/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110918225541/http://aoboo.jp/tohotenjinkyo/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡27."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 7 ====
        i = 7
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("7_top_frame.png",
                   [Source("https://web.archive.org/web/20120524221554/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("7_7th_top_illust.jpg",
                   [Source("https://web.archive.org/web/20120119001226/http://www.aoboo.jp/tohotenjinkyo/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="illustrated by蘭戸せる（天使の羽）"),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20120524221554/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第7回 東方天神響", "Touhou Tenjinkyou 7",
                "東方天神響7"
            ],
            dates="2012.01.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20120524221554/http://www.aoboo.jp/tohotenjinkyo/circle.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20120416222757/http://aoboo.jp/tohotenjinkyo/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡28."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou sp1 ====
        i = "sp1"
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("8_8th_top_illust.jpg",
                   [Source("https://web.archive.org/web/20120903065901/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="illustrated by 蘭戸せる（ 天使の羽）"),
            Medium("8_top_frame.png",
                   [Source("https://web.archive.org/web/20120903065901/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1767798637467!5m2!1sen!2sfr",
                description="インテックス大阪",
                sources=[Source("https://web.archive.org/web/20120903065901/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "東方天神響SPECIAL～こみ★トレ20回記念特別企画～", "Touhou Tenjinkyou SPECIAL - Comi★Tore 20kai Kinen Tokubetsu Kikaku",
                "東方天神響SPECIAL1", "Touhou Tenjinkyou SPECIAL 1"
            ],
            dates="2012.09.02",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20120903065901/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20120903021604/http://tenjinkyo.web.fc2.com/04circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of こみっくトレジャー20."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 8 ====
        i = 8
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("8_8th_top_illust.jpg",
                   [Source("https://web.archive.org/web/20120903065901/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="illustrated by 蘭戸せる（ 天使の羽）"),
            Medium("8_top_frame.png",
                   [Source("https://web.archive.org/web/20120903065901/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20120903065901/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第8回 東方天神響", "Touhou Tenjinkyou 8",
                "東方天神響8"
            ],
            dates="2012.09.16",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20120903065901/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡30."
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou sp2 ====
        i = "sp2"
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("sp2_SP02_top_illust.jpg",
                   [Source("https://web.archive.org/web/20130125182533/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="SP02 illustrated by はじけ☆あきら（はじけ組っ！）"),
            Medium("9_top_frame.jpg",
                   [Source("https://web.archive.org/web/20130125182533/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1767798637467!5m2!1sen!2sfr",
                description="インテックス大阪",
                sources=[Source("https://web.archive.org/web/20130125182533/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "東方天神響SPECIAL2～こみ★トレ10周年特別企画～", "Touhou Tenjinkyou SPECIAL 2 - Comi★Tore 10th Anniversary Tokubetsu Kikaku",
                "東方天神響SPECIAL2", "Touhou Tenjinkyou SPECIAL 2"
            ],
            dates="2013.01.13",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130125182533/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20121217094752/http://tenjinkyo.web.fc2.com/04circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of こみトレ21."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 9 ====
        i = 9
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("9_09th_top_illust.jpg",
                   [Source("https://web.archive.org/web/20140319103942/http://tenjinkyo.web.fc2.com/images/09th_top_illust.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                    Source("Credits: https://web.archive.org/web/20130125182533/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                    comments="09th illustrated by 隈太郎（くまのもり）"),
            Medium("9_top_frame.jpg",
                   [Source("https://web.archive.org/web/20130125182533/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]), 
            #   
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20130125182533/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第9回 東方天神響", "Touhou Tenjinkyou 9",
                "東方天神響9"
            ],
            dates="2013.01.20",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130125182533/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles, likely incomplete: https://web.archive.org/web/20121217094752/http://tenjinkyo.web.fc2.com/04circle_list.html#01", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡31."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou sp3 ====
        i = "sp3"
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("sp3_sp03_top_illust.jpg",
                   [Source("https://web.archive.org/web/20160505174708/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="SP03 illustrated by 藤乃かごめ（幻葬教団）"),
            Medium("10_top_frame_special.png",
                [Source("https://web.archive.org/web/20130315172610/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1767798637467!5m2!1sen!2sfr",
                description="インテックス大阪",
                sources=[Source("https://web.archive.org/web/20130315172610/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "東方天神響SPECIAL3 ～こみ★トレ22 ニャンニャン企画～", "Touhou Tenjinkyou SPECIAL 3 - Comi★Tore 22 Nyan Nyan Kikaku",
                "東方天神響SPECIAL3", "Touhou Tenjinkyou SPECIAL 3"
            ],
            dates="2013.09.01",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130315172610/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of こみトレ22."
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touho_tenjinkyou 10 ====
        i = 10
        name = f"touho_tenjinkyou{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("10_10th_top_illust.jpg", 
                   [Source("https://web.archive.org/web/20130315172610/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="10th illustrated by 隈太郎（くまのもり）"),
            Medium("10_top_frame_special.png",
                [Source("https://web.archive.org/web/20130315172610/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20502.090269735538!2d130.3545810370608!3d33.5925780439991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3541924d02e6b64b%3A0xb79cd978d2ed54c2!2sMizuho%20PayPay%20Dome%20FUKUOKA!5e0!3m2!1sen!2sfr!4v1767793741898!5m2!1sen!2sfr",
                description="福岡Yahoo! JAPANドーム (Note: now Mizuho PayPay Dome)",
                sources=[Source("https://web.archive.org/web/20130315172610/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "第10回 東方天神響", "Touhou Tenjinkyou 10",
                "東方天神響10"
            ],
            dates="2013.06.09",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130315172610/http://tenjinkyo.web.fc2.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20211204202815/http://tenjinkyo.web.fc2.com/04circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of COMIC CITY福岡32."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    # ==== event group ====
    media = [
        Medium("eg_twittertohoaicon.jpg",
               [Source("https://web.archive.org/web/20100515033633/http://www.aoboo.jp/tohotenjinkyo/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_banner.png",
               [Source("https://web.archive.org/web/20090622074534/http://www.aoboo.jp:80/tohotenjinkyo/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_T1karakusaya.jpg",
               [Source("https://web.archive.org/web/20100917134526/http://aoboo.jp/tohotenjinkyo/t1_04.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_T1masumenos.jpg",
            [Source("https://web.archive.org/web/20100917134427/http://aoboo.jp/tohotenjinkyo/t1_02.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_T1sukancho.jpg",
               [Source("https://web.archive.org/web/20100917134345/http://aoboo.jp/tohotenjinkyo/t1_03.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_T1unpopin.jpg",
               [Source("https://web.archive.org/web/20100917134235/http://aoboo.jp/tohotenjinkyo/t1_06.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_T1chiya.jpg",
               [Source("https://web.archive.org/web/20100917134550/http://aoboo.jp/tohotenjinkyo/t1_05.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_T1_aryisubery.jpg",
               [Source("https://web.archive.org/web/20100917134753/http://aoboo.jp/tohotenjinkyo/t1_01.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_01-s.jpg",
               [Source("https://web.archive.org/web/20110810113358/http://aoboo.jp/tohotenjinkyo/images/t1_2011_01/01-s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_02-s.jpg",
               [Source("https://web.archive.org/web/20110810113411/http://aoboo.jp/tohotenjinkyo/images/t1_2011_01/02-s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_03-s.jpg",
               [Source("https://web.archive.org/web/20110810113217/http://aoboo.jp/tohotenjinkyo/images/t1_2011_01/03-s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_04-s.jpg",
               [Source("https://web.archive.org/web/20110810113227/http://aoboo.jp/tohotenjinkyo/images/t1_2011_01/04-s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_05-s.jpg",
               [Source("https://web.archive.org/web/20110810113434/http://aoboo.jp/tohotenjinkyo/images/t1_2011_01/05-s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_06-s.jpg",
               [Source("https://web.archive.org/web/20110810113153/http://aoboo.jp/tohotenjinkyo/images/t1_2011_01/06-s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_07-s.jpg",
               [Source("https://web.archive.org/web/20110810113507/http://aoboo.jp/tohotenjinkyo/images/t1_2011_01/07-s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_08-s.jpg",
               [Source("https://web.archive.org/web/20110810113158/http://aoboo.jp/tohotenjinkyo/images/t1_2011_01/08-s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_keihin_web_yunomimarisa.jpg",
            [Source("https://web.archive.org/web/20100917075940/http://aoboo.jp/tohotenjinkyo/images/keihin_web_yunomimarisa.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["http://tenjinkyo.web.fc2.com/", "http://aoboo.jp/tohotenjinkyo/", "https://x.com/tohotenjinkyo", "https://twilog.togetter.com/tohotenjinkyo"]

    event_group = EventGroup(
        aliases=[
            "東方天神響", "Touhou Tenjinkyou "
        ],
        events=[],
        media=media,
        links=links,
        comments=None,
        description=None,
    )
    
    # Reorder events and add to event group
    events_raw_sorted = sorted(events_raw, key=lambda er: er['dates'])
    
    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print(f"Saving {Path(__file__).name} database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

