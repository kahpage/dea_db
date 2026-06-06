# Notes:
# Perhaps find 3rd,6th circle lists via url similar to 5th https://web.archive.org/web/20140125021337/http://project-d.biz/20140202circlelist.html

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

    thwikicc = "https://thwiki.cc/%E5%A4%A9%E7%8B%97%E5%A4%A7%E4%BA%BA%E7%9A%84%E5%B7%A5%E4%BD%9C"

    if True: # ==== tengusama_no_oshigoto 1 ====
        i = 1
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("1_tengu_top.jpg",
                   [Source("https://web.archive.org/web/20100603060915/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by たちゆれ（たちゆれさん）."),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20100603060915/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事", "Tengusama no Oshigoto",
                "天狗様のお仕事1", "Tengusama no Oshigoto 1",
            ],
            dates="2010.06.13",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20100603060915/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20100927042506/http://ketto.com/mimiken/alllist.cgi?91,%93V%8B%E7%97l%82%CC%82%A8%8Ed%8E%96", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description="Part of 東方素芸祭.",
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 2 ====
        i = 2
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("2_tengu2_top.jpg",
                   [Source("https://web.archive.org/web/20111012023125/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by 風瑛なづき（Amtarte）."),
            Medium("2_0410_haitizu.png",
                   [Source("http://web.archive.org/web/20110909153053/http://project-d.biz/eiyasho/circle-list.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO大展示ホール",
                sources=[Source("https://web.archive.org/web/20111012023125/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事2", "Tengusama no Oshigoto 2",
            ],
            dates="2011.04.10",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20111012023125/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: http://web.archive.org/web/20110909153053/http://project-d.biz/eiyasho/circle-list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 3 ====
        i = 3
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("3_tengu3_top.jpg",
                   [Source("https://web.archive.org/web/20121016014735/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by 啓々（啓々堂(pixiv)）."),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[Source("https://web.archive.org/web/20121115190927/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事・参", "Tengusama no Oshigoto 3", 
                "天狗様のお仕事3"
            ],
            dates="2012.03.18",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20121016014735/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 4 ====
        i = 4
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("4_tengu4_top.jpg",
                   [Source("https://web.archive.org/web/20130406064824/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by 祭唄ソラト（Rainbow Vanilla） "),
            Medium("4_20130310_catalog_top.jpg",
                   [Source("https://web.archive.org/web/20130406064824/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by 茜屋（茜屋ぐーたら店） "),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[Source("https://web.archive.org/web/20130323014434/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事4", "Tengusama no Oshigoto 4",
            ],
            dates="2013.03.10",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130323014434/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: http://web.archive.org/web/20130209202039/http://project-d.biz/eiyasho/circle-list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description="Simultaneous with 月の宴６, 小春小径４, 御阿礼祭, PrivateService",
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 5 ====
        i = 5
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("5_tengu5_top.jpg",
                   [Source("https://web.archive.org/web/20131227220942/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by ヤナギユウ（猫御所） "),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[Source("https://web.archive.org/web/20130727114609/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事・五", "Tengusama no Oshigoto 5",
                "天狗様のお仕事5"
            ],
            dates="2014.02.02",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130727114609/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20140125021337/http://project-d.biz/20140202circlelist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 6 ====
        i = 6
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("6_tengu6_top.jpg",
                   [Source("https://web.archive.org/web/20150205105313/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by 祭唄（RainbowVanilla） "),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO",
                sources=[Source("https://web.archive.org/web/20150326204346/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事・六", "Tengusama no Oshigoto 6",
                "天狗様のお仕事6",
            ],
            dates="2015.02.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20150326204346/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20150215083619/http://project-d.biz/eiyasho/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (alt): https://web.archive.org/web/20150414133404/http://project-d.biz/suwako/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 7 ====
        i = 7
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("7_tengu7_top.png",
                   [Source("https://web.archive.org/web/20160110082645/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by 祭唄（RainbowVanilla） "),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO",
                sources=[Source("https://web.archive.org/web/20160109170238/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事・七", "Tengusama no Oshigoto 7",
                "天狗様のお仕事7"
            ],
            dates="2016.03.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20160109170238/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20160306174301/http://project-d.biz/eiyasho/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (alt): https://web.archive.org/web/20160417145414/http://project-d.biz/suwako/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official))
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 8 ====
        i = 8
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("8_tengu8_top.png",
                   [Source("https://web.archive.org/web/20170625044421/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO",
                sources=[Source("https://web.archive.org/web/20161105173738/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事八", "Tengusama no Oshigoto 8",
                "天狗様のお仕事8"
            ],
            dates="2017.03.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20161105173738/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170504223846/http://project-d.biz/tohosaiji/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 9 ====
        i = 9
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("9_tengu9_top.png",
                   [Source("https://web.archive.org/web/20180218204152/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="チラシ絵　Illustration by ゾウノセ（薬味さらい）"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO",
                sources=[Source("https://web.archive.org/web/20161105173738/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事九", "Tengusama no Oshigoto 9",
                "天狗様のお仕事9"
            ],
            dates="2018.03.25",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20161105173738/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20180207183811/http://project-d.biz/tohosaiji/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 10 ====
        i = 10
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("10_tengusama10_top-1.png",
                   [Source("https://web.archive.org/web/20220116173815/http://project-d.biz/tohosaiji/wp-content/uploads/sites/8/2020/08/tengusama10_top-1.png", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO",
                sources=[Source("https://web.archive.org/web/20251016151721/https://project-d.biz/tohosaiji/?m=202103", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事10", "Tengusama no Oshigoto 10",
            ],
            dates="2021.03.07",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251016151721/https://project-d.biz/tohosaiji/?m=202103", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description="Part of 東方合同祭事・漆.",
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 11 ====
        i = 11
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("11_天狗様のお仕事11（レイヤ統合）.jpg",
                   [Source("https://web.archive.org/web/20251116100245/https://project-d.biz/tohosaiji/?m=202110", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[Source("https://web.archive.org/web/20251116100245/https://project-d.biz/tohosaiji/?m=202110", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事11", "Tengusama no Oshigoto 11",
            ],
            dates="2022.03.06",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251116100245/https://project-d.biz/tohosaiji/?m=202110", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 12 ====
        i = 12
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            # Location(
            #     iframe_url="",
            #     description="",
            #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            # ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事12", "Tengusama no Oshigoto 12",
            ],
            dates="2023.03.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://thwiki.cc/%E5%A4%A9%E7%8B%97%E5%A4%A7%E4%BA%BA%E7%9A%84%E5%B7%A5%E4%BD%9C", (ReliabilityTypes.Likely, OriginTypes.External)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 13 ====
        i = 13
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            # Location(
            #     iframe_url="",
            #     description="",
            #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            # ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事13", "Tengusama no Oshigoto 13",
            ],
            dates="2024.02.10",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://thwiki.cc/%E5%A4%A9%E7%8B%97%E5%A4%A7%E4%BA%BA%E7%9A%84%E5%B7%A5%E4%BD%9C", (ReliabilityTypes.Likely, OriginTypes.External)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tengusama_no_oshigoto 14 ====
        i = 14
        name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("14_天狗様のお仕事14（レイヤ統合）.jpg",
                   [Source("https://web.archive.org/web/20251116084722/https://project-d.biz/tohosaiji/?m=202410", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1768059722361!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[Source("https://web.archive.org/web/20251116084722/https://project-d.biz/tohosaiji/?m=202410", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事14", "Tengusama no Oshigoto 14",
            ],
            dates="2025.02.08",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251116084722/https://project-d.biz/tohosaiji/?m=202410", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None,
            description=None,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    # ==== event group ====
    media = [
        Medium("eg_tengu_bn.jpg",
               [Source("https://web.archive.org/web/20110129213518/http://project-d.biz/tengu/tengu_bn.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["http://project-d.biz/tengu/", "https://x.com/tuki_no_utage"]
    # https://dic.pixiv.net/a/%E5%A4%A9%E7%8B%97%E6%A7%98%E3%81%AE%E3%81%8A%E4%BB%95%E4%BA%8B
    # https://shiosyakeyakini.info/touhouEvent/pb_event.php?id=122

    event_group = EventGroup(
        aliases=[
            "天狗様のお仕事", "Tengusama no Oshigoto",
        ],
        events=[],
        media=media,
        links=links,
        comments="Part of 東方合同祭事 series.",
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
        

