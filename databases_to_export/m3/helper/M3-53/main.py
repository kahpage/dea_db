from db_structs import Circle, Medium, Source, ReliabilityTypes, OriginTypes
from pathlib import Path
import json
from bs4 import BeautifulSoup
import re
import requests
import lxml
from typing import Any, TypedDict, NotRequired

PATH_M3_HELPER_CURRENT = Path(__file__).parent
PATH_M3_HELPER = PATH_M3_HELPER_CURRENT.parent
PATH_M3 = PATH_M3_HELPER.parent
PATH_M3_MEDIA = PATH_M3 / "media"

class CircleJsonItemURL(TypedDict):
    text: str
    url: str


class CircleJsonItemKeyword(TypedDict):
    text: str
    phonetic: str


class CircleJsonItemEmbed(TypedDict):
    type: str  # website
    id: str  # sub url

class CircleJsonItemPosition(TypedDict):
    area: str
    no: str

class CircleJsonItem(TypedDict):
    id: int  # circle id
    name: str  # circle name
    phonetic: str  # circle name phonetic
    genre: str  # genre
    spaceSize: int  # number of booth spaces
    adult: bool  # whether the circle has adult content
    prText: str  # circle comments
    links: dict[str, CircleJsonItemURL]  # Links
    keywords: list[CircleJsonItemKeyword]  # Keywords
    realSp: NotRequired[CircleJsonItemPosition]  # Position (real)
    webSp: NotRequired[CircleJsonItemPosition]  # Position (web)


def get_circles_json_or_local_copy(url: str, i: int) -> list[CircleJsonItem]:
    """Retrieve circles.json content. If a local copy exists, use it instead of fetching."""
    local_copy_path = PATH_M3_HELPER_CURRENT / f"raw{i:02d}_circles.json"

    circles_json: dict[str, list[CircleJsonItem]]
    if local_copy_path.exists():
        print(
            f"Using local copy for circles.json of M3-{i:02d} at {local_copy_path} ..."
        )
        with local_copy_path.open("r", encoding="utf-8") as f:
            circles_json = json.load(f)
    else:
        print(f"Fetching circles.json for M3-{i:02d} at {url} ...")
        response = requests.get(url)
        with local_copy_path.open("w", encoding="utf-8") as f:
            f.write(response.text)
        circles_json = response.json()

    return circles_json["items"]

def get_cut_url(item_id: int, cut_index: int) -> str:
    return f"https://catalog.m3net.jp/2024s/circlecuts/{item_id}-{cut_index}.png"


if __name__ == "__main__":
    i = 53
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    circle_json_url = "https://catalog.m3net.jp/2024s/resources/circles.json"

    # circles.json
    circles_json_items = get_circles_json_or_local_copy(circle_json_url, i)
    print(
        f"Retrieved {len(circles_json_items)} circles from circles.json for M3-{i:02d}. Sample entry:"
    )

    PATH_M3_MEDIA_CURRENT = PATH_M3_MEDIA / f"{i:02d}"
    skip_media_dl = False
    media_files = set()
    # If media exists:
    if PATH_M3_MEDIA_CURRENT.exists():
        skip_media_dl = True
        print(f"Media folder for {name} already exists at {PATH_M3_MEDIA_CURRENT}, skipping media download ...")
        media_files = set(f.name for f in PATH_M3_MEDIA_CURRENT.glob("*"))
    PATH_M3_MEDIA_CURRENT.mkdir(exist_ok=True)

    # # Print all unique keys with examples
    # item_keys = {}
    # for item in circles_json_items:
    #     for key in item.keys():
    #         if key not in item_keys and item[key] not in (None, "", [], {}):
    #             item_keys[key] = item[key]
    # print(f"Unique keys in circles.json for M3-{i:02d}: {sorted(item_keys.keys())}")
    # print(f"Example values for each key:")
    # for key, value in item_keys.items():
    #     print(f"  {key}: {value}")
    # exit()
    # Process circles
    print(f"Processing circles for {name} ...")
    circles: list[Circle] = []

    for item in circles_json_items:
        # id: int  # circle id

        # aliases: list[str]
        # pen_names: Optional[list[str]]
        # position: Optional[str]
        # sources: Optional[list[Source]]
        # media: Optional[list[Medium]]
        # links: Optional[list[str]]
        # comments: Optional[str]

        aliases = [item["name"]]
        pen_names = None

        comments_parts: list[str] = []
        if item["phonetic"]:
            comments_parts.append(f"Name katakana: {item['phonetic']}")
        if item["genre"]:
            comments_parts.append(f"Genre: {item['genre']}")
        if item["prText"]:
            comments_parts.append(f"{item['prText']}")
        if item["spaceSize"] and item["spaceSize"] != 1:
            if item["spaceSize"] == 0:  # TODO: remove
                raise ValueError(f"Invalid spaceSize 0 for circle id {item['id']}")
            comments_parts.append(f"Booth space size: {item['spaceSize']}")
        if item["keywords"]:
            keywords_parts: list[str] = []
            for kw in item["keywords"]:
                if kw["text"]:
                    keywords_parts.append(f"{kw['text']} ({kw['phonetic']})")
            comments_parts.append(f"Keywords: {', '.join(keywords_parts)}")
        comments = "\n".join(comments_parts) if comments_parts else None

        positions = []
        if "realSp" in item and item["realSp"]:
            area, no = item["realSp"]["area"], item["realSp"]["no"]
            positions.append(f"{area}-{no}")
        if "webSp" in item and item["webSp"]:
            area, no = item["webSp"]["area"], item["webSp"]["no"]
            positions.append(f"{area}-{no} (Web)")
        position = ", ".join(positions)
        if position.strip() == "":
            raise ValueError(f"Empty position for circle id {item['id']}")

        links: list[str] = []  # Links
        for link_key, link in item["links"].items():
            if link["url"]:
                links.append(
                    f"{link['url']}" + (f" ({link['text']})" if link["text"] else "")
                )

        media: list[Medium] = []
        # Try downloading circle cuts
        # Download cuts, if not already downloaded
        if not skip_media_dl:
            cut_index = 1
            while True:
                cut_url = get_cut_url(item['id'], cut_index)
                response = requests.get(cut_url)
                if not response.ok:
                    break
                if len(response.content) < 500:  # Heuristic for "no image" response
                    break
                
                print(f"Downloaded {item['id']}_{cut_index}.png from {cut_url}")
                cut_path = PATH_M3_MEDIA_CURRENT / f"{item['id']}_{cut_index}.png"
                with cut_path.open("wb") as f:
                    f.write(response.content)    
                cut_index += 1

        # Detect downloaded cuts and add to media
        cut_index = 1
        while True:
            if f"{item['id']}_{cut_index}.png" not in media_files:
                break
            cut_url = get_cut_url(item['id'], cut_index)
            media.append(
                Medium(
                    path=f"{i:02d}/{item['id']}_{cut_index}.png",
                    sources=[
                        Source(
                            cut_url, (ReliabilityTypes.Reliable, OriginTypes.Official)
                        )
                    ],
                )
            )
            cut_index += 1

        circles.append(
            Circle(
                aliases=aliases,
                pen_names=pen_names,
                position=position,
                sources=None,  # No separate sources beyond media
                media=media if media else None,
                links=links if links else None,
                comments=comments,
            )
        )
    
    # Print a safe ASCII-escaped summary to avoid UnicodeEncodeError
    summary = f"Retrieved {len(circles)} circles for {name}."
    print(summary.encode('ascii', errors='backslashreplace').decode('ascii'))

    # Export circles
    circles_output_path = PATH_M3_HELPER_CURRENT / f"circles_{i:02d}.json"
    out = [c.get_json() for c in circles]
    with circles_output_path.open("w+", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)