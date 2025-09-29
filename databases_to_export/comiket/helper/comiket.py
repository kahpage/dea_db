# About:
# About archives https://www.comiket.co.jp/info-a/ExhibitCatalog.html
# Pdf files for newer comikets https://webcatalog-archives.circle.ms/
# Manga recap https://www.comiket.co.jp/info-a/MR/mr.html
# Archive  cominavi https://www.comi-navi.com/contents/html/archive.htm
# http://www.ahoge.com and similar websites

# https://www.comiket.co.jp/catarom/
# https://int.webcatalog.circle.ms/
# https://webcatalog.circle.ms/


from db_structs import Medium, Circle, Event, EventGroup, Source, ReliabilityTypes, OriginTypes
from pathlib import Path
import json
from bs4 import BeautifulSoup, Comment
import re
import requests
from typing import Any

def prefix_all_circle_media_of_event(event_raw: dict[str, Any], prefix: str) -> None:
    """
    Prefix all media URLs of circles in the event with the given prefix.
    """
    if "circles" not in event_raw:
        return
    for circle_raw in event_raw["circles"]:
        if "media" not in circle_raw:
            continue
        for medium in circle_raw.get("media", []):
            if medium.get("path"):
                medium["path"] = prefix + medium["path"]

if __name__ == '__main__':
    SAVE_INTER_JSON = False
    save_folder_path = Path(__file__).parent
    events_raw: list[Any] = []
    
    if True: # ==== C106 ====
        i = 106

        circles_ = []
        media_ = [
            Medium("106_CWC_C106L.png",
                   [Source("https://web.archive.org/web/20250726082151/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("106_CWC_C106.png",
                   [Source("https://web.archive.org/web/20250726082151/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("106_C106CtlgWeb.jpeg",
                   [Source("https://web.archive.org/web/20250716040318/https://comiket.co.jp/info-a/C106/C106distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：Anmi（サークル：メガネ女子） ２日目南ａ43ab"),
            Medium("106_C106Kamibukuro.jpeg",
                   [Source("https://web.archive.org/web/20250716040318/https://comiket.co.jp/info-a/C106/C106distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="ラスト：ideolo（サークル：NEKO WORLDi) 　１日目西め60ab"),
            Medium("https://web.archive.org/web/20250409184101/https://www.comiket.co.jp/info-c/C106/C106Appset.pdf",
                   [Source("https://web.archive.org/web/20250716040318/https://comiket.co.jp/info-a/C106/C106distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙イラスト：ぴこぴこぐらむ（サークル：プラチナきのこ）  ２日目東ア83ab"),
            Medium("https://www.comiket.co.jp/info-a/C106/C106CtlgNotes.pdf",
                   [Source("https://www.comiket.co.jp/info-a/C106/C106CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2025.08.16 - 2025.08-17",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://www.comiket.co.jp/info-a/CatalogShop.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C105 ====
        i = 105

        circles_ = []
        media_ = [
            Medium("105_CWC_C105L.png",
                   [Source("https://web.archive.org/web/20250717100148/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("105_CWC_C105.png",
                   [Source("https://web.archive.org/web/20250627101710/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("105_C105CtlgWeb.jpeg",
                   [Source("https://web.archive.org/web/20250112211002/https://comiket.co.jp/info-a/C105/C105distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：美好よしみ（サークル：MY ROOM) ２日目西め63b"),
            Medium("105_C105Kamibukuro.png",
                   [Source("https://web.archive.org/web/20250112211002/https://comiket.co.jp/info-a/C105/C105distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：おしおしお（サークル：OSHIOSHIO) ２日目西め19a デザイン：モージ"),
            Medium("https://web.archive.org/web/20240731183307/https://www.comiket.co.jp/info-c/C105/C105Appset.pdf",
                   [Source("https://web.archive.org/web/20250112211002/https://comiket.co.jp/info-a/C105/C105distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙イラスト：あまみね（サークル：あまみねこカフェ) ２日目西へ20a"),
            Medium("https://web.archive.org/web/20250112211614mp_/https://comiket.co.jp/info-a/C105/C105kigyou/C105Kigyou_Booth_Pamphlet.pdf",
                   [Source("https://web.archive.org/web/20250112211614/https://comiket.co.jp/info-a/C105/C105kigyou/", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：rioka（サークル：サザンブルースカイ） １日目東ａ09a"),
            Medium("https://web.archive.org/web/20250607011803/https://www.comiket.co.jp/info-a/C105/C105CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20250607011803/https://www.comiket.co.jp/info-a/C105/C105CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2024.12.29 - 2024.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20250112211002/https://comiket.co.jp/info-a/C105/C105distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

            
    if True: # ==== C104 ====
        i = 104

        circles_ = []
        media_ = [
            Medium("104_CWC_C104L.png",
                   [Source("https://web.archive.org/web/20240731183307/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("104_CWC_C104.png",
                   [Source("https://web.archive.org/web/20240731183307/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("104_C104CtlgWeb.jpeg",
                   [Source("https://web.archive.org/web/20250415212758/https://www.comiket.co.jp/info-a/C104/C104distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：タカヤマトシアキ（サークル：T.com）　デザイン：宮本祐輔"),
            Medium("104_C104Kamibukuro.png",
                   [Source("https://web.archive.org/web/20250415212758/https://www.comiket.co.jp/info-a/C104/C104distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：アシマ（サークル：flourish）"),
            Medium("https://web.archive.org/web/20240703194739/https://www2.comiket.co.jp/info-c/C104/C104Appset.pdf",
                   [Source("https://web.archive.org/web/20250415212758/https://www.comiket.co.jp/info-a/C104/C104distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙イラスト：れぶん（サークル：れぶん） 2日目東ｐ17b"),
            Medium("104_C104_pamphlet_thumb.png",
                   [Source("https://web.archive.org/web/20250415212758/https://www.comiket.co.jp/info-a/C104/C104distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：みきさい（サークル：アンディスクライブド） 2日目東ｑ01b"),
            Medium("https://web.archive.org/web/20250304232241/https://www.comiket.co.jp/info-a/C104/C104kigyou/C104Kigyou_Booth_Pamphlet.pdf",
                   [Source("https://web.archive.org/web/20250415212758/https://www.comiket.co.jp/info-a/C104/C104distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：みきさい（サークル：アンディスクライブド） 2日目東ｑ01b"),
            Medium("https://web.archive.org/web/20250528142328/https://www.comiket.co.jp/info-a/C104/C104CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20250528142328/https://www.comiket.co.jp/info-a/C104/C104CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),                  
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2024.08.11 - 2024.08.12",
            circles=circles_,
            media=media_,
            sources=[
                # Source("Date: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C103 ====
        i = 103

        circles_ = []
        media_ = [
            Medium("103_CWC_C103.png",
                   [Source("https://web.archive.org/web/20231209043210/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("103_CWC_C103L.png",
                   [Source("https://web.archive.org/web/20231209043210/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("103_C103CtlgWeb.png",
                   [Source("https://web.archive.org/web/20250115003253/https://www.comiket.co.jp/info-a/C103/C103distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：バーニア600（サークル：ぢま鉄） 2日目東Ａ91b"),
            Medium("103_C103KamibukuroL.png",
                   [Source("https://web.archive.org/web/20250115003253/https://www.comiket.co.jp/info-a/C103/C103distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：もみじ真魚（サークル：こもれびのーと） 2日目西め54a"),
            Medium("https://web.archive.org/web/20231209054804/https://www2.comiket.co.jp/info-c/C103/C103Appset.pdf",
                   [Source("https://web.archive.org/web/20250115003253/https://www.comiket.co.jp/info-a/C103/C103distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙イラスト：桜沢いづみ（サークル：CHRONOLOG） ２日目東Ｃ31b"),
            Medium("103_C103_pamphlet_thumb.png",
                   [Source("https://web.archive.org/web/20250115003253/https://www.comiket.co.jp/info-a/C103/C103distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：くるみつ（サークル：POPLOOP） ２日目西せ26a"),
            Medium("https://web.archive.org/web/20240420131922/https://www2.comiket.co.jp/info-a/C103/C103kigyou/C103Kigyou_Booth_Pamphlet.pdf",
                   [Source("https://web.archive.org/web/20250115003253/https://www.comiket.co.jp/info-a/C103/C103distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：くるみつ（サークル：POPLOOP） ２日目西せ26a"),
            Medium("https://web.archive.org/web/20250404165729/https://www.comiket.co.jp/info-a/C103/C103CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20250404165729/https://www.comiket.co.jp/info-a/C103/C103CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2023.12.30 - 2023.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20250115003253/https://www.comiket.co.jp/info-a/C103/C103distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C102 ====
        i = 102

        circles_ = []
        media_ = [
            Medium("102_CWC_C102.png",
                   [Source("https://web.archive.org/web/20230718060813/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("102_CWC_C102L.png",
                   [Source("https://web.archive.org/web/20230718060813/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("102_C102CtlgWeb.jpeg",
                   [Source("https://web.archive.org/web/20250404192004/https://www.comiket.co.jp/info-a/C102/C102distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：とりヒコ（サークル：SUZURO） 1日目西き23b"),
            Medium("102_C102KamibukuroL.jpeg",
                   [Source("https://web.archive.org/web/20250404192004/https://www.comiket.co.jp/info-a/C102/C102distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：絶叫（サークル：白血球赤血球） 1日目西ふ15a"),
            Medium("https://web.archive.org/web/20230718060813/https://www2.comiket.co.jp/info-c/C102/C102Appset.pdf",
                   [Source("https://web.archive.org/web/20230718060813/https://www2.comiket.co.jp/info-c/C102/C102Appset.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                    Source("https://web.archive.org/web/20230125004924/https://www2.comiket.co.jp/info-a/C101/C101distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙イラスト：佐伯ソラ（サークル：ぽよぴよスカイ） ２日目東ス53a\n表紙イラスト：スガ（サークル：L-wing）"),
            Medium("102_C102_pamphlet_thumb.png",
                   [Source("https://web.archive.org/web/20230718060813/https://www2.comiket.co.jp/info-c/C102/C102Appset.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：茉宮祈芹（サークル：Chericot*Rozel） ２日目東Ａ27ab"),
            Medium("https://web.archive.org/web/20240718224720/https://www2.comiket.co.jp/info-a/C102/C102kigyou/C102Kigyou_Booth_Pamphlet.pdf",
                   [Source("https://web.archive.org/web/20230718060813/https://www2.comiket.co.jp/info-c/C102/C102Appset.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：茉宮祈芹（サークル：Chericot*Rozel） ２日目東Ａ27ab"),
            Medium("https://web.archive.org/web/20230718060813/https://www2.comiket.co.jp/info-a/C102/C102CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20230718060813/https://www2.comiket.co.jp/info-a/C102/C102CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2023.08.12 - 2023.08.13",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20250404192004/https://www.comiket.co.jp/info-a/C102/C102distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C101 ====
        i = 101

        circles_ = []
        media_ = [
            Medium("101_CWC_C101.png",
                   [Source("https://web.archive.org/web/20221229101630/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("101_CWC_C101L.png",
                   [Source("https://web.archive.org/web/20221229101630/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("101_C101CtlgWeb.jpeg",
                   [Source("https://web.archive.org/web/20230125004924/https://www2.comiket.co.jp/info-a/C101/C101distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：LAM／デザイン：カトウ　（サークル：雷雷公社）"),
            Medium("101_C101KamibukuroL.jpeg",
                   [Source("https://web.archive.org/web/20230125004924/https://www2.comiket.co.jp/info-a/C101/C101distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：蒼喬（サークル：理蒼郷）"),
            Medium("https://web.archive.org/web/20231127050807/https://www2.comiket.co.jp/info-c/C101/C101Appset.pdf",
                   [Source("https://web.archive.org/web/20250405040850/https://www.comiket.co.jp/info-a/C100/C100distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：桜ひより（サークル：ひよこサブレ）"),
            Medium("https://web.archive.org/web/20230720080945/https://www2.comiket.co.jp/info-a/C101/C101CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20230720080945/https://www2.comiket.co.jp/info-a/C101/C101CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2012.12.30 - 2012.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20230125004924/https://www2.comiket.co.jp/info-a/C101/C101distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C100 ====
        i = 100

        circles_ = []
        media_ = [
            Medium("100_CWC_C100.png",
                   [Source("https://web.archive.org/web/20220806165810/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("100_CWC_C100L.png",
                   [Source("https://web.archive.org/web/20220806165810/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("100_C100LogoAll.png",
                   [Source("https://web.archive.org/web/20220806183134/https://www.comiket.co.jp/info-c/C100/C100Logo.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20220812173152/https://www2.comiket.co.jp/info-c/C100/c100_logo.zip",
                   [Source("https://web.archive.org/web/20220806183134/https://www.comiket.co.jp/info-c/C100/C100Logo.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("100_C100CtlgWeb.jpeg",
                   [Source("https://web.archive.org/web/20250405040850/https://www.comiket.co.jp/info-a/C100/C100distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙原画：武内崇（サークル：竹帚） 彩色・仕上げ：こやまひろかず 背景：ゆうろ ロゴ：WINFANWORKS "),
            Medium("100_C100KamibukuroL.png",
                   [Source("https://web.archive.org/web/20250405040850/https://www.comiket.co.jp/info-a/C100/C100distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：Dr.モロー（サークル：モロモロ） デザイン：木緒なち（サークル：コロリメイジ）"),
            Medium("https://web.archive.org/web/20220806165810/https://www2.comiket.co.jp/info-a/C100/C100CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20220806165810/https://www2.comiket.co.jp/info-a/C100/C100CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20231127050808/https://www2.comiket.co.jp/info-c/C100/C100Appset.pdf",
                   [Source("https://web.archive.org/web/20231127050808/https://www2.comiket.co.jp/info-c/C100/C100Appset.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2022.08.13 - 2022.08.14",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20250405040850/https://www.comiket.co.jp/info-a/C100/C100distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C99 ====
        i = 99

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250404190005/https://www.comiket.co.jp/info-a/C99A/C99Adistributions.html'
        media_ = [
            Medium("99_CWC_C99.png",
                   [Source("https://web.archive.org/web/20211224125426/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("99_CWC_C99L.png",
                   [Source("https://web.archive.org/web/20211224125426/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("99_C99A_key_visual.png",
                   [Source("https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="キービジュアル：Hiten"),
            Medium("99_C99KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：ERIMO（サークル：ERIMO）"),
            Medium("https://web.archive.org/web/20250406071744/https://www2.comiket.co.jp/info-a/C99A/C99ACtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20250406071744/https://www2.comiket.co.jp/info-a/C99A/C99ACtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20241207212737/https://www2.comiket.co.jp/info-c/C99A/C99AAppset.pdf",
                   [Source("https://web.archive.org/web/20241207212737/https://www2.comiket.co.jp/info-c/C99A/C99AAppset.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2021.05.02 - 2021.05.02 → 2021.12.30 - 2021.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20211224125426/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Postponed: https://www.comiket.co.jp/info-a/C99/C99Notice2.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C98 ====
        i = 98

        circles_ = []
        media_ = [
            Medium("98_CWC_C98.png",
                   [Source("https://web.archive.org/web/20210804112536/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("98_CWC_C98L.png",
                   [Source("https://web.archive.org/web/20210804112536/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("98_98CtlgWeb.jpeg",
                   [Source('https://web.archive.org/web/0/https://web.archive.org/web/20200428115034/https://www.comiket.co.jp/info-a/C98/AirComiket98.html', (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙 イラスト：くるみつ（サークル：POPLOOP）／デザイン：レク 注意漫画：あづみ一樹（サークルComeThrough）"),
            Medium("98_98CtlgRomWeb.jpeg",
                   [Source("https://web.archive.org/web/0/https://web.archive.org/web/20200428115034/https://www.comiket.co.jp/info-a/C98/AirComiket98.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：いとうのいぢ（サークル：富士壺機械）" ),
            Medium("98_kenketsu-logo_c098.png",
                   [Source("https://web.archive.org/web/2/https://www.comiket.co.jp/info-a/C98/C98Covid19Notice5.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("98_40th_CHRONICLE_Hyoshi.jpeg",
                   [Source("https://web.archive.org/web/2/https://www.comiket.co.jp/info-a/C98/C98Covid19Notice5.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("https://web.archive.org/web/20240614144426/https://www.comiket.co.jp/info-a/C98/C98CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20240614144426/https://www.comiket.co.jp/info-a/C98/C98CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("98_C98Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250307200729/https://www.comiket.co.jp/info-a/C97/C97distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：MATSUDA98（サークル：MATSUDASTYLE）"),
            Medium("98_C98KamibukuroL.jpeg",
                   [Source("https://web.archive.org/web/0/https://web.archive.org/web/20200428115034/https://www.comiket.co.jp/info-a/C98/AirComiket98.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Perhaps rather エアコミケ 1 #TODO"),
            Medium("98_C98KamibukuroS.jpeg",
                   [Source("https://web.archive.org/web/0/https://web.archive.org/web/20200428115034/https://www.comiket.co.jp/info-a/C98/AirComiket98.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Perhaps rather エアコミケ 1 #TODO"),
            Medium("98_AirComiketniconico.jpeg",
                   [Source("https://web.archive.org/web/0/https://web.archive.org/web/20200428115034/https://www.comiket.co.jp/info-a/C98/AirComiket98.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Perhaps rather エアコミケ 1 #TODO"),
            Medium("98_C98Wristband.png",
                   [Source("https://web.archive.org/web/0/https://web.archive.org/web/20200428115034/https://www.comiket.co.jp/info-a/C98/AirComiket98.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Perhaps rather エアコミケ 1 #TODO"),
            Medium("https://web.archive.org/web/20210117023521/https://www.comiket.co.jp/info-a/C98/C98CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20210117023521/https://www.comiket.co.jp/info-a/C98/C98CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2020.05.02 - 2020.05.05 (CANCELLED)",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date, Cancellation: https://www.comiket.co.jp/info-a/C98/C98Covid19Notice2.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C97 ====
        i = 97

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250307200729/https://www.comiket.co.jp/info-a/C97/C97distributions.html'
        media_ = [
            Medium("97_CWC_C97.png",
                   [Source("https://web.archive.org/web/20191228070306/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("97_CWC_C97L.png",
                   [Source("https://web.archive.org/web/20191228070306/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("97_wristband.png",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("97_C97CtlgWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ヤマコ（サークル：HoneyWorks）"),
            Medium("97_C97KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：よー清水（サークル：鳥猫アクアリウム）"),
            Medium("97_C97KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：吉田誠治（サークル：TNK）"),
            Medium("97_C97_kigyouPamf_H1.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="ウエダハジメ（サークル：貧血エレベーター）"),
            Medium("97_C97CtlgRomWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ヤマコ（サークル：HoneyWorks）"),
            Medium("https://web.archive.org/web/20191224170102/https://www2.comiket.co.jp/info-a/C97/C97CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20191224170102/https://www2.comiket.co.jp/info-a/C97/C97CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("97_C97Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250405002744/https://www.comiket.co.jp/info-a/C96/C96distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="めんつゆ（サークル：わんわんスライム）"),
            Medium("https://web.archive.org/web/20191222101125/https://www2.comiket.co.jp/info-a/C97/C97CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20191222101125/https://www2.comiket.co.jp/info-a/C97/C97CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2019.12.28 - 2019.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)


    if True: # ==== C96 ====
        i = 96

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250405002744/https://www.comiket.co.jp/info-a/C96/C96distributions.html'
        media_ = [
            Medium("96_CWC_C96.png",
                   [Source("https://web.archive.org/web/20190801005145/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("96_CWC_C96L.png",
                   [Source("https://web.archive.org/web/20190801005145/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("96_C96CtlgWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：加藤さやか（サークル：TRiS）"),
            Medium("96_wristband.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("96_C96KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="nocras（サークル：Orbital Express）"),
            Medium("96_C96KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="望月けい（サークル：生け贄）"),
            Medium("96_C96kigyouPamf.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：にじはし そら（サークル：art en ciel.)"),
            Medium("96_C96CtlgRomWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：加藤さやか（サークル：TRiS）"),
            Medium("https://www.comiket.co.jp/info-a/C96/C96CtlgNotes.pdf",
                   [Source("https://www.comiket.co.jp/info-a/C96/C96CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , ),
            Medium("96_C96Moushikomisho.jpeg",
                   [Source('https://web.archive.org/web/20250621082023/https://comiket.co.jp/info-a/C95/C95distributions.html', (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：天河藍（サークル：マシュマロ響団）"),
            Medium("https://web.archive.org/web/20190714122807/https://www2.comiket.co.jp/info-a/C96/C96CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20190714122807/https://www2.comiket.co.jp/info-a/C96/C96CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2019.08.09 - 2019.08.12",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C95 ====
        i = 95

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250621082023/https://comiket.co.jp/info-a/C95/C95distributions.html'
        media_ = [
            Medium("95_CWC_C95.png",
                   [Source("https://web.archive.org/web/20181228011104/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("95_CWC_C95L.png",
                   [Source("https://web.archive.org/web/20181228011104/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("95_C95CtlgWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ワダアルコ（サークル：ワダメモ）"),
            Medium("95_C95KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：晩杯あきら（サークル：奴は仮名）"),
            Medium("95_C95KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：タキザワアスカ（サークル：屋上ラビュー）"),
            Medium("95_C95_kigyouPamf_H1.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：LAM（サークル：LAMLAB)"),
            Medium("95_C95CtlgRomWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ワダアルコ（サークル：ワダメモ）"),
            Medium("95_C95Moushikomisho.jpeg",
                   [Source('https://web.archive.org/web/20250404235221/https://www.comiket.co.jp/info-a/C94/C94distributions.html', (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：タケノコ（サークル：くがつここのか）"),
            Medium("http://web.archive.org/web/20181225091914/https://www2.comiket.co.jp/info-a/C95/C95CtlgNotes.pdf",
                   [Source("http://web.archive.org/web/20181225091914/https://www2.comiket.co.jp/info-a/C95/C95CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2018.12.29 - 2018.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)


    if True: # ==== C94 ====
        i = 94

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250404235221/https://www.comiket.co.jp/info-a/C94/C94distributions.html'
        media_ = [
            Medium("94_CWC_C94.png",
                   [Source("https://web.archive.org/web/20180805092358/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("94_CWC_C94L.png",
                   [Source("https://web.archive.org/web/20180805092358/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("94_C94CtlgWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：あおいれびん（サークル：万有）"),
            Medium("94_C94KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：POKImari(サークル：POKIZM)"),
            Medium("94_C94KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：にゃごしま（サークル：UNDRESS）"),
            Medium("94_C94kigyouPamf.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ぴこぴこぐらむ（サークル：プラチナきのこ)"),
            Medium("94_C94CtlgRomWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：あおいれびん（サークル：万有）"),
            Medium("94_C94Moushikomisho.jpeg",
                   [Source('https://web.archive.org/web/20250114175314/https://www.comiket.co.jp/info-a/C93/C93distributions.html', (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：わに（サークル：クロコダイルティアーズ）"),
            Medium("http://web.archive.org/web/20180805092452/https://www2.comiket.co.jp/info-a/C94/C94CtlgNotes.pdf",
                   [Source("http://web.archive.org/web/20180805092452/https://www2.comiket.co.jp/info-a/C94/C94CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2018.08.10 - 2018.08.12",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C93 ====
        i = 93

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250114175314/https://www.comiket.co.jp/info-a/C93/C93distributions.html'
        media_ = [
            Medium("93_CWC_C93.png",
                   [Source("https://web.archive.org/web/20171228130502/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("93_CWC_C93L.png",
                   [Source("https://web.archive.org/web/20171228130502/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("93_C93CtlgWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：Mika Pikazo（サークル：MikaPikaZo）"),
            Medium("93_C93KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：加藤アカツキ(サークル：残像アパートメント)"),
            Medium("93_C93KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：空乃金魚（サークル：☆ぱぐＰａｌｅｔｔｅ☆）"),
            Medium("93_C93kigyouPamf.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：早川あかり（サークル：MUSES　GARDEN)"),
            Medium("93_C93CtlgRomWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：Mika Pikazo（サークル：MikaPikaZo）"),
            Medium("93_C93Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250114195114/https://www.comiket.co.jp/info-a/C92/C92distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：蜜野はち（サークル：posy）"),
            Medium("https://web.archive.org/web/20171223135916/http://www2.comiket.co.jp/info-a/C93/C93CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20171223135916/http://www2.comiket.co.jp/info-a/C93/C93CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2017.12.29 - 2017.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C92 ====
        i = 92

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250114195114/https://www.comiket.co.jp/info-a/C92/C92distributions.html'
        media_ = [
            Medium("92_CWC_C92.png",
                   [Source("https://web.archive.org/web/20170809142827/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("92_CWC_C92L.png",
                   [Source("https://web.archive.org/web/20170809142827/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("92_92CtlgWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：としお(サークル：凍傷炎)"),
            Medium("92_C92KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：mocha（サークル：Cotton）"),
            Medium("92_C92KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：タカトウアユミ（サークル：リズミカ）"),
            Medium("92_C92_kigyouPamf.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ニリツ（サークル：ニリツハイハン）"),
            Medium("92_92CtlgRomWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：としお(サークル：凍傷炎)"),
            Medium("92_C92Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250114223928/https://www.comiket.co.jp/info-a/C91/C91distributi", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：炬太郎（サークル：炬燵太郎）"),
            Medium("http://web.archive.org/web/20170901210455/http://www2.comiket.co.jp/info-a/C92/C92CtlgNotes.pdf",
                   [Source("http://web.archive.org/web/20170901210455/http://www2.comiket.co.jp/info-a/C92/C92CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2017.08.11 - 2017.08.13",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C91 ====
        i = 91

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250114195114/https://www.comiket.co.jp/info-a/C91/C91distributions.html'
        media_ = [
            Medium("91_CWC_C91.png",
                   [Source("https://web.archive.org/web/20161216093131/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("91_CWC_C91L.png",
                   [Source("https://web.archive.org/web/20161216093131/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("91_C91CtlgWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：主犯(サークル：刑法第６０条)"),
            Medium("91_C91KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：もりのほん（サークル：ForestRest）"),
            Medium("91_C91KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：くるみあべし（サークル：にっけるめっきし）"),
            Medium("91_C91kigyouPamf_H1s.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：笹森トモエ（NANIMOSHINAI）"),
            Medium("91_C91CtlgRomWeb.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：主犯(サークル：刑法第６０条)"),
            Medium("91_C91Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250114103757/https://www.comiket.co.jp/info-a/C90/C90distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：しけー（サークル：行脚堂）"),
            Medium("http://web.archive.org/web/20170706163938/http://www.comiket.co.jp/info-a/C91/C91CtlgNotes.pdf",
                   [Source("http://web.archive.org/web/20170706163938/http://www.comiket.co.jp/info-a/C91/C91CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2016.12.29 - 2016.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C90 ====
        i = 90

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250114103757/https://www.comiket.co.jp/info-a/C90/C90distributions.html'
        media_ = [
            Medium("90_CWC_C90.png",
                   [Source("https://web.archive.org/web/20160809172540/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("90_CWC_C90L.png",
                   [Source("https://web.archive.org/web/20160809172540/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("90_C90Ctlg.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：蔦(サークル：泥沼分室)／表紙デザイン：鯖(サークル：LHA-2）"),
            Medium("90_C90amibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：ヤマモトナオキ（サークル：ヤマモトナオキ）"),
            Medium("90_C90KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：うゆ（サークル：cartoon-tv）"),
            Medium("90_C90KigyoPamphlet.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：コダマ（コダマンダラ）／表紙デザイン：柊椋（I.S.W）"),
            Medium("90_C90CtlgRom.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：蔦(サークル：泥沼分室)／表紙デザイン：鯖(サークル：LHA-2）"),
            Medium("90_C90Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250114180440/https://www.comiket.co.jp/info-a/C89/C89distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表示イラスト：飯尾（サークル：柴漬け）"),
            Medium("https://web.archive.org/web/20170706163059/http://www.comiket.co.jp/info-a/C90/C90CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20170706163059/http://www.comiket.co.jp/info-a/C90/C90CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2016.08.12 - 2016.08.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C89 ====
        i = 89

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250114180440/https://www.comiket.co.jp/info-a/C89/C89distributions.html'
        media_ = [
            Medium("89_CWC_C89.png",
                   [Source("https://web.archive.org/web/20160105141546/http://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("89_CWC_C89L.png",
                   [Source("https://web.archive.org/web/20160105141546/http://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("89_C89CtlgSasshi.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：スー（サークル：vgmt）"),
            Medium("89_C89KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：かわく（サークル：カワクウズウズ）"),
            Medium("89_C89KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：せんむ（サークル：GRAPHIC!!）"),
            Medium("89_C89KigyoPamphlet.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="ファルまろ（サークル：よっこらペンシル）"),
            Medium("89_C89CtlgRom.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="スー（サークル：vgmt）"),
            Medium("89_C89Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250115023056/https://www.comiket.co.jp/info-a/C88/C88distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙イラスト：シキブ（サークル：OPERA）"),
            Medium("https://web.archive.org/web/20160307171702/http://www.comiket.co.jp/info-a/C89/C89CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20160307171702/http://www.comiket.co.jp/info-a/C89/C89CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2015.12.29 - 2015.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C88 ====
        i = 88

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250115023056/https://www.comiket.co.jp/info-a/C88/C88distributions.html'
        media_ = [
            Medium("88_CWC_C88.png",
                   [Source("https://web.archive.org/web/20150807051111/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("88_CWC_C88L.png",
                   [Source("https://web.archive.org/web/20150807051111/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("88_C88CtlgSasshi.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：新谷かおる（サークル：八十八夜）"),
            Medium("88_C88KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：マツオヒロミ（サークル：六花弁三片紅）"),
            Medium("88_C88KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：鉄板！（サークル：ギラギライズ）"),
            Medium("88_C88KigyoPamphlet.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="おかだアンミツ（サークル：フェザー・クラウン）"),
            Medium("88_C88CtlgRom.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：新谷かおる（サークル：八十八夜）"),
            Medium("88_C88Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250114195114/https://www.comiket.co.jp/info-a/C87/C87distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表示イラスト：茶森（サークル：tyamorix）"),
            Medium("https://web.archive.org/web/20160307171317/http://www.comiket.co.jp/info-a/C88/C88CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20160307171317/http://www.comiket.co.jp/info-a/C88/C88CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("88_1600px-C88-firstdaycircleticket.jpg",
                   [Source('https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%9F%E3%83%83%E3%82%AF%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%83%E3%83%88', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2015.08.14 - 2015.08.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C87 ====
        i = 87

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250114195114/https://www.comiket.co.jp/info-a/C87/C87distributions.html'
        media_ = [
            Medium("87_CWC_C87.png",
                   [Source("https://web.archive.org/web/20141230063426/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("87_CWC_C87L.jpeg",
                   [Source("https://web.archive.org/web/20141230063426/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("87_C87CtlgSasshi.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：なかじまゆか（サークル：Digital Lover）"),
            Medium("87_C87KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：カズキヨネ（サークル：壱角）"),
            Medium("87_C87KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：上野キミコ（サークル：はちみつバタつきパン）"),
            Medium("87_C87KigyoPamphlet.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：なつめえり（サークル：いちごさいず）"),
            Medium("87_C87CtlgRom.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="なかじまゆか（サークル：Digital Lover）"),
            Medium("87_C87Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250115004137/https://www.comiket.co.jp/info-a/C86/C86distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：シン太（サークル：あばらが痛い）"),
            Medium("https://web.archive.org/web/20150723111350/http://www.comiket.co.jp/info-a/C87/C87CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20150723111350/http://www.comiket.co.jp/info-a/C87/C87CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2014.12.28 - 2014.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C86 ====
        i = 86

        circles_ = []
        dist_url = 'https://web.archive.org/web/20250115004137/https://www.comiket.co.jp/info-a/C86/C86distributions.html'
        media_ = [
            Medium("86_CWC_C86.png",
                   [Source("https://web.archive.org/web/20140813005350/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("86_CWC_C86L.jpeg",
                   [Source("https://web.archive.org/web/20140813005350/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("86_C86CtlgSasshi.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ゆーげん（サークル：キャッスルトン）"),
            Medium("86_C86KamibukuroL.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：吾可子（サークル：徒野）"),
            Medium("86_C86KamibukuroS.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：えすとえむ（サークル：VOSTOK）"),
            Medium("86_C86KigyoPamphlet.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：水あさと（サークル：オレンジミル）"),
            Medium("86_C86CtlgRom.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ゆーげん（サークル：キャッスルトン）"),
            Medium("86_C85Moushikomisho.jpeg",
                   [Source("https://web.archive.org/web/20250114181842/https://www.comiket.co.jp/info-a/C85/C85distributions.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：みわべさくら（サークル：Pion）\nNote: This is indeed the filename."),
            Medium("http://web.archive.org/web/20140813052412/http://www.comiket.co.jp/info-a/C86/C86CtlgNotes.pdf",
                   [Source("http://web.archive.org/web/20140813052412/http://www.comiket.co.jp/info-a/C86/C86CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2014.08.15 - 2014.08.17",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C85 ====
        i = 85

        circles_ = []
        dist_url = 'https://web.archive.org/web/20140209004153/https://www.comiket.co.jp/'
        media_ = [
            Medium("85_CWC_C85.jpeg",
                   [Source("https://web.archive.org/web/20140209004153/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("85_CWC_C85L.jpeg",
                   [Source("https://web.archive.org/web/20140209004153/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("85_C85CtlgSasshi.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：星野リリィ（サークル：harenti-cinema）"),
            Medium("85_C85KamibukuroDai.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：バーニア600（サークル：さくらぢま）"),
            Medium("85_C85KamibukuroSho.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="イラスト：らいらっく（サークル：P-F easy）"),
            Medium("85_C85KigyoPamphlet.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：植田亮（サークル：Fancy Fantasia）"),
            Medium("85_C85CtlgRom.jpeg",
                   [Source(dist_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：星野リリィ（サークル：harenti-cinema）"),
            Medium("https://web.archive.org/web/20250720012010/https://www.comiket.co.jp/info-a/C85/C85CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20250720012010/https://www.comiket.co.jp/info-a/C85/C85CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2013.12.29 - 2013.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {dist_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C84 ====
        i = 84

        circles_ = []
        media_ = [
            Medium("84_CWC_C84.png",
                   [Source("https://web.archive.org/web/20130807234600/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("84_CWC_C84L.png",
                   [Source("https://web.archive.org/web/20130807234600/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("84_C84CtlgWeb.jpeg",
                   [Source('https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="カントク（サークル：5年目の放課後）"),
            Medium("84_C84CtlgRomWeb.jpeg",
                   [Source('https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="カントク（サークル：5年目の放課後）"),
            Medium("https://web.archive.org/web/20140508104230/http://www.comiket.co.jp/info-a/C84/C84CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20140508104230/http://www.comiket.co.jp/info-a/C84/C84CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2013.08.10 - 2013.08.12",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C83 ====
        i = 83

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("83_C83CtlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="小嶋ララ子（サークル：DISCOTICA）"),
            Medium("83_C83CtlgRomWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="小嶋ララ子（サークル：DISCOTICA）"),
            Medium("https://web.archive.org/web/20130121010627/http://www.comiket.co.jp/info-a/C83/C83CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20130121010627/http://www.comiket.co.jp/info-a/C83/C83CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2012.12.29 - 2012.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C82 ====
        i = 82

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("82_C82CtlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="岸田メル（サークル：迷子通信）"),
            Medium("82_C82CtlgRomWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="岸田メル（サークル：迷子通信）"),
            Medium("https://web.archive.org/web/20120803045334/http://www.comiket.co.jp/info-a/C82/C82CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20120803045334/http://www.comiket.co.jp/info-a/C82/C82CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2012.08.10 - 2012.08.12",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)
       
    if True: # ==== C81 ====
        i = 81

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("81_C81CtlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="れっどべあ（サークル：ＴＥＸ－ＭＥＸ）"),
            Medium("81_C81CtlgRomWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="れっどべあ（サークル：ＴＥＸ－ＭＥＸ）"),
            Medium("https://web.archive.org/web/20120117065744/http://www.comiket.co.jp/info-a/C81/C81CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20120117065744/http://www.comiket.co.jp/info-a/C81/C81CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2011.12.29 - 2011.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)
     
    if True: # ==== C80 ====
        i = 80

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("80_C80CtlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="猿屋ハチ(サークル：ハチ丸)"),
            Medium("80_C80CtlgRomWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="猿屋ハチ(サークル：ハチ丸)"),
            Medium("https://web.archive.org/web/0/https://www.comiket.co.jp/info-a/C80/C80CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/0/https://www.comiket.co.jp/info-a/C80/C80CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2011.08.12 - 2011.08.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C79 ====
        i = 79

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("79_C79CtlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：的井けるな（サークル：素敵！無敵!!ムッキムキ）"),
            Medium("79_C79CtlgRomWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：的井けるな（サークル：素敵！無敵!!ムッキムキ）"),
            Medium("https://web.archive.org/web/20110810042254/http://www.comiket.co.jp/info-a/C79/C79CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20110810042254/http://www.comiket.co.jp/info-a/C79/C79CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2010.12.29 - 2010.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C78 ====
        i = 78

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("78_C78CtlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：田丸浩史（サークル：甲冑娘）"),
            Medium("78_C78CtlgRomWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：田丸浩史（サークル：甲冑娘）"),
            Medium("https://web.archive.org/web/20120121152321/http://www.comiket.co.jp/info-a/C78/C78CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20120121152321/http://www.comiket.co.jp/info-a/C78/C78CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2010.08.13 - 2010.08.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C77 ====
        i = 77

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("77_C77romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：いちば仔牛（サークル：ＵＧＯ）"),
            Medium("77_C77ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：いちば仔牛（サークル：ＵＧＯ）"),
            Medium("https://web.archive.org/web/20140508100143/http://www.comiket.co.jp/info-a/C77/C77CtlgNotes.pdf",
                   [Source("_https://web.archive.org/web/20140508100143/http://www.comiket.co.jp/info-a/C77/C77CtlgNotes.pdf__", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2009.12.29 - 2009.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C76 ====
        i = 76

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("76_C76ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：七瀬あや（サークル：きりみ屋）"),
            Medium("76_C76romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：七瀬あや（サークル：きりみ屋）"),
            Medium("https://web.archive.org/web/20140508101530/http://www.comiket.co.jp/info-a/C76/C76CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20140508101530/http://www.comiket.co.jp/info-a/C76/C76CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2009.08.14 - 2009.08.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C75 ====
        i = 75

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("75_C75ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：蒼樹うめ（サークル：apricot+）"),
            Medium("75_C75romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：蒼樹うめ（サークル：apricot+）"),
            Medium("https://web.archive.org/web/20140508102929/http://www.comiket.co.jp/info-a/C75/C75CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20140508102929/http://www.comiket.co.jp/info-a/C75/C75CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2008.12.28 - 2008.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C74 ====
        i = 74

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("74_C74ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：和々（サークル：C.）"),
            Medium("74_C74romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：和々（サークル：C.）"),
            Medium("https://web.archive.org/web/20110822081645/http://www.comiket.co.jp/info-a/C74/C74CtlgNotes.pdf",
                   [Source("https://web.archive.org/web/20110822081645/http://www.comiket.co.jp/info-a/C74/C74CtlgNotes.pdf", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2008.08.15 - 2008.08.17",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C73 ====
        i = 73

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("73_C73ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ペプシ（サークル：Pepu）"),
            Medium("73_C73romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：ペプシ（サークル：Pepu）"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2007.12.29 - 2007.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C72 ====
        i = 72

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("72_C72ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：市原てつ乃＆雨宮カズユキ"),
            Medium("72_C72romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：市原てつ乃＆雨宮カズユキ"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2007.08.17 - 2007.08.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C71 ====
        i = 71

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("71_C71ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：結城信輝"),
            Medium("71_C71romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：結城信輝"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2006.12.29 - 2006.12.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C70 ====
        i = 70

        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("70_C70ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：七尾奈留"),
            Medium("70_C70romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：七尾奈留"),
             Medium("70_CD-ROM_catalogue_c70.png",
                    [Source('https://archive.org/details/comiket-70-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-70-cd",
                    [Source('https://archive.org/details/comiket-70-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2006.08.11 - 2006.08.13",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C70 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C70" / "process" / "c70_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C69 ====
        i = 69

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("69_C69ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：みつみ美里"),
            Medium("69_C69romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：みつみ美里"),
             Medium("69_CD-ROM_catalogue_c69.png",
                    [Source('https://archive.org/details/comiket-69-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-69-cd",
                    [Source('https://archive.org/details/comiket-69-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2005.12.29 - 2005.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C69 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C69" / "process" / "c69_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C68 ====
        i = 68

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("68_C68ctlgWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：米倉けんご"),
            Medium("68_C68romWeb.jpeg",
                   [Source(chrono_url, (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：米倉けんご"),
             Medium("68_CD-ROM_catalogue_c68.png",
                    [Source('https://archive.org/details/comiket-68-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-68-cd",
                    [Source('https://archive.org/details/comiket-68-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2005.08.12 - 2005.08.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C68 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C68" / "process" / "c68_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C67 ====
        i = 67

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("67_CD-ROM_catalogue_c67.png",
                    [Source('https://archive.org/details/comiket-67-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-67-cd",
                    [Source('https://archive.org/details/comiket-67-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("67_i-img1200x1200-1695177941lxximd251864.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/s1106995112', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：袁藤沖人(1,700円)紙袋：ウエダハジメ ／ 真柴順プレス：みつみ美里"),
             Medium("67_i-img1200x1200-16951779417xwhua251864.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/s1106995112', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2004.12.29 - 2004.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C67 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C67" / "process" / "c67_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C66 ====
        i = 66

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("66_CD-ROM_catalogue_c66.png",
                    [Source('https://archive.org/details/comiket-66-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-66-cd",
                    [Source('https://archive.org/details/comiket-66-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("66_i-img800x600-15572394524vzi7e17419.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/u275679031', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：大嶋優木(1,800円)紙袋：笹井 ／ 稲葉せいこプレス：まんぼう高橋"),
             Medium("66_i-img800x600-1557239468ealrlj33343.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/u275679031', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2004.08.13 - 2004.08.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C66 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C66" / "process" / "c66_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C65 ====
        i = 65

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("65_CD-ROM_catalogue_c65.png",
                    [Source('https://archive.org/details/comiket-65-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-65-cd",
                    [Source('https://archive.org/details/comiket-65-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("65_i-img1200x1200-17376921016919rg198t18673.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/c1170626690', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：ミギー(1,800円)紙袋：音子 ／ ワダナヲプレス：ししまる　けんや"),
             Medium("65_i-img1200x1200-17376921017226rytx5418673.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/c1170626690', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2003.12.28 - 2003.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C65 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C65" / "process" / "c65_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C64 ====
        i = 64

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("64_CD-ROM_catalogue_c64.png",
                    [Source('https://archive.org/details/comiket-64-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-64-cd",
                    [Source('https://archive.org/details/comiket-64-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("64_i-img800x600-1557239661oah47729971.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/g345640356', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：テクノサマタ(1,800円)紙袋：御茶漬海苔プレス：杉本要"),
             Medium("64_i-img800x600-1557239674j6pexz854657.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/g345640356', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2003.08.15 - 2003.08.17",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C64 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C64" / "process" / "c64_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C63 ====
        i = 63

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("63_CD-ROM_catalogue_c63.png",
                    [Source('https://archive.org/details/comiket-63-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-63-cd",
                    [Source('https://archive.org/details/comiket-63-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("63_i-img1200x1200-17404606390522q8dynt15291.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/m1174786961', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：うたたねひろゆき(1,800円)紙袋：篁よしやす ／ 浪花愛プレス：歩詩味土"),
             Medium("63_i-img1200x1200-17404606390831ixtff315291.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/m1174786961', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("63_kamikomike_no13.jpg",
                    [Source('https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2002.12.28 - 2002.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C63 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C63" / "process" / "c63_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C62 ====
        i = 62

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("62_CD-ROM_catalogue_c62.png",
                    [Source('archive.org/details/comiket-62-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("archive.org/details/comiket-62-cd",
                    [Source('archive.org/details/comiket-62-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("62_i-img800x600-1557239798hbo10l17938.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/t647136169', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：ＳＨＯＩＣＨＩ(1,800円)紙袋：ＥＡＲＯ ／ 稲垣有プレス：天草ポチ"),
             Medium("62_i-img800x600-1557239814ug8aga33662.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/t647136169', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2002.08.09 - 2002.08.11",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C62 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C62" / "process" / "c62_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C61 ====
        i = 61

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("61_CD-ROM_catalogue_c61.png",
                    [Source('https://archive.org/details/comiket-61-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-61-cd",
                    [Source('https://archive.org/details/comiket-61-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("61_i-img1200x1200-17404610643232mi50aq462.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/j1174790973', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：悠(1,700円)紙袋：高川ヨ志ノリプレス：中戸川収"),
             Medium("61_i-img1200x1200-174046106435590wrazp462.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/j1174790973', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2001.12.29 - 2001.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C61 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C61" / "process" / "c61_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C60 ====
        i = 60

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("60_CD-ROM_catalogue_c60.png",
                    [Source('https://archive.org/details/comiket-60-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-60-cd",
                    [Source('https://archive.org/details/comiket-60-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("60_i-img800x600-1557239947ywqwfl17865.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/s661029000', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：門井亜矢(1,800円)紙袋：潮干珠生姑プレス：久下じゅんこ"),
             Medium("60_i-img800x600-1557239962sklbtp17865.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/s661029000', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2001.08.10 - 2001.08.12",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C60 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C60" / "process" / "c60_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C59 ====
        i = 59

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("59_CD-ROM_catalogue_c59.png",
                    [Source('https://archive.org/search?query=comiket-59-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/search?query=comiket-59-cd",
                    [Source('https://archive.org/search?query=comiket-59-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("59_m57650797079_1.jpg",
                    [Source('https://jp.mercari.com/item/m57650797079', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：六道神士(1,600円)紙袋：亜樹良のりかずプレス：泉みなと"),
             Medium("59_m57650797079_3.jpg",
                    [Source('https://jp.mercari.com/item/m57650797079', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2000.12.29 - 2000.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C59 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C59" / "process" / "c59_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C58 ====
        i = 58

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("https://archive.org/details/comiket-58-cd",
                    [Source('https://archive.org/details/comiket-58-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-58-cd",
                    [Source('https://archive.org/details/comiket-58-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("58_i-img800x600-15572401205us3qe18297.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/c745955894', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：朱目牌(1,700円)紙袋：古谷トシタカプレス：このまつりえこ"),
             Medium("58_i-img800x600-1557240151skajyy16997.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/c745955894', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("58_kamikomike_no07.jpg",
                    [Source('https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="2000.08.11 - 2000.08.13",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C58 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C58" / "process" / "c58_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C57 ====
        i = 57

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("57_CD-ROM_catalogue_c57.png",
                    [Source('https://archive.org/details/comiket-56-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("https://archive.org/details/comiket-57-cd",
                    [Source('https://archive.org/details/comiket-57-cd', (ReliabilityTypes.Reliable, OriginTypes.Official))]),
             Medium("57_i-img1200x1200-1674310121lsr8tf398162.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/j1079327618', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：ＣＨＯＣＯ(1,600円)紙袋：りんプレス：ひのき一志"),
             Medium("57_i-img1200x1200-1674310121lgbdwn398162.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/j1079327618', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1999.12.24 - 1999.12.26",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C57 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C57" / "process" / "c57_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C56 ====
        i = 56

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("56_CD-ROM_catalogue_c56.png",
                    [Source('https://archive.org/details/comiket-56-cd', (ReliabilityTypes.Reliable, OriginTypes.External))]),
             Medium("https://archive.org/details/comiket-56-cd",
                    [Source('https://archive.org/details/comiket-56-cd', (ReliabilityTypes.Reliable, OriginTypes.External))]),
             Medium("56_i-img1200x1200-17427022311960dqrbqp71826.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/k1178114051', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：平野耕太＆山田秋太郎(1,700円)紙袋：いちば仔牛プレス：睦月藤緒"),
             Medium("56_i-img1200x1200-17427022313076obt5rx71826.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/k1178114051', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1999.08.13 - 1999.08.15",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: C56 Catalog CD (see media)", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "catalogs" / "C56" / "process" / "c56_circles.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        prefix_all_circle_media_of_event(event_raw, f"{i}catarom/")
        events_raw.append(event_raw)
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event_raw, f, indent=4, ensure_ascii=False)

    if True: # ==== C55 ====
        i = 55

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("55_m76573394901_1.jpg",
                    [Source('https://jp.mercari.com/item/m76573394901', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：山本一隆(1,400円)紙袋：ＴＯＲＡプレス：七瀬葵"),
             Medium("55_m76573394901_2.jpg",
                    [Source('https://jp.mercari.com/item/m76573394901', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1998.12.29 - 1998.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C54 ====
        i = 54

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("54_m14368885160_1.jpg",
                    [Source('https://jp.mercari.com/item/m14368885160', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：森永みるく(1,600円)紙袋：青樹緫プレス：依澄杳稀"),
             Medium("54_m14368885160_2.jpg",
                    [Source('https://jp.mercari.com/item/m14368885160', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1998.08.14 - 1998.08.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C53 ====
        i = 53

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("53_i-img898x1198-1633932250ftmy6v653709.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/v1011531278', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：タカハシマコ(1,400円)紙袋：下北沢鈴成プレス：セツコ山田"),
             Medium("53_i-img898x1198-1633932250bez9e6653709.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/v1011531278', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1997.12.28 - 1997.12.29",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C52 ====
        i = 52

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("52_i-img1200x1200-17370974759052rzvhft32.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/w1169732337', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("52_i-img1200x1200-17370974759284wa3xlc32.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/w1169732337', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("52_m27421199273_1.jpg",
                    [Source('https://jp.mercari.com/item/m27421199273', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("52_m27421199273_3.jpg",
                    [Source('https://jp.mercari.com/item/m27421199273', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("52_m27421199273_2.jpg",
                    [Source('https://jp.mercari.com/item/m27421199273', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：おがきちかと小笠原史・猫玄(1,500円･2冊)うちわ：まつながあやこ 紙袋：ＣＨＯＣＯプレス：仙人の卵"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1997.08.15 - 1997.08.17",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            comments="There seem to have been two catalogs, SIDE 1 and SIDE 2. I have no idea what these sides correspond to."
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C51 ====
        i = 51

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("51_i-img800x600-1557241018xxalob31057.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/t646685119', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：黒沼オディール(1,400円)紙袋：乃美やすはるプレス：相田みゆき"),
             Medium("51_i-img800x600-1557241035umdp3h784499.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/t646685119', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1996.12.28 - 1996.12.29",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C50 ====
        i = 50

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("50_i-img800x600-1557241123jundx317651.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/u276446504', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：白泉らら(1,200円)うちわ：塚本ひじく紙袋：セイン流プレス：Ｓ茶屋町"),
             Medium("50_i-img800x600-1557241139ftolj819078.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/u276446504', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="	1996.08.03 - 	1996.08.04",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C49 ====
        i = 49

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("49_i-img1200x1200-17341611307995pxd7rp35203.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1165394582', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("49_i-img1200x1200-17341611308283owhxfu35203.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1165394582', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("49_i-img1200x1200-17341611309066wjbyuq35203.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1165394582', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：水人蔦楽(1,000円)紙袋：加藤茶吉プレス：山崎貴一"),
             Medium("49_kamikomike_no09.jpg",
                    [Source('https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1995.12.29 - 1995.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C48 ====
        i = 48

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("48_i-img1200x1200-1686408376puurvb521306.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/v1095067219', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("48_i-img1200x1200-168640837617neng521306.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/v1095067219', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("48_i-img1200x1200-1686408376tdfubp521306.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/v1095067219', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("48_i-img1200x1200-17487544840449vwgi8x101656.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/1187098375', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("48_i-img1200x1200-17487544840811xeatav101656.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/1187098375', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("48_i-img1200x1200-1686408376tdfubp521306.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/v1095067219', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：高河ゆん(1,300円･2冊)うちわ：むっちりむうにい紙袋：友里のえる プレス：竹田やよい"),
             Medium("i-img1200x900-17425442225590of3bz790587.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1177895362', (ReliabilityTypes.Guess, OriginTypes.External))]
                    , comments="Likely that second catalog's spine between the 48th and 47th.")
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1995.08.18 - 1995.08.20",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            description="20th anniversary comiket, first 3-days event."
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C47 ====
        i = 47

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("47_i-img1200x1200-17367355706823y0dvmb187829.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/j1169155385', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("47_i-img1200x1200-17367355707122giuuwl187829.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/j1169155385', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("47_i-img1200x1200-17367355707427snhmrm187829.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/j1169155385', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：グレビッチ栗原(1,000円)紙袋：タカハシマコプレス：門井亜矢"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1994.12.29 - 1994.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C46 ====
        i = 46

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("46_i-img450x600-1655607254hwbu0c545482.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/k1055058689', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("46_i-img450x600-1655607254orbj09540575.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/k1055058689', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("46_i-img1200x1200-174875080356248wvq9p35.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/g1187119867', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：波羅ぽこん(1,000円)うちわ：介錯紙袋：川猫めぐみ"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1994.08.07 - 1994.08.08",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C45 ====
        i = 45

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("45_zhoro75968.jpg.webp",
                    [Source('https://www.suruga-ya.jp/product/detail/ZHORO75968', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("45_i-img640x480-1665205832d4cucu205017.jpg",
                    [Source('https://cqybif.axlman.ru.com/index.php?main_page=product_info&products_id=24860', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("45_i-img640x480-1665205849nahv2g206257.jpg",
                    [Source('https://cqybif.axlman.ru.com/index.php?main_page=product_info&products_id=24860', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：相原ひでお(1,000円)紙袋：村田蓮爾"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1993.12.29 - 1993.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C44 ====
        i = 44

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("44_i-img1200x1200-17487548135944ortyfn175377.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/1187101506', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("44_i-img1200x1200-174875481362685r8u8h175377.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/1187101506', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("44_i-img1200x1200-1748754813653762aa3e175377.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/1187101506', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments=""),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1993.08.15 - 1993.08.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C43 ====
        i = 43

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("43_i-img600x450-14602829191460282918.89873425hmrp0i3425.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/h224342493', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：西村有未(800円)紙袋：槙夢民"),
             Medium("43_kamikomike_no06.jpg",
                    [Source('https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1992.12.29 - 1992.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C42 ====
        i = 42

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("42_i-img1200x1200-1612424585guunua216345.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/z50719750', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("42_i-img1200x1200-1612424585hjewly216345.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/z50719750', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：たつねこ(800円)紙袋：水沢充"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1992.08.15 - 1992.08.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C41 ====
        i = 41

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("41_i-img946x1200-1679813644angldn175385.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/b1086269540', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("41_i-img1200x728-1679813644lts3al175385.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/b1086269540', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：次元美良(800円)紙袋：まのとのま"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1991.12.29 - 1991.12.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C40 ====
        i = 40

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("40_i-img1200x1200-17350348834178hzwle5311028.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/v1166743151', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("40_i-img1200x1200-173503488344647obznq311028.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/v1166743151', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：まのとのま(800円)うちわ：吾妻ひでお紙袋：まのとのま"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1991.08.16 - 1991.08.17",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C39 ====
        i = 39

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("39_i-img847x1200-1696310837905xo1722644.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/p1108590080', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：おときた・たかお(700円)紙袋：くまだまり"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1990.12.23 - 1990.12.24",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C38 ====
        i = 38

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("38_i-img900x1200-17429206106573zec6sq877.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/f1178416745', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("38_i-img900x1200-17429206106785puorn8877.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/f1178416745', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("38_i-img900x1200-17429206106996s71kmf877.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/f1178416745', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：岩崎つばさ(700円)うちわ：うたたねひろゆき紙袋：くまだまり ／ マーク"),
             Medium("38_kamikomike_no05.jpg",
                    [Source('https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="Probably official goods."),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1990.08.18 - 1990.08.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C37 ====
        i = 37

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("37_i-img916x1200-1679814609gtitwg178226.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/f1086271666', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("37_i-img1200x690-1679814609tavmhp178226.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/f1086271666', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("37_i-img946x1200-1679814609h4sd2f178226.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/f1086271666', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：新田真子(600円)紙袋：へうがけん"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1989.12.23 - 1989.12.24",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C36 ====
        i = 36

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("36_i-img450x600-1655606757s5wsc0578960.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/h1055047527', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("36_i-img450x600-1655606757rhr8st572441.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/h1055047527', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("36_i-img1200x664-1679814176eow4j3172091.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/g1086278116', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：本多且典(600円)うちわ：たつねこ紙袋：へうがけん"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1989.08.13 - 1989.08.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C35 ====
        i = 35

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("35_i-img894x1200-1679815638l3hhm8173587.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/f1086270147', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("35_i-img1200x638-1679815638mx6tpi173587.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/f1086270147', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("35_i-img848x1200-1679815638azwwmr173587.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/f1086270147', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：杏夢(500円)紙袋：乙田基"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1989.03.25 - 1989.03.26",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C34 ====
        i = 34

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("34_i-img900x1200-1679815816nzaq22170742.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/r1086273702', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("34_i-img1200x690-1679815816r3nfdq170742.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/r1086273702', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("34_i-img916x1200-1679815816rkjdna170742.jpg",
                    [Source('https://paypayfleamarket.yahoo.co.jp/item/r1086273702', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：毛羽毛現(500円)うちわ：新田真子紙袋：乙田基"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1988.08.13 - 1988.08.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C33 ====
        i = 33

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("33_i-img1200x1200-17396784328775bcl7px36.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/k1173640865', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("33_i-img1200x1200-17396784329893dbdxvr36.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/k1173640865', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("33_i-img1200x1200-17396784329040lhxt0f36.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/k1173640865', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：迎夏生(400円)紙袋：Dr.モローテレカ：柴田文明／毛羽毛現"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1987.12.26 - 1987.12.27",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C32 ====
        i = 32

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("32_i-img1200x1200-17396792213462g7adbm25.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1173632445', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("32_i-img1200x1200-173967922147205zsgis25.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1173632445', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：宇都宮斉(400円)うちわ：Ａｌｅｘ 紙袋：Dr.モロー テレカ：須賀邦彦／松田紘佳／おおや和美／真鍋譲治"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1987.08.08 - 1987.08.09",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C31 ====
        i = 31

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("31_i-img1200x1200-17396773036017aw3iq16214.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/o1173657210', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("31_i-img1200x1200-17396773037539ym9rkc6214.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/o1173657210', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("31_i-img1200x1200-17396773036384eckwmz6214.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/o1173657210', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：竹田やよい(300円)紙袋：厦門潤テレカ：毛羽毛現／新田真子"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1986.12.27 - 1986.12.28",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C30 ====
        i = 30

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("30_0000876716.jpeg",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=289123', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("30_0000876718.avif",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=289123', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：乙田基(300円)うちわ：川猫めぐみ紙袋：弓月光 ／ 火鳥紅星テレカ：さえぐさじゅん"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1986.08.10",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C29 ====
        i = 29

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("29_i-img1200x1200-17396766323092jgcmb147515.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/c1173633539', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("29_i-img1200x1200-17396766324232s9hjbe47515.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/c1173633539', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：進上真樹(300円)紙袋：迎麻紀"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1985.12.29",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C28 ====
        i = 28

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("28_i-img1200x1200-17396770038539svgbov19425.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1173635881', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("28_i-img1200x1200-17396770040181xagzxc19425.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1173635881', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("28_i-img1200x1200-173967700396058u9kfl19425.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1173635881', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("28_i-img1200x1200-173967700404186yo4sa19425.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/n1173635881', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：あろひろし(300円)うちわ：さえぐさじゅん／とりみき"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1985.08.11",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C27 ====
        i = 27

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("27_0000876707.avif",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=289120', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("27_0000876709.jpeg",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=289120', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：STUDIO　AWAKE(200円)"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1984.12.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C26 ====
        i = 26

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("26_0000876704.avif",
                    [Source('https://k.mandarake.co.jp/auction/item/itemInfoJa.html?index=289119', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("26_0000876706.jpeg",
                    [Source('https://k.mandarake.co.jp/auction/item/itemInfoJa.html?index=289119', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：ＫＥＩＴＨ(200円)うちわ：吾妻ひでお"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1984.08.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C25 ====
        i = 25

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("25_0000876701.avif",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=289118', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("25_0000876703.avif",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=289118', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('A blog post: http://blog.sangatsukan.com/article/73947772.html', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：さえぐさじゅん(200円)"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1983.12.25",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C24 ====
        i = 24

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("24_0000876698.avif",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=289117', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("24_0000876700.avif",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=289117', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="表紙：火野妖子(200円)うちわ：吾妻ひでお"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1983.08.07",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C23 ====
        i = 23

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("23_26152136_218239258717584_1315410657264271360_n.jpg",
                    [Source('https://www.instagram.com/p/BdTErLmDpLO/?img_index=1', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("23_25024393_2087570141498449_5958770805369208832_n.jpg",
                    [Source('https://www.instagram.com/p/BdTErLmDpLO/?img_index=1', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("23_1038501204.jpg",
                    [Source('https://aucfree.com/items/378292495', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="ポスター：ありせみほ表紙：ありせみほ(100円)"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1983.04.03",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C22 ====
        i = 22

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("22_536352903_18519782992019873_1734364163910063066_n.jpg",
                    [Source('https://www.instagram.com/p/DNeSfpQSjV5/', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="ポスター：千之ナイフ表紙：千之ナイフ(100円)"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1982.12.26",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C21 ====
        i = 21

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("21_4b67b93777f65bdac4a9b9ae6dbf329da9efa594.jpg",
                    [Source('https://www.bilibili.com/opus/214906441072705006', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("21_Dvto72lU8AAoTQF.jpg",
                    [Source('https://x.com/comiketofficial/status/1079571967454277632', (ReliabilityTypes.Likely, OriginTypes.Official))]),
             Medium("21_Dvto72DVYAA6PeU.jpg",
                    [Source('https://x.com/comiketofficial/status/1079571967454277632', (ReliabilityTypes.Likely, OriginTypes.Official))]),
             Medium("21_Dvto73UVsAILYCT.jpg",
                    [Source('https://x.com/comiketofficial/status/1079571967454277632', (ReliabilityTypes.Likely, OriginTypes.Official)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                     , comments="ポスター：岩崎摂表紙：岩崎摂(100円)"),
             Medium("21_mmi_catalog_03.jpg",
                    [Source('https://nlab.itmedia.co.jp/cont/articles/3230088/', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1982.08.08",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            comments="Note: According to the x post, C21 was the first comiket with a catalogue: https://x.com/comiketofficial/status/1079571967454277632"
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C20 ====
        i = 20

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("20_i-img640x640-1667725069ce86db225196.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/f1071125160', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("20_i-img640x640-1667724991s95wxb216893.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/f1071125160', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("20_i-img640x640-1667725069o1iwqg225196.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/f1071125160', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("20_i-img640x640-1667725039tto6aj225251.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/f1071125160', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("20_0001778870.avif",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=589914', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("20_0001778872.jpeg",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=589914', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("MISSING ILLUSTRATION !",
                    [Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="ポスター：板橋節子"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1982.03.21",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            comments="Blog post: https://soorce.hatenablog.com/entry/20061112/p1"
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C19 ====
        i = 19

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            Medium("19_GyjobcnaQAEJvdA.jpg",
                [Source('https://x.com/phobby_ss/status/1957069602875433014', (ReliabilityTypes.Guess, OriginTypes.External))]
                , comments="Not sure if this is the official illustration"),                
             Medium("19_0001778868.jpeg",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=589913', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("MISSING ILLUSTRATION ?",
                    [Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="ポスター：吾妻ひでお"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1981.12.20",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C18 ====
        i = 18

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("18_EXOXoptUcAAa6yR.jpg",
                    [Source('https://x.com/comiketofficial/status/1257515000471543810', (ReliabilityTypes.Guess, OriginTypes.Official))]
                    , comments="About C18 according to tweet, probably released at C19 (コミケの歴史19 + date matches)"),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：くまだまり"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1981.08.15 - 1981.08.16",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C17 ====
        i = 17

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：永久保貴一"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1981.04.05",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C16 ====
        i = 16

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("16_0001778865.jpeg",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=589912', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("16_0001778867.jpeg",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=589912', (ReliabilityTypes.Likely, OriginTypes.External))]),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：さえぐさじゅん"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1980.12.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C15 ====
        i = 15

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("1415_s1152572644.1.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.2.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.3.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.4.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.5.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.6.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("15_0001778861.avif",
                    [Source('https://img.mandarake.co.jp/aucimg/8/8/6/4/0001778864.jpeg', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("15_0001778863.avif",
                    [Source('https://img.mandarake.co.jp/aucimg/8/8/6/4/0001778864.jpeg', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("15_0001778864.avif",
                    [Source('https://img.mandarake.co.jp/aucimg/8/8/6/4/0001778864.jpeg', (ReliabilityTypes.Likely, OriginTypes.External))]),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：竹沢コウ"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1980.09.14",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C14 ====
        i = 14

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("1415_s1152572644.1.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.2.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.3.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.4.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.5.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1415_s1152572644.6.jpg",
                    [Source('https://aucview.aucfan.com/yahoo/s1152572644/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("14_EXOXKZFUwAAZ8d0.jpg",
                    [Source('https://x.com/comiketofficial/status/1257515000471543810', (ReliabilityTypes.Likely, OriginTypes.Official))]),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：星野安治"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1980.05.11",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C13 ====
        i = 13

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("13_mmi_catalog_01.jpg",
                    [Source('https://nlab.itmedia.co.jp/cont/articles/3230088/', (ReliabilityTypes.Likely, OriginTypes.External))]),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：竹田やよい"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1979.12.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C12 ====
        i = 12

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("12_i-img900x1200-1721663809cusqig107713.jpg",
                    [Source('https://auctions.yahoo.co.jp/jp/auction/c1145684080', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("12_0001778858.jpeg",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=589910', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("12_0001778860.jpeg",
                    [Source('https://ekizo.mandarake.co.jp/auction/item/itemInfoJa.html?index=589910', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("12_EXOS7RQUMAAZdWY.jpg",
                    [Source('https://x.com/comiketofficial/status/1257510060416045056', (ReliabilityTypes.Likely, OriginTypes.External))]),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：水野流風"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1979.07.28 - 1979.07.29",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C11 ====
        i = 11

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：あららぎるるる"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1979.04.08",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C10 ====
        i = 10

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("10_0001645899.avif",
                    [Source('https://k.mandarake.co.jp/auction/item/itemInfoJa.html?index=556019', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="ポスター：朔原萌"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1978.12.17",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C9 ====
        i = 9

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("9_EXOSt8lUMAE2V74.jpg",
                    [Source('https://x.com/comiketofficial/status/1257510060416045056', (ReliabilityTypes.Likely, OriginTypes.Official))]),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：原田央男"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1978.07.29 - 1978.07.30",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C8 ====
        i = 8

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External))]),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：鈴木哲也"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1978.04.02",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C7 ====
        i = 7

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("7_1565344172978.jpg",
                    [Source('https://www.oricon.co.jp/special/53473/', (ReliabilityTypes.Likely, OriginTypes.External)),
                     Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="ポスター：銀子"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1977.12.18",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C6 ====
        i = 6

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("6_Du26326VsAEYvsk.jpg",
                    [Source('https://x.com/kudan2002/status/1075721868257067008', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("6_Gp7YCcXaMAAEtDV.jpg",
                    [Source('https://x.com/comiketofficial/status/1918208033110540685', (ReliabilityTypes.Doubtful, OriginTypes.Official))]),
             Medium("6_20241107-OYT1I50139-1.webp",
                    [Source('https://www.yomiuri.co.jp/culture/subcul/20241107-OYT1T50161/', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="Old news article about comiket, perhaps the first known."),
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：伝陽一郎"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1977.07.30 - 1977.07.31",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C5 ====
        i = 5

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：さべあのま"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1977.04.10",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C4 ====
        i = 4

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External)),
            #          Source('Authors: https://www.comiket.co.jp/archives/Chronology.html', (ReliabilityTypes.Likely, OriginTypes.External))]
            #         , comments="ポスター：高橋裕子"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1976.12.19",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C3 ====
        i = 3

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
            #  Medium("",
            #         [Source('', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1976.07.25",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C2 ====
        i = 2

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("2_FSMNQ4vVUAACdl4.jpg",
                    [Source('https://x.com/comiketofficial/status/1523175293519015936', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("2_FSMNQ4zVIAApso2.jpg",
                    [Source('https://x.com/comiketofficial/status/1523175293519015936', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("2_FSMNQ47VEAAeXNI.jpg",
                    [Source('https://x.com/comiketofficial/status/1523175293519015936', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("2_FSMNQ4_VIAAWMsl.jpg",
                    [Source('https://x.com/comiketofficial/status/1523175293519015936', (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1976.04.04",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ]
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)

    if True: # ==== C1 ====
        i = 1

        circles_ = []
        chrono_url = "https://web.archive.org/web/20250710153917/https://www.comiket.co.jp/archives/Chronology.html"
        media_ = [
             Medium("1_03.jpg",
                    [Source('https://gigazine.net/news/20120314-comiket/', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1_FR8rZD-UYAAajym.jpg",
                    [Source('https://x.com/comiket_air/status/1521988045481906178', (ReliabilityTypes.Likely, OriginTypes.External))]),
             Medium("1_FR8rZEFVkAAm3e7.jpg",
                    [Source('https://x.com/comiket_air/status/1521988045481906178', (ReliabilityTypes.Likely, OriginTypes.Official))]),
             Medium("1_CAUju1EUMAEF9gk.jpg",
                    [Source('https://posfie.com/@tokyoedit/p/BktoaLJ', (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="Unknown authors !"),
            ]
        event = Event(
            aliases=[f"C{i}", f"コミックマーケット{i}", f"Comiket {i}", f"Comic Market {i}", ],
            dates="1975.12.21",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {chrono_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            comments="Some works apparently released at C1: https://pst-pallet.com/2018/12/07/comike/"
        )
        events_raw.append(event.get_json())
        if SAVE_INTER_JSON:
            with (save_folder_path / f"C{i:03d}.json").open("w+", encoding='utf-8') as f:
                json.dump(event.get_json(), f, indent=4, ensure_ascii=False)



# TODO next
# Add the dvd catalogues
# https://web.archive.org/web/20211201091656/http://comiket.co.jp/info-a/MR/mr.html
# https://www.comiket.co.jp/info-c/C86/C86comiketmanual.pdf
#https://web.archive.org/web/20200202201044/https://www.comiket.co.jp/info-c/ComiketPress/N01/index.html
# https://web.archive.org/web/20211112160750/https://www.comiket.co.jp/info-c/ComiketPress/N03/index.html
# press 50 https://www.comiket.co.jp/info-a/C96/C96distributions.html
# https://www.comiket.co.jp/archives/Chronology.html
# https://www.comiket.co.jp/info-a/C98/AirComiket98.html
# https://web.archive.org/web/20191227223043/https://www.comiket.co.jp/info-c/C97/ShinkanCard/#1
# コミケットスペシャル６ OTAKU SUMMIT 2015 in https://www.comiket.co.jp/archives/Chronology.html

        # ==== event group ====
        media = [
            Medium("20250726082151_50thLogoTitle.png",
                   [Source("https://web.archive.org/web/20250726082151/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20231209043210_C83WebCatalog_bn.png",
                   [Source("https://web.archive.org/web/20231209043210/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20231209043210_cmk_banner.gif",
                   [Source("20231209043210_cmk_banner.gif", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20240731183307_comike45_banner03.jpeg",
                   [Source("https://web.archive.org/web/20240731183307/https://www.comiket.co.jp/", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("20250405162821_comiket45th.jpeg",
                   [Source("https://web.archive.org/web/20250405162821/https://www.comiket.co.jp/info-a/AC2/Cmk45thBook.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("92_Hataraku2.jpeg",
                   [Source('https://web.archive.org/web/20250114195114/https://www.comiket.co.jp/info-a/C92/C92distributions.html', (ReliabilityTypes.Reliable, OriginTypes.Official))]
                   , comments="表紙：羽柴麟（サークル：あおしま～ズ）"),
            Medium("i-img1200x900-17425442225590of3bz790587.jpg",
                   [Source("https://auctions.yahoo.co.jp/jp/auction/n1177895362", (ReliabilityTypes.Likely, OriginTypes.External))]
                   , comments="Catalogs together form a larger pictures"),
            Medium("g1180330133.jpg",
                   [Source("https://auctions.yahoo.co.jp/jp/auction/g1180330133", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("n1188396438.jpg",
                   [Source("https://auctions.yahoo.co.jp/jp/auction/n1188396438", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("h1108191249.jpg",
                   [Source("https://auctions.yahoo.co.jp/jp/auction/h1108191249", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("20230216141756175521_bbc7f14cd1f7bdf9fd82de1685d722e4.jpg",
                   [Source("https://www.kosho.or.jp/products/detail.php?product_id=458192002", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("e776f88893ed086dbc2d8a926f0390076624199e.jpg@1192w.avif",
                   [Source("https://www.bilibili.com/opus/214906441072705006", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("c14-17_05.jpg",
                   [Source("https://gigazine.net/news/20120314-comiket/", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("c19-30_06.jpg",
                   [Source("https://gigazine.net/news/20120314-comiket/", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("c31-33_07.jpg",
                   [Source("https://gigazine.net/news/20120314-comiket/", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("c31-39_08.jpg",
                   [Source("https://gigazine.net/news/20120314-comiket/", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("c40-49_09_m.jpg",
                   [Source("https://gigazine.net/news/20120314-comiket/", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("c50+_10.jpg",
                   [Source("https://gigazine.net/news/20120314-comiket/", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("GyhI-gHaEAEBOrd.jpg",
                   [Source("https://x.com/sekai_official_/status/1956894292305395940", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("FxcIzqXaUAEVcHh.jpg",
                   [Source("https://x.com/koujint/status/1664473009477001216", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("FxcIzqWaUAISlzC.jpg",
                   [Source("https://x.com/koujint/status/1664473009477001216", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("FxcIzqbagAEuJue.jpg",
                   [Source("https://x.com/koujint/status/1664473009477001216", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("kamikomike_no14.jpg",
                   [Source("https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("kamikomike_no18.jpg",
                   [Source("https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("kamikomike_no19.jpg",
                   [Source("https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("kamikomike_no30.jpg",
                   [Source("https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("kamikomike_no31.jpg",
                   [Source("https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("kamikomike_no02.jpg",
                   [Source("https://www.meiji.ac.jp/manga/yonezawa_lib/archives/exh-kamicomiket/exh-kamicomiket_archive03.html", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("EfBtYEXU4AAqnkZ.jpg",
                   [Source("https://x.com/yone_lib/status/1292653419639889920", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("EfBtZeCVAAIC8F8.jpg",
                   [Source("https://x.com/yone_lib/status/1292653419639889920", (ReliabilityTypes.Likely, OriginTypes.External))]),
            Medium("EXKY5TiU0AAKWYy.jpg",
                   [Source("https://x.com/comiketofficial/status/1257235808156651520", (ReliabilityTypes.Likely, OriginTypes.Official))]
                   , comments="I could not identify the related event (C2 c3 or C4)"),
            Medium("コミックマーケットの会場の変遷 [616JLtfDoT8].mkv",
                   [Source("https://www.youtube.com/watch?v=616JLtfDoT8", (ReliabilityTypes.Likely, OriginTypes.External)),
                    Source("https://hatenanews.com/articles/201409/22341", (ReliabilityTypes.Likely, OriginTypes.External))]
                    , comments="Features high resolution C1 circle map !"),
        ]
        links = ["https://comiket.co.jp/", "https://web.archive.org/web/19990117015250/http://www.inter-g7.or.jp/g2/manga/HTML/MARKET.html", "https://x.com/comiketofficial"]

        event_group = EventGroup(
            aliases=["Comic Market", "Comiket", "コミックマーケット", "コミケ", "C"],
            events=[],
            media=media,
            links=links,
            comments="C21 was had first comiket catalog (https://x.com/comiketofficial/status/1079571967454277632)"
        )
        
        if SAVE_INTER_JSON: # deprecated way of doing things
            event_group_raw = event_group.get_json()
            events_raw = []
            for file in sorted(save_folder_path.glob("C*.json"), key=lambda x: x.stem):
                with file.open("r", encoding='utf-8') as f:
                    event_json = json.load(f)
                events_raw.append(event_json)
            event_group_raw["events"] = events_raw

            event_group_new = EventGroup.load_from_json_old(event_group_raw)
        else:
            event_group_raw = event_group.get_json()
            event_group_raw["events"] = events_raw[::-1]
            event_group_new = EventGroup.load_from_json_old(event_group_raw)
        event_group_new.save(save_folder_path)
            

