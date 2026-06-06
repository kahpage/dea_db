
from db_structs import Medium, Circle, Event, EventGroup, Source, ReliabilityTypes, OriginTypes, Location, is_to_add
from pathlib import Path
import json
from typing import Any
from bs4 import BeautifulSoup, Comment
import re
import requests
import lxml

PATH_M3_HELPER_CURRENT = Path(__file__).parent
PATH_M3_HELPER = PATH_M3_HELPER_CURRENT.parent
PATH_M3 = PATH_M3_HELPER.parent
PATH_M3_MEDIA = PATH_M3 / "media"

def soup_via_fetch_or_local_copy(url: str, i: int) -> BeautifulSoup:
    """Retrieve respective soup. If a local html copy exists, use it instead of fetching."""
    local_copy_path = PATH_M3_HELPER_CURRENT / f"raw{i:02d}.htm"
    if local_copy_path.exists():
        print(f"Using local copy for M3-{i:02d} at {local_copy_path} ...")
        with local_copy_path.open("rb") as f:
            soup = BeautifulSoup(f.read(), features="lxml")
    else:
        print(f"Fetching M3-{i:02d} at {url} ...")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "lxml")
        with local_copy_path.open("wb+") as f:
            f.write(response.content)
    return soup

if __name__ == '__main__':
    i = 2
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    PATH_M3_MEDIA_CURRENT = PATH_M3_MEDIA / f"{i:02d}"
    skip_media_dl = False
    # If media exists:
    if PATH_M3_MEDIA_CURRENT.exists():
        skip_media_dl = True
        print(f"Media folder for {name} already exists at {PATH_M3_MEDIA_CURRENT}, skipping media download ...")
    PATH_M3_MEDIA_CURRENT.mkdir(exist_ok=True)
    m3_page = "https://www.m3net.jp/event/1998f.php"

    # Retrieve circles
    circles_: list[Circle] = []
    # Fetch the m3_page
    soup = soup_via_fetch_or_local_copy(m3_page, i)

    switch_details = soup.select("div.switchDetail")
    switch_names = soup.select("p.switchTitle")
    # Find the indices of sections that are "サークルカット集" so we can
    # access the corresponding title/genre for each image block.
    details_indices = [idx for idx in range(len(switch_details)) if "サークルカット集" in switch_names[idx].get_text(strip=True)]
    def _extract_genre(full_title: str) -> str:
        # Expect titles like: "[ 音響 - オリジナル (1/4) ]　サークルカット集"
        # Extract content inside brackets and drop any parenthetical counts.
        m = re.search(r"\[([^\]]+)\]", full_title)
        if m:
            g = m.group(1)
        else:
            g = full_title.replace("サークルカット集", "")
        # Remove trailing parenthesis groups like (1/4)
        g = re.sub(r"\s*\([^\)]*\)", "", g).strip()
        return g

    def _extract_position_from_img_name(img_name: str):
        # Given names like 'a01ab.jpg' or 'cut_a01ab.jpg' or '02_cut_a01ab.jpg',
        # extract the position token and normalize the leading letter to uppercase.
        stem = Path(img_name).stem
        # strip common prefixes (digits and 'cut_')
        stem = re.sub(r'^(?:\d+_)?(?:cut_)?', '', stem)
        m = re.search(r'([A-Za-z])(\d{2,}\w*)', stem)
        if not m:
            return None
        return f"{m.group(1).upper()}{m.group(2)}"

    for idx in details_indices:
        d = switch_details[idx]
        # full title contains genre + 'サークルカット集', e.g.
        # "[ 音響 - オリジナル (1/4) ]　サークルカット集"
        full_title = switch_names[idx].get_text(strip=True)
        # normalize the genre label (e.g. "音響 - オリジナル")
        genre = _extract_genre(full_title)
        rows = d.select("table tr")
        rows_image_blocks = [d for d in rows if d.select_one("table img")]
        rows_name_blocks = [d for d in rows if not d.select_one("table img")]
        # print(len(rows_image_blocks), len(rows_name_blocks))

        for k in range(len(rows_image_blocks)):
            cut_blocks = rows_image_blocks[k].select("td")
            name_blocks = rows_name_blocks[k].select("td")
            for j in range(len(cut_blocks)):
                cut_block = cut_blocks[j]
                name_block = name_blocks[j]
                media_: list[Medium] = []

                position_val = None
                for img_tag in cut_block.select("img"):
                    img_name = re.search(r"/([^/]+)$", img_tag["src"]).group(1)
                    img_file_name = f'cut_{img_name}'

                    if position_val is None:
                        position_val = _extract_position_from_img_name(img_name)

                    if not skip_media_dl:
                        # download image
                        img_url = f"https://www.m3net.jp/img/event/m3_{i:02d}/{img_name}"
                        print(f"Fetching image at {img_url}")
                        img_resp = requests.get(img_url)
                        if img_resp.status_code != 200:
                            raise ValueError(f"Failed to fetch image {img_name}, status code: {img_resp.status_code}")
                        img_path = PATH_M3_MEDIA_CURRENT / img_file_name
                        with img_path.open("wb+") as img_file:
                            img_file.write(img_resp.content)

                    media_.append(Medium(
                        f"{i:02d}/{img_file_name}",
                        [Source("https://www.m3net.jp/event/1998s.php", (ReliabilityTypes.Reliable, OriginTypes.Official))]
                    ))

                links_ = [name_block.select_one("a")["href"] if name_block.select_one("a") else None]
                if len(links_) == 1 and links_[0] is None:
                    links_ = []

                circles_.append(Circle(
                    aliases=[f"{name_block.get_text(strip=True)}"],
                    media=media_,
                    links=links_ if is_to_add(links_) else None,
                    comments=f"Genre: {genre}\n{cut_block.get_text(strip=True)}",
                    position=position_val
                ))
    print(f"Retrieved {len(circles_)} circles for {name}.")

    # Export circles
    circles_output_path = PATH_M3_HELPER_CURRENT / f"circles_{i:02d}.json"
    out = [c.get_json() for c in circles_]
    with circles_output_path.open("w+", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)