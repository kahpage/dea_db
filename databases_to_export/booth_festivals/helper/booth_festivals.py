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

def int_to_chinese_numeral(num: int) -> str:
    numerals = {
        0: "零", 1: "一", 2: "二", 3: "三", 4: "四",
        5: "五", 6: "六", 7: "七", 8: "八", 9: "九",
        10: "十"
    }
    if num <= 10:
        return numerals[num]
    else:
        tens = num // 10
        units = num % 10
        if tens == 1:
            return f"十{numerals[units]}" if units != 0 else "十"
        else:
            return f"{numerals[tens]}十{numerals[units]}" if units != 0 else f"{numerals[tens]}十"

if __name__ == '__main__':
    save_folder_path = Path(__file__).parent.parent
    events_raw: list[Any] = []
    
    # ==================================
    #  APOLLO series
    # ==================================
    if True: # ==== apollo 1 ====
        i = 1
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/apollo"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2014.11.28 - 2014.12.01",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== apollo 2  ====
        i = 2
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/apollo02"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2015.11.20 - 2015.11.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== apollo 3 ====
        i = 3
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/apollo03"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2016.02.19 - 2016.02.21",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== apollo 4 ====
        i = 4
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/apollo04"
        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2016.06.17 - 2016.06.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== apollo 5 ====
        i = 5
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/apollo05"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2016.11.18 - 2016.11.20",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== apollo 6 ====
        i = 6
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/apollo06"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2017.06.17 - 2017.06.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== apollo 7 ====
        i = 7
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/apollo07"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2017.11.18 - 2017.11.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== apollo 8 ====
        i = 8
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-apollo08"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2018.06.01 - 2018.06.03",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== apollo 9 ====
        i = 9
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-apollo09"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2018.11.17 - 2018.11.18",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== apollo 10 ====
        i = 10
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-apollo10"

        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2019.11.23 - 2019.11.24",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== apollo 11 ====
        i = 11
        name = f"apollo_{i:02d}"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-apollo11"
        circles_ = []
        media_ = []
        event = Event(
            aliases=[f"BOOTH Festival APOLLO {i}", f"APOLLO {i}", f"APOLLO 第{int_to_chinese_numeral(i)}回"],
            dates="2021.08.28 - 2021.08.28",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "apollo" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    # ==================================
    #  Other Booth Festivals
    # ==================================
    if True: # ==== アナログゲーム回 ====
        name = "アナログゲーム回"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-analoguegames"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival アナログゲーム回1", "BOOTH Festival Analog Games 1","アナログゲーム回"],
            dates="2018.04.06 - 2018.04.08",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== アナログゲーム回2 ====
        name = "アナログゲーム回 2"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-analoguegames2"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival アナログゲーム回2", "BOOTH Festival Analog Games 2"],
            dates="2018.09.08 - 2018.09.09",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== アナログゲーム回3 ====
        name = "アナログゲーム回 3"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-analoguegames3"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival アナログゲーム回3", "BOOTH Festival Analog Games 3"],
            dates="2019.12.07 - 2019.12.08",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== イラスト・マンガ・書籍回 ====
        name = "イラスト・マンガ・書籍回"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-books"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival イラスト・マンガ・書籍回", "BOOTH Festival Illustration, Manga, and Books", "Book Fest"],
            dates="2018.05.11 - 2018.05.13",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== デジタルゲーム回 ====
        name = "デジタルゲーム回"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-digitalgames"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival デジタルゲーム回", "BOOTH Festival Digital Games"],
            dates="2019.03.16 - 2019.03.17",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== 東方Project オンリー回 ====
        name = "東方Project オンリー回"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-touhouproject"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival 東方Project オンリー回", "BOOTH Festival Touhou Project Only"],
            dates="2019.05.11 - 2019.05.12",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== アズールレーン オンリー回  ====
        name = "アズールレーン オンリー回"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-azurlane"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival アズールレーン オンリー回", "BOOTH Festival Azur Lane Only"],
            dates="2019.05.11 - 2019.05.12",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ドールズフロントライン回 ====
        name = "ドールズフロントライン回"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-dollsfrontline"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival ドールズフロントライン回", "BOOTH Festival Dolls Frontline", "BOOTH Festival Girls' Frontline"],
            dates="2020.02.08 - 2020.02.09",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ボカコレ回 ====
        name = "ボカコレ回"
        print(f"Processing {name} ...")
        event_url = "https://booth.pm/ja/events/bf-vocacolle"
        circles_ = []
        media_ = []
        event = Event(
            aliases=["BOOTH Festival ボカコレ回", "BOOTH Festival Vocacolle"],
            dates="2020.12.11 - 2020.12.13",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {event_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles: {event_url} (website scrape on 2025.12.15)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            links=[event_url]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "booth_festivals" / f"{name}.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    # ==== event group ====
    media = [
    ]
    links = ["https://booth.pm/ja"]

    event_group = EventGroup(
        aliases=["BOOTH Festival"],
        events=[],
        media=media,
        links=links,
        comments="Booth Festivals are a series of online events held on BOOTH."
    )
    events_raw_sorted = sorted(events_raw, key=lambda er: er["dates"])
    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print("Saving apollo database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

