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

if __name__ == '__main__':
    save_folder_path = Path(__file__).parent.parent
    events_raw: list[Any] = []

    thwikicc = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD"
    main_page = "https://reitaisai.com/"

    if True: # ==== arts1 ====
        name = "arts1"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC1%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("1_arts1.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東ホール",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭1", "博麗神社秋季例大祭1", "Hakurei Jinja Shuuki Reitaisai 1", "Autumn Reitaisai 1", "ARTS1", "第一回 博麗神社秋季例大祭"],
            dates="2014.11.24 ",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20141024075725/http://reitaisai.com/arts1/circlelist/block/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20141024075716/http://reitaisai.com/arts1/circlelist/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts2 ====
        i = 2
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東ホール",
                sources=[Source("https://web.archive.org/web/20151020062424/http://reitaisai.com/arts2", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭2", "博麗神社秋季例大祭2", "Hakurei Jinja Shuuki Reitaisai 2", "Autumn Reitaisai 2", "ARTS2", "第二回 博麗神社秋季例大祭"],
            dates="2015.10.18",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20151020062424/http://reitaisai.com/arts2", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://web.archive.org/web/20151020062424/http://reitaisai.com/arts2", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts3 ====
        i = 3
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC3%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3ホール",
                sources=[Source(f"Url name of http://s.reitaisai.com/arts3/block123/ and {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭3", "博麗神社秋季例大祭3", "Hakurei Jinja Shuuki Reitaisai 3", "Autumn Reitaisai 3", "ARTS3", "第三回 博麗神社秋季例大祭"],
            dates="2016.10.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): http://s.reitaisai.com/arts3/block123/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts4 ====
        i = 4
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC4%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東1・2・3ホール",
                sources=[Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭4", "博麗神社秋季例大祭4", "Hakurei Jinja Shuuki Reitaisai 4", "Autumn Reitaisai 4", "ARTS4", "第四回 博麗神社秋季例大祭"],
            dates="2017.10.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): http://s.reitaisai.com/arts4/block/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts5 ====
        i = 5
        name = f"arts{i}"
        thwikicc_local = ""
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東ホール",
                sources=[Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭5", "博麗神社秋季例大祭5", "Hakurei Jinja Shuuki Reitaisai 5", "Autumn Reitaisai 5", "ARTS5", "第五回 博麗神社秋季例大祭"],
            dates="2018.10.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source(f"Participating circles (1): {thwikicc_local} (unverified)", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"Official circle list is dead and unarchived (https://reitaisai.com/arts5/?page_id=307)\nFor more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts6 ====
        i = 6
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC6%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト西ホール",
                sources=[Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭6", "博麗神社秋季例大祭6", "Hakurei Jinja Shuuki Reitaisai 6", "Autumn Reitaisai 6", "ARTS6", "第六回 博麗神社秋季例大祭"],
            dates="2019.10.06",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source("Participating circles (1): http://s.reitaisai.com/arts6/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts7 ====
        i = 7
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC7%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト西ホール",
                sources=[Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭7", "博麗神社秋季例大祭7", "Hakurei Jinja Shuuki Reitaisai 7", "Autumn Reitaisai 7", "ARTS7", "第七回 博麗神社秋季例大祭"],
            dates="2020.10.18",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source("Participating circles (1): https://reitaisai.com/arts7/%E3%80%90%E9%85%8D%E7%BD%AE%E7%95%AA%E5%8F%B7%E9%A0%86%E3%80%91%E3%82%B5%E3%83%BC%E3%82%AF%E3%83%AB%E9%85%8D%E7%BD%AE/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts8 ====
        i = 8
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC8%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト青海展示棟",
                sources=[Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭8", "博麗神社秋季例大祭8", "Hakurei Jinja Shuuki Reitaisai 8", "Autumn Reitaisai 8", "ARTS8", "第八回 博麗神社秋季例大祭"],
            dates="2021.10.24",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://reitaisai.com/arts8/circlelist_1/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts9 ====
        i = 9
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC9%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト西ホール",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭9", "博麗神社秋季例大祭9", "Hakurei Jinja Shuuki Reitaisai 9", "Autumn Reitaisai 9", "ARTS9", "第九回 博麗神社秋季例大祭"],
            dates="2022.10.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://reitaisai.com/arts9/place-assign/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts10 ====
        i = 10
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC10%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東ホール",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭10", "博麗神社秋季例大祭10", "Hakurei Jinja Shuuki Reitaisai 10", "Autumn Reitaisai 10", "ARTS10", "第十回 博麗神社秋季例大祭"],
            dates="2023.11.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://reitaisai.com/arts10/place-assign-announce/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts11 ====
        i = 11
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC11%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト南展示棟",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭11", "博麗神社秋季例大祭11", "Hakurei Jinja Shuuki Reitaisai 11", "Autumn Reitaisai 11", "ARTS11", "第十一回 博麗神社秋季例大祭"],
            dates="2024.10.20",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://reitaisai.com/arts11/circle-place-assign/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== arts12 ====
        i = 12
        name = f"arts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC12%E5%B1%8A%E6%91%8A%E4%BD%8D/%E3%83%87%EF%BD%9E%E3%81%93%E9%83%A8%E5%88%86"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_arts{i}.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト西ホール",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["秋季例大祭12", "博麗神社秋季例大祭12", "Hakurei Jinja Shuuki Reitaisai 12", "Autumn Reitaisai 12", "ARTS12", "第十二回 博麗神社秋季例大祭"],
            dates="2025.10.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://reitaisai.com/arts12/circle-place-assign/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)


    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (ReliabilityTypes.Likely, OriginTypes.External)),
        #         Source("", (ReliabilityTypes.Likely, OriginTypes.External))]
        #         , comments=""),
    ]
    links = ["https://reitaisai.com/", "https://x.com/HakureijinjyaS", "https://www.youtube.com/channel/UCWgWAk02r-HKSYX2h6wnJVA"]

    event_group = EventGroup(
        aliases=["博麗神社秋季例大祭", "Hakurei Jinja Shuuki Reitaisai", "秋季例大祭", "Autumn Reitaisai", "ARTS"],
        events=[],
        media=media,
        links=links,
        comments=f"Most sources were taken from {thwikicc}. As on thwiki.cc, several circle count discrepancies exist compared to official sources (not sourced here but can be seen on thwiki.cc)."
    )
    for event_raw in events_raw:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print("Saving arts database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

