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

    if True: # ==== gensouongaku ====
        name = "gensouongaku"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("gensouongaku/gensouongakufes.jpg",
                   [Source("https://web.archive.org/web/20200514213650/http://gensouongaku.info/fes/a.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                    Source("Illustrator: https://web.archive.org/web/20190506200348/http://gensouongaku.info/fes/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="イラスト：くまのかつお"),
            Medium("gensouongaku/D0trgwQVsAE9UfV.jpg",
                   [Source("https://x.com/gensouongaku/status/1102092751774990337/photo/1", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("gensouongaku/D0iYYI8U8AAL_Ge.jpg",
                   [Source("https://x.com/gensouongaku/status/1101297657451032576/photo/1", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("gensouongaku/幻想音楽祭ロゴちいさい.png",
                   [Source("https://web.archive.org/web/20190506200348/http://gensouongaku.info/fes/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("gensouongaku/",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("gensouongaku/",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12987.533970601125!2d139.6959019!3d35.5318767!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60186099fb404b45%3A0xaf9a6f040b65ff4c!2z5bed5bSO5biC55Sj5qWt5oyv6IiI5Lya6aSo!5e0!3m2!1sja!2sfr!4v1767106071059!5m2!1sja!2sfr",
                description="川崎市産業振興会館 4F",
                sources=[Source("https://web.archive.org/web/20210512091343/http://gensouongaku.info/fes/s/about/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["幻想音楽祭", "Gensou Ongaku Sai", "Gensou Ongaku Fes"],
            dates="2019.03.02",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20210512091343/http://gensouongaku.info/fes/s/about/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20201108000340/https://gensouongaku.info/fes/s/circlelist/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            links=["https://x.com/gensouongaku",
                   "http://gensouongaku.info/fes/"],
            description="Doujin music venue themed around fantasy music hosted by しちごさん。（霜月はるか・日山尚）",
            comments="Additionnal CD list: https://web.archive.org/web/20211127024412/http://gensouongaku.info/fes/s/cdlist/"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== touhousugeimatsuri ====
        name = "touhousugeimatsuri"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("touhousugeimatsuri/sugeilogo.gif",
                   [Source("https://web.archive.org/web/20100926130402/http://ketto.com/sugei/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("touhousugeimatsuri/sugei1hyousi.jpg",
                   [Source("https://web.archive.org/web/20100927055641/http://ketto.com/sugei/sugei1ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("touhousugeimatsuri/",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767562526864!5m2!1sen!2sfr",
                description="大田区産業プラザPiO１階大展示ホール",
                sources=[Source("https://web.archive.org/web/20100926130402/http://ketto.com/sugei/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["東方素芸祭", "Touhou Sugei Matsuri"],
            dates="2010.06.13",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20100926130402/http://ketto.com/sugei/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20100927065217/http://ketto.com/mimiken/alllist.cgi?91", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            links=["http://ketto.com/sugei/"], # Links
            description="Touhou project-themed doujin event.",
            comments=None
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
    ]
    links = []

    event_group = EventGroup(
        aliases=["One-off events"],
        events=[],
        media=media,
        links=links,
        # comments="",
        description="Events that seem to have happened only once, avoids creating separate event groups for them.",
    )
    
    # Reorder events and add to event group
    events_raw_sorted = sorted(events_raw, key=lambda er: er['dates'])
    
    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print(f"Saving {Path(__file__).name} database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

