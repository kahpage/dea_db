# Notes:
# Looking for circle list, here lamp2 https://x.com/mppfak1150/status/2004041232553857237
# -> Go through similar posts from main  tweeter: https://x.com/tamayuranohi/status/2003150810834960397?s=20    
#TODO: This might prove there are 29 participants indeed: https://x.com/tamayuranohi/status/2003149274583085057?s=20

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

    if True: # ==== tamayuratomosibi 1 ====
        i = 1
        name = f"tamayuratomosibi{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("1_tumblr_a7ce4c4c1bdbecfeb0e60c680506cfb2_dfc38878_2048.jpg",
                   [Source("https://web.archive.org/web/20250917015413/https://tamayuratomosibi.tumblr.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="メインビジュアル：niru  https://www.pixiv.net/users/38334959"),
            Medium("1_tumblr_392b38839eb9af40d7fe8b8a43b76743_6f86c868_2048.jpg",
                   [Source("https://web.archive.org/web/20250917015413/https://tamayuratomosibi.tumblr.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("1_tumblr_inline_t0xpm8yoZz1xdvzhz_500.jpg",
                   [Source("https://web.archive.org/web/20250915203804/https://tamayuratomosibi.tumblr.com/sa-kuru", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("1_G8lo7ITacAAcmHr.jpg",
                   [Source("https://x.com/tamayuranohi/status/2002247909514059948", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Venue layout."),
            Medium("1_hampai.png",
                   [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Screenshot of event page on hamp.ai because the page cannot be easily archived."),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3280.461086723975!2d135.50391230000002!3d34.6935485!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000e6e7cca81681%3A0x35904a0741816399!2sOsaka%20City%20Central%20Public%20Hall!5e0!3m2!1sen!2sfr!4v1767052274930!5m2!1sen!2sfr",
                description="大阪市中央公会堂　 〒530-0005 大阪府大阪市北区中之島１丁目１−２７",
                sources=[Source("https://web.archive.org/web/20250917015413/https://tamayuratomosibi.tumblr.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["たまゆらの灯は夜を還く", "Tamayura no Hi wa Yoru wo Iku", "たまゆらのひはよるをいく", 
                     "Tamayura no Tomosibi", "Tamayura no Tomoshibi",
                     "たまゆらの灯は夜を還く 第1灯", "Tamayura no Hi wa Yoru wo Iku 1",],
            dates="2025.12.25",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20250917015413/https://tamayuratomosibi.tumblr.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Aliase (official transcription): https://web.archive.org/web/20250917015413/https://tamayuratomosibi.tumblr.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Aliase (Tamayura no Tomosibi): Tumblr url 'https://tamayuratomosibi.tumblr.com/'", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Alt: https://touhougarakuta.com/news/250815b/", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt)),
                Source("Participating circles: media '1_hampai.png' or https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== tamayuratomosibi 2 ====
        i = 2
        name = f"tamayuratomosibi{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
                Medium("2_tumblr_e9ac6aaae9ad696d3af059070ea1db91_120bb193_1280.jpg",
                    [Source("https://web.archive.org/web/20251230000632/https://tamayuratomosibi.tumblr.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
                Medium("2_tumblr_inline_t80x1ycqiE1xdvzhz_500.png",
                    [Source("https://web.archive.org/web/20251230000814/https://tamayuratomosibi.tumblr.com/sa-kuru", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
                # Medium("",
                #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
                # Medium("",
                #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
                # Medium("",
                #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
                # Medium("",
                #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2924.4599221655717!2d138.85226029999998!3d37.4413288!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5ff5a857f2b508f3%3A0x3ec1e492fecbb101!2sAtrium%20Nagaoka!5e1!3m2!1sen!2sfr!4v1767053449031!5m2!1sen!2sfr",
                description="アトリウム長岡 白鳳の間・天平の間",
                sources=[Source("https://web.archive.org/web/20251230000632/https://tamayuratomosibi.tumblr.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["たまゆらの灯は夜を還く 第2灯", "Tamayura no Hi wa Yoru wo Iku 2", "たまゆらのひはよるをいく2", 
                     "Tamayura no Tomosibi 2", "Tamayura no Tomoshibi 2",
            ],
            dates="2026.08.01",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251230000632/https://tamayuratomosibi.tumblr.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Alt: https://touhougarakuta.com/news/251229a/", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt)),
            ],
            locations=locations,
            comments="Held in collaboration with a festival at Nagaoka https://nagaokamatsuri.com/august_2/"
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
    links = ["https://tamayuratomosibi.tumblr.com/", "https://x.com/tamayuranohi"]

    event_group = EventGroup(
        aliases=[
            "たまゆらの灯は夜を還く", 
            "Tamayura no Hi wa Yoru wo Iku", 
            "たまゆらのひはよるをいく", 
            "Tamayura no Tomosibi", 
            "Tamayura no Tomoshibi",
        ],
        events=[],
        media=media,
        links=links,
        comments="Doujinshi event focused on Marisa Kirisame from Touhou Project.",
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
        

