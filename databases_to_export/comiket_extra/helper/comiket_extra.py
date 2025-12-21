# Notes:

from db_structs import Medium, Circle, Event, EventGroup, Source, ReliabilityTypes, OriginTypes, Location
from pathlib import Path
import json
from typing import Any

if __name__ == '__main__':
    save_folder_path = Path(__file__).parent.parent
    events_raw: list[Any] = []

    chronology = "https://www.comiket.co.jp/archives/Chronology.html"

    if True: # ==== comiket special 1 ====
        name = "cs1"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d51859.91488004924!2d139.3770644646894!3d35.67097679999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6018e37fedeeaaab%3A0x483db6a0ce507bbd!2sYotsuyakokaido!5e0!3m2!1sen!2sfr!4v1760361911992!5m2!1sen!2sfr",
                description="四谷公会堂 (probably the following point, venue now closed)",     
                sources=[Source(chronology, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["コミケスペシャル", "Comiket Special", "コミケスペシャル1", "Comiket Special 1"],
            dates="1978.05.06",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chronology}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles (1): ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== comiket in Hitotsubashi  ====
        name = "cinh"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3148.0599210587065!2d139.44097876301052!3d35.694112352737754!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6018e3f78c83a239%3A0x14d00eff5243c3c3!2sHitotsubashi%20University!5e0!3m2!1sen!2sfr!4v1766318423087!5m2!1sen!2sfr",
                description="一橋大学　21番教室",
                sources=[Source(chronology, (ReliabilityTypes.Likely, OriginTypes.External))],
                comments="Could not guess building."
            ),
        ]
        event = Event(
            aliases=["コミックマーケットin一橋祭", "Comiket in Hitotsubashi"],
            dates="1978.11.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chronology}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles (1): ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== comiket special 2 ====
        name = "cs2"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3241.9948860201334!2d139.774440975332!3d35.65249763155262!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6018898058281359%3A0x3f19f43c3253a292!2sTokyo%20International%20Trade%20Fair%20Memorial%20Monument!5e0!3m2!1sen!2sfr!4v1766318715213!5m2!1sen!2sfr",
                description="東京国際見本市会場（晴海）： 東京国際貿易センター（東館）",
                sources=[Source(chronology, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["さよなら晴海!!コミケットスペシャル", "Sayonara Harumi!! Comiket Special", "コミケスペシャル2", "Comiket Special 2"],
            dates="1996.03.17",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chronology}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles (1): ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw!?
        events_raw.append(event_raw)

    if True: # ==== comiket special 3 ====
        name = "cs3"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3577.441819084488!2d127.72980977496475!3d26.279773487005095!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x34e56ca503aaaaab%3A0xeb769b84d6de2088!2sOkinawa%20Convention%20Centre!5e0!3m2!1sen!2sfr!4v1766318874294!5m2!1sen!2sfr",
                description="沖縄コンベンションセンター",
                sources=[Source(chronology, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["リゾコミin沖縄コミケットスペシャル３", "Rizocomi in Okinawa Comiket Special 3", "コミケスペシャル3", "Comiket Special 3"],
            dates="2005.03.21",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chronology}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles (1): ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== comiket special 4 ====
        name = "cs4"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京国際展示場（東京ビッグサイト）西１～４ホール",
                sources=[Source(chronology, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["30周年記念24耐(!？)コミケットスペシャル4", "30th Anniversary 24-Hour (!?) Comiket Special 4", "コミケスペシャル4", "Comiket Special 4"],
            dates="2005.03.21",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chronology}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles (1): ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== comiket special 5 ====
        name = "cs5"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3212.2389123800253!2d140.45706888885493!3d36.37921000000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60222445f6e0b909%3A0x1121abc0ca35f0f6!2z44ix5LyK5Yui55SaIOacrOekvg!5e0!3m2!1sen!2sfr!4v1766319258125!5m2!1sen!2sfr",
                description="伊勢甚泉町北ビル他",
                sources=[Source(chronology, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["コみケッとスペシャル５ in 水戸", "Comiket Special 5 in Mito", "コミケスペシャル5", "Comiket Special 5"],
            dates="2010.08.14 - 2010.08.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chronology}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles (1): ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== comiket special 6 ====
        name = "cs6"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source(, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.177406807312!2d140.02847468885494!3d35.648000500000016!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x602281f5c1bbfea1%3A0xcf5976a9132d99ff!2sMakuhari%20Messe%20International%20Exhibition%20Hall%201-3!5e0!3m2!1sen!2sfr!4v1766319427431!5m2!1sen!2sfr",
                description="幕張メッセ ホール2～3(一日目)、ホール1～3(二日目)",
                sources=[Source(chronology, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["コミケットスペシャル６ OTAKU SUMMIT 2015", "Comiket Special 6 OTAKU SUMMIT 2015", "コミケスペシャル6", "Comiket Special 6"],
            dates="2015.03.28 - 2015.03.29",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chronology}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles (1): ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (ReliabilityTypes.Likely, OriginTypes.External)),
        #         Source("", (ReliabilityTypes.Likely, OriginTypes.External))]
        #         , comments=""),
    ]
    links = ["https://comiket.co.jp/", "https://web.archive.org/web/19990117015250/http://www.inter-g7.or.jp/g2/manga/HTML/MARKET.html", "https://x.com/comiketofficial"]

    event_group = EventGroup(
        aliases=["Comiket extra events"],
        events=[],
        media=media,
        links=links,
        description="Extra events related to Comiket.",
        # comments=f""
    )
    for event_raw in events_raw:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print("Saving arts database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")


