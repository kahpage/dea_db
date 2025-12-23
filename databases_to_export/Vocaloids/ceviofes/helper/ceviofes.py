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
    main_page = "https://www.cevio-festa.com/index.php"

    if True: # ==== ceviofes 1 ====
        i = 1
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("1_1558.png",
                   [Source("https://vocadb.net/E/1558/cevio-festa", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("1_cevio_clear_web.png",
                   [Source("https://web.archive.org/web/20221004105227/https://birdzberth.com/ceviofesta/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3267.750895527388!2d135.7783858753033!3d35.01294036639623!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x600108e5fdb0fb75%3A0x32f576fbc1dc5042!2sMiyako%20Messe%20(Kyoto%20International%20Exhibition%20Hall)!5e0!3m2!1sen!2sfr!4v1766522554867!5m2!1sen!2sfr",
                description="京都市勧業館みやこめっせ （京都ボカロ合同内）",
                sources=[Source("https://web.archive.org/web/20160307144655/http://www.birdzberth.com/ceviofesta/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["CeVIO FeSTA!"],
            dates="2016.03.06",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Participating circles: https://web.archive.org/web/20221004105227/https://birdzberth.com/ceviofesta/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 2 ====
        i = 2
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("2_公開用.png",
                   [Source("https://web.archive.org/web/20170317144513/http://www.cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3267.750895527388!2d135.7783858753033!3d35.01294036639623!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x600108e5fdb0fb75%3A0x32f576fbc1dc5042!2sMiyako%20Messe%20(Kyoto%20International%20Exhibition%20Hall)!5e0!3m2!1sen!2sfr!4v1766522554867!5m2!1sen!2sfr",
                description="京都市勧業館みやこめっせ",
                sources=[Source("https://web.archive.org/web/20170317144513/http://www.cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["CeVIO FeSTA!!"],
            dates="2017.03.05",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20170317144513/http://www.cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 3 ====
        i = 3
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("3_2018.png",
                   [Source("https://web.archive.org/web/20170913083225/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_DWTwlRYVAAE7FmG.png",
                   [Source("https://x.com/CeVIO_FeSTA/status/965161036776071175/photo/1", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3270.3698286546264!2d135.7483044753005!3d34.9473382699402!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60010587a8d65d7b%3A0xc0fa6c9a0c5ce765!2sKy%C5%8Dto%20Pulse%20Plaza!5e0!3m2!1sen!2sfr!4v1766525117766!5m2!1sen!2sfr",
                description="京都府総合見本市会館",
                sources=[Source("https://web.archive.org/web/20170913083225/https://cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["CeVIO FeSTA!!!"],
            dates="2018.02.25",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20170913083225/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 4 ====
        i = 4
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("4_2019.png",
                   [Source("https://web.archive.org/web/20180818143623/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3261.8799848060507!2d136.89817667530988!3d35.15961375845239!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6003773304255e3f%3A0xd4139c5263a87615!2zSmFwYW4sIOOAkjQ2MC0wMDExIEFpY2hpLCBOYWdveWEsIE5ha2EgV2FyZCwgxYxzdSwgMi1jaMWNbWXiiJIxOSDmhJvnn6XnnIzkuK3lsI_kvIHmpa3npo_npYnkvJrppKg!5e0!3m2!1sen!2sfr!4v1766525204354!5m2!1sen!2sfr",
                description="名古屋企業福祉会館",
                sources=[Source("https://web.archive.org/web/20180818143623/https://cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["CeVIO FeSTA 4"],
            dates="2019.04.14",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20180818143623/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 5 ====
        i = 5
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("5_2020.png",
                   [Source("https://web.archive.org/web/20191116214326/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3267.750895527388!2d135.7783858753033!3d35.01294036639623!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x600108e5fdb0fb75%3A0x32f576fbc1dc5042!2sMiyako%20Messe%20(Kyoto%20International%20Exhibition%20Hall)!5e0!3m2!1sen!2sfr!4v1766522554867!5m2!1sen!2sfr",
                description="京都市勧業館みやこめっせ",
                sources=[Source("https://web.archive.org/web/20191116214326/https://cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["CeVIO FeSTA 5"],
            dates="2020.04.05",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20191116214326/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles, since next archived version refers to 2021 event and has different list: https://web.archive.org/web/20210119085129/https://www.cevio-festa.com/circlelist.php", (ReliabilityTypes.Likely, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 6 ====
        i = 6
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("6_2021.jpg",
                   [Source("https://web.archive.org/web/20201109072533/https://www.cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3261.8799848060507!2d136.89817667530988!3d35.15961375845239!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6003773304255e3f%3A0xd4139c5263a87615!2zSmFwYW4sIOOAkjQ2MC0wMDExIEFpY2hpLCBOYWdveWEsIE5ha2EgV2FyZCwgxYxzdSwgMi1jaMWNbWXiiJIxOSDmhJvnn6XnnIzkuK3lsI_kvIHmpa3npo_npYnkvJrppKg!5e0!3m2!1sen!2sfr!4v1766525204354!5m2!1sen!2sfr",
                description="名古屋企業福祉会館",
                sources=[Source("https://web.archive.org/web/20201109072533/https://www.cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["CeVIO FeSTA 6"],
            dates="2021.03.27",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20201109072533/https://www.cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20210920025821/https://www.cevio-festa.com/circlelist.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 7 ====
        i = 7
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("7_2022.png",
                   [Source("https://web.archive.org/web/20220401025719/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3261.8799848060507!2d136.89817667530988!3d35.15961375845239!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6003773304255e3f%3A0xd4139c5263a87615!2zSmFwYW4sIOOAkjQ2MC0wMDExIEFpY2hpLCBOYWdveWEsIE5ha2EgV2FyZCwgxYxzdSwgMi1jaMWNbWXiiJIxOSDmhJvnn6XnnIzkuK3lsI_kvIHmpa3npo_npYnkvJrppKg!5e0!3m2!1sen!2sfr!4v1766525204354!5m2!1sen!2sfr",
                description="名古屋企業福祉会館",
                sources=[Source("https://web.archive.org/web/20220401025719/https://cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["CeVIO FeSTA 7"],
            dates="2022.07.10",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20220401025719/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20220704054542/https://www.cevio-festa.com/circlelist.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 8 ====
        i = 8
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("8_2023.png",
                   [Source("https://web.archive.org/web/20221129144933/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3261.8799848060507!2d136.89817667530988!3d35.15961375845239!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6003773304255e3f%3A0xd4139c5263a87615!2zSmFwYW4sIOOAkjQ2MC0wMDExIEFpY2hpLCBOYWdveWEsIE5ha2EgV2FyZCwgxYxzdSwgMi1jaMWNbWXiiJIxOSDmhJvnn6XnnIzkuK3lsI_kvIHmpa3npo_npYnkvJrppKg!5e0!3m2!1sen!2sfr!4v1766525204354!5m2!1sen!2sfr",
                description="名古屋企業福祉会館",
                sources=[Source("https://web.archive.org/web/20221129144933/https://cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["CeVIO FeSTA 8"],
            dates="2023.03.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20221129144933/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20230323120603/https://cevio-festa.com/circlelist.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 9 ====
        i = 9
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("9_2024.png",
                   [Source("https://web.archive.org/web/20231207233306/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3261.8799848060507!2d136.89817667530988!3d35.15961375845239!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6003773304255e3f%3A0xd4139c5263a87615!2zSmFwYW4sIOOAkjQ2MC0wMDExIEFpY2hpLCBOYWdveWEsIE5ha2EgV2FyZCwgxYxzdSwgMi1jaMWNbWXiiJIxOSDmhJvnn6XnnIzkuK3lsI_kvIHmpa3npo_npYnkvJrppKg!5e0!3m2!1sen!2sfr!4v1766525204354!5m2!1sen!2sfr",
                description="名古屋企業福祉会館",
                sources=[Source("https://web.archive.org/web/20231207233306/https://cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["CeVIO FeSTA 9"],
            dates="2024.03.03",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20231207233306/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20240211105835/https://www.cevio-festa.com/circlelist.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ceviofes 10 ====
        i = 10
        name = f"ceviofes{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("10_2025.png",
                   [Source("https://web.archive.org/web/20241113154506/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3266.350537890214!2d136.84010438885497!3d35.047974200000006!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6003790005e237bb%3A0x74023c0e5069057b!2z44Od44O844OI44Oh44OD44K744Gq44GU44KEIOOCpOODmeODs-ODiOmkqA!5e0!3m2!1sen!2sfr!4v1766526153606!5m2!1sen!2sfr",
                description="ポートメッセなごや イベント館",
                sources=[Source("https://web.archive.org/web/20241113154506/https://cevio-festa.com/", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["CeVIO FeSTA 10"],
            dates="2025.03.23",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20241113154506/https://cevio-festa.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20250226133003/https://www.cevio-festa.com/circlelist.php", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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
        Medium("eg_banner.jpg",
               [Source("https://web.archive.org/web/20160307144523/http://www.birdzberth.com/ceviofesta/images/banner.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["https://www.cevio-festa.com", "https://x.com/CeVIO_FeSTA", "https://birdzberth.com/ceviofesta/"]

    event_group = EventGroup(
        aliases=["CeVIO FeSTA", "チェビフェス"],
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
    
    print("Saving arts database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

