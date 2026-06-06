# https://www.m3net.jp/event/index.php

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
    is_to_add,
)
from pathlib import Path
import json
from typing import Any
from bs4 import BeautifulSoup, Comment
import re
import requests
import lxml

PATH_M3_HELPER = Path(__file__).parent
PATH_M3 = PATH_M3_HELPER.parent
PATH_M3_MEDIA = PATH_M3 / "media"

if __name__ == "__main__":
    save_folder_path = PATH_M3
    events_raw: list[Any] = []
    active_events: list[int | str] = list(range(1, 100)) + ["大阪"]

    i = 1
    if i in active_events:  # ==== M3-01 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/1998s.php"

        media_ = [
            Medium(
                "01_m3_01.jpg",
                [
                    Source(
                        "https://www.m3net.jp/event/1998s.php",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            )
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d405.0289070291701!2d139.7870744599309!3d35.69592640552837!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb36b54452d%3A0xf1a3e2377b154969!2z6LK444GX5Lya6K2w5a6kIOadseS6rOaWh-WFt-WFseWSjOS8mumkqCDmtYXojYnmqYs!5e0!3m2!1sen!2sfr!4v1759867497811!5m2!1sen!2sfr",
                description="東京文具共和会館 2F",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-1998春", "M3-98春"],
            dates="1998.03.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.30",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 2
    if i in active_events:  # ==== M3-02 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/1998f.php"

        media_ = [
            Medium(
                "02_m3_02.jpg",
                [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            )
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="TRC (東京流通センター)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-1998秋", "M3-98秋"],
            dates="1998.09.20",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Positions: deduced from cut image file names at {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.30",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 3
    if i in active_events:  # ==== M3-03 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/1999s.php"

        media_ = [
            Medium(
                "03_m3_03.jpg",
                [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            )
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d405.0289070291701!2d139.7870744599309!3d35.69592640552837!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb36b54452d%3A0xf1a3e2377b154969!2z6LK444GX5Lya6K2w5a6kIOadseS6rOaWh-WFt-WFseWSjOS8mumkqCDmtYXojYnmqYs!5e0!3m2!1sen!2sfr!4v1759867497811!5m2!1sen!2sfr",
                description="東京文具共和会館 2F",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-1999春", "M3-99春"],
            dates="1999.04.18",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.30",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 4
    if i in active_events:  # ==== M3-04 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/1999f.php"

        circles_: list[Circle] = []
        media = [
            Medium(
                "04_m3_04.jpg",
                [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3240.1426955868546!2d139.787468075688!3d35.69810597258177!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb459950641%3A0x99332c088b0f7aa5!2sTokyo%20Wholesale%20Center%20Cooperative!5e0!3m2!1sen!2sfr!4v1760203962030!5m2!1sen!2sfr",
                description="東京卸商センター 3F",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-1999秋", "M3-99秋"],
            dates="1999.10.03",
            circles=circles_,
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.30",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 5
    if i in active_events:  # ==== M3- ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2000s.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3240.1426955868546!2d139.787468075688!3d35.69810597258177!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb459950641%3A0x99332c088b0f7aa5!2sTokyo%20Wholesale%20Center%20Cooperative!5e0!3m2!1sen!2sfr!4v1760203962030!5m2!1sen!2sfr",
                description="東京卸商センター 3F",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2000春"],
            dates="2000.04.23",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.30",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 6
    if i in active_events:  # ==== M3-06 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2000f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="TRC 東京流通センター",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2000秋"],
            dates="2000.11.05",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 7
    if i in active_events:  # ==== M3-07 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2001s.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d405.0289070291701!2d139.7870744599309!3d35.69592640552837!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb36b54452d%3A0xf1a3e2377b154969!2z6LK444GX5Lya6K2w5a6kIOadseS6rOaWh-WFt-WFseWSjOS8mumkqCDmtYXojYnmqYs!5e0!3m2!1sen!2sfr!4v1759867497811!5m2!1sen!2sfr",
                description="東京文具共和会館 2・3F",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2001春"],
            dates="2001.04.30",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 8
    if i in active_events:  # ==== M3-08 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2001f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3240.1426955868546!2d139.787468075688!3d35.69810597258177!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb459950641%3A0x99332c088b0f7aa5!2sTokyo%20Wholesale%20Center%20Cooperative!5e0!3m2!1sen!2sfr!4v1760203962030!5m2!1sen!2sfr",
                description="東京卸商センター 3F",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2001秋"],
            dates="2001.10.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 9
    if i in active_events:  # ==== M3-09 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2002s.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3240.1426955868546!2d139.787468075688!3d35.69810597258177!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb459950641%3A0x99332c088b0f7aa5!2sTokyo%20Wholesale%20Center%20Cooperative!5e0!3m2!1sen!2sfr!4v1760203962030!5m2!1sen!2sfr",
                description="東京卸商センター 3F",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2002春"],
            dates="2002.04.28",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 10
    if i in active_events:  # ==== M3-10 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2002f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3240.1426955868546!2d139.787468075688!3d35.69810597258177!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb459950641%3A0x99332c088b0f7aa5!2sTokyo%20Wholesale%20Center%20Cooperative!5e0!3m2!1sen!2sfr!4v1760203962030!5m2!1sen!2sfr",
                description="東京卸商センター3F展示場",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2002秋"],
            dates="2002.10.27",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 11
    if i in active_events:  # ==== M3-11 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2003s.php"

        media_ = [
            Medium(
                "11_20030430055714_m3_11_cat.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20030430055714/http://mmm.panic.or.jp:80/image/m3_11_cat.jpg",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            )
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2003春"],
            dates="2003.05.04",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 12
    if i in active_events:  # ==== M3-12 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2003f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2003秋"],
            dates="2003.10.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            comments="Lost catalogue cover: https://web.archive.org/web/20031011182500/http://mmm.panic.or.jp:80/m3_12_cat.html",
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 13
    if i in active_events:  # ==== M3- ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2004s.php"

        media_ = [
            Medium(
                "13_m3_13.jpg",
                [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            )
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2004春"],
            dates="2004.05.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 14
    if i in active_events:  # ==== M3-14 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2004f.php"

        media_ = [
            Medium(
                "14_20070728212237_m3_14.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070728212237/http://www.m3net.jp:80/image/m3_14.jpg",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            )
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2004秋"],
            dates="2004.10.09",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 15
    if i in active_events:  # ==== M3-15 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2005s.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2005春"],
            dates="2005.05.01",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            comments="Corrupted catalog image: https://www.m3net.jp/img/event/m3_15.jpg",
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 16
    if i in active_events:  # ==== M3-16 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2005f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2005秋"],  # 春 秋
            dates="2005.11.13",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 17
    if i in active_events:  # ==== M3-17 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2006s.php"

        media_ = [
            Medium(
                "17_20060430015541_m17cat.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20060430015541/http://www.m3net.jp:80/image/m17cat.jpg",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            )
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2006春"],  # 春 秋
            dates="2006.04.29",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circle: https://web.archive.org/web/20061212003031fw_/http://www.m3net.jp/m3_17/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 18
    if i in active_events:  # ==== M3-18 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2006f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2006秋"],  # 春 秋
            dates="2006.10.09",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20061212003359/http://www.m3net.jp/m3_18/circle.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 19
    if i in active_events:  # ==== M3-19 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2007s.php"

        media_ = [
            Medium(
                "19_19_20070308124325_m3_19_planA.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070308124325/http://www.m3net.jp:80/m3_19_planA.jpg",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            )
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2007春"],  # 春 秋
            dates="2007.04.29",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20070714203329/http://www.m3net.jp/m3_19/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 20
    if i in active_events:  # ==== M3-20 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2007f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ・PiO (大展示ホール/小展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2007秋"],  # 春 秋
            dates="2007.10.08",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: http://www.ahoge.com/old/2007event.html (Likely not to have missing circles as it is a 300 space venue and the list has 361 unique space positions)",
                    (ReliabilityTypes.Likely, OriginTypes.External),
                ),
            ],
            locations=locations,
            last_edited="2026.05.30",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    n = "大阪"
    if n in active_events:  # ==== M3-大阪 ====
        name = f"M3-{n}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2008osaka.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3280.626181212536!2d135.4836250756423!3d34.68938297292369!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e658eb20202f%3A0xc3e1552c4163ec4!2sGrand%20Cube%20Osaka%20(Osaka%20International%20Convention%20Center)!5e0!3m2!1sen!2sfr!4v1760221173598!5m2!1sen!2sfr",
                description="グランキューブ大阪 10F会議室(1001～1003)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=["M3-大阪", "M3-OSAKA", "M3-2008osaka"],  # 春 秋
            dates="2008.03.09",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Alias 'M3-2008osaka' from url: https://www.m3net.jp/event/2008osaka.php",
                    (ReliabilityTypes.Likely, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{n}" / f"circles_{n}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 21
    if i in active_events:  # ==== M3-21 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2008s.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ・PiO (大展示ホール/小展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2008春"],  # 春 秋
            dates="2008.05.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 22
    if i in active_events:  # ==== M3-22 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2008f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ・PiO",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2008秋"],  # 春 秋
            dates="2008.10.13",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    n = "Festa"
    if i in active_events:  # ==== M3-Festa ====
        name = f"M3-{n}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2008festa.php"

        media_ = [
            Medium(
                "Festa_haichi.gif",
                [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "Festa_M3Festa.pdf",
                [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "Festa_plan.jpg",
                [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51870.19369178282!2d139.68455124863283!3d35.65515299999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1760220990307!5m2!1sen!2sfr",
                description="東京都立産業貿易センター 浜松町館 3F展示室",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=["M3-Festa", "M3-2008festa", "エムスリーフェスタ"],  # 春 秋
            dates="2008.11.24",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Alias '2008festa' and 'エムスリーフェスタ' from url https://www.m3net.jp/event/2008festa.php",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 23
    if i in active_events:  # ==== M3-23 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2009s.php"

        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25969.42090179059!2d139.70210698661896!3d35.549315445297644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1760204504687!5m2!1sen!2sfr",
                description="大田区産業プラザ PiO (大展示ホール)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2009春"],  # 春 秋
            dates="2009.05.05",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open(
            "r", encoding="utf-8"
        ) as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 24
    if i in active_events:  # ==== M3-24 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2009f.php"

        media_ = [
            # Medium(",
            #        [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))])
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.0809002298374!2d139.6459722753115!3d35.45279154248986!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cffb2d826f7%3A0x9f88529083fb131a!2sOsanbashi%20Hall!5e0!3m2!1sen!2sfr!4v1760205422589!5m2!1sen!2sfr",
                description="大さん橋ホール (横浜港大さん橋国際客船ターミナル内) [会場アクセス] (http://www.osanbashi.com/map/index.html)",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2009秋"], # 春 秋
            dates="2009.10.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    f"Date, Participating circles: {m3_page}",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            last_edited="2026.05.31",
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 25
    if (i in active_events): # ==== M3-25 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2010s.php"

        media_ = [
            Medium("25_20120419064147_manga.jpg",
                   [Source("https://web.archive.org/web/20120419064147/http://www.m3net.jp/m3_25/manga.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))])
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター(TRC)第2展示場 E～Fホール",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2010春"], # 春 秋
            dates="2010.05.05",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date, Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.05.31"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 26
    if (i in active_events): # ==== M3-26 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2010f.php"

        media_ = [
            Medium("26_m3-26_jouei_list.pdf",
                   [Source("https://www.m3net.jp/pdf/m3-26_jouei_list.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))])
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター(TRC)第2展示場 E～Fホール",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2010秋"], # 春 秋
            dates="2010.10.31",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date, Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.05.31"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 27
    if (i in active_events): # ==== M3-27 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2011s.php"

        media_ = [
            Medium("27_20120408214344_m3_27_cat.jpg",
                   [Source("https://web.archive.org/web/20120408214344/http://www.m3net.jp/m3_27/m3_27_cat.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("27_20110722113333_manga.jpg",
                   [Source("https://web.archive.org/web/20110722113333/http://www.m3net.jp/m3_27/manga.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("27_m3-27_jouei_list.pdf",
                   [Source("https://www.m3net.jp/pdf/m3-27_jouei_list.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター(TRC)第1展示場 A～Dホール",
                sources=[
                    Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))
                ],
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2011春"], # 春 秋
            dates="2011.05.01",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date, Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="・動画「M3準備会からのご案内」(ニコニコ動画: http://www.nicovideo.jp/watch/sm14229809\n・YouTube: http://www.youtube.com/watch?v=beGpYk-IKAA)\n・M3-2011春 映像上映作品リスト: https://www.m3net.jp/pdf/m3-27_jouei_list.pdf\nNote: One can see the event catalog cover from the video here https://youtu.be/beGpYk-IKAA?si=LRqQy7kXKiVml7tE&t=126",
            last_edited="2026.05.30"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 28
    if (i in active_events): # ==== M3-28 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2011f.php"

        media_ = [
            Medium("28_m3-28_jouei_list.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("28_m3_28_Halls.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("28_m3_28_D-hall.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("28_20120314232737_m3_28_manga.jpg",
                   [Source("https://web.archive.org/web/20120314232737/http://www.m3net.jp/m3_28/m3_28_manga.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター(TRC)第1展示場、第2展示場",
                sources=[Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2011秋"], # 春 秋
            dates="2011.10.30",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date, Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="・動画「M3準備会からのご案内」([ニコニコ動画](http://www.nicovideo.jp/watch/sm15925549)・[YouTube](http://www.youtube.com/watch?v=EJzzLBHfG20))\n・[M3-2011秋 映像上映作品リスト](https://www.m3net.jp/pdf/m3-28_jouei_list.pdf)",
            last_edited="2026.05.31"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 29
    if (i in active_events): # ==== M3-29 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2012s.php"

        media_ = [
            Medium("29_20130605070138_m3_29_cat.jpg",
                   [Source("https://web.archive.org/web//http://www.m3net.jp/img/event/m3_29_cat.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_m3_29_E-hall.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_2019042729_20120601035300_imgIndex01.jpg",
                   [Source("https://web.archive.org/web/20120601035300/http://www.m3net.jp/img/imgIndex01.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_01.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/01.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_02.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/02.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_03.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/03.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_04.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/04.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_05.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/05.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_06.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/06.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162719_07.jpg",
                   [Source("https://web.archive.org/web/20190427162719/http://www.m3net.jp/img/enjoy/07.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_08.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/08.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_09.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/09.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162717_10.jpg",
                   [Source("https://web.archive.org/web/20190427162717/http://www.m3net.jp/img/enjoy/10.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162718_11.jpg",
                   [Source("https://web.archive.org/web/20190427162718/http://www.m3net.jp/img/enjoy/11.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162718_12.jpg",
                   [Source("https://web.archive.org/web/20190427162718/http://www.m3net.jp/img/enjoy/12.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162719_13.jpg",
                   [Source("https://web.archive.org/web/20190427162719/http://www.m3net.jp/img/enjoy/13.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162718_14.jpg",
                   [Source("https://web.archive.org/web/20190427162718/http://www.m3net.jp/img/enjoy/14.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162719_15.jpg",
                   [Source("https://web.archive.org/web/20190427162719/http://www.m3net.jp/img/enjoy/15.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162718_16.jpg",
                   [Source("https://web.archive.org/web/20190427162718/http://www.m3net.jp/img/enjoy/16.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162718_17.jpg",
                   [Source("https://web.archive.org/web/20190427162718/http://www.m3net.jp/img/enjoy/17.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162719_18.jpg",
                   [Source("https://web.archive.org/web/20190427162719/http://www.m3net.jp/img/enjoy/18.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("29_20190427162719_19.jpg",
                   [Source("https://web.archive.org/web/20190427162719/http://www.m3net.jp/img/enjoy/19.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター(TRC)第一展示場、第二展示場",
                sources=[Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2012春"], # 春 秋
            dates="2012.04.30",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date, Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.05.31"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 30
    if (i in active_events): # ==== M3-30 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2012f.php"

        media_ = [
            Medium("30_20130115050030_imgIndex2012f.jpg",
                   [Source("https://web.archive.org/web/20130115050030/http://www.m3net.jp/img/imgIndex2012f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("30_20130125132558_imgIndex2012f_a.jpg",
                   [Source("https://web.archive.org/web/20130125132558/http://www.m3net.jp/img/imgIndex2012f_a.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("30_M3-30_Halls.pdf",
                   [Source("https://www.m3net.jp/pdf/M3-30_Halls.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))])
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="TRC 第二展示場1階[Eホール]",
                sources=[Source("https://www.m3net.jp/pdf/M3-30_kigyo_haichi.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2012秋"], # 春 秋
            dates="2012.10.28",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://puellabyte.github.io/events", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.01"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 31
    if (i in active_events): # ==== M3-31 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2013s.php"

        media_ = [
            Medium("31_20130517122334_m3_31_cat.jpg",
                   [Source("https://web.archive.org/web//http://www.m3net.jp/m3_31/m3_31_cat.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("31_M3-31_cat_errata.pdf",
                   [Source("https://www.m3net.jp/pdf/M3-31_cat_errata.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("31_20190926073700_imgIndex2013.jpg",
                   [Source("https://web.archive.org/web/20190926073700/http://www.m3net.jp/img/imgIndex2013.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("31_20130507091950_imgIndex2013end.jpg",
                   [Source("https://web.archive.org/web/20130507091950/http://www.m3net.jp/img/imgIndex2013end.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC 第一展示場/第二展示場)",
                sources=[Source("M3-31 catalog cover", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2013春"], # 春 秋
            dates="2013.04.29",
            circles=[],
            media=media_,
            sources=[
                Source("Date: M3-31 catalog cover", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.01"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 32
    if (i in active_events): # ==== M3-32 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2013f.php"

        media_ = [
            Medium("32_20131221180300_imgIndex2013Autumn.jpg",
                   [Source("https://web.archive.org/web/20131221180300/http://www.m3net.jp/img/imgIndex2013Autumn.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("32_M3-32_haichi.pdf",
                   [Source("https://www.m3net.jp/event/2013f.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 32_20131221180300_imgIndex2013Autumn.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2013秋"], # 春 秋
            dates="2013.10.27",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date, Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.01"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 33
    if (i in active_events): # ==== M3-33 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2014s.php"

        media_ = [
            Medium("33_20141111192532_imgIndex2014s.jpg",
                   [Source("https://web.archive.org/web/20141111192532/http://www.m3net.jp/img/imgIndex2014s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("33_20140528025710_imgIndex2014sEnd.jpg",
                   [Source("https://web.archive.org/web/20140528025710/http://www.m3net.jp/img/imgIndex2014sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("33_M3-33_haichi.pdf",
                   [Source("https://www.m3net.jp/event/2014s.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 33_20140528025710_imgIndex2014sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2014春"], # 春 秋
            dates="2014.04.27",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date, Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.01"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 34
    if (i in active_events): # ==== M3-34 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2014f.php"

        media_ = [
            Medium("34_20140712122657_imgIndex2014f.jpg",
                   [Source("https://web.archive.org/web/20140712122657/http://www.m3net.jp/img/imgIndex2014f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("34_20141124155949_imgIndex2014fEnd.jpg",
                   [Source("https://web.archive.org/web/20141124155949/http://www.m3net.jp/img/imgIndex2014fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("34_m3_34_Halls.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 34_20140712122657_imgIndex2014f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2014秋"], # 春 秋
            dates="2014.10.26",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 34_20140712122657_imgIndex2014f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.01"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 35
    if (i in active_events): # ==== M3-35 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2015s.php"

        media_ = [
            Medium("35_m3_35_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog35.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("35_20150213014104_imgIndex2015s.jpg",
                   [Source("https://web.archive.org/web/20150213014104/http://www.m3net.jp/img/imgIndex2015s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("35_m3_35_Halls.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 35_20150213014104_imgIndex2015s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2015春"], # 春 秋
            dates="2015.04.26",
            circles=[],
            media=media_,
            sources=[
                Source("Date: M3-35 catalog cover", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 36
    if (i in active_events): # ==== M3-36 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2015f.php"

        media_ = [
            Medium("36_m3_36_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog36.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("36_20150816062748_imgIndex2015f.jpg",
                   [Source("https://web.archive.org/web/20190212000000*/http://www.m3net.jp/img/imgIndex2015f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("36_20160103053158_imgIndex2015fEnd.jpg",
                   [Source("https://web.archive.org/web/20160103053158/http://www.m3net.jp/img/imgIndex2015fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("36_m3-36_plan.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 36_20150816062748_imgIndex2015f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2015秋"], # 春 秋
            dates="2015.10.25",
            circles=[],
            media=media_,
            sources=[
                Source("Date: 36_20150816062748_imgIndex2015f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 37
    if (i in active_events): # ==== M3-37 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2016s.php"

        media_ = [
            Medium("37_m3_37_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog37.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("37_20160109110605_imgIndex2016s.jpg",
                   [Source("https://web.archive.org/web/20160109110605/http://www.m3net.jp/img/imgIndex2016s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("37_20210401053258_imgIndex2016sEnd.jpg",
                   [Source("https://web.archive.org/web/20210401053258/http://www.m3net.jp/img/imgIndex2016sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("37_M3tuushin37map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 37_20210401053258_imgIndex2016sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2016春"], # 春 秋
            dates="2016.04.24",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 37_20210401053258_imgIndex2016sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 38
    if (i in active_events): # ==== M3-38 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2016f.php"

        media_ = [
            Medium("38_m3_38_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog38.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("38_20160611160224_imgIndex2016f.jpg",
                   [Source("https://web.archive.org/web/20160611160224/http://www.m3net.jp/img/imgIndex2016f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("38_20170311112851_imgIndex2016fEnd.jpg",
                   [Source("https://web.archive.org/web/20170311112851/http://www.m3net.jp/img/imgIndex2016fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("38_M3tuushin38map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 38_20160611160224_imgIndex2016f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2016秋"], # 春 秋
            dates="2016.10.30",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 38_20160611160224_imgIndex2016f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 39
    if (i in active_events): # ==== M3-39 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2017s.php"

        media_ = [
            Medium("39_m3_39_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog39.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("39_20170427161949_imgIndex2017s.jpg",
                   [Source("https://web.archive.org/web/20170427161949/http://www.m3net.jp/img/imgIndex2017s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("39_20180131140958_imgIndex2017sEnd.jpg",
                   [Source("https://web.archive.org/web/20180131140958/http://www.m3net.jp/img/imgIndex2017sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("39_M3tuushin39map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 39_20180131140958_imgIndex2017sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2017春"], # 春 秋
            dates="2017.04.30",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 39_20180131140958_imgIndex2017sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 40
    if (i in active_events): # ==== M3-40 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2017f.php"

        media_ = [
            Medium("40_m3_40_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog40.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("40_20170609033859_imgIndex2017f.jpg",
                   [Source("https://web.archive.org/web/20170609033859/http://www.m3net.jp/img/imgIndex2017f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("40_M3tuushin40map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 40_20170609033859_imgIndex2017f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2017秋"], # 春 秋
            dates="2017.10.29",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 40_20170609033859_imgIndex2017f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 41
    if (i in active_events): # ==== M3- ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2018s.php"

        media_ = [
            Medium("41_m3_41_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog41.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("41_20180128180033_imgIndex2018s.jpg",
                   [Source("https://web.archive.org/web/20180128180033/http://www.m3net.jp/img/imgIndex2018s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("41_20220104002001_imgIndex2018sEnd.jpg",
                   [Source("https://web.archive.org/web/20220104002001/http://www.m3net.jp/img/imgIndex2018sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("41_M3tuushin41map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 41_20220104002001_imgIndex2018sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2018春"], # 春 秋
            dates="2018.04.29",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 41_20220104002001_imgIndex2018sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 42
    if (i in active_events): # ==== M3-42 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/2018f.php"

        media_ = [
            Medium("42_m3_42_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog42.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("42_20180723112533_imgIndex2018f.jpg",
                   [Source("https://web.archive.org/web/20180723112533/http://www.m3net.jp/img/imgIndex2018f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("42_20181209080559_imgIndex2018fEnd.jpg",
                   [Source("https://web.archive.org/web/20181209080559/http://www.m3net.jp/img/imgIndex2018fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("42_M3tuushin42map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 42_20181209080559_imgIndex2018fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2018秋"], # 春 秋
            dates="2018.10.28",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 42_20181209080559_imgIndex2018fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 43
    if (i in active_events): # ==== M3-43 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2019s.php"

        media_ = [
            Medium("43_m3_43_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog43.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("43_20190402133304_imgIndex2019s.jpg",
                   [Source("https://web.archive.org/web/20190402133304/http://www.m3net.jp/img/imgIndex2019s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("43_20190503065746_imgIndex2019End.jpg",
                   [Source("https://web.archive.org/web/20190503065746/http://www.m3net.jp/img/imgIndex2019End.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("43_M3tuushin43map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 43_20190402133304_imgIndex2019s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2019春"], # 春 秋
            dates="2019.04.28",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 43_20190402133304_imgIndex2019s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 44
    if (i in active_events): # ==== M3-44 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2019f.php"

        media_ = [
            Medium("44_m3_44_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog44.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("44_20190702045120_imgIndex2019f.jpg",
                   [Source("https://web.archive.org/web/20190702045120/http://www.m3net.jp/img/imgIndex2019f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("44_20191216124254_imgIndex2019fEnd.jpg",
                   [Source("https://web.archive.org/web/20191216124254/http://www.m3net.jp/img/imgIndex2019fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("44_M3tuushin44map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 44_20191216124254_imgIndex2019fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2019秋"], # 春 秋
            dates="2019.10.27",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 44_20191216124254_imgIndex2019fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 45
    if (i in active_events): # ==== M3-45 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2020s.php"

        media_ = [
            Medium("45_m3_45_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog45.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("45_20200217232440_imgIndex2020s.jpg",
                   [Source("https://web.archive.org/web/20200217232440/http://www.m3net.jp/img/imgIndex2020s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("45_20200303013824_imgIndex2020sEnd.jpg",
                   [Source("https://web.archive.org/web/20200303013824/https://www.m3net.jp/img/imgIndex2020sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("45_M3tuushin45map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 45_20200303013824_imgIndex2020sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2020春"], # 春 秋
            dates="2020.03.01",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 45_20200303013824_imgIndex2020sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 46
    if (i in active_events): # ==== M3-46 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2020f.php"

        media_ = [
            Medium("46_m3_46_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog46.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("46_20200724144638_imgIndex2020f.jpg",
                   [Source("https://web.archive.org/web/20200724144638/http://www.m3net.jp/img/imgIndex2020f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("46_20201030151801_imgIndex2020f_.jpg",
                   [Source("https://web.archive.org/web/20201030151801/http://www.m3net.jp/img/imgIndex2020f_.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("46_20201109184917_imgIndex2020fEnd_.jpg",
                   [Source("https://web.archive.org/web/20201109184917/https://www.m3net.jp/img/imgIndex2020fEnd_.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("46_M3tuushin46map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("46_m3-46_virtualLayout.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 46_20200724144638_imgIndex2020f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
            Location(
                description="+ Web event (https://www.m3net.jp/m3_46/m3-46_virtualLayout.pdf)",
                sources=[Source("Banner 46_20201109184917_imgIndex2020fEnd_.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2020秋"], # 春 秋
            dates="2020.10.25",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 46_20200724144638_imgIndex2020f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note & Virtual participations: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: 島番号[A]～[R]は第一展示場、[あ]～[か]は第二展示場1階、[キ]～[ス]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 47
    if (i in active_events): # ==== M3-47 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2021s.php"

        media_ = [
            Medium("47_m3_47_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog47.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("47_20210126193207_imgIndex2021s.jpg",
                   [Source("https://web.archive.org/web/20210126193207/http://www.m3net.jp/img/imgIndex2021s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("47_20210506023407_imgIndex2021sEnd.jpg",
                   [Source("https://web.archive.org/web/20210506023407/http://www.m3net.jp/img/imgIndex2021sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("47_M3tuushin47map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("47_m3-47_WebEvent_Map.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 47_20210126193207_imgIndex2021s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
            Location(
                description="+ Web event (https://www.m3net.jp/m3_47/m3-47_WebEvent_Map.pdf)",
                sources=[Source("Banner 47_20210126193207_imgIndex2021s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2021春"], # 春 秋
            dates="2021.04.25",
            circles=[],
            media=media_,
            sources=[
                Source("Date: 47_20210126193207_imgIndex2021s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note & Virtual participations: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: 島番号[A]～[R]は第一展示場、[あ]～[か]は第二展示場1階、[キ]～[ス]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 48
    if (i in active_events): # ==== M3-48 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2021f.php"

        media_ = [
            Medium("48_m3_48_catA.png",
                   [Source("http://www.m3net.jp/attendance/catalog48.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("48_m3_48_catB.png",
                   [Source("http://www.m3net.jp/attendance/catalog48.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("48_20210705071611_imgIndex2021f.jpg",
                   [Source("https://web.archive.org/web/20210705071611/http://www.m3net.jp/img/imgIndex2021f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("48_20211113163225_imgIndex2021fEnd.jpg",
                   [Source("https://web.archive.org/web/20211113163225/https://www.m3net.jp/img/imgIndex2021fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("48_M3tuushin48map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("48_m3-48_WebEvent_Map.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 48_20210705071611_imgIndex2021f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
            Location(
                description="+ Web event (https://www.m3net.jp/m3_48/m3-48_WebEvent_Map.pdf)",
                sources=[Source("Banner 48_20210705071611_imgIndex2021f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2021秋"], # 春 秋
            dates="2021.10.31",
            circles=[],
            media=media_,
            sources=[
                Source("Date: 48_20210705071611_imgIndex2021f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note & Virtual participations: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: 島番号[A]～[T]は第一展示場、[あ]～[か]は第二展示場1階、[キ]～[ス]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 49
    if (i in active_events): # ==== M3-49 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2022s.php"

        media_ = [
            Medium("49_m3_49_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog49.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("49_20220324121958_imgIndex2022s.jpg",
                   [Source("https://web.archive.org/web/20220324121958/https://www.m3net.jp/img/imgIndex2022s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("49_20220516163402_imgIndex2022sEnd.jpg",
                   [Source("https://web.archive.org/web/20220516163402/http://www.m3net.jp/img/imgIndex2022sEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("49_M3tuushin49map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("49_m3-49_WebEvent_Map.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 49_20220324121958_imgIndex2022s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
            Location(
                description="+ Web event (https://www.m3net.jp/m3_49/m3-49_WebEvent_Map.pdf)",
                sources=[Source("Banner 49_20220324121958_imgIndex2022s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2022春"], # 春 秋
            dates="2022.04.24",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 49_20220324121958_imgIndex2022s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note & Virtual participations: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: 島番号[A]～[P]は第一展示場、[あ]～[お]は第二展示場1階、[カ]～[サ]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 50
    if (i in active_events): # ==== M3-50 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2022f.php"

        media_ = [
            Medium("50_m3_50_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog50.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("50_20220702115333_imgIndex2022f.jpg",
                   [Source("https://web.archive.org/web/20220702115333/https://www.m3net.jp/img/imgIndex2022f.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("50_20221203141601_imgIndex2022fEnd.jpg",
                   [Source("https://web.archive.org/web/20221203141601/http://www.m3net.jp/img/imgIndex2022fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("50_M3tuushin50map_web.pdf",
                   [Source("https://www.m3net.jp/event/circle2022f.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 50_20221203141601_imgIndex2022fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2022秋"], # 春 秋
            dates="2022.10.30",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 50_20221203141601_imgIndex2022fEnd.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://catalog.m3net.jp/2022f/circles.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: 島番号[A]～[R]は第一展示場、[あ]～[お]は第二展示場1階、[カ]～[サ]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.06"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 51
    if (i in active_events): # ==== M3-51 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2023s.php"

        media_ = [
            Medium("51_m3_51_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog51.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("51_imgIndex2023S.png",
                   [Source("https://web.archive.org/web/20230412061554/http://www.m3net.jp/img/imgIndex2023S.png", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("51_imgIndex2023S_0501.png",
                   [Source("https://web.archive.org/web/20230502163708/https://www.m3net.jp/img/imgIndex2023S_0501.png", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("51_M3tuushin51map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 51_imgIndex2023S_0501.png", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2023春"], # 春 秋
            dates="2023.04.30",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 51_imgIndex2023S_0501.png", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://catalog.m3net.jp/2023s/circles.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note 2: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: on https://www.m3net.jp/event/circle2023s.php, M3tuushin53map_web.pdf is linked instead of M3tuushin51map_web.pdf\nNote: 島番号[A]～[Q]は第一展示場、[あ]～[お]は第二展示場1階、[カ]～[サ]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.06"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 52
    if (i in active_events): # ==== M3-52 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2023f.php"

        media_ = [
            Medium("52_m3_52_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog52.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("52_keyvisual.png",
                   [Source("https://catalog.m3net.jp/2023f/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20250915124428/https://www.m3net.jp/m3_52/M3-2023F.catalog.pdf",
                   [Source("https://web.archive.org/web/20250915124428/https://www.m3net.jp/m3_52/M3-2023F.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("52_M3tuushin52map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Catalog (M3-2023F.catalog.pdf)", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2023秋"], # 春 秋
            dates="2023.10.29",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Catalog (M3-2023F.catalog.pdf)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://catalog.m3net.jp/2023f/circles.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: 島番号[A]～[T]は第一展示場、[あ]～[か]は第二展示場1階、[キ]～[ス]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 53
    if (i in active_events): # ==== M3-53 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2024s.php"

        media_ = [
            Medium("53_m3_53_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog53.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("53_20240330230728_imgIndex2024s.jpg",
                   [Source("https://web.archive.org/web/20231216012914/https://www.m3net.jp/img/imgIndex2024s.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("53_20240612092213_imgIndex2024s_w-end.jpg",
                   [Source("https://web.archive.org/web/20240612092213/https://www.m3net.jp/img/imgIndex2024s_w-end.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("53_M3tuushin53map_web.pdf",
                   [Source("http://www.m3net.jp/m3_53/M3tuushin53map_web.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20240612185411/https://www.m3net.jp/m3_53/M3-2024S.catalog.pdf",
                   [Source("https://web.archive.org/web/20240612185411/https://www.m3net.jp/m3_53/M3-2024S.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 53_20240612092213_imgIndex2024s_w-end.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2024春"], # 春 秋
            dates="2024.04.28",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 53_20240612092213_imgIndex2024s_w-end.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://catalog.m3net.jp/2024s/circles.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: 島番号[A]～[T]は第一展示場、[あ]～[か]は第二展示場1階、[キ]～[ス]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 54
    if (i in active_events): # ==== M3-54 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/event/circle2024f.php"

        media_ = [
            Medium("54_m3_54_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog54.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("54_20240805075053_imgIndex2024a.jpg",
                   [Source("https://web.archive.org/web/20240805075053/http://www.m3net.jp/img/imgIndex2024a.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("54_20241113232004_imgIndex2024a_w-end.jpg",
                   [Source("https://web.archive.org/web/20241113232004/https://www.m3net.jp/img/imgIndex2024a_w-end.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("54_M3tuushin54map_web.pdf",
                   [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20250427031227/https://www.m3net.jp/m3_54/M3-2024F.catalog.pdf",
                   [Source("https://web.archive.org/web/20250427031227/https://www.m3net.jp/m3_54/M3-2024F.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Catalog: M3-2024F.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2024秋"], # 春 秋
            dates="2024.10.27",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Catalog M3-2024F.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://catalog.m3net.jp/2024f/circles.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Note: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Note: 島番号[A]～[V]は第一展示場、[あ]～[か]は第二展示場1階、[キ]～[シ]は第二展示場2階、[黒]～[金]はWeb会場です。",
            last_edited="2026.06.02"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 55
    if (i in active_events): # ==== M3-55 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://www.m3net.jp/attendance/circle2025s.php"

        media_ = [
            Medium("55_m3_55_cat.png",
                   [Source("http://www.m3net.jp/attendance/catalog55.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("55_keyvisual.png",
                   [Source("https://catalog.m3net.jp/archive/2025s/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("55_M3tuushin55map_web.pdf",
                   [Source("https://www.m3net.jp/attendance/circle2025s.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20250713022024/https://www.m3net.jp/m3_55/M3-2025S.catalog.pdf",
                   [Source("https://web.archive.org/web/20250713022024/https://www.m3net.jp/m3_55/M3-2025S.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("Banner 55_keyvisual.png", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2025春"], # 春 秋
            dates="2025.04.27",
            circles=[],
            media=media_,
            sources=[
                Source("Date: Banner 55_keyvisual.png", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://catalog.m3net.jp/2025s/circles.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.04"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 56
    if (i in active_events): # ==== M3-56 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")
        m3_page = "https://catalog.m3net.jp/2025f/circles.html"

        media_ = [
            Medium("56_M3-2025F.catalog.png",
                   [Source("First page of https://www.m3net.jp/m3_56/M3-2025F.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("56_keyvisual.webp",
                   [Source("https://catalog.m3net.jp/2025f/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("56_M3tuushin56map_web.pdf",
                   [Source("https://www.m3net.jp/attendance/circle2025f.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://www.m3net.jp/m3_56/M3-2025F.catalog.pdf",
                   [Source("https://www.m3net.jp/m3_56/M3-2025F.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("https://catalog.m3net.jp/2025f/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2025秋"],
            dates="2025.10.06",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://catalog.m3net.jp/2025f/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://catalog.m3net.jp/2025f/circles.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.05"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    i = 57
    if (i in active_events): # ==== M3-57 ====
        name = f"M3-{i:02d}"
        print(f"Processing {name} ...")

        media_ = [
            Medium("57_canvas.png",
                   [Source("First page of https://www.m3net.jp/m3_57/M3-2026S.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("57_keyvisual_2026s.png",
                   [Source("https://catalog.m3net.jp/2026s/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://www.m3net.jp/m3_57/M3-2026S.catalog.pdf",
                   [Source("https://www.m3net.jp/m3_57/M3-2026S.catalog.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("57_M3tuushin57map_web.pdf",
                   [Source("https://www.m3net.jp/attendance/circle2026s.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("",
                   [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
                description="東京流通センター (TRC)",
                sources=[Source("https://catalog.m3net.jp/2026s/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=[f"M3-{i:02d}", "M3-2026春"],
            dates="2026.04.26",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://catalog.m3net.jp/2026s/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://catalog.m3net.jp/2026s/circles/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.06.05"
        )
        event_raw = event.get_json()
        # Retrieve circles
        with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    # i = 
    # if (i in active_events): # ==== M3- ====
    #     name = f"M3-{i:02d}"
    #     print(f"Processing {name} ...")
    #     m3_page =

    #     media_ = [
    #         Medium("",
    #                [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    #         Medium("",
    #                [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    #         Medium("",
    #                [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    #         Medium("",
    #                [Source(, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    #         ]
    #     locations = [
    #         Location(
    #             iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6489.961600896923!2d139.7417581761773!3d35.57886570190225!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186178f12a486d%3A0x4fc2afb490aab5f6!2sTokyo%20Ryutsu%20Center!5e0!3m2!1sen!2sfr!4v1759871108185!5m2!1sen!2sfr",
    #             description="東京流通センター (TRC)",
    #             sources=[Source("Banner ", (ReliabilityTypes.Reliable, OriginTypes.Official))]
    #         ),
    #     ]
    #     event = Event(
    #         aliases=["M3-", "M3-", "M3-"],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             Source("Date: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
    #             Source(f"Participating circles: {m3_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
    #         ],
    #         locations=locations,
    #         last_edited="2026.06.02"
    #     )
    #     event_raw = event.get_json()
    #     # Retrieve circles
    #     with (Path(__file__).parent / f"M3-{i:02d}" / f"circles_{i:02d}.json").open("r", encoding='utf-8') as f:
    #         circles_raw = json.load(f)
    #     event_raw["circles"] = circles_raw
    #     events_raw.append(event_raw)

    # ==== event group ====
    media = [
        Medium("20200330165516_background.jpg",
               [Source("https://web.archive.org/web/20200330165516/http://www.m3net.jp/exCatalog/image/background.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("20220424082236_M3-20thAnniversary.pdf",
               [Source("https://web.archive.org/web/20220424082236/http://www.m3net.jp/attendance/M3-20thAnniversary.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("20190203071953_20th.jpg",
               [Source("https://web.archive.org/web/20190203071953/http://www.m3net.jp/img/20th.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
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
    links = ["https://ttc.ninja-web.net/kantai-parade", "https://x.com/kantai_parade"]

    event_group = EventGroup(
        aliases=["M3", "エムスリー", "Music Media-Mix Market"],
        events=[],
        media=media,
        links=[
            "https://www.m3net.jp/",
            "http://mmm.panic.or.jp/",
            "https://x.com/m3doujin",
        ],
        sources=[
            Source(
                "Alias 'Music Media-Mix Market': https://web.archive.org/web/19990428190424/http://mmm.panic.or.jp/",
                (ReliabilityTypes.Reliable, OriginTypes.Official),
            ),
            Source(
                "Alias 'エムスリー': https://www.m3net.jp/event/2008festa.php",
                (ReliabilityTypes.Reliable, OriginTypes.Official),
            ),
        ],
        comments=None,
        description=None,
        last_edited="2026.06.03",
    )

    # Reorder events and add to event group
    events_raw_sorted = sorted(events_raw, key=lambda er: er["dates"])

    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(save_folder_path, indent=None)
    print("Done")
