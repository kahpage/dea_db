# Notes, todo:
# ###DONE: https://ketto.com/tvm/*, http://ketto.com/mimiken/clist.cgi*, http://ketto.com/mimiken/alllist.cgi*, https://ketto.xsrv.jp/html/mimiken/*
# - more circle lists, perhaps base on http://ketto.com/tvm/indexX.shtml urls, see from tvm 4 "4_tvm_logo4.gif"
# - find tweeter / other sns
# - tvm34, chou but only 1 medium
# - tvm38 cover + author
# - tvm40,41,43... cover + author
# - position tvm44
# - tvm50 cover
# - tvm52 cover and other 5X covers
# - missing N_tvm_logoN.gif for N=21,26,45-50,54-56

# To save to wayback machine
# - https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm49 & upadte links
# - same for 'circles: https://ketto\.' search

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

    puella = "https://puellabyte.github.io/events"

    if True: # ==== tvm 1 ====
        i = 1
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("1_20071020193402_tvm_logo.gif",
                   [Source("https://web.archive.org/web/20200927183424/https://ketto.com/tvm/index071106.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザ",
                sources=[Source("https://web.archive.org/web/20250619191234/http://npass.net/the_vocloid_mst/", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER",   "ボーマス",  "VOM@S", 
                     "THE VOC＠LOiD M＠STER 1", "ボーマス1", "VOM@S1", "tvm1"],
            dates="2007.11.03",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20071020193402/http://ketto.com/tvm/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20250619191234/http://npass.net/the_vocloid_mst/", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 2 ====
        i = 2
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("2_tvm1hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm2ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],  
                   comments="カタログ表紙イラスト：胡 せんり　様（サークル：うみやませんり）."),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1766761385232!5m2!1sen!2sfr",
                description="神奈川県：川崎市産業振興会館 ４階 企画展示室",
                sources=[Source("https://ketto.com/tvm/tvm2ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 2", "ボーマス2", "VOM@S2", "tvm2"],
            dates="2008.01.13",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm2ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (DEAD): https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm2", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 3 ====
        i = 3
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("3_tvm3hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm3ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="カタログ表紙イラスト：七瀬 葵　様（サークル：姫神）"),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO　1階　大展示ホール 1/3面",
                sources=[Source("https://ketto.com/tvm/tvm3ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 3", "ボーマス3", "VOM@S3", "tvm3"],
            dates="2008.03.23",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm3ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (DEAD): https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm3", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 4 ====
        i = 4
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("4_tvm4hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm4ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="カタログ表紙イラスト：北乃友利　様（サークル：foreheadS）"),
            Medium("4_tvm_logo4.gif",
                   [Source("https://web.archive.org/web/20100102215253/http://ketto.com/tvm/index080630.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO　1階　大展示ホール 1/2面",
                sources=[Source("https://ketto.com/tvm/tvm4ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 4", "ボーマス4", "VOM@S4", "tvm4"],
            dates="2008.06.29",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm4ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110603040450/http://ketto.com/mimiken/alllist.cgi?173", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 5 ====
        i = 5
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("5_tvm5hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm5ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="カタログ表紙イラスト：河井珠蘭　様（サークル：瀬久ノ原）"),
            Medium("5_tvm_logo5.gif",
                   [Source("https://web.archive.org/web/20100102213817/http://ketto.com/tvm/index080925.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO　1階　大展示ホール 全面",
                sources=[Source("https://ketto.com/tvm/tvm5ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 5", "ボーマス5", "VOM@S5", "tvm5"],
            dates="2008.09.23",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm5ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110603040435/http://ketto.com/mimiken/alllist.cgi?183", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 6 ====
        i = 6
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("6_tvm6hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm6ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="カタログ表紙イラスト：ななろば華　様（サークル：祭社）"),
            Medium("6_tvm_logo6.gif",
                   [Source("https://web.archive.org/web/20100102211831/http://ketto.com/tvm/index081202.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.318557480467!2d139.64316731143288!3d35.44690717254969!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc864754fd%3A0xedeb81e0799aefc2!2z5pel5pys44CB44CSMjMxLTAwMjMg56We5aWI5bed55yM5qiq5rWc5biC5Lit5Yy65bGx5LiL55S677yS!5e0!3m2!1sja!2sfr!4v1766762349057!5m2!1sja!2sfr",
                description="横浜産貿ホール マリネリア",
                sources=[Source("https://ketto.com/tvm/tvm6ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 6", "ボーマス6", "VOM@S6", "tvm6"],
            dates="2008.11.30",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm6ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110603034917/http://ketto.com/mimiken/alllist.cgi?186", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 7 ====
        i = 7
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("7_tvm7hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm7ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="カタログ表紙イラスト：桜はんぺん　様（サークル：Petite*Cerisier）"),
            Medium("7_tvm7logo.gif",
                   [Source("https://web.archive.org/web/20100102205055/http://ketto.com/tvm/index090226.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3239.4781867159977!2d139.79620487533484!3d35.71445652814888!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188ec3d981d0f5%3A0x82b2ec9f4699aec6!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Taito%20Building!5e0!3m2!1sen!2sfr!4v1766762586915!5m2!1sen!2sfr",
                description="都立産業貿易センター(台東館)７階",
                sources=[Source("https://ketto.com/tvm/tvm7ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 7", "ボーマス7", "VOM@S7", "tvm7"],
            dates="2009.02.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm7ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20101219163247/http://ketto.com/mimiken/alllist.cgi?191", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 8 ====
        i = 8
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("8_tvm8hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm8ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="カタログ表紙イラスト：伊賀智輝　様（サークル：しかばね工房）"),
            Medium("8_tvm8logo.gif",
                   [Source("https://web.archive.org/web/20100102201852/http://ketto.com/tvm/index090519.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO　1階　大展示ホール 全面",
                sources=[Source("https://ketto.com/tvm/tvm8ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 8", "ボーマス8", "VOM@S8", "tvm8"],
            dates="2009.05.17",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm8ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20101219162923/http://ketto.com/mimiken/alllist.cgi?8", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 9 ====
        i = 9
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("9_tvm9hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm9ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="カタログ表紙イラスト：ながれぼし （サークル：たーみなる☆げん 　配置：A22）"),
            Medium("9_tvm9logo.gif",
                   [Source("https://web.archive.org/web/20100102195507/http://ketto.com/tvm/index090908.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO　1階　大展示ホール 全面",
                sources=[Source("https://ketto.com/tvm/tvm9ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 9", "ボーマス9", "VOM@S9", "tvm9"],
            dates="2009.09.06",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm9ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20101219162826/http://ketto.com/mimiken/alllist.cgi?9", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 10 ====
        i = 10
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("10_tvm10hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm10ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="カタログ表紙イラスト：なぎみそ 様"),
            Medium("10_tvm10logo.gif",
                   [Source("https://web.archive.org/web/20100102193754/http://ketto.com/tvm/index091117.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ文化会館2F展示ホールD-234",
                sources=[Source("https://ketto.com/tvm/tvm10ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]   
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 10", "ボーマス10", "VOM@S10", "tvm10"],
            dates="2009.11.15",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm10ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110603021406/http://ketto.com/mimiken/alllist.cgi?206", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 11 ====
        i = 11
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("11_tvm11hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm11ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            Medium("11_20100102191838_tvm11logo.gif",
                   [Source("https://web.archive.org/web/20100102191838/http://ketto.com/tvm/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("11_tvm11logo.gif",
                   [Source("https://web.archive.org/web/20100102192639/http://ketto.com/tvm/index091202.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("11_tvm11logo_special.gif",
                   [Source("https://web.archive.org/web/20101101084048/http://ketto.com/tvm/index100211.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO　1階　大展示ホール 全面",
                sources=[Source("https://ketto.com/tvm/tvm11ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 11", "ボーマス11", "VOM@S11", "tvm11"],
            dates="2010.02.07",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm11ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20101219161820/http://ketto.com/mimiken/alllist.cgi?61", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 12 ====
        i = 12
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("12_tvm12hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm12ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト： MACCO 様"
                   ),
            Medium("12_tvm_logo12.gif",
                   [Source("https://web.archive.org/web/20100925223517/http://ketto.com/tvm/index100510.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO　1階　大展示ホール 全面",
                sources=[Source("https://ketto.com/tvm/tvm12ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 12", "ボーマス12", "VOM@S12", "tvm12"],
            dates="2010.05.09",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm12ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110520001138/http://ketto.com/mimiken/alllist.cgi?88", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 13 ====
        i = 13
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("13_tvm13hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm13ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト： yamo 様"),
            Medium("13_tvm_logo13.gif",
                   [Source("https://web.archive.org/web/20100925122850/http://ketto.com/tvm/index100803.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="PIO",
                sources=[Source("https://ketto.com/tvm/tvm13ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 13", "ボーマス13", "VOM@S13", "tvm13"],
            dates="2010.07.19",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm13ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110519233819/http://ketto.com/mimiken/alllist.cgi?105", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 14 ====
        i = 14
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("14_tvm14hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm14ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト： 百円ライター 様"),
            Medium("14_tvm_logo14.gif",
                   [Source("https://web.archive.org/web/20101031183408/http://ketto.com/tvm/?e4a1", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ文化会館3F展示ホールC",
                sources=[Source("https://ketto.com/tvm/tvm14ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 14", "ボーマス14", "VOM@S14", "tvm14"],
            dates="2010.11.14",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm14ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110519224318/http://ketto.com/mimiken/alllist.cgi?145", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 15 ====
        i = 15
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("15_tvm15hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm15ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト： 田村ヒロ 様"),
            Medium("15_tvm_logo15.gif",
                   [Source("https://web.archive.org/web/20110519220635/http://ketto.com/tvm/index20110130.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ文化会館2F展示ホールD",
                sources=[Source("https://ketto.com/tvm/tvm15ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 15", "ボーマス15", "VOM@S15", "tvm15"],
            dates="2011.01.16",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm15ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110519221845/http://ketto.com/mimiken/alllist.cgi?16", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 16 ====
        i = 16
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("16_tvm16hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm16ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト： たま 様"),
            Medium("16_tvm_logo16.gif",
                   [Source("https://web.archive.org/web/20110713145103/http://ketto.com/tvm/index110613.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ　ワールドインポートマート4階展示ホールA2・3",
                sources=[Source("https://ketto.com/tvm/tvm16ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 16", "ボーマス16", "VOM@S16", "tvm16"],
            dates="2011.06.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm16ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110519220904/http://ketto.com/mimiken/alllist.cgi?30", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 17 ====
        i = 17
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("17_tvm17hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm17ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト： またよし 様"),
            Medium("17_tvm_logo17.gif",
                   [Source("https://web.archive.org/web/20111108111835/http://ketto.com/tvm/index110908.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ　文化会館2F展示ホールD",
                sources=[Source("https://ketto.com/tvm/tvm17ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 17", "ボーマス17", "VOM@S17", "tvm17"],
            dates="2011.09.04",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm17ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110713145157/http://ketto.com/mimiken/alllist.cgi?19", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 18 ====
        i = 18
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("18_tvm18hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm18ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト： CAFFEIN 様"),
            Medium("18_tvm_logo18.gif",
                   [Source("https://web.archive.org/web/20120104214642/http://ketto.com/tvm/index111123.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA2・3",
                sources=[Source("https://ketto.com/tvm/tvm18ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 18", "ボーマス18", "VOM@S18", "tvm18"],
            dates="2011.11.19",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm18ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (DEAD): https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm18", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 19 ====
        i = 19
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("19_tvm19hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm19ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト： Miu 様"),
            Medium("19_tvm_logo19.gif",
                   [Source("https://web.archive.org/web/20120325184205/http://ketto.com/tvm/index20120206.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA2・3",
                sources=[Source("https://ketto.com/tvm/tvm19ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 19", "ボーマス19", "VOM@S19", "tvm19"],
            dates="2012.02.05",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm19ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20120104212523/http://ketto.com/mimiken/alllist.cgi?73", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 20 ====
        i = 20
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("20_tvm20hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm20ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：デミタス 様"),
            Medium("20_20130429203301_deh.jpg",
                   [Source("https://web.archive.org/web/20130429203301/http://ketto.com/tvm/tvm20con/deh.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20_20130429214856_yun.jpg",
                   [Source("https://web.archive.org/web/20130429214856/http://ketto.com/tvm/tvm20con/yun.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20_20130429201351_title.jpg",
                   [Source("https://web.archive.org/web/20130429201351/http://ketto.com/tvm/tvm20con/title.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20_20120325184131_ane.jpg",
                   [Source("https://web.archive.org/web/20120325184131/http://ketto.com/tvm/tvm20con/ane.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20_bomasbnr_476_140.jpg",
                   [Source("https://web.archive.org/web/20120325184001/http://ketto.com/tvm/bomasbnr_476_140.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20_tvm_logo20in.gif",
                   [Source("https://web.archive.org/web/20120627165959/http://ketto.com/tvm/index20120509.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm20ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 20", "ボーマス20", "VOM@S20", "tvm20",
                     "THE VOC＠LOiD M＠STER 20", "THE VOC＠LOiD CHOU M＠STER 20"
                     ],
            dates="2012.04.28",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm20ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20120627164312/http://ketto.com/mimiken/alist.cgi?mi=79&sf=&spf=1", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 21 ====
        i = 21
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("21_tvm21hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm21ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="表紙イラスト： 村上ゆいち 様"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA1・2・3",
                sources=[Source("https://ketto.com/tvm/tvm21ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 21", "ボーマス21", "VOM@S21", "tvm21"],
            dates="2012.07.08",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm21ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629083518/http://ketto.com/mimiken/alist2.cgi?95", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 22 ====
        i = 22
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("22_tvm22hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm22ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：hatsuko 様"),
            Medium("22_tvm_logo22.gif",
                   [Source("https://web.archive.org/web/20130516031642/http://ketto.com/tvm/index20120911.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12970.580425251434!2d139.7720709554199!3d35.636474600000014!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889bfc2444add%3A0xd107706301e3e668!2sAriake%20Arena!5e0!3m2!1sen!2sfr!4v1766771035655!5m2!1sen!2sfr",
                description="ディファ有明",
                sources=[Source("https://ketto.com/tvm/tvm22ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC@LOiD M＠STER 22 Night Special", "ボーマス22", "VOM@S22", "tvm22",
                     "THE VOC＠LOiD M＠STER 22",
                     ],
            dates="2012.08.31",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm22ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629042947/http://ketto.com/mimiken/alist2.cgi?101", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 23 ====
        i = 23
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("23_tvm23hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm23ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="表紙イラスト： ちゃもーい 様"),
            Medium("23_tvm23_logo.gif",
                   [Source("https://web.archive.org/web/20130425023456/http://ketto.com/tvm/index20130110.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA1・2・3",
                sources=[Source("https://ketto.com/tvm/tvm23ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 23", "ボーマス23", "VOM@S23"],
            dates="2012.12.15",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm23ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20180309050815/http://ketto.com/mimiken/alist.cgi?116", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 24 ====
        i = 24
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("24_tvm24hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm24ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：noala さん"),
            Medium("24_20130424170621_bomasbnr_600_60.jpg",
                   [Source("https://web.archive.org/web/20130424170621/http://ketto.com/tvm/bomasbnr_600_60.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("24_20130429202359_con_title.jpg",
                   [Source("https://web.archive.org/web/20130429202359/http://ketto.com/tvm/tvm24con/con_title.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("24_20130429202649_tvm24hyousi.jpg",
                   [Source("https://web.archive.org/web/20130429202649/http://ketto.com/tvm/tvm24con/tvm24hyousi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("24_20130429213437_nivo_24_illustdata.jpg",
                   [Source("https://web.archive.org/web/20130429213437/http://ketto.com/tvm/tvm24con/nivo_24_illustdata.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("24_20130429200800_02239_130301.jpg",
                   [Source("https://web.archive.org/web/20130429200800/http://ketto.com/tvm/tvm24con/02239_130301.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("24_tvm24_logo.gif",
                   [Source("https://web.archive.org/web/20240115015320/https://ketto.com/tvm/index20130508.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm20ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 24", "ボーマス24", "VOM@S24", "tvm24",
                     "THE VOC＠LOiD M＠STER 24", "THE VOC＠LOiD CHOU M＠STER 24"
                     ],
            dates="2013.04.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm24ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20130425033955/http://ketto.com/mimiken/alist.cgi?128", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 25 ====
        i = 25
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("25_tvm25hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm25ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="表紙イラスト： 佳奈 様"),
            Medium("25_tvm25_logo.gif",
                   [Source("https://web.archive.org/web/20240115015217/https://ketto.com/tvm/index20130712.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA1・2・3",
                sources=[Source("https://ketto.com/tvm/tvm25ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 25", "ボーマス25", "VOM@S25"],
            dates="2013.07.07",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm25ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629055913id_/http://ketto.com/mimiken/alist2.cgi?140", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 26 ====
        i = 26
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("26_tvm26hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm26ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="表紙イラスト： Automatic Colors 様"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12970.580425251434!2d139.7720709554199!3d35.636474600000014!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889bfc2444add%3A0xd107706301e3e668!2sAriake%20Arena!5e0!3m2!1sen!2sfr!4v1766771035655!5m2!1sen!2sfr",
                description="ディファ有明",
                sources=[Source("https://ketto.com/tvm/tvm26ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC@LOiD M＠STER 26 Night Special", "ボーマス26", "VOM@S26", "tvm26",
                     "THE VOC＠LOiD M＠STER 26",
                     ],
            dates="2013.08.30 - 2013.08.31",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm26ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629091251/http://ketto.com/mimiken/alist2.cgi?12", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 27 ====
        i = 27
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("27_tvm27hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm27ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="表紙イラスト： へちま 様"),
            Medium("27_tvm27_logo.gif",
                   [Source("https://web.archive.org/web/20140412005906/http://ketto.com/tvm/index20140109.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  文化会館2F 展示ホールD",
                sources=[Source("https://ketto.com/tvm/tvm27ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 27", "ボーマス27", "VOM@S27"],
            dates="2013.11.17",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm27ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629064318/http://ketto.com/mimiken/alist2.cgi?33", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 28 ====
        i = 28
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("28_tvm28hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm28ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：姉を見事に使いこなす妹 さん"),
            Medium("28_20150330093103_02297_140318.jpg",
                   [Source("https://web.archive.org/web/20150330093103/http://ketto.com/tvm/tvm28con/02297_140318.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("28_20150330085542_28con_title.jpg",
                   [Source("https://web.archive.org/web/20150330085542/http://ketto.com/tvm/tvm28con/28con_title.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("28_20150330091844_02301_140320.jpg",
                   [Source("https://web.archive.org/web/20150330091844/http://ketto.com/tvm/tvm28con/02301_140320.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("28_20150330091536_2296_140318.jpg",
                   [Source("https://web.archive.org/web/20150330091536/http://ketto.com/tvm/tvm28con/2296_140318.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("28_tvm28_logo.gif",
                   [Source("https://web.archive.org/web/20140701153006/http://ketto.com/tvm/index20140513.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm28ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 28", "ボーマス28", "VOM@S28", "tvm28",
                     "THE VOC＠LOiD M＠STER 28", "THE VOC＠LOiD CHOU M＠STER 28"
                     ],
            dates="2014.04.26 - 2014.04.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm28ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20140729151127/http://ketto.com/mimiken/alist2.cgi?149", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 29 ====
        i = 29
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("29_tvm29hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm29ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：れいな さん"
                   ),
            Medium("29_tvm29_logo.gif",
                   [Source("https://web.archive.org/web/20141211004453/http://ketto.com/tvm/index20140818.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA2・3",
                sources=[Source("https://ketto.com/tvm/tvm29ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 29", "ボーマス29", "VOM@S29"],
            dates="2014.07.13",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm29ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20140701163534/http://ketto.com/mimiken/alist2.cgi?67", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 30 ====
        i = 30
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("30_tvm30hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm30ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：seri さん"
                   ),
            Medium("30_tvm30_logo.gif",
                   [Source("https://web.archive.org/web/20150321151137/http://ketto.com/tvm/index20150115.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  文化会館2F 展示ホールD",
                sources=[Source("https://ketto.com/tvm/tvm30ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 30", "ボーマス30", "VOM@S30"],
            dates="2014.11.15",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm30ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20141211002218/http://ketto.com/mimiken/alist2.cgi?134", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 31 ====
        i = 31
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("31_tvm31hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm31ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：弥生 さん"
                   ),
            Medium("31_20221207014702_tvm31kkc.jpg",
                   [Source("https://web.archive.org/web/20221207014702/http://ketto.com/tvm/tvm31con/tvm31kkc.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("31_20221207034812_tvm31awashima.jpg",
                   [Source("https://web.archive.org/web/20221207034812/http://ketto.com/tvm/tvm31con/tvm31awashima.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("31_20221208073819_tvm31yayoi.jpg",
                   [Source("https://web.archive.org/web/20221208073819/http://ketto.com/tvm/tvm31con/tvm31yayoi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("31_tvm31_logo.gif",
                   [Source("https://web.archive.org/web/20150316033345/http://ketto.com/tvm/tvm31_logo.gif", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm31ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 31", "ボーマス31", "VOM@S31", "tvm31",
                     "THE VOC＠LOiD M＠STER 31", "THE VOC＠LOiD CHOU M＠STER 31"
                    ],
            dates="2015.04.25 - 2015.04.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm31ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20150321141805/http://ketto.com/mimiken/alist2.cgi?157", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 32 ====
        i = 32
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("32_tvm32hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm32ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：jimmy さん"
                   ),
            Medium("32_tvm32_logo.gif",
                   [Source("https://web.archive.org/web/20151019214707/http://ketto.com/tvm/index20150813.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA2・3",
                sources=[Source("https://ketto.com/tvm/tvm32ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 32", "ボーマス32", "VOM@S32"],
            dates="2015.07.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm32ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629050649/http://ketto.com/mimiken/alist2.cgi?166", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Circle list probably includes circles from the 'スプラケット' event held simultaneously."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 33 ====
        i = 33
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("33_tvm33hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm33ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：kkc さん"
                   ),
            Medium("33_tvm33logo.png",
                   [Source("https://web.archive.org/web/20160316073721/http://ketto.com/tvm/index20160115.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ　文化会館2F　展示ホールD",
                sources=[Source("https://ketto.com/tvm/tvm33ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 33", "ボーマス33", "VOM@S33"],
            dates="2015.11.14",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm33ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629132140/http://ketto.com/mimiken/alist2.cgi?124", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("みみけ33 circles excluded: https://web.archive.org/web/20160412121418/http://ketto.com/mimiken/alist2.cgi?124,%82%DD%82%DD%82%AF33", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Circle list may include circles from other events held simulatneously, I excluded known 'みみけ33' circles."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 34 ====
        i = 34
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("34_tvm34hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm34ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：宵月秦 さん"
                   ),
            Medium("34_tvm34logo.png",
                   [Source("https://web.archive.org/web/20160306141429/http://ketto.com/tvm/tvm34logo.png", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm34ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 34", "ボーマス34", "VOM@S34", "tvm34",
                     "THE VOC＠LOiD M＠STER 34", "THE VOC＠LOiD CHOU M＠STER 34"
                     ],
            dates="2016.04.29 - 2016.04.30",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm34ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629075447/http://ketto.com/mimiken/alist2.cgi?9", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 35 ====
        i = 35
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("35_tvm35hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm35ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：いろた さん"
                   ),
            Medium("35_tvm35logo.png",
                   [Source("https://web.archive.org/web/20170317025028/http://ketto.com/tvm/index20160804.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA1",
                sources=[Source("https://ketto.com/tvm/tvm35ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 35", "ボーマス35", "VOM@S35"],
            dates="2016.07.10",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm35ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629052407/http://ketto.com/mimiken/alist2.cgi?73", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Circle list may include circles of events held simultaneously."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 36 ====
        i = 36
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("36_tvm36hyousi.jpg",
                   [Source("https://ketto.com/tvm/tvm36ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：水素 さん"
                   ),
            Medium("36_tvm36logo.png",
                   [Source("https://web.archive.org/web/20180120050616/http://ketto.com/tvm/index20170117.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO１階大展示ホール",
                sources=[Source("https://ketto.com/tvm/tvm36ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 36", "ボーマス36", "VOM@S36"],
            dates="2016.11.05",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm36ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170317005530/http://ketto.com/mimiken/alist2.cgi?144,%83%7B%81%5B%83%7D%83X36", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 37 ====
        i = 37
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("37_20221208015927_nmkz.jpg",
                   [Source("https://web.archive.org/web/20221208015927/http://ketto.com/tvm/tvm37con/nmkz.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("37_20221208023829_takahasi.jpg",
                   [Source("https://web.archive.org/web/20221208023829/http://ketto.com/tvm/tvm37con/takahasi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("37_20221208104635_tsukita.jpg",
                   [Source("https://web.archive.org/web/20221208104635/http://ketto.com/tvm/tvm37con/tsukita.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("37_20181117113416_tvm37hyousi.jpg",
                   [Source("https://web.archive.org/web/20181117113416/http://ketto.com/tvm/tvm37hyousi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("37_tvm37logo.png",
                   [Source("https://web.archive.org/web/20171001180709/http://ketto.com/tvm/index20170804.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm37ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 37", "ボーマス37", "VOM@S37", "tvm37",
                     "THE VOC＠LOiD M＠STER 37", "THE VOC＠LOiD CHOU M＠STER 37"
                     ],
            dates="2017.04.29",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm37ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170629102334/http://ketto.com/mimiken/alist2.cgi?31", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 38 ====
        i = 38
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("38_tvm38logo.png",
                   [Source("https://web.archive.org/web/20170929073213/http://ketto.com/tvm/?f2d5", (ReliabilityTypes.Reliable, OriginTypes.Official))]),   
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ  ワールドインポートマート4階展示ホールA1",
                sources=[Source("https://ketto.com/tvm/tvm38ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 38", "ボーマス38", "VOM@S38"],
            dates="2017.11.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm38ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm38", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 39 ====
        i = 39
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("39_20190717091516_1.jpg",
                   [Source("https://web.archive.org/web/20190717091516/http://ketto.com/tvm/tvm39con/1.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("39_20190717091516_2.jpg",
                   [Source("https://web.archive.org/web/20190717091516/http://ketto.com/tvm/tvm39con/2.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("39_20190717091516_3.jpg",
                   [Source("https://web.archive.org/web/20190717091516/http://ketto.com/tvm/tvm39con/3.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("39_tvm39logo.png",
                   [Source("https://web.archive.org/web/20180203143958/http://ketto.com/tvm/?3038", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm39ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 39", "ボーマス39", "VOM@S39", "tvm39",
                     "THE VOC＠LOiD M＠STER 39", "THE VOC＠LOiD CHOU M＠STER 39"
                     ],
            dates="2018.04.28",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://ketto.com/tvm/tvm39ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm39", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 40 ====
        i = 40
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("40_tvm40logo.png",
                   [Source("https://web.archive.org/web/20181117113243/http://ketto.com/tvm/index20180719.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ文化会館2階 展示ホールD",
                sources=[Source("https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm40", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 40", "ボーマス40", "VOM@S40"],
            dates="2018.07.16",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm40", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 41 ====
        i = 41
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("41_1947.png",
                   [Source("https://vocadb.net/E/1947/the-vocloid-mster-41", (ReliabilityTypes.Likely, OriginTypes.External))],
                #    comments=""
                   ),
            Medium("41_tvm41logo.png",
                   [Source("https://web.archive.org/web/20210316154258/http://ketto.com/tvm/index20190205.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ文化会館2階 展示ホールD",
                sources=[Source("https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm41", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 41", "ボーマス41", "VOM@S41"],
            dates="2018.11.18",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm41", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 42 ====
        i = 42
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("42_20220309020626_2.jpg",
                   [Source("https://web.archive.org/web/20220309020626/https://ketto.com/tvm/tvm42con/2.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("42_20220312153838_1.jpg",
                   [Source("https://web.archive.org/web/20220312153838/https://ketto.com/tvm/tvm42con/1.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("42_20220317043733_3.jpg",
                   [Source("https://web.archive.org/web/20220317043733/https://ketto.com/tvm/tvm42con/3.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("42_tvm42logo.png",
                   [Source("https://web.archive.org/web/20190715012335/http://ketto.com/tvm/?dcf1", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm42", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 42", "ボーマス42", "VOM@S42", "tvm42",
                     "THE VOC＠LOiD M＠STER 42", "THE VOC＠LOiD CHOU M＠STER 42"
                     ],
            dates="2019.04.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm42", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 43 ====
        i = 43
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("43_tvm43logo.png",
                   [Source("https://web.archive.org/web/20210929043434/http://ketto.com/tvm/index20200122.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ文化会館2階 展示ホールD",
                sources=[Source("https://web.archive.org/web/20251226180416/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm43", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 43", "ボーマス43", "VOM@S43"],
            dates="2019.11.17",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20251226180416/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm43", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 44 ====
        i = 44
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("44_tvm44logo.png",
                   [Source("https://web.archive.org/web/20200425073330/http://ketto.com/tvm/index20200420.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://web.archive.org/web/20200325102937/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm44", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 44", "ボーマス44", "VOM@S44", "tvm44",
                     "THE VOC＠LOiD M＠STER 44", "THE VOC＠LOiD CHOU M＠STER 44"
                     ],
            dates="2020.04.18",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20200325102937/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm44", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 45 ====
        i = 45
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("45_20211026065354_tvm45hyousi.jpg",
                   [Source("https://web.archive.org/web/20211026065354/https://ketto.com/tvm/tvm45hyousi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            Medium("45_20200915235425_tvm45twi.jpg",
                   [Source("https://web.archive.org/web/20200915235425/https://ketto.com/tvm/tvm45twi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.914586241518!2d139.7161255888549!3d35.72831910000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188d121c16d9c1%3A0xf516d5df37b4b24d!2sSunshine%20City%20Exhibition%20Hall%20D!5e0!3m2!1sen!2sfr!4v1766768674758!5m2!1sen!2sfr",
                description="サンシャインシティ文化会館2階 展示ホールD",
                sources=[Source("https://web.archive.org/web/20250415182928/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm45", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 45", "ボーマス45", "VOM@S45"],
            dates="2020.11.15",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20250415182928/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm45", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 46 ====
        i = 46
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("46_20210411021653_tvm46hyousi.jpg",
                   [Source("https://web.archive.org/web/20210411021653/http://ketto.com/tvm/tvm46hyousi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20251228112051/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm46", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 46", "ボーマス46", "VOM@S46"],
            dates="2021.05.23 → 2021.11.20",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20251228112051/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm46", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Postponed: {puella}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 47 ====
        i = 47
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("47_20220421033926_tvm47CM.jpg",
                   [Source("https://web.archive.org/web/20220421033926/https://ketto.com/tvm/tvm47CM.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20251228112614/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm47", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 47", "ボーマス47", "VOM@S47"],
            dates="2022.02.12 → 2022.07.03",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20251228112614/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm47", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 48 ====
        i = 48
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("48_20220224155042_tvm48twi.jpg",
                   [Source("https://web.archive.org/web/20220224155042/https://ketto.com/tvm/tvm48twi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            Medium("48_20230412165138_1.jpg",
                   [Source("https://web.archive.org/web/20230412165138/http://ketto.com/tvm/tvm48con/1.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("48_20230412165137_2.jpg",
                   [Source("https://web.archive.org/web/20230412165137/http://ketto.com/tvm/tvm48con/2.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("48_20220503002158_3.jpg",
                   [Source("https://web.archive.org/web/20220503002158/https://ketto.com/tvm/tvm48con/3.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://web.archive.org/web/20251228113000/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm48", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 48", "ボーマス48", "VOM@S48", "tvm48",
                     "THE VOC＠LOiD M＠STER 48", "THE VOC＠LOiD CHOU M＠STER 48"
                     ],
            dates="2022.04.29",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20251228113000/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm48", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 49 ====
        i = 49
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("49_20220802103817_tvm49CM.jpg",
                   [Source("https://web.archive.org/web/20220802103817/https://ketto.com/tvm/tvm49CM.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1622.4614245873063!2d139.74702373866853!3d35.58029602459979!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601861bc691ff473%3A0x3c65b91947c29bba!2sTRC%20First%20Exhibition%20Hall!5e0!3m2!1sen!2sfr!4v1766790392057!5m2!1sen!2sfr",
                description="TRC東京流通センター第一展示場ABホール ",
                sources=[Source("https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm49", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 49", "ボーマス49", "VOM@S49"],
            dates="2022.11.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm49", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 50 ====
        i = 50
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("50_20230602153705_tvm50twi.jpg",
                   [Source("https://web.archive.org/web/20230602153705/https://ketto.com/tvm/tvm50twi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.8217084738917!2d139.33816588885495!3d35.6567641!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60191ddd90908ea1%3A0x34e81277b2818321!2sTokyo%20Tama%20Mirai%20Messe%20Exhibition%20Room%20C%2FD!5e0!3m2!1sen!2sfr!4v1766788127368!5m2!1sen!2sfr",
                description="東京たま未来メッセ全展示室",
                sources=[Source("https://web.archive.org/web/20230113142557/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm50", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 50", "ボーマス50", "VOM@S50"],
            dates="2023.02.19",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm50", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 51 ====
        i = 51
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("51_20230408114125_tvm51twi.jpg",
                   [Source("https://web.archive.org/web/20230408114125/https://ketto.com/tvm/tvm51twi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            Medium("51_20230413203638_kusu.jpg",
                   [Source("https://web.archive.org/web/20230413203638/http://ketto.com/tvm/tvm51con/kusu.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("51_20240402153253_jimi.jpg",
                   [Source("https://web.archive.org/web/20240402153253/http://ketto.com/tvm/tvm51con/jimi.jpg ", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("51_20230413040327_melu.jpg",
                   [Source("https://web.archive.org/web/20230413040327/http://ketto.com/tvm/tvm51con/melu.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("51_tvm51clogo.png",
                   [Source("https://web.archive.org/web/20231112044800/https://www.ketto.com/tvm/index20230502.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm20ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 51", "ボーマス51", "VOM@S51", "tvm51",
                     "THE VOC＠LOiD M＠STER 51", "THE VOC＠LOiD CHOU M＠STER 51"
                     ],
            dates="2023.04.29",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20230409132025/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm51", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 52 ====
        i = 52
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("52_tvm52logo.png",
                   [Source("https://web.archive.org/web/20231112044420/https://www.ketto.com/tvm/index20230804.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20230619084605/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm52", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 52", "ボーマス52", "VOM@S52"],
            dates="2023.07.23",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20230619084605/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm52", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 53 ====
        i = 53
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("53_tvm53hyousi.jpg",
                   [Source("https://web.archive.org/web/20231112044023/https://ketto.com/tvm/tvm53hyousi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            Medium("53_tvm53logo.png",
                   [Source("https://web.archive.org/web/20231130052612/https://www.ketto.com/tvm/index20231121.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20231112044409/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm53", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 53", "ボーマス53", "VOM@S53"],
            dates="2023.11.17",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20231112044409/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm53", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 54 ====
        i = 54
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("54_6697.png",
                   [Source("https://vocadb.net/E/6697/the-vocloid-mster-54s", (ReliabilityTypes.Likely, OriginTypes.External))],
                #    comments=""
                   ),
            Medium("54_tvm54logo.png",
                   [Source("https://web.archive.org/web/20231130052557/https://www.ketto.com/tvm/tvm54logo.png", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20240108153949/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm54", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 54.S", "THE VOC＠LOiD M＠STER 54", "ボーマス54", "VOM@S54"],
            dates="2024.01.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20240108153949/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm54", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 55 ====
        i = 55
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("55_20250301090057_merucyans.jpg",
                   [Source("https://web.archive.org/web/20250301090057/https://ketto.com/tvm/tvm55con/merucyans.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            Medium("55_20250301090057_asteroid_stella.jpg",
                   [Source("https://web.archive.org/web/20250301090057/https://ketto.com/tvm/tvm55con/asteroid_stella.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("55_20250301090057_akiben.jpg",
                   [Source("https://web.archive.org/web/20250301090057/https://ketto.com/tvm/tvm55con/akiben.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("55_6698.png",
                   [Source("https://vocadb.net/E/6698/the-vocloid-cho-mster-55", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://web.archive.org/web/20240504114400/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm55", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 55", "ボーマス55", "VOM@S55", "tvm55",
                     "THE VOC＠LOiD M＠STER 55", "THE VOC＠LOiD CHOU M＠STER 55"
                     ],
            dates="2024.04.27 - 2024.04.28",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20240504114400/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm55", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 56 ====
        i = 56
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("56_tvm56logo.png",
                   [Source("https://web.archive.org/web/20240607003059/http://ketto.com/tvm/?76cb=", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20240715124116/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm56", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 56", "ボーマス56", "VOM@S56"],
            dates="2024.07.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20240715124116/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm56", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 57 ====
        i = 57
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("57_tvm57logo.png",
                   [Source("https://web.archive.org/web/20250314124225/http://ketto.com/tvm/index20241124.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1622.4614245873063!2d139.74702373866853!3d35.58029602459979!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601861bc691ff473%3A0x3c65b91947c29bba!2sTRC%20First%20Exhibition%20Hall!5e0!3m2!1sen!2sfr!4v1766790392057!5m2!1sen!2sfr",
                description="TRC東京流通センター第一展示場 ",
                sources=[Source("https://web.archive.org/web/20240930160643/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm57", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 57", "ボーマス57", "VOM@S57"],
            dates="2024.11.23",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20240930160643/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm57", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 58 ====
        i = 58
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("58_tvm58logo.png",
                   [Source("https://web.archive.org/web/20250301090024/http://ketto.com/tvm/index20250129.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766760726321!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20241223123456/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm58", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 58", "ボーマス58", "VOM@S58"],
            dates="2025.01.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm58", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 59 ====
        i = 59  
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("59_20250410050335_sabaku.jpg",
                   [Source("https://web.archive.org/web/20250410050335/https://ketto.com/tvm/tvm59con/sabaku.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            Medium("59_20250410050924_ast.jpg",
                   [Source("https://web.archive.org/web/20250410050924/https://ketto.com/tvm/tvm59con/ast.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("59_20250410050334_aoi.jpg",
                   [Source("https://web.archive.org/web/20250410050334/https://ketto.com/tvm/tvm59con/aoi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("59_tvm59clogo.png",
                   [Source("https://web.archive.org/web/20250601231744/http://ketto.com/tvm/index20250502.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.com/tvm/tvm20ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD 超 M＠STER 59", "ボーマス59", "VOM@S59", "tvm59",
                     "THE VOC＠LOiD M＠STER 59", "THE VOC＠LOiD CHOU M＠STER 59"
                     ],
            dates="2025.04.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20250316134417/https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm59", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 60 ====
        i = 60
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("60_20250601231746_tvm_twi.jpg",
                   [Source("https://web.archive.org/web/20250601231746/https://ketto.com/tvm/tvm_twi.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments=""
                   ),
            Medium("60_tvm60cm.webp",
                   [Source("https://web.archive.org/web/20251010103551/http://ketto.com/tvm/index20250721.shtml", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：いらすとがかり様"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.1900108045256!2d140.03295367533178!3d35.64768993181651!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6022821fd52ebfdf%3A0xcec0c09c4bed45e0!2sMakuhari%20Messe!5e0!3m2!1sen!2sfr!4v1766770606094!5m2!1sen!2sfr",
                description="幕張メッセ",
                sources=[Source("https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm60", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 60", "ボーマス60", "VOM@S60"],
            dates="2025.07.19",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm60", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== tvm 61 ====
        i = 61
        name = f"tvm{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("61_tvm61logo.png",
                   [Source("https://web.archive.org/web/20251210004352/http://ketto.com/tvm/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                #    comments=""
                   ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1622.4614245873063!2d139.74702373866853!3d35.58029602459979!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601861bc691ff473%3A0x3c65b91947c29bba!2sTRC%20First%20Exhibition%20Hall!5e0!3m2!1sen!2sfr!4v1766790392057!5m2!1sen!2sfr",
                description="TRC東京流通センター第一展示場ABCホール",
                sources=[Source("https://web.archive.org/web/20251116114415/https://ketto.com/tvm/tvm61youkou.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["THE VOC＠LOiD M＠STER 61", "ボーマス61", "VOM@S61"],
            dates="2025.11.29",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251116114415/https://ketto.com/tvm/tvm61youkou.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm61", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    # ==== event group ====
    media = [
        Medium("eg_20071020193402_tvm_bana.gif",
               [Source("https://web.archive.org/web/20071020193402/http://ketto.com/tvm/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["https://ketto.com/tvm/", "Something like https://ketto.xsrv.jp/html/mimiken/clist.cgi?tvm9", "https://x.com/vocaloid_mas"]

    event_group = EventGroup(
        aliases=["THE VOC＠LOiD M＠STER", "ボーマス", "VOM@S", "tvm"],
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
        

