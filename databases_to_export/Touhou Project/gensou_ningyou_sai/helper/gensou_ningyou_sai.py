# Notes:
# TODO Email them ?

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

    thwikicc = "https://thwiki.cc/%E5%B9%BB%E6%83%B3%E4%BA%BA%E5%BD%A2%E7%A5%AD"

    if True: # ==== gensou_ningyou_sai u ====
        i = "u"
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("u_20130102064718_合同ちらし2.jpg",
                   [Source("https://web.archive.org/web/20130102064718/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("u_530px-幻想人形祭1目录.jpg",
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
                "幻想人形祭・卯", "Gensou Ningyou Sai U",
                "幻想人形祭(1st)", "Gensou Ningyou Sai (1st)"
            ],
            dates="2013.04.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20140307211133/http://yougakudan.blogspot.jp/2013/03/blog-post_26.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles, at least 11 participants but should be 19 according to thwiki.cc (dead) : first post of https://web.archive.org/web/20130421061901/http://yougakudan.blogspot.jp/?m=1", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！4."
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai chou ====
        i = "chou"
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("chou_20140508160625_チラシ_2.jpg",
                   [Source("https://web.archive.org/web/20140508160625/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",
                sources=[Source("https://web.archive.org/web/20160129155153/http://yougakudan.blogspot.jp/2013/03/blog-post.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭・長", "Gensou Ningyou Sai Chou",
                "幻想人形祭(2nd)", "Gensou Ningyou Sai (2nd)"
            ],
            dates="2014.09.14",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20160129155153/http://yougakudan.blogspot.jp/2013/03/blog-post.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！5."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai shimo ====
        i = "shimo"
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("shimo_20160826174801_チラシ統合版.jpg",
                   [Source("https://web.archive.org/web/20160826174801/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3246.738269635372!2d139.6984898753267!3d35.535465037968315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2sKawasaki%20City%20Industrial%20Promotion%20Hall!5e0!3m2!1sen!2sfr!4v1767614782814!5m2!1sen!2sfr",
                description="川崎市産業振興会館",   
                sources=[Source("https://web.archive.org/web/20160818114141/http://yougakudan.blogspot.jp/2013/03/blog-post.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭・霜", "Gensou Ningyou Sai Shimo",
                "幻想人形祭(3rd)", "Gensou Ningyou Sai (3rd)"
            ],
            dates="2016.11.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20160818114141/http://yougakudan.blogspot.jp/2013/03/blog-post.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source('Participating circles: https://web.archive.org/web/20161116020013/http://yougakudan.blogspot.jp/2016/10/6.html', (ReliabilityTypes.Guess, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！6."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai 1 ====
        i = 1
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("1_20171021125833_hp20171111.jpg",
                   [Source("https://web.archive.org/web/20171021125833/http://yougakudann.onlyevent.info/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
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
                "幻想人形祭", "Gensou Ningyou Sai",
                "幻想人形祭1", "Gensou Ningyou Sai 1",
                "幻想人形祭(4th)", "Gensou Ningyou Sai (4th)"
            ],
            dates="2017.11.11",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: web.archive.org/web/20171023135929/http://yougakudan.blogspot.jp/2016/10/7.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！7."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai 2 ====
        i = 2
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
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
                "幻想人形祭2", "Gensou Ningyou Sai 2",
                "幻想人形祭(5th)", "Gensou Ningyou Sai (5th)"
            ],
            dates="2018.09.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20181124073957/http://yougakudan.blogspot.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！8."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai 3 ====
        i = 3
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
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
                "幻想人形祭3", "Gensou Ningyou Sai 3",
                "幻想人形祭(6th)", "Gensou Ningyou Sai (6th)"
            ],
            dates="2019.09.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20251107154156/http://yougakudan.blogspot.com/2016/10/blog-post_24.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！9."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai 4 ====
        i = 4
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
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
                "幻想人形祭4", "Gensou Ningyou Sai 4",
                "幻想人形祭(7th)", "Gensou Ningyou Sai (7th)"
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
            comments="Simultaneous to 幺樂団カァニバル！10."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai 4R ====
        i = "4R"
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
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
                "幻想人形祭4R", "Gensou Ningyou Sai 4R",
                "幻想人形祭(8th)", "Gensou Ningyou Sai (8th)"
            ],
            dates="2021.02.27 → CANCELLED",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20210514014026/http://yougakudann.dojin.com/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Cancelled: https://x.com/yougakudan_info/status/1354041811749097474", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！10R."
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai 5 ====
        i = 5
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
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
                "幻想人形祭5", "Gensou Ningyou Sai 5",
                "幻想人形祭(9th)", "Gensou Ningyou Sai (9th)"
            ],
            dates="2022.03.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20220307155313/http://yougakudann.dojin.com/splist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！11."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== gensou_ningyou_sai 6 ====
        i = 6
        name = f"gensou_ningyou_sai{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("6_531px-幻想人形祭9.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
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
                "幻想人形祭6", "Gensou Ningyou Sai 6",
                "幻想人形祭(10th)", "Gensou Ningyou Sai (10th)"
            ],
            dates="2023.07.09",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://x.com/yougakudan_info/status/1677296406711910400", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20240126080406/https://yougakudann.dojin.com/splist.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Simultaneous to 幺樂団カァニバル！12."
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["https://yougakudann.dojin.com/", "https://yougakudan.blogspot.com", "https://x.com/yougakudan_info", "https://x.com/yougakudann"]

    event_group = EventGroup(
        aliases=[
            "幻想人形祭", "Gensou Ningyou Sai",
        ],
        events=[],
        media=media,
        links=links,
        comments=None,
        description="Child doujin events of 幺樂団カァニバル！ (Yougakudann Carnival).",
    )
    
    # Reorder events and add to event group
    events_raw_sorted = sorted(events_raw, key=lambda er: er['dates'])
    
    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print(f"Saving {Path(__file__).name} database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

