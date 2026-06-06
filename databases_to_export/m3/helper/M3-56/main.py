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


class CircleJsonItem(TypedDict):
    id: int  # circle id
    name: str  # circle name
    phonetic: str  # circle name phonetic
    genre: str  # genre
    spaceSize: int  # number of booth spaces
    adult: bool  # whether the circle has adult content
    prText: str  # circle comments
    embeds: list[CircleJsonItemEmbed]  # Embedded content
    links: dict[str, CircleJsonItemURL]  # Links
    keywords: list[CircleJsonItemKeyword]  # Keywords
    area: str  # position area
    number: str  # position number
    prCut: NotRequired[str] # URL for prCut image, if exists


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


def embed_to_url(embed: CircleJsonItemEmbed) -> str:
    embed_type = embed["type"]
    embed_id = embed["id"]
    if embed_type == "youtube":
        return f"https://www.youtube.com/watch?v={embed_id}"
    elif embed_type == "soundcloud":
        return f"https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/{embed_id}&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
    elif embed_type == "nicovideo":
        return f"https://www.nicovideo.jp/watch/{embed_id}"
    raise ValueError(f"Unknown embed type: {embed_type}")

def get_cut_url(item_id: int, cut_index: int) -> str:
    return f"https://catalog.m3net.jp/archive/2025f/circlecuts/large/{item_id}-{cut_index}.webp"

if __name__ == "__main__":
    i = 56
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    circle_json_url = "https://catalog.m3net.jp/archive/2025f/resources/circles.json"

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
    else:
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

        position = f"{item['area']} {item['number']}"
        if position.strip() == "":
            raise ValueError(f"Empty position for circle id {item['id']}")

        links: list[str] = []  # Links
        for link_key, link in item["links"].items():
            if link["url"]:
                links.append(
                    f"{link['url']}" + (f" ({link['text']})" if link["text"] else "")
                )

        media: list[Medium] = []
        for embed in item["embeds"]:
            if not embed["type"]:
                if embed["id"]:
                    print(
                        f"Warning: Embed with missing type but has id '{embed['id']}' for circle id {item['id']}. Skipping."
                    )
                continue

            embed_url = embed_to_url(embed)
            media.append(
                Medium(
                    path=embed_url,
                    sources=[
                        Source(
                            embed_url, (ReliabilityTypes.Reliable, OriginTypes.Official)
                        )
                    ],
                )
            )
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
                
                print(f"Downloaded {item['id']}_{cut_index}.webp from {cut_url}")  
                cut_path = PATH_M3_MEDIA_CURRENT / f"{item['id']}_{cut_index}.webp"
                with cut_path.open("wb") as f:
                    f.write(response.content)  
                cut_index += 1

        # Detect downloaded cuts and add to media
        cut_index = 1
        while True:
            if f"{item['id']}_{cut_index}.webp" not in media_files:
                break
            cut_url = get_cut_url(item['id'], cut_index)
            media.append(
                Medium(
                    path=f"{i:02d}/{item['id']}_{cut_index}.webp",
                    sources=[
                        Source(
                            cut_url, (ReliabilityTypes.Reliable, OriginTypes.Official)
                        )
                    ],
                )
            )
            cut_index += 1
        
        # If prCut, try downloading prCut
        if "prCut" in item and item["prCut"]:
            prcut_url = item["prCut"]
            prcut_extension = prcut_url.split(".")[-1]
            prcut_filename = f"{item['id']}_prCut.{prcut_extension}"
            # if already downloaded, skip
            if prcut_filename not in media_files:
                response = requests.get(prcut_url)
                if response.ok and len(response.content) >= 500:  # Heuristic for valid image
                    print(f"Downloaded {prcut_filename} from {prcut_url}")
                    cut_path = PATH_M3_MEDIA_CURRENT / prcut_filename
                    with cut_path.open("wb") as f:
                        f.write(response.content)
                    media_files.add(prcut_filename)  # Add to media_files to avoid re-downloading if appears again
            
            # If prCut is available (either just downloaded or already existed), add to media
            if prcut_filename in media_files:
                media.append(
                    Medium(
                        path=f"{i:02d}/{prcut_filename}",
                        sources=[
                            Source(
                                prcut_url, (ReliabilityTypes.Reliable, OriginTypes.Official)
                            )
                        ],
                    )
                )
            
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