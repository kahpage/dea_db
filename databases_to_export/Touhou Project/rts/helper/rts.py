# Notes:
# https://reitaisai.com/tw3/
# For all media: https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD

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
    main_page = "https://reitaisai.com/"
    
    if True: # ==== rts1 ====
        name = "rts1"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("1_rts1.jpg",
                   [Source("https://thwiki.cc/%E6%96%87%E4%BB%B6:%E4%BE%8B%E5%A4%A7%E7%A5%AD%E7%AC%AC%E4%B8%80%E5%B1%8A%E6%8F%92%E7%94%BB5.jpg", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.7941391636386!2d139.7214917753278!3d35.55878603669143!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1764927903746!5m2!1sen!2sfr",
                description="大田区産業プラザPiO",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC1%E5%B1%8A%E6%91%8A%E4%BD%8D", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭1", "博麗神社例大祭", "Hakurei Jinja Reitaisai", "Reitaisai 1", "RTS1", "第一回 博麗神社例大祭"],
            dates="2004.04.18",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://jiyugiga.sakura.ne.jp/reitaisai_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://x.com/KOR_jiyugiga/status/1240620466961670145/photo/1", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC1%E5%B1%8A%E6%91%8A%E4%BD%8D (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
                Source("Participating circles (notes): Circles in Tweeter picture / thwiki.cc but not on reitaisai_list: 'Twinkle Snows', 'まりおねっと装甲猟兵', '月黄泉の街', Circles on reitaisai_list but not on thwiki.cc: 'マリオネット装甲猟兵', 'ＮＥＫＯＧＯＹＡ'", (ReliabilityTypes.Doubtful, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts2 ====
        # TODO: urls from thwikicc or https://web.archive.org/web/20050830234407/http://www.reitaisai.com/link.html
        name = "rts2"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("2_rts2.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.8869299207713!2d139.75819397533215!3d35.655157331406656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1765013084604!5m2!1sen!2sfr",
                description="東京都立産業貿易センター浜松町館",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭2", "博麗神社例大祭2", "Hakurei Jinja Reitaisai 2", "Reitaisai 2", "RTS2", "第二回 博麗神社例大祭"],
            dates="2005.05.04",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20050828173158/http://www.reitaisai.com/clist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts3 ====
        name = "rts3"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("3_rts3.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.9144102765254!2d139.71805677533547!3d35.7283234273863!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1765014060173!5m2!1sen!2sfr",
                description="サンシャインシティ 展示ホールD",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭3", "博麗神社例大祭3", "Hakurei Jinja Reitaisai 3", "Reitaisai 3", "RTS3", "第三回 博麗神社例大祭"],
            dates="2006.05.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20060423161331/http://www.reitaisai.com/clist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC3%E5%B1%8A%E6%91%8A%E4%BD%8D (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts4 ====
        name = "rts4"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("rts4.jpg",
            #        [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.9144102765254!2d139.71805677533547!3d35.7283234273863!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1765014060173!5m2!1sen!2sfr",
                description="サンシャインシティ 展示ホールD",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭4", "博麗神社例大祭4", "Hakurei Jinja Reitaisai 4", "Reitaisai 4", "RTS4", "第四回 博麗神社例大祭"],
            dates="2007.05.20",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20070604075910/http://www5b.biglobe.ne.jp/~cck/r4_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC4%E5%B1%8A%E6%91%8A%E4%BD%8D (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts5 ====
        name = "rts5"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("rts5.jpg",
            #        [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト 西4ホール",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC5%E5%B1%8A%E6%91%8A%E4%BD%8D", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭5", "博麗神社例大祭5", "Hakurei Jinja Reitaisai 5", "Reitaisai 5", "RTS5", "第五回 博麗神社例大祭"],
            dates="2008.05.25",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://www5b.biglobe.ne.jp/~cck/list/rei5_list_tu.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC5%E5%B1%8A%E6%91%8A%E4%BD%8D 	2008-05-25 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts6 ====
        name = "rts6"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("6_rts6.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東3・4・5・6ホール",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC6%E5%B1%8A%E6%91%8A%E4%BD%8D/%E3%81%82%EF%BD%9E%E3%81%91%E9%83%A8%E5%88%86", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭6", "博麗神社例大祭6", "Hakurei Jinja Reitaisai 6", "Reitaisai 6", "RTS6", "第六回 博麗神社例大祭"],
            dates="2009.03.08",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): http://www.green.dti.ne.jp/maisan/gensoukyou/reitaisai6_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC6%E5%B1%8A%E6%91%8A%E4%BD%8D/%E3%81%82%EF%BD%9E%E3%81%91%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts7 ====
        name = "rts7"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東2・3・4・5・6ホール",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC7%E5%B1%8A%E6%91%8A%E4%BD%8D/%E3%81%82%EF%BD%9E%E3%81%91%E9%83%A8%E5%88%86", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭7", "博麗神社例大祭7", "Hakurei Jinja Reitaisai 7", "Reitaisai 7", "RTS7", "第七回 博麗神社例大祭"],
            dates="2010.03.14",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): http://www.green.dti.ne.jp/maisan/gensoukyou/reitaisai7_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC7%E5%B1%8A%E6%91%8A%E4%BD%8D/%E3%81%82%EF%BD%9E%E3%81%91%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts8 ====
        name = "rts8"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3・4・5・6ホール",
                sources=[Source("https://web.archive.org/web/20110928120540/http://www.reitaisai.com/circlelists/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭8", "博麗神社例大祭8", "Hakurei Jinja Reitaisai 8", "Reitaisai 8", "RTS8", "第八回 博麗神社例大祭"],
            dates="2011.05.08",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20110928120540/http://www.reitaisai.com/circlelists/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC8%E5%B1%8A%E6%91%8A%E4%BD%8D/%EF%BB%BF%E3%81%82%EF%BD%9E%E3%81%95%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts9 ====
        name = "rts9"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("9_rts9.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3・4・5・6ホール",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC9%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9EM%E9%83%A8%E5%88%86", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭9", "博麗神社例大祭9", "Hakurei Jinja Reitaisai 9", "Reitaisai 9", "RTS9", "第九回 博麗神社例大祭"],
            dates="2012.05.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): http://g-mirror.gptwm.com/reitaisai/reitaisai9_poslist.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC9%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9EM%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="TODO: use list from thwiki.cc to provide circle links too.\nFor more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts10 ====
        name = "rts10"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("10_rts10.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3・4・5・6ホール",
                sources=[Source("https://web.archive.org/web/20130727035307/http://reitaisai.com/list_circle1#circlelist_top", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭10", "博麗神社例大祭10", "Hakurei Jinja Reitaisai 10", "Reitaisai 10", "RTS10", "第十回 博麗神社例大祭"],
            dates="2013.05.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20130727035307/http://reitaisai.com/list_circle1#circlelist_top", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC10%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9EM%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts11 ====
        name = "rts11"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("11_rts11.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3・4・5・6ホール",
                sources=[Source("https://web.archive.org/web/20150316084312/https://reitaisai.com/rts11/rts11/block123", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭11", "博麗神社例大祭11", "Hakurei Jinja Reitaisai 11", "Reitaisai 11", "RTS11", "第十一回 博麗神社例大祭"],
            dates="2014.05.11",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20150316084312/https://reitaisai.com/rts11/rts11/block123", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://web.archive.org/web/20170708043332/https://reitaisai.com/rts11/rts11/block456", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (3): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC11%E5%B1%8A%E6%91%8A%E4%BD%8D/%E3%81%99%EF%BD%9E%E3%81%AD%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)


    if True: # ==== rts12 ====
        name = "rts12"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("12_rts12.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3・4・5・6ホール",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC12%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9EN%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭12", "博麗神社例大祭12", "Hakurei Jinja Reitaisai 12", "Reitaisai 12", "RTS12", "第十二回 博麗神社例大祭"],
            dates="2015.05.10",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20170227062610/http://reitaisai.com/rts12/name-circle", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC12%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9EN%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="TODO: use list from thwiki.cc to provide circle links too.\nFor more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)


    if True: # ==== rts13 ====
        name = "rts13"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("13_rts13.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3・4・5・6ホール",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC13%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9E%E3%81%88%E9%83%A8%E5%88%86", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭13", "博麗神社例大祭13", "Hakurei Jinja Reitaisai 13", "Reitaisai 13", "RTS13", "第十三回 博麗神社例大祭"],
            dates="2016.05.08",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): http://s.reitaisai.com/rts13/block12/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): http://s.reitaisai.com/rts13/block456/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC13%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9E%E3%81%88%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)


    if True: # ==== rts14 ====
        name = "rts14"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("14_rts14.jpg",
                   [Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3・4・5・6ホール",
                sources=[Source("https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC14%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9ES%E9%83%A8%E5%88%86", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭14", "博麗神社例大祭14", "Hakurei Jinja Reitaisai 14", "Reitaisai 14", "RTS14", "第十四回 博麗神社例大祭"],
            dates="2017.05.07",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): http://s.reitaisai.com/rts14/block/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC14%E5%B1%8A%E6%91%8A%E4%BD%8D/A%EF%BD%9ES%E9%83%A8%E5%88%86 (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== rts15 ====
        name = "rts15"
        print(f"Processing {name} ...")
        cover_url = "https://reitaisai.com/rts15/?p=532"

        circles_ = []
        media_ = [
            Medium("15_rts15.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト 東ホール",
                sources=[Source(cover_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭15", "博麗神社例大祭15", "Hakurei Jinja Reitaisai 15", "Reitaisai 15", "RTS15", "第十五回 博麗神社例大祭"],
            dates="2018.05.06",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {cover_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: http://s.reitaisai.com/rts15block/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts16 ====
        name = "rts16"
        print(f"Processing {name} ...")
        cover_url = "https://reitaisai.com/"

        circles_ = []
        media_ = [
            Medium("16_rts16.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト 西ホール",
                sources=[Source(cover_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭16", "博麗神社例大祭16", "Hakurei Jinja Reitaisai 16", "Reitaisai 16", "RTS16", "第十六回 博麗神社例大祭"],
            dates="2019.05.05",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {cover_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: http://s.reitaisai.com/rts16/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts17 ====
        name = "rts17"
        print(f"Processing {name} ...")
        cover_url = "https://reitaisai.com/rts17/?p=519/"

        circles_ = []
        media_ = [
            Medium("17_rts17.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
        ]
        event = Event(
            aliases=["例大祭17", "博麗神社例大祭17", "Hakurei Jinja Reitaisai 17", "Reitaisai 17", "RTS17", "第十七回 博麗神社例大祭"],
            dates="2020.03.22 -> 2020.05.17 -> Cancelled",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {cover_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://reitaisai.com/rts17/?p=222", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("First postpone: https://reitaisai.com/rts17/?p=574", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Cancelled: https://reitaisai.com/rts17/?p=616", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts18 ====
        name = "rts18"
        print(f"Processing {name} ...")
        cover_url = "https://reitaisai.com"

        circles_ = []
        media_ = [
            Medium("18_rts18.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3269.3863784911905!2d138.4034139753016!3d34.97198546860932!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601a361bad3e7279%3A0x119718565bb552e2!2sTwin%20Messe%20Shizuoka!5e0!3m2!1sen!2sfr!4v1764886167746!5m2!1sen!2sfr",
                description="ツインメッセ静岡",
                sources=[Source("https://reitaisai.com/rts18/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭18", "博麗神社例大祭18", "Hakurei Jinja Reitaisai 18", "Reitaisai 18", "RTS18", "第十八回 博麗神社例大祭"],
            dates="2021.03.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://reitaisai.com/rts18/list_1/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: this is also '第一回博麗神社例大祭in静岡'.\nFor more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts19 ====
        name = "rts19"
        print(f"Processing {name} ...")
        cover_url = "https://reitaisai.com"

        circles_ = []
        media_ = [
            Medium("19_rts19.png",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト 東ホール",
                sources=[Source("https://reitaisai.com/rts19/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭19", "博麗神社例大祭19", "Hakurei Jinja Reitaisai 19", "Reitaisai 19", "RTS19", "第十九回 博麗神社例大祭"],
            dates="2022.05.08",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://reitaisai.com/rts19/accepted-circle-list/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts20 ====
        name = "rts20"
        print(f"Processing {name} ...")
        cover_url = "https://reitaisai.com"

        circles_ = []
        media_ = [
            Medium("20_rts20.png",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト 東ホール",
                sources=[Source("https://reitaisai.com/rts20/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭20", "博麗神社例大祭20", "Hakurei Jinja Reitaisai 20", "Reitaisai 20", "RTS20", "第二十回 博麗神社例大祭"],
            dates="2023.05.07",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/rts20/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://reitaisai.com/rts20/place-assign/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts21 ====
        name = "rts21"
        print(f"Processing {name} ...")
        cover_url = "https://reitaisai.com"

        circles_ = []
        media_ = [
            Medium("21_rts21.png",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東4・5・6ホール",
                sources=[Source("https://reitaisai.com/rts21/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭21", "博麗神社例大祭21", "Hakurei Jinja Reitaisai 21", "Reitaisai 21", "RTS21", "第二十一回 博麗神社例大祭"],
            dates="2024.05.03",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/rts21/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://reitaisai.com/rts21/circle-place-assign/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== rts22 ====
        name = "rts22"
        print(f"Processing {name} ...")
        cover_url = "https://reitaisai.com"

        circles_ = []
        media_ = [
            Medium("22_rts22.png",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東3・4・5・6ホール",
                sources=[Source("https://reitaisai.com/rts22/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭22", "博麗神社例大祭22", "Hakurei Jinja Reitaisai 22", "Reitaisai 22", "RTS22", "第二十二回 博麗神社例大祭"],
            dates="2025.05.05",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/rts22/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: https://reitaisai.com/rts22/circle-place-assign/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="For more media, see https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)



    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (ReliabilityTypes.Likely, OriginTypes.External)),
        #         Source("", (ReliabilityTypes.Likely, OriginTypes.External))]
        #         , comments=""),
    ]
    links = ["https://reitaisai.com/", "https://x.com/HakureijinjyaS", "https://www.youtube.com/channel/UCWgWAk02r-HKSYX2h6wnJVA"]

    event_group = EventGroup(
        aliases=["博麗神社例大祭", "例大祭", "Reitaisai", "RTS"],
        events=[],
        media=media,
        links=links,
        comments="Most sources were taken from https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD#15. As on thwiki.cc, several circle count discrepancies exist compared to official sources (not sourced here but can be seen on thwiki.cc)."
    )
    for event_raw in events_raw:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print("Saving rts database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

