# Notes:
# TODO: go through date urls for circle participation lists
# TODO: perhaps "东方合同展会2016新春！" (cf thwikicc)

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

    thwikicc = "https://thwiki.cc/%E5%A6%96%E7%B2%BE%E5%85%83%E6%B0%94%EF%BC%81"

    if True: # ==== youseigenki 1 ====
        i = 1
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("1_cirno_top2.jpg",
                   [Source("https://web.archive.org/web/20101231035441/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            Medium("1_539px-妖精元气！1插画.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767611219328!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ大展示",
                sources=[Source("https://web.archive.org/web/20100222144933/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！", "Yousei Genki!",
                "ようせいげんき！1", "Yousei Genki! 1"
            ],
            dates="2010.09.05",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20100222144933/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110811213205/http://www.puniket.com/cirno/cirno_list01.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultanous with 幺樂団カァニバル！."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 2 ====
        i = 2
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
            #        comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.8869299207763!2d139.75819397533223!3d35.655157331406535!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1767707517708!5m2!1sen!2sfr",
                description="都立産業貿易センター浜松町館 ４、５Ｆ（２フロア開催予定）",
                sources=[Source("https://web.archive.org/web/20120118101603/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！2", "Yousei Genki! 2"
            ],
            dates="2011.09.19",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20120118101603/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 3 ====
        i = 3
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("3_531px-妖精元气！3.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.8869299207763!2d139.75819397533223!3d35.655157331406535!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1767707517708!5m2!1sen!2sfr",
                description="都立産業貿易センター浜松町館",
                sources=[Source("https://web.archive.org/web/20121016051727/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！3", "Yousei Genki! 3"
            ],
            dates="2012.09.09",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20121016051727/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 4 ====
        i = 4
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("4_cirno_top4_01.jpg",
                   [Source("https://web.archive.org/web/20130119161557/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[Source("https://web.archive.org/web/20130119161557/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                'ようせいげんき！4', "Yousei Genki! 4"
            ],
            dates="2013.01.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130119161557/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20130323154552/http://www.puniket.com/aka/2013_0127_lisi02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 5 ====
        i = 5
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("5_cirno_top5_01.jpg",
                   [Source("https://web.archive.org/web/20130812023818/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[Source("https://web.archive.org/web/20130812023818/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！5", "Yousei Genki! 5"
            ],
            dates="2013.09.08",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130812023818/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 6 ====
        i = 6
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("6_cirno_top6_01.jpg",
                   [Source("https://web.archive.org/web/20141105010647/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[Source("https://web.archive.org/web/20141105010647/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！6", "Yousei Genki! 6"
            ],
            dates="2014.01.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20141105010647/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20131229062508/http://www.puniket.com/aka/0112toho_aka11_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 7 ====
        i = 7
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("7_cirno_top7_01.jpg",
                   [Source("https://web.archive.org/web/20150622183222/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[Source("https://web.archive.org/web/20150622183222/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！7", "Yousei Genki! 7"
            ],
            dates="2015.03.14",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20150622183222/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20150313173421/http://www.puniket.com/aka/aka12_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 8 ====
        i = 8
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("8_cirno_top8_01.jpg",
                   [Source("https://web.archive.org/web/20160704031420/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[Source("https://web.archive.org/web/20160704031420/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！8", "Yousei Genki! 8"
            ],
            dates="2016.01.24",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20160704031420/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20160113213041/http://www.puniket.com/aka/touhou124_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 9 ====
        i = 9
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("9_cirno_top9_01.jpg",
                   [Source("https://web.archive.org/web/20170822143330/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[Source("https://web.archive.org/web/20170822143330/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！9", "Yousei Genki! 9"
            ],
            dates="2017.01.29",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20170822143330/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170202002107/http://www.puniket.com/aka/aka14_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 10 ====
        i = 10
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("10_cirno_top10_01.jpg",
                   [Source("https://web.archive.org/web/20180524070705/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[Source("https://web.archive.org/web/20180524070705/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！10", "Yousei Genki! 10"
            ],
            dates="2018.02.11",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20180524070705/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20180212143447/http://www.puniket.com/aka/toho2018haru_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 11 ====
        i = 11
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("11_cirno_top11_01.jpg",
                   [Source("https://web.archive.org/web/20181017031647/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[Source("https://web.archive.org/web/20181017031647/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！11", "Yousei Genki! 11"
            ],
            dates="2018.09.15",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20181017031647/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20211203033926/http://www.puniket.com/aka/toho2018aki_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 12 ====
        i = 12
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("12_cirno_top12_01.jpg",
                   [Source("https://web.archive.org/web/20190921115430/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[Source("https://web.archive.org/web/20190921115430/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！12", "Yousei Genki! 12"
            ],
            dates="2019.01.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20190921115430/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20220828175049/http://www.puniket.com/aka/toho2019haru_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 13 ====
        i = 13
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("13_cirno_top13_01.jpg",
                   [Source("https://web.archive.org/web/20200224140724/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[Source("https://web.archive.org/web/20200224140724/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！13", "Yousei Genki! 13"
            ],
            dates="2020.02.02",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20200224140724/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20200210101842/http://www.puniket.com/aka/toho2020w_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 14 ====
        i = 14
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("14_cirno_top14_01.jpg",
                   [Source("https://web.archive.org/web/20210729132933/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[Source("https://web.archive.org/web/20210729132933/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！14", "Yousei Genki! 14"
            ],
            dates="2021.01.24",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20210729132933/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (date matches, not ようせいげんき！13 but ようせいげんき！14): https://web.archive.org/web/20210113043127/http://www.puniket.com/aka/toho2021w_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 15 ====
        i = 15
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("15_cirno_top15_01.jpg",
                   [Source("https://web.archive.org/web/20220604060245/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[Source("https://web.archive.org/web/20220604060245/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！15", "Yousei Genki! 15"
            ],
            dates="2022.01.30",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20220604060245/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20230319233813/http://www.puniket.com/touhou/toho2023w_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 16 ====
        i = 16
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("16_cirno_top16_01.jpg",
                   [Source("https://web.archive.org/web/20230718063821/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1767709807444!5m2!1sen!2sfr",
                description="横浜産貿ホールマリネリア",
                sources=[Source("https://web.archive.org/web/20230718063821/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！16", "Yousei Genki! 16"
            ],
            dates="2023.02.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20230718063821/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 17 ====
        i = 17
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("17_cirno_top17_01.jpg",
                   [Source("https://web.archive.org/web/20240912164712/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[Source("https://web.archive.org/web/20240912164712/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！17", "Yousei Genki! 17"
            ],
            dates="2024.01.28",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20240912164712/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20240204115609/http://www.puniket.com/touhou/toho2024w_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== youseigenki 18 ====
        i = 18
        name = f"youseigenki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("18_cirno_top18_01.jpg",
                   [Source("https://web.archive.org/web/20250912011749/https://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767707815208!5m2!1sen!2sfr",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[Source("https://web.archive.org/web/20250912011749/https://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！18", "Yousei Genki! 18"
            ],
            dates="2025.02.02",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20250912011749/https://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20250122123336/http://www.puniket.com/touhou/toho2025w_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    # if True: # ==== youseigenki 19 ====
    #     i = 19
    #     name = f"youseigenki{i}"
    #     print(f"Processing {name} ...")
    #     circles_ = []
    #     media_ = [
    #         Medium("",
    #                [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #                comments="Illustration by HAM（points)"),
    #         # Medium("",
    #         #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    #         ]
    #     locations = [
    #         Location(
    #             iframe_url="",
    #             description="",
    #             sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]
    #         ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             "ようせいげんき！19", "Yousei Genki! 19"
    #         ],
    #         dates="2026.03.20",
    #         circles=circles_,
    #         media=media_,
    #         sources=[
    #             Source("Date: https://web.archive.org/web/20260106143956/https://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
    #             # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
    #         ],
    #         locations=locations,
    #         comments=None
    #     )
    #     event_raw = event.get_json()
    #     # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
    #     #     circles_raw = json.load(f)
    #     # event_raw["circles"] = circles_raw
    #     events_raw.append(event_raw)
    
    # ==== event group ====
    media = [
        Medium("eg_cirno_ba01b.jpg",
               [Source("https://web.archive.org/web/20100710045110/http://www.puniket.com/cirno/ol_cirno.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_cirno_cut1.png",
               [Source("https://web.archive.org/web/20100710045019/http://www.puniket.com/cirno/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
               comments="Illustration by いちご"),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = []

    event_group = EventGroup(
        aliases=[
            "ようせいげんき！", "Yousei Genki!",
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
        

