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

    if True: # ==== kantai_parade 1 ====
        i = 1
        name = f"kantai_parade{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("1_C6Zr4ArUYAYWPjl.jpg",
                   [Source("https://x.com/kantai_parade/status/839477268212690948", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration: 夢ノ紫也 様（ドリームプロジェクト）"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3263.000796717689!2d136.89578397530863!3d35.13165365996889!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x600379fe92208121%3A0xc830505a7700eaa6!2sNagoya%20Congress%20Center!5e0!3m2!1sen!2sfr!4v1767607427804!5m2!1sen!2sfr",
                description="名古屋国際会議場 イベントホール",
                sources=[Source("https://web.archive.org/web/20171003002245/http://ttc.ninja-web.net/kantai-parade/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["艦隊ぱれーど", "Kantai Parade"],
            dates="2017.10.15",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20210616180516/http://ttc.ninja-web.net/kantai-parade/about_kantai-parade.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170913141445/http://ttc.ninja-web.net/kantai-parade/kantai-parade_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Part of 名古屋熱田同人祭 (Nagoya Atsuta Doujin Festival).",
            last_edited="2026.05.30"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== kantai_parade 2 ====
        i = 2
        name = f"kantai_parade{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("2_kantai-parade02.jpg",
                   [Source("https://web.archive.org/web/20210724033421/http://ttc.ninja-web.net/kantai-parade/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration: ナオ様 （Easygoing)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3263.000796717689!2d136.89578397530863!3d35.13165365996889!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x600379fe92208121%3A0xc830505a7700eaa6!2sNagoya%20Congress%20Center!5e0!3m2!1sen!2sfr!4v1767607427804!5m2!1sen!2sfr",
                description="名古屋国際会議場白鳥ホール",
                sources=[Source("https://web.archive.org/web/20210724033421/http://ttc.ninja-web.net/kantai-parade/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["艦隊ぱれーど2", "Kantai Parade 2"],
            dates="2018.11.04",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20210724033421/http://ttc.ninja-web.net/kantai-parade/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (dead): http://ttc.ninja-web.net/nagoya-doujin-fes/181104_circlelist.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            last_edited="2026.05.30"
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
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
    links = ["https://ttc.ninja-web.net/kantai-parade", "https://x.com/kantai_parade"]

    event_group = EventGroup(
        aliases=["艦隊ぱれーど", "Kantai Parade"],
        events=[],
        media=media,
        links=links,
        comments=None,
        description=None,
        last_edited="2026.05.30"
    )
    
    # Reorder events and add to event group
    events_raw_sorted = sorted(events_raw, key=lambda er: er['dates'])
    
    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print(f"Saving {Path(__file__).name} database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

