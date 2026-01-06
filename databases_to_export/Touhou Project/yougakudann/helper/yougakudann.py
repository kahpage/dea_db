# Notes:

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

    thwikicc = "https://thwiki.cc/%E5%B9%BA%E4%B9%90%E5%9B%A2%E5%98%89%E5%B9%B4%E5%8D%8E%EF%BC%81"

    if True: # ==== yougakudann 1 ====
        i = 1
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("1_609.jpg", 
                [Source("https://static.touhoudb.com/img/releaseevent/mainOrig/609.jpg?v=4", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("1_20100805061627__.jpg", 
                [Source("https://web.archive.org/web/20100805061627/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767611219328!5m2!1sen!2sfr",
                description="大田区産業プラザPiO 大展示ホール ",
                sources=[Source("Official event poster, see media.", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！", "Yougakudann Carnival"
            ],
            dates="2010.09.05",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20100831015410/http://www.puniket.com/cirno/cirno_list01.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 2 ====
        i = 2
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("2_20110504203536_修正RCB.jpg",
                   [Source("https://web.archive.org/web/20110504203536/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("2_alice.png",
                   [Source("https://web.archive.org/web/20110818095504/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("2_539px-幺乐团嘉年华！2插画1.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767611219328!5m2!1sen!2sfr",
                description="大田区産業プラザＰiＯ ２Ｆ",
                sources=[Source("https://web.archive.org/web/20110813183615/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！2", "Yougakudann Carnival 2"
            ],
            dates="2011.05.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20110813183615/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: http://web.archive.org/web/20110818095504/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 3 ====
        i = 3
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("3_20110823032834_yougkau3.jpg",
                   [Source("https://web.archive.org/web/20110823032834/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_20120103193638_スタッフ募集イラスト.jpg",
                   [Source("https://web.archive.org/web/20120103193638/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_20120501222648_haiti.jpg",
                   [Source("https://web.archive.org/web/20120501222648/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_20121201215154_阿求なんちゃってカラー.jpg",
                   [Source("https://web.archive.org/web/20121201215154/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767611219328!5m2!1sen!2sfr",
                description="大田区産業プラザＰiＯ ２Ｆ",
                sources=[Source("http://web.archive.org/web/20120930113317/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！3", "Yougakudann Carnival 3"
            ],
            dates="2012.05.06",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: http://web.archive.org/web/20120930113317/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 4 ====
        i = 4
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("4_20130102064718_合同ちらし2.jpg", 
                   [Source("https://web.archive.org/web/20130102064718/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_20130218061201_yougaku4.jpg", 
                   [Source("https://web.archive.org/web/20130218061201/http://2.bp.blogspot.com/-QpU83U-ecoc/UMROK39X0xI/AAAAAAAAAJc/ksL4bHg3zP4/s1600/yougaku4.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_539px-幺乐团嘉年华！4目录.jpg",
                     [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20140307211133/http://yougakudan.blogspot.jp/2013/03/blog-post_26.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！4", "Yougakudann Carnival 4"
            ],
            dates="2013.04.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20140307211133/http://yougakudan.blogspot.jp/2013/03/blog-post_26.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭・卯."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 5 ====
        i = 5
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("5_20140508160625_チラシ_2.jpg", 
                   [Source("https://web.archive.org/web/20140508160625/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("http://web.archive.org/web/20160211064625/http://yougakudan.blogspot.jp/2013/03/blog-post_26.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！5", "Yougakudann Carnival 5"
            ],
            dates="2014.09.14",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: http://web.archive.org/web/20160211064625/http://yougakudan.blogspot.jp/2013/03/blog-post_26.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭・長."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 6 ====
        i = 6
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("6_20160826174801_チラシ統合版.jpg", 
                   [Source("https://web.archive.org/web/20160826174801/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",   
                sources=[Source("https://web.archive.org/web/20160818122309/http://yougakudan.blogspot.jp/2011/08/blog-post.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！6", "Yougakudann Carnival 6"
            ],
            dates="2016.11.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20160818122309/http://yougakudan.blogspot.jp/2011/08/blog-post.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20161116020013/http://yougakudan.blogspot.jp/2016/10/6.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭・霜."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 7 ====
        i = 7
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("7_20171021125833_hp20171111.jpg", 
                [Source("https://web.archive.org/web/20171021125833/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("7_536px-幺乐团嘉年华！7目录扉页.png",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20171023135929/http://yougakudan.blogspot.jp/2016/10/7.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！7", "Yougakudann Carnival 7"
            ],
            dates="2017.11.11",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20171023135929/http://yougakudan.blogspot.jp/2016/10/7.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭 (4th edition)."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 8 ====
        i = 8
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("8_20180909025756_告知イラスト(日程).jpg", 
                   [Source("https://web.archive.org/web/20171021125833/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20181124073957/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！8", "Yougakudann Carnival 8"
            ],
            dates="2018.09.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20181124073957/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭2 (5th edition)."
        )   
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 9 ====
        i = 9
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("9_20190903204904_yougaku9hp.jpg", 
                   [Source("https://web.archive.org/web/20190903204904/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20251107154156/http://yougakudan.blogspot.com/2016/10/blog-post_24.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！9", "Yougakudann Carnival 9"
            ],
            dates="2019.09.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20251107154156/http://yougakudan.blogspot.com/2016/10/blog-post_24.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭3 (6th edition)."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 10 ====
        i = 10
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("10_20200202101652_yougaku9hp.jpg",
                   [Source("https://web.archive.org/web/20200202101652/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20200202101652/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！10", "Yougakudann Carnival 10"
            ],
            dates="2020.09.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20200202101652/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20200918213738/http://yougakudann.dojin.com/splist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://x.com/yougakudan_info/status/1306931482003349505/photo/1", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("NOT cancelled: https://x.com/yougakudan_info/status/1309738651878735873", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭4 (7th edition)."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 10R ====
        i = "10R"
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("10R_20210514014026_yougaku9hp.jpg", 
                [Source("https://web.archive.org/web/20210514014026/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20210514014026/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！10R", "Yougakudann Carnival 10R"
            ],
            dates="2021.02.27 → CANCELLED",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20210514014026/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Cancelled: https://x.com/yougakudan_info/status/1354041811749097474", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭4R (8th edition)."
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 11 ====
        i = 11
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("11_20220307155313_yougaku9hp.jpg",
                [Source("https://web.archive.org/web/20220307155313/http://yougakudann.dojin.com/splist.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.8869299207763!2d139.75819397533223!3d35.655157331406535!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1767630940588!5m2!1sen!2sfr",
                description="東京都立産業貿易センター 浜松町館",
                sources=[Source("Official poster, see media.", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！11", "Yougakudann Carnival 11"
            ],
            dates="2022.03.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20220307155313/http://yougakudann.dojin.com/splist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭5 (9th edition)."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 12 ====
        i = 12
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("12_1677296406711910400_F0bvkc4aQAIa_Sd.jpg", 
                [Source("https://x.com/yougakudan_info/status/1677296406711910400", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.8869299207763!2d139.75819397533223!3d35.655157331406535!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1767630940588!5m2!1sen!2sfr",
                description="京都立産業貿易センター浜松町館　3階展示室南側",
                sources=[Source("https://x.com/yougakudan_info/status/1677296406711910400", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！12", "Yougakudann Carnival 12"
            ],
            dates="2023.07.09",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://x.com/yougakudan_info/status/1677296406711910400", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20240126080406/https://yougakudann.dojin.com/splist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幻想人形祭6 (10th edition)."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 13 ====
        i = 13
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("13_20240713045959_yougaku9hp.png", 
                [Source("https://web.archive.org/web/20240713045959/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20240713045959/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！13", "Yougakudann Carnival 13"
            ],
            dates="2024.07.15",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20240713045959/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20240617123132/https://yougakudann.dojin.com/splist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 14 ====
        i = 14
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("14_20250613020651_yougaku9hp.jpg", 
                [Source("https://web.archive.org/web/20250613020651/https://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767611219328!5m2!1sen!2sfr",
                description="大田区産業プラザPiO　1F大展示ホール",
                sources=[Source("https://web.archive.org/web/20250418010838/https://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！14", "Yougakudann Carnival 14"
            ],
            dates="2025.06.29",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20250418010838/https://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20250613160029/https://yougakudann.dojin.com/splist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=None
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== yougakudann 15 ====
        i = 15
        name = f"yougakudann{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("15_yougakudan15.jpg",
                   [Source("https://web.archive.org/web/20251117175521/https://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20251117175521/https://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幺樂団カァニバル！15", "Yougakudann Carnival 15"
            ],
            dates="2026.04.19",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251117175521/https://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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
    
    # ==== event group ====
    media = [
        Medium("eg_banner1_banneryuka.jpg", 
               [Source("https://web.archive.org/web/20100805061627/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_banner2_bannershin.jpg", 
               [Source("https://web.archive.org/web/20100805061627/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["https://yougakudann.dojin.com/", "https://yougakudan.blogspot.com", "https://x.com/yougakudan_info", "https://x.com/yougakudann"]

    event_group = EventGroup(
        aliases=["幺樂団カァニバル", "Yougakudann Carnival"],
        events=[],
        media=media,
        sources=[
            Source('Alias "yougakudann", from url of official blog https://yougakudann.dojin.com/', (ReliabilityTypes.Reliable, OriginTypes.Official)),
        ],
        links=links,
        comments=None,
        description="Doujin events focused on PC-98 Touhou Projects related works.",
    )
    
    # Reorder events and add to event group
    events_raw_sorted = sorted(events_raw, key=lambda er: er['dates'])
    
    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print(f"Saving {Path(__file__).name} database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

