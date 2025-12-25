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
    main_page = "https://web.archive.org/web/20050204025708/http://eco.ket.jp/page002.html"

    if True: # ==== ecoket 10 ====
        i = 10
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("10_ecoket10.jpg",
                   [Source("https://web.archive.org/web/20070222041308/http://eco.ket.jp:80/ecoket10.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51870.19369178282!2d139.68867112167965!3d35.65515299999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1766594568409!5m2!1sen!2sfr",
                description="東京・浜松町　都立産業貿易センター２Ｆホール",
                sources=[Source("https://web.archive.org/web/20050204025708/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["エコケット10 ～ＦＩＮＡＬ～", "EcoKet 10 ~FINAL~"],
            dates="2004.11.03",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20050204025708/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20070222041448/http://eco.ket.jp:80/ecoket10_clist.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 9 ====
        i = 9
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

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
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3245.794139163649!2d139.72149177532782!3d35.558786036691345!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601860f87f5da4e3%3A0x8a0493a2f4accfb0!2sOta%20City%20Industrial%20Plaza%20PiO!5e0!3m2!1sen!2sfr!4v1766595182391!5m2!1sen!2sfr",
                description="東京・蒲田　大田区産業プラザＰｉｏ大展示ホール",
                sources=[Source("https://web.archive.org/web/20040810060849/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51870.19369178282!2d139.68867112167965!3d35.65515299999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1766594568409!5m2!1sen!2sfr",
                description="東京・浜松町　都立産業貿易センター２Ｆ",
                sources=[Source("https://web.archive.org/web/20040810060849/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                comments="Old location before date change."
            ),  
        ]
        event = Event(
            aliases=["エコケット9", "EcoKet 9"],
            dates="2004.05.05 → 2004.05.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Date postponed: https://web.archive.org/web/20040810060849/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20050207073946/http://eco.ket.jp/ecoket9_c_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 8 ====
        i = 8
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("8_ecoket8.jpg",
                   [Source("https://web.archive.org/web/20031212193452/http://eco.ket.jp/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51870.19369178282!2d139.68867112167965!3d35.65515299999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1766594568409!5m2!1sen!2sfr",
                description="東京・浜松町　都立産業貿易センター",
                sources=[Source("https://web.archive.org/web/20030604192740/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["エコケット8", "EcoKet 8"],
            dates="2003.10.13",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20050207073559/http://eco.ket.jp/ecoket8_c_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 7 ====
        i = 7
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("7_img003.jpg",
                   [Source("https://web.archive.org/web/20030604192520/http://eco.ket.jp/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51870.19369178282!2d139.68867112167965!3d35.65515299999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1766594568409!5m2!1sen!2sfr",
                description="東京・浜松町　都立産業貿易センター",
                sources=[Source("https://web.archive.org/web/20030410132005/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["エコケット7", "EcoKet 7"],
            dates="2003.05.05",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20040724054104/http://eco.ket.jp:80/ecoket7_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 6 ====
        i = 6
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

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
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51870.19369178282!2d139.68867112167965!3d35.65515299999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1766594568409!5m2!1sen!2sfr",
                description="東京・浜松町　都立産業貿易センター",
                sources=[Source("https://web.archive.org/web/20020607025109/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["エコケット6", "EcoKet 6"],
            dates="2002.11.04",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
    #     with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
    #         circles_raw = json.load(f)
    #     event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 5 ====
        i = 5
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

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
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51870.19369178282!2d139.68867112167965!3d35.65515299999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1766594568409!5m2!1sen!2sfr",
                description="東京・浜松町　都立産業貿易センター",
                sources=[Source("https://web.archive.org/web/20011217200603/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["エコケット5", "EcoKet 5"],
            dates="2002.05.05",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
    #     with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
    #         circles_raw = json.load(f)
    #     event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 4 ====
        i = 4
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("4_ecoice_top8.jpg",
                   [Source("https://web.archive.org/web/20010827001039/http://sakura.comike.to:80/ecoket/ecoice_top8.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_ecoice_top9.jpg",
                   [Source("https://web.archive.org/web/20050708002450/http://candy-network.org/~ecoket/ecoice_top9.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3240.142518569291!2d139.78746807533398!3d35.69811032904744!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb459950641%3A0x99332c088b0f7aa5!2sTokyo%20Wholesale%20Center%20Cooperative!5e0!3m2!1sen!2sfr!4v1766598701862!5m2!1sen!2sfr",
                description="東京卸商センター３Ｆ",
                sources=[Source("https://web.archive.org/web/20010602194507/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["エコケット4", "EcoKet 4"],
            dates="2001.11.18",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231003137/http://sakura.comike.to/ecoket/c_list4.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 3 ====
        i = 3
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("3_eco_teleca.jpg",
                   [Source("https://web.archive.org/web/20010826233507/http://sakura.comike.to:80/ecoket/eco_teleca.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_ecoice_top7.jpg",
                   [Source("https://web.archive.org/web/20010826235049/http://sakura.comike.to:80/ecoket/ecoice_top7.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51870.19369178282!2d139.68867112167965!3d35.65515299999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188b60c0d52981%3A0x5db20f81d038f20c!2sTokyo%20Metropolitan%20Industrial%20Trade%20Center%20Hamamatsuch%C5%8D!5e0!3m2!1sen!2sfr!4v1766594568409!5m2!1sen!2sfr",
                description="東京・浜松町 都立産業貿易センター２Ｆ",
                sources=[Source("https://web.archive.org/web/20001102054729/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),  
        ]
        event = Event(
            aliases=["エコケット3", "EcoKet 3"],
            dates="2001.04.01",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231002259/http://sakura.comike.to/ecoket/c_list3.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 2 ====
        i = 2
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

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
            # Location(
            #     iframe_url="",
            #     description="",
            #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            # ),  
        ]
        event = Event(
            aliases=["エコケット2", "EcoKet 2"],
            dates="2000.09.03",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20020217224245/http://sakura.comike.to/ecoket/c_list2.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 1 ====
        i = 1
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("1_pic7.gif",
                   [Source("https://web.archive.org/web/20250601191910/https://www.tinami.com/x/riuichi/04/page3.html", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13340.919230578898!2d139.7796962715368!3d35.69466653579947!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188eb36b54452d%3A0xf1a3e2377b154969!2z6LK444GX5Lya6K2w5a6kIOadseS6rOaWh-WFt-WFseWSjOS8mumkqCDmtYXojYnmqYs!5e0!3m2!1sen!2sfr!4v1766598149913!5m2!1sen!2sfr",
                description="東京文具共和会館",
                sources=[Source("https://www.tinami.com/x/riuichi/04/page3.html", (ReliabilityTypes.Likely, OriginTypes.External))]
            ),  
        ]
        event = Event(
            aliases=["エコケット1", "EcoKet 1"],
            dates="2000.04.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231002137/http://sakura.comike.to/ecoket/c_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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
        Medium("eg_img005.jpg",
               [Source("https://web.archive.org/web/20031212193452/http://eco.ket.jp/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_ecoice_top.jpg",
               [Source("https://web.archive.org/web/20020220045015/http://sakura.comike.to/ecoket/images/ecoice_top.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_ecoice_top2.jpg",
               [Source("https://web.archive.org/web/20020220045935/http://sakura.comike.to/ecoket/images/ecoice_top2.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["http://eco.ket.jp/index.html", "http://sakura.comike.to/ecoket/", "http://candy-network.org/~ecoket/"]

    event_group = EventGroup(
        aliases=["エコケット", "EcoKet"],
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
        

