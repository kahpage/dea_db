# Notes:
# Circle list source for 5

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

    if True: # ==== vocaloid fantasia 1 ====
        i = 1
        name = f"vocaloid_fantasia{i}"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/20100805082022/http://vocaloid-fantasia.com/about.htm"

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1766944440923!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["VOCALOID Fantasia", "VOCALOID Fantasia 1"],
            dates="2010.09.05",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20100815195259/http://vocaloid-fantasia.com/circle1.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== vocaloid fantasia 2 ====
        i = 2
        name = f"vocaloid_fantasia{i}"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/20110903030244/https://vocaloid-fantasia.com/about02.htm"

        circles_ = []
        media_ = [
            Medium("2_vocafan02.jpg",
                   [Source("https://web.archive.org/web/20110202163749/http://vocaloid-fantasia.com/gazou/vocafan02.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("2_vocafan02_2.jpg",
                   [Source("https://web.archive.org/web/20251228215041/https://vocaloid-fantasia.com/gazou/vocafan02.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1766944440923!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["VOCALOID Fantasia 2"],
            dates="2011.09.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20110914172653/http://vocaloid-fantasia.com/cir02-iciran-k.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
    
    if True: # ==== vocaloid fantasia 3 ====
        i = 3
        name = f"vocaloid_fantasia{i}"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/20240228191408/https://vocaloid-fantasia.com/about03.htm"

        circles_ = []
        media_ = [
            Medium("3_vocafan03.jpg",
                   [Source("https://web.archive.org/web/20120119054705/http://vocaloid-fantasia.com/gazou/vocafan03.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_vocafan3.jpg",
                   [Source("https://web.archive.org/web/20120119095136/http://vocaloid-fantasia.com/gazou/vocafan3.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_vocafan03_2.jpg",
                   [Source("https://web.archive.org/web/20251228215056/https://vocaloid-fantasia.com/gazou/vocafan03.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_haichi03.jpg",
                   [Source("https://web.archive.org/web/20130530090329/http://vocaloid-fantasia.com/cir-iciran03.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1766944440923!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["VOCALOID Fantasia 3"],
            dates="2012.09.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/2/http://vocaloid-fantasia.com/cir-iciran03.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== utafan 1 ====
        i = 1
        name = f"utafan{i}"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/20140421182456/http://vocaloid-fantasia.com/utafan.htm"

        circles_ = []
        media_ = [
            Medium("utau1_utaufan.gif",
                   [Source("https://web.archive.org/web/20140421182456/http://vocaloid-fantasia.com/utafan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1766944440923!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["UTAU Fantasia", "UTAU Fantasia 1"],
            dates="2012.09.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Inclusion in VOCALOID Fantasia 3: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Included in VOCALOID Fantasia 3."
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== vocaloid fantasia 4 ====
        i = 4
        name = f"vocaloid_fantasia{i}"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/2/https://vocaloid-fantasia.com/about04.htm"

        circles_ = []
        media_ = [
            Medium("4_vocafan04.jpg",
                   [Source("https://web.archive.org/web/20160811220905/http://vocaloid-fantasia.com/ippan04.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_haichi.jpg",
                   [Source("https://web.archive.org/web/20131207042859/http://vocaloid-fantasia.com/cir-iciran04.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1766944440923!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["VOCALOID Fantasia 4"],
            dates="2013.09.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/2/https://vocaloid-fantasia.com/cir-iciran04.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== utafan 2 ====
        i = 2
        name = f"utafan{i}"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/20160829041202/http://vocaloid-fantasia.com/utafan02.htm"

        circles_ = []
        media_ = [
            Medium("utau2_utaufan2.gif",
                   [Source("https://web.archive.org/web/20160829041202/http://vocaloid-fantasia.com/utafan02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1766944440923!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["UTAU Fantasia 2"],
            dates="2013.09.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Inclusion in VOCALOID Fantasia 4: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== koetuki ====
        name = "koetuki"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/20130608060607/http://vocaloid-fantasia.com/koetuki/about.htm"

        circles_ = []
        media_ = [
            Medium("koetuki_koetuki.jpg",
                   [Source("https://web.archive.org/web/20241113055819/https://vocaloid-fantasia.com/koetuki/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("koetuki_talk.PNG",
                   [Source("https://web.archive.org/web/20241113055819/https://vocaloid-fantasia.com/koetuki/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("koetuki_koetuki.gif",
                   [Source("https://web.archive.org/web/20130613085458/http://vocaloid-fantasia.com/koetuki/koetuki.gif", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("koetuki_10top.png",
                   [Source("https://web.archive.org/web/20251107041835/https://vocaloid-fantasia.com/koetuki/goudou.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("koetuki_11main.jpg",
                   [Source("https://web.archive.org/web/20251107041835/https://vocaloid-fantasia.com/koetuki/goudou.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("koetuki_99_banner_m.jpg",
                   [Source("https://web.archive.org/web/20251107041835/https://vocaloid-fantasia.com/koetuki/goudou.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("koetuki_koetuki-h.gif",
                   [Source("https://web.archive.org/web/20150118021338/http://vocaloid-fantasia.com/koetuki/ippan.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1766944440923!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["この声届け、月までも", "Kono Koe Todoke, Tsuki made mo", "koetuki", "konokoetuki"],
            dates="2013.09.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20150118021908/http://vocaloid-fantasia.com/koetuki/cir-iciran04.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Inclusion in VOCALOID Fantasia 4: see both participating circles.", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments="Event included in VOCALOID Fantasia 4",
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== vocaloid fantasia 5 ====
        i = 5
        name = f"vocaloid_fantasia{i}"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/20160326090831/http://vocaloid-fantasia.com/about05.htm"

        circles_ = []
        media_ = [
            Medium("5_vocafan5.gif",
                   [Source("https://web.archive.org/web/20140829181638/http://vocaloid-fantasia.com/gazou/vocafan5.gif", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3240.5041645703045!2d139.7804061753337!3d35.68920912953642!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889520a5d69ef%3A0xe6ef2b5af497cb6!2sMensh%C5%8D%20Kaikan!5e0!3m2!1sen!2sfr!4v1766944596587!5m2!1sen!2sfr",
                description="東京・綿商会館",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["VOCALOID Fantasia 5"],
            dates="2014.09.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== vocaloid fantasia 6 ====
        i = 6
        name = f"vocaloid_fantasia{i}"
        print(f"Processing {name} ...")
        local_about = "https://web.archive.org/web/20250417022424/https://vocaloid-fantasia.com/about06.htm"

        circles_ = []
        media_ = [
            Medium("6_vocafan6.jpg",
                   [Source("https://web.archive.org/web/20251015073257/https://vocaloid-fantasia.com/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("6_haichi6.gif",
                   [Source("https://web.archive.org/web/20250416144828/https://vocaloid-fantasia.com/cir-iciran06.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3250.3085795254374!2d139.64325747532268!3d35.44715424279784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1766944440923!5m2!1sen!2sfr",
                description="横浜産貿ホールマリネリア",
                sources=[Source(local_about, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["VOCALOID Fantasia Final", "VOCALOID Fantasia 6"],
            dates="2015.02.21",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {local_about}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20250416144828/https://vocaloid-fantasia.com/cir-iciran06.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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
        Medium("eg_top_banner.gif",
               [Source("https://web.archive.org/web/20160326090831/http://vocaloid-fantasia.com/about05.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_banner.gif",
               [Source("https://web.archive.org/web/20101230133938/http://vocaloid-fantasia.com/banner.gif", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_x2_4b5407c.jpg",
               [Source("https://web.archive.org/web/20110613091525/http://vocaloid-fantasia.com/gazou/x2_4b5407c.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("https://web.archive.org/web/20250416144840/https://vocaloid-fantasia.com/janken.mp4",
               [Source("https://web.archive.org/web/20150113104813/http://vocaloid-fantasia.com/janken.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_DSC0881.jpg",
               [Source("https://web.archive.org/web/20110613092057/http://vocaloid-fantasia.com/repo/_DSC0881.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("https://web.archive.org/web/20110613091931/http://vocaloid-fantasia.com/retch.pdf",
               [Source("https://web.archive.org/web/20110613091931/http://vocaloid-fantasia.com/retch.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("https://web.archive.org/web/20160430005630/http://vocaloid-fantasia.com/koetuki/hannyu.pdf",
               [Source("https://web.archive.org/web/20160430005630/http://vocaloid-fantasia.com/koetuki/hannyu.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("https://web.archive.org/web/20160327010420/http://vocaloid-fantasia.com/hannyu06.pdf",
               [Source("https://web.archive.org/web/20160327010420/http://vocaloid-fantasia.com/hannyu06.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
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
    links = ["https://vocaloid-fantasia.com/", "https://x.com/vocafan0905", "https://x.com/konokoetuki"]

    event_group = EventGroup(
        aliases=["VOCALOID Fantasia", "vocafan"],
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
        

