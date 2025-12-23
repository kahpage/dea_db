# Notes:
# TODO: cross source with thwikicc for links

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
    main_page = "https://koromu-toho.com/"
    thwikicc = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6"

    if True: # ==== koromu 21 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC21%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 21
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("21_krm21-catalog-index.webp",
                   [Source("https://web.archive.org/web/20251004192536/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("21_admission.png-600x600.png",
                   [Source("https://web.archive.org/web/20251004192536/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("21_cosplay.png-600x600.png",
                   [Source("https://web.archive.org/web/20251004192536/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20241203044446/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢21", "Touhou Kouroumu 21", "TK 21", "東方紅楼夢第21回"],
            dates="2025.10.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20241203044446/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20251123144210/https://koromu-toho.com/koromu21/list_cn.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 20 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC20%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 20
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("20_krm20-catalog.webp",
                   [Source("https://web.archive.org/web/20240913135816/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20_admission-1-600x600.png",
                   [Source("https://web.archive.org/web/20240913135816/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20_cos-600x600.png",
                   [Source("https://web.archive.org/web/20240913135816/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20240829155743/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢20", "Touhou Kouroumu 20", "TK 20", "東方紅楼夢第20回"],
            dates="2024.10.06",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20240829155743/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20240829160550/https://koromu-toho.com/koromu20/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 19.5 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC19.5%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = "19.5"
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("19.5_东方红楼梦19.5梦之世纪_魅知之旅2插画1.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("19.5_536px-东方红楼梦19.5梦之世纪_魅知之旅2插画2.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1123.1210291560942!2d141.52740900791073!3d39.32832068826737!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5f85fbe1ea04794b%3A0xc198632485cff120!2sAeria%20Tono!5e0!3m2!1sen!2sfr!4v1766405444450!5m2!1sen!2sfr",
                description="岩手県遠野市　あえりあ遠野",
                sources=[
                    Source("https://web.archive.org/web/20240422210747/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                    Source("Maps point with matching name", (ReliabilityTypes.Guess, OriginTypes.External)),
                    ],
                comments="Name matches but is that a venue ?"
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢19.5", "Touhou Kouroumu 19.5", "TK 19.5", "東方紅楼夢第19.5回"],
            dates="2024.06.01",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20240422210747/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20250615161304/https://yumemichi.koromu-toho.com/koromu19-5_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 19 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC19%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 19
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("19_krm19-catalog-428x605.png",
                   [Source("https://web.archive.org/web/20230902041558/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("19_admission-600x600.png",
                   [Source("https://web.archive.org/web/20230902041558/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("19_cosplay-600x600.png",
                   [Source("https://web.archive.org/web/20230902041558/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20230902041558/https://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢19", "Touhou Kouroumu 19", "TK 19", "東方紅楼夢第19回"],
            dates="2023.10.15",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20230902041558/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/2/https://koromu-toho.com/koromu19_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 18 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC18%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 18
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("18_2022-606x848.png",
                   [Source("https://web.archive.org/web/20220925111326/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("18_livepockettop-600x600.png",
                   [Source("https://web.archive.org/web/20220925111326/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("18_livepocketcostop-640x640.png",
                   [Source("https://web.archive.org/web/20220925111326/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20221001044720/https://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢18", "Touhou Kouroumu 18", "TK 18", "東方紅楼夢第18回"],
            dates="2022.10.09",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20221001044720/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20250908090628/https://koromu-toho.com/koromu18_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 17 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC17%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 17
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("17_livepocket17-top-2646x2646.png",
                   [Source("https://web.archive.org/web/20211024012246/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("17_542px-红楼梦17目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20211006034122/https://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢17", "Touhou Kouroumu 17", "TK 17", "東方紅楼夢第17回"],
            dates="2021.10.10 → 2021.11.28",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20211006034122/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Postponed: previous date https://web.archive.org/web/20211006034122/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20231019122127/https://koromu-toho.com/koromu17_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 16 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC16%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 16
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("16_krm15-top-640x640.png",
                   [Source("https://web.archive.org/web/20200927045502/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("16_519px-红楼梦16目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20201002122935/https://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢16", "Touhou Kouroumu 16", "TK 16", "東方紅楼夢第16回"],
            dates="2020.10.11",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20201002122935/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20231019122157/https://koromu-toho.com/koromu16_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 15 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC15%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 15
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("15_15-catalogb5-1000x1399.png",
                   [Source("https://web.archive.org/web/20191020134959/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪　ホール6C/6D ",
                sources=[Source("https://web.archive.org/web/20191020134959/https://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢15", "Touhou Kouroumu 15", "TK 15", "東方紅楼夢第15回"],
            dates="2019.10.13",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20191020134959/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20250417021630/https://koromu-toho.com/koromu15_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 14 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC14%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 14
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("14_koromu2018-hyoushi-1-800x1140.png",
                   [Source("https://web.archive.org/web/20181007200352/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20181017062536/https://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢14", "Touhou Kouroumu 14", "TK 14", "東方紅楼夢第14回"],
            dates="2018.10.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20181017062536/https://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/2/https://koromu-toho.com/koromu14_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 13 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC13%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 13
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("13_koromu13.png",
                   [Source("https://web.archive.org/web/20170809211619/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("13_红楼梦13目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪・インテックス大阪",
                sources=[Source("https://web.archive.org/web/20170924195613/http://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢13", "Touhou Kouroumu 13", "TK 13", "東方紅楼夢第13回"],
            dates="2017.10.22",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20170924195613/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20241214005853/https://koromu-toho.com/koromu13_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 12 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC12%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 12  
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("12_koromu12.png",
                   [Source("https://web.archive.org/web/20160301025453/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("12_531px-红楼梦12目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20160831164016/http://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢12", "Touhou Kouroumu 12", "TK 12", "東方紅楼夢第12回"],
            dates="2016.10.09",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20160831164016/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20231019122123/https://koromu-toho.com/koromu12_list/list_all.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 11 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC11%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 11
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("11_koromu11.png",
                   [Source("https://web.archive.org/web/20150503102035/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("11_koromu11_cat.png",
                   [Source("https://web.archive.org/web/20151019041421/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("11_539px-红楼梦11插画2.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20151007083501/http://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢11", "Touhou Kouroumu 11", "TK 11", "東方紅楼夢第11回"],
            dates="2015.11.01",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20151007083501/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20231019122150/https://koromu-toho.com/koromu11_list/hall4_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://web.archive.org/web/20231019122124/https://koromu-toho.com/koromu11_list/hall6_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (3): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 10 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC10%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 10
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("10_koromu10.png",
                   [Source("https://web.archive.org/web/20140209024149/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("10_530px-红楼梦10目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20141008031226/http://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢10", "Touhou Kouroumu 10", "TK 10", "東方紅楼夢第10回"],
            dates="2014.10.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20141008031226/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20231019122127/https://koromu-toho.com/koromu10_list/list_koromu10.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 9.5 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC9.5%E5%B1%8A%E6%91%8A%E4%BD%8D" 
        i = "9.5"
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("9.5_527px-红楼梦9.5插画.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("9.5_535px-红楼梦9.5目录.png",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1123.1210291560942!2d141.52740900791073!3d39.32832068826737!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5f85fbe1ea04794b%3A0xc198632485cff120!2sAeria%20Tono!5e0!3m2!1sen!2sfr!4v1766405444450!5m2!1sen!2sfr",
                description="岩手県遠野市　あえりあ遠野",
                sources=[
                    Source("https://web.archive.org/web/20180716085719/http://yumemichi.koromu-toho.com/circle_list.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                    Source("Maps point with matching name", (ReliabilityTypes.Guess, OriginTypes.External)),
                    ],
                comments="Name matches but is that a venue ?"
            ),
        ]
        event = Event(
            aliases=["東方紅楼夢9.5", "Touhou Kouroumu 9.5", "TK 9.5", "東方紅楼夢第9.5回"],
            dates="2014.03.02",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20180716085719/http://yumemichi.koromu-toho.com/circle_list.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20180716085719/http://yumemichi.koromu-toho.com/circle_list.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 9 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC9%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 9
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("9_koromu9_1.jpg",
                   [Source("https://web.archive.org/web/20130627115703/http://koromu-toho.com/pict/koromu9_1.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("9_koromu9.jpg",
                   [Source("https://web.archive.org/web/20130327220917/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("9_红楼梦9目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20130204123145/http://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢9", "Touhou Kouroumu 9", "TK 9", "東方紅楼夢第9回"],
            dates="2013.10.13",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20130204123145/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20231019122155/https://koromu-toho.com/koromu9_list/all_circle_all_9th_4kan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://web.archive.org/web/20231019122120/https://koromu-toho.com/koromu9_list/all_circle_all_9th_5kan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (3): https://web.archive.org/web/20231019122130/https://koromu-toho.com/koromu9_list/all_circle_all_9th_6kan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (4): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 8 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC8%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 8
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("8_koromu8_1.png",
                   [Source("https://web.archive.org/web/20120409043504/http://koromu-toho.com/k/index.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("8_koromu8_2.jpg",
                   [Source("https://web.archive.org/web/20120605034004/http://koromu-toho.com/k/index.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("8_红楼梦8目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20120301115709/http://koromu-toho.com:80/k/index.php", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢8", "Touhou Kouroumu 8", "TK 8", "東方紅楼夢第8回"],
            dates="2012.10.07",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20120301115709/http://koromu-toho.com:80/k/index.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20250815062544/https://koromu-toho.com/k/koromu8_lists/all_circle_all_8th_4.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://web.archive.org/web/20231019122123/https://koromu-toho.com/k/koromu8_lists/all_circle_all_8th_5.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (3): https://web.archive.org/web/20231019122140/https://koromu-toho.com/k/koromu8_lists/all_circle_all_8th_6.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (4): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 7 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC7%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 7
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("7_koromu7_1.jpg",
                   [Source("https://web.archive.org/web/20110519231351/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("7_koromu7_2_1.jpg",
                   [Source("https://web.archive.org/web/20120813113818/http://koromu-toho.com/pict/koromu7_2_1.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("7_koromu7_2_2.jpg",
                   [Source("https://web.archive.org/web/20110919141039/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("7_koromu7_2_3.jpg",
                   [Source("https://web.archive.org/web/20110312084539/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("7_koromu7_2_4.jpg",
                   [Source("https://web.archive.org/web/20110622065649/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("7_红楼梦7目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20110519231351/http://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢7", "Touhou Kouroumu 7", "TK 7", "東方紅楼夢第7回"],
            dates="2011.10.16",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20110519231351/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20130303030517/https://koromu-toho.com/koromu7_list/all_circle_all.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 6 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC6%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 6
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("6_koromu6_1.jpg",
                   [Source("https://web.archive.org/web/20130430120510/http://koromu-toho.com/pict/koromu6_1.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("6_koromu6_2.jpg",
                   [Source("https://web.archive.org/web/20100609041435/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("6_koromu6_4.jpg",
                   [Source("https://web.archive.org/web/20100323192335/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("6_红楼梦6目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪府　インテックス大阪",
                sources=[Source("https://web.archive.org/web/20100812102851/http://koromu-toho.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢6", "Touhou Kouroumu 6", "TK 6", "東方紅楼夢第6回"],
            dates="2010.10.11",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20100812102851/http://koromu-toho.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20110613105558/http://kasumiya.in.coocan.jp/koromu6_circle/all_circle_all.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 5 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC5%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 5
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("5_koromu5_1.jpg",
                   [Source("https://web.archive.org/web/20090316210045/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("5_红楼梦5目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3282.665699941879!2d135.41707937528685!3d34.637887386581454!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e84fcb000001%3A0xc09cc9c85e6b90f2!2sINTEX%20Osaka!5e0!3m2!1sen!2sfr!4v1766404299771!5m2!1sen!2sfr",
                description="大阪・インテックス大阪６号館Ａゾーン",
                sources=[Source("https://web.archive.org/web/20091207065315/http://karen.saiin.net:80/~kouroumu-toho/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢5", "Touhou Kouroumu 5", "TK 5", "東方紅楼夢第5回"],
            dates="2009.10.11",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20091207065315/http://karen.saiin.net:80/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20100210132937/http://karen.saiin.net/~kouroumu-toho/koromu5_spaceNum/A.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 4 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC4%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 4
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("4_koromu4_1.jpg",
                   [Source("https://web.archive.org/web/20080422180210/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_koromu4_2.jpg",
                   [Source("https://web.archive.org/web/20080307130841/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_koromu4_3.jpg",
                   [Source("https://web.archive.org/web/20090226050352/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_红楼梦4目录.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3267.750895527388!2d135.7783858753033!3d35.01294036639623!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x600108e5fdb0fb75%3A0x32f576fbc1dc5042!2sMiyako%20Messe%20(Kyoto%20International%20Exhibition%20Hall)!5e0!3m2!1sen!2sfr!4v1766483868733!5m2!1sen!2sfr",
                description="京都・京都市勧業館みやこめっせ 第３展示場全面",
                sources=[Source("https://web.archive.org/web/20080410200719/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢4", "Touhou Kouroumu 4", "TK 4", "東方紅楼夢第4回"],
            dates="2008.11.02",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20080410200719/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20081014020545/http://karen.saiin.net/~kouroumu-toho/4_last/koromu4_haiti_1.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (2): https://web.archive.org/web/20081014020551/http://karen.saiin.net/~kouroumu-toho/4_last/koromu4_haiti_2.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (3): https://web.archive.org/web/20081011015604/http://karen.saiin.net/~kouroumu-toho/4_last/koromu4_haiti_3.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (4): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 3 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC3%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 3
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("3_koromu3_1.jpg",
                   [Source("https://web.archive.org/web/20070701225227/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_红楼梦3插画2.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("3_红楼梦3插画3.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("3_红楼梦3插画4.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3267.750895527388!2d135.7783858753033!3d35.01294036639623!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x600108e5fdb0fb75%3A0x32f576fbc1dc5042!2sMiyako%20Messe%20(Kyoto%20International%20Exhibition%20Hall)!5e0!3m2!1sen!2sfr!4v1766483868733!5m2!1sen!2sfr",
                description="京都・京都市勧業館みやこめっせ 第３展示場全面",
                sources=[Source("https://web.archive.org/web/20070924233021/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢3", "Touhou Kouroumu 3", "TK 3", "東方紅楼夢第3回"],
            dates="2007.11.04",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20070924233021/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20100111194413/http://karen.saiin.net/~kouroumu-toho/all_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 2 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 2
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("2_koromu.jpg",
                   [Source("https://web.archive.org/web/20070205030700/http://karen.saiin.net:80/~kouroumu-toho/pict/koromu.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("2_koromu2.jpg",
                   [Source("https://web.archive.org/web/20070205030723/http://karen.saiin.net:80/~kouroumu-toho/pict/koromu2.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("2_koromu3.jpg",
                   [Source("https://web.archive.org/web/20070205030730/http://karen.saiin.net:80/~kouroumu-toho/pict/koromu3.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("2_koromu4.jpg",
                   [Source("https://web.archive.org/web/20070205030740/http://karen.saiin.net:80/~kouroumu-toho/pict/koromu4.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("2_koromu5.jpg",
                   [Source("https://web.archive.org/web/20070205030752/http://karen.saiin.net:80/~kouroumu-toho/pict/koromu5.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3267.750895527388!2d135.7783858753033!3d35.01294036639623!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x600108e5fdb0fb75%3A0x32f576fbc1dc5042!2sMiyako%20Messe%20(Kyoto%20International%20Exhibition%20Hall)!5e0!3m2!1sen!2sfr!4v1766483868733!5m2!1sen!2sfr",
                description="京都・京都市勧業館みやこめっせ 第３展示場全面",
                sources=[Source("https://web.archive.org/web/20061006133749/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢2", "Touhou Kouroumu 2", "TK 2", "東方紅楼夢第2回"],
            dates="2006.11.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20061006133749/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20100111195526/http://karen.saiin.net/~kouroumu-toho/all_circle_number.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koromu 1 ====
        thwikicc_local = "https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6/%E7%AC%AC1%E5%B1%8A%E6%91%8A%E4%BD%8D"
        i = 1
        name = f"koromu{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("1_info_1.jpg",
                   [Source("https://web.archive.org/web/20050305115409/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("1_info_2_2.jpg",
                   [Source("https://web.archive.org/web/20050405040816/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("1_kouroumu_top3.jpg",
                   [Source("https://web.archive.org/web/20051116160819/http://karen.saiin.net/~kouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3278.813280603828!2d135.49089977529113!3d34.73510063136704!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e4498ff60287%3A0xac494ef2e8fffd48!2sShin-Osaka%20Sen%E2%80%99i%20City%20(Yumesse)!5e0!3m2!1sen!2sfr!4v1766490000388!5m2!1sen!2sfr",
                description="大阪・新大阪ｾﾝｲｼﾃｨ２号館５階展示場全面",
                sources=[Source("https://web.archive.org/web/20051118055357/http://karen.saiin.net/%7Ekouroumu-toho/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["東方紅楼夢", "Touhou Kouroumu", "TK",
                     "東方紅楼夢1", "Touhou Kouroumu 1", "TK 1", "東方紅楼夢第1回"],
            dates="2005.09.11",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20051118055357/http://karen.saiin.net/%7Ekouroumu-toho/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20100108141708/http://karen.saiin.net/~kouroumu-toho/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    # ==== event group ====
    media = []
    links = ["http://koromu-toho.com/", "http://karen.saiin.net/~kouroumu-toho/", "https://x.com/koromu_th"]

    event_group = EventGroup(
        aliases=["東方紅楼夢", "Touhou Kouroumu", "TK"],
        events=[],
        media=media,
        links=links,
        comments=None,
        description="To see banners media, refer to https://thwiki.cc/%E4%B8%9C%E6%96%B9%E7%BA%A2%E6%A5%BC%E6%A2%A6.",
    )
    
    # Reorder events and add to event group
    events_raw_sorted = sorted(events_raw, key=lambda er: er['dates'])
    
    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print("Saving arts database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

