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

    thwikicc = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD"
    main_page = "https://reitaisai.com/"

    if True: # ==== rts SP ====
        i = "sp1"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%ADSP/%E7%AC%AC1%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium(f"{i}_rts{i}.jpg",
            #        [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト東4・5・6ホール",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭SP", "博麗神社例大祭SP", "Hakurei Jinja Reitaisai SP", "Reitaisai SP", "RTS SP",
                     "博麗神社例大祭 (スペシャル)", "Hakurei Jinja Reitaisai Special",
                     "RTS SP1"],
            dates="2010.09.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source("Participating circles (1): https://web.archive.org/web/20100920094703/http://www.reitaisai.jp/circle/a.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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


    if True: # ==== rts ====
        i = "sp2"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%ADSP/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium(f"{i}_rts{i}.jpg",
            #        [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.918835313837!2d139.79293267568477!3d35.629727372603924!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601889dc629d1e7b%3A0xa4d1509a76045a01!2sTokyo%20Big%20Sight!5e0!3m2!1sen!2sfr!4v1760364136540!5m2!1sen!2sfr",
                description="東京ビッグサイト",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭SP2", "博麗神社例大祭SP2", "Hakurei Jinja Reitaisai SP2", "Reitaisai SP2", "RTS SP2",
                     "博麗神社例大祭 (スペシャル2)", "Hakurei Jinja Reitaisai Special 2"],
            dates="2011.09.11",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source("Participating circles (1): https://web.archive.org/web/20111123184511/http://reitaisai.jp/circlelists/search/circles/0", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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
        
    if True: # ==== rts tw1 ====
        i = "tw1"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E5%8F%B0%E6%B9%BE/%E7%AC%AC1%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_rts{i}.jpg",
                   [Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.157410346451!2d121.48567198885495!3d25.062653400000016!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a8e04de11a41%3A0xf27d8644141a1a2c!2z5paw5YyX5biC5LiJ6YeN5Y2A6auU6IKy5aC0!5e0!3m2!1sen!2sfr!4v1765667463705!5m2!1sen!2sfr",
                description="台灣新北市三重區體育場",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭in台灣1", "博麗神社例大祭in台灣1", "Hakurei Jinja Reitaisai in Taiwan 1", "Reitaisai in Taiwan 1", "RTS TW1", "第一回博麗神社例大祭in台灣"],
            dates="2015.06.06",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source(f"Participating circles (1): {thwikicc_local} (not sourced)", (ReliabilityTypes.Likely, OriginTypes.External)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== rts tw1.5 ====
        i = "tw1.5"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%B1%95%E4%BC%9A%E4%BD%9C%E5%93%81%E5%88%97%E8%A1%A8?e=%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E5%8F%B0%E6%B9%BE%231_5"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_rts{i}.jpg",
                   [Source(thwikicc_local, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3615.422751134836!2d121.53199438885494!3d25.019723499999984!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a9882cdb7da3%3A0xa00da84819efa80d!2z5ZyL56uL6Ie654Gj5aSn5a24IOiIiumrlOiCsumkqA!5e0!3m2!1sen!2sfr!4v1765667988483!5m2!1sen!2sfr",
                description="台灣台北市台灣大學體育館1樓",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭in台灣1.5", "博麗神社例大祭in台灣1.5", "Hakurei Jinja Reitaisai in Taiwan 1.5", "Reitaisai in Taiwan 1.5", "RTS TW1.5"],
            dates="2016.02.21",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                # Source("Participating circles (1): ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            comments=f"For more media, see {thwikicc}"
        )
        event_raw = event.get_json()
        # with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
        #     circles_raw = json.load(f)
        # event_raw["circles"] = circles_raw
        events_raw.append(event_raw)
        
    if True: # ==== rts tw2 ====
        i = "tw2"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E5%8F%B0%E6%B9%BE/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_rts{i}.jpg",
                   [Source(thwikicc_local, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                # iframe_url="",
                description="台灣台北市大同區承德路三段232號B2 卡市達創業加油站 圓山基地\nCould not find on map.",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭in台灣2", "博麗神社例大祭in台灣2", "Hakurei Jinja Reitaisai in Taiwan 2", "Reitaisai in Taiwan 2", "RTS TW2", "第二回博麗神社例大祭in台灣"],
            dates="2017.05.28",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source("Participating circles (1): https://afongcp.wixsite.com/rtstw2/clist", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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
        
    if True: # ==== rts tw3 ====
        i = "tw3"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E5%8F%B0%E6%B9%BE/%E7%AC%AC3%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_rts{i}.jpg",
                   [Source(thwikicc_local, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.7172049418177!2d121.5574002749248!3d25.043669437902942!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442abbf542aa63d%3A0xf465480fe2b78e8!2z5p2-5bGx5paH5Ym15ZyS5Y2A5aSa5Yqf6IO95bGV5ryU5buz!5e0!3m2!1sen!2sfr!4v1765669424444!5m2!1sen!2sfr",
                description="台北市信義區光復南路133號 松山文創園區 多功能展覽廳",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭in台灣3", "博麗神社例大祭in台灣3", "Hakurei Jinja Reitaisai in Taiwan 3", "Reitaisai in Taiwan 3", "RTS TW3", "第三回博麗神社例大祭in台灣"],
            dates="2019.06.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source("Participating circles (1): https://afongcp.wixsite.com/rtstw3/c-list", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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
        
    if True: # ==== rts tw4 ====
        i = "tw4"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E5%8F%B0%E6%B9%BE/%E7%AC%AC4%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_rts{i}.jpg",
                   [Source(thwikicc_local, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3614.170192198398!2d121.48826167492543!3d25.062220087155513!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442a91e321ce29b%3A0xc1e931184d134a1e!2sSanchong%20Comprehensive%20Gymnasium!5e0!3m2!1sen!2sfr!4v1765669518871!5m2!1sen!2sfr",
                description="台灣新北市三重區綜合體育館",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭in台灣4", "博麗神社例大祭in台灣4", "Hakurei Jinja Reitaisai in Taiwan 4", "Reitaisai in Taiwan 4", "RTS TW4", "第四回博麗神社例大祭in台灣"],
            dates="2024.09.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {thwikicc_local}", (ReliabilityTypes.Likely, OriginTypes.External)),
                Source("Participating circles (1): https://reitaisai.com/tw4/acceptance_circle/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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

    if True: # ==== rts gt1 ====
        i = "gt1"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E6%96%B0%E6%BD%9F/%E7%AC%AC1%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_rts{i}.png",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3149.20231801618!2d139.04368337543548!3d37.87895100615289!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5ff4c8c27b40493b%3A0xf98af3a56ebcef90!2sSangyo%20Shinko%20Center!5e0!3m2!1sen!2sfr!4v1765716159376!5m2!1sen!2sfr",
                description="新潟市産業振興センター",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭in新潟1", "博麗神社例大祭in新潟1", "Hakurei Jinja Reitaisai in Niigata 1", "Reitaisai in Niigata 1", "RTS GT1", "第一回博麗神社例大祭in新潟"],
            dates="2022.03.20",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://gataket.com/list/reitai_03c/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://gataket.com/list/reitai_03c/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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

    if True: # ==== rts gt2 ====
        i = "gt2"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E6%96%B0%E6%BD%9F/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_rts{i}.png",
                   [Source(thwikicc_local, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3149.20231801618!2d139.04368337543548!3d37.87895100615289!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5ff4c8c27b40493b%3A0xf98af3a56ebcef90!2sSangyo%20Shinko%20Center!5e0!3m2!1sen!2sfr!4v1765716159376!5m2!1sen!2sfr",
                description="新潟市産業振興センター",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭in新潟2", "博麗神社例大祭in新潟2", "Hakurei Jinja Reitaisai in Niigata 2", "Reitaisai in Niigata 2", "RTS GT2", "第二回博麗神社例大祭in新潟"],
            dates="2024.12.01",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://gataket.com/list/g179/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://gataket.com/list/g179/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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

    if True: # ==== rts gt3 ====
        i = "gt3"
        name = f"rts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E6%96%B0%E6%BD%9F/%E7%AC%AC3%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium(f"{i}_rts{i}.png",
                   [Source(thwikicc_local, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3149.20231801618!2d139.04368337543548!3d37.87895100615289!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5ff4c8c27b40493b%3A0xf98af3a56ebcef90!2sSangyo%20Shinko%20Center!5e0!3m2!1sen!2sfr!4v1765716159376!5m2!1sen!2sfr",
                description="新潟市産業振興センター",
                sources=[Source(thwikicc_local, (ReliabilityTypes.Likely, OriginTypes.External))]
            ),
        ]
        event = Event(
            aliases=["例大祭in新潟3", "博麗神社例大祭in新潟3", "Hakurei Jinja Reitaisai in Niigata 3", "Reitaisai in Niigata 3", "RTS GT3", "第三回博麗神社例大祭in新潟"],
            dates="2025.11.30",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://gataket.com/list/g182/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://gataket.com/list/g182/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
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

    if True: # ==== srts 2 ====
        i = "2"
        name = f"srts{i}"
        thwikicc_local = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD_in_%E9%9D%99%E5%86%88/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("s2_srts2.jpg",
                   [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3269.38637849115!2d138.40341397530162!3d34.97198546860931!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601a361bad3e7279%3A0x119718565bb552e2!2sTwin%20Messe%20Shizuoka!5e0!3m2!1sen!2sfr!4v1765717400870!5m2!1sen!2sfr",
                description="ツインメッセ静岡",
                sources=[Source("https://reitaisai.com/srts2/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            ),
        ]
        event = Event(
            aliases=["例大祭in静岡2", "博麗神社例大祭in静岡2", "Hakurei Jinja Reitaisai in Shizuoka 2", "Reitaisai in Shizuoka 2", "RTS S2", "第二回博麗神社例大祭in静岡"],
            dates="2025.03.23",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://reitaisai.com/srts2/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles (1): https://reitaisai.com/srts2/circle-place-assign/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(f"Participating circles (2): {thwikicc_local} (well sourced)", (ReliabilityTypes.Reliable, OriginTypes.External)),
            ],
            locations=locations,
            comments="Note: '第一回博麗神社例大祭in静岡' actually is RTS 18."
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
    links = ["https://reitaisai.com/", "https://x.com/HakureijinjyaS", "https://www.youtube.com/channel/UCWgWAk02r-HKSYX2h6wnJVA", 
             "https://x.com/reitaisai_sp"
             ]

    event_group = EventGroup(
        aliases=["博麗神社例大祭 (other events)", "Hakurei Jinja Reitaisai (other events)", "秋季例大祭 (other events)", "Reitaisai (other events)", "RTS (other events)"],
        events=[],
        media=media,
        links=links,
        description="RTS (博麗神社例大祭) events not of the main numbered series, such as the SP (Special) events.",
        comments=f"Most sources were taken from {thwikicc}. As on thwiki.cc, several circle count discrepancies exist compared to official sources (not sourced here but can be seen on thwiki.cc)."
    )
    for event_raw in events_raw:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print("Saving arts database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")
        

