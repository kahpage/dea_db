# Notes:
# Search for catalog pictures on online shops (since Mawari)

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

    thwikicc = "https://thwiki.cc/%E5%A2%83%E7%95%8C%E6%89%80%E8%A7%81%E5%88%B0%E7%9A%84%E5%A4%96%E7%95%8C"

    if True: # ==== kyoukaikaramietakeshiki 1 ====
        i = 1
        name = f"kyoukaikaramietakeshiki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("1_境界所见到的外界顶图1.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("1_536px-境界所见到的外界顶图2.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("https://web.archive.org/web/20250112160330/http://www.green.dti.ne.jp/maisan/gensoukyou/image/kyoukaikaramietakeshiki.pdf",
                   [Source("https://web.archive.org/web/20250112160330/http://www.green.dti.ne.jp/maisan/gensoukyou/image/kyoukaikaramietakeshiki.pdf", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.8869299207763!2d139.75819397533223!3d35.655157331406535!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1767458437732!5m2!1sen!2sfr",
                description="東京都立産業貿易センター浜松町館5階",
                sources=[Source("https://web.archive.org/web/20250112160330/http://www.green.dti.ne.jp/maisan/gensoukyou/image/kyoukaikaramietakeshiki.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["境界から視えた外界", "Kyoukai kara Mieta Keshiki"],
            dates="2010.11.28",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://www.pixiv.net/event_detail.php?event_id=792", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20250112160330/http://www.green.dti.ne.jp/maisan/gensoukyou/image/kyoukaikaramietakeshiki.pdf", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== kyoukaikaramietakeshiki 2 ====
        i = 2
        name = f"kyoukaikaramietakeshiki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("2_top03.jpg",
                   [Source("https://web.archive.org/web/20121124122035/http://kyoukai.biz/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration:はふり(Lapin Asile)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.8869299207763!2d139.75819397533223!3d35.655157331406535!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1767458437732!5m2!1sen!2sfr",
                description="東京都港区海岸1-7-8東京都立産業貿易センター　浜松町館",
                sources=[Source("https://www.pixiv.net/event_detail.php?event_id=2084", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["境界から視えた外界-廻-", "Kyoukai kara Mieta Keshiki -Mawari-"],
            dates="2012.09.09",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://www.pixiv.net/event_detail.php?event_id=2084", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20130608043923/http://kyoukai.biz:80/list01.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== kyoukaikaramietakeshiki 3 ====
        i = 3
        name = f"kyoukaikaramietakeshiki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("3_top04.jpg",
                   [Source("https://web.archive.org/web/20140518000247/http://kyoukai.biz/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration:ランコの姉(豚乙女)"),
            Medium("3_top05.jpg",
                   [Source("https://web.archive.org/web/20140812085832/http://kyoukai.biz/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration:桜庭友紀(PERSONAL COLOR)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767459499500!5m2!1sen!2sfr",
                description="東京都東京都大田区南蒲田１−２０−２０大田区産業プラザPiO",
                sources=[Source("https://www.pixiv.net/event_detail.php?event_id=4382", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["境界から視えた外界-結-", "Kyoukai kara Mieta Keshiki -Yui-"],
            dates="2015.02.21",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://www.pixiv.net/event_detail.php?event_id=4382", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20150728094209/http://project-d.biz/tohosaiji/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of the 2015 東方合同祭事参 venue: https://web.archive.org/web/20150224200242/http://project-d.biz/tohosaiji/event.html"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== kyoukaikaramietakeshiki 4 ====
        i = 4
        name = f"kyoukaikaramietakeshiki{i}"
        print(f"Processing {name} ...")
        circles_ = []
        media_ = [
            Medium("4_top06.jpg",
                   [Source("https://web.archive.org/web/20170425073255/http://kyoukai.biz/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration:鳥居すみ(airdrop)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163642!2d139.7214917753278!3d35.55878603669134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1767459499500!5m2!1sen!2sfr",
                description="東京都大田区南蒲田１丁目２０−２０大田区産業プラザPiO",
                sources=[Source("https://www.pixiv.net/event_detail.php?event_id=5852", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["境界から視えた外界-至-", "Kyoukai kara Mieta Keshiki -Itaru-"],
            dates="2017.03.26",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://www.pixiv.net/event_detail.php?event_id=5852", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170504223846/http://project-d.biz/tohosaiji/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of the 2017 東方合同祭事 venue: https://web.archive.org/web/20170504223846/http://project-d.biz/tohosaiji/circle_list.html"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    # ==== event group ====
    media = [
        Medium("eg_banner.jpg",
               [Source("https://web.archive.org/web/20121124122035/http://kyoukai.biz/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["https://kyoukai.biz/", "https://x.com/kyoukai_hifuu", "https://yumemichi.koromu-toho.com/"]

    event_group = EventGroup(
        aliases=[
            "境界から視えた外界",
            "Kyoukai kara Mieta Keshiki",
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
        

