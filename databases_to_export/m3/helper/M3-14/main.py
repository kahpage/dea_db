
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
    i = 14
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    PATH_M3_MEDIA_CURRENT = PATH_M3_MEDIA / f"{i:02d}"
    skip_media_dl = False
    # If media exists:
    if PATH_M3_MEDIA_CURRENT.exists():
        skip_media_dl = True
        print(f"Media folder for {name} already exists at {PATH_M3_MEDIA_CURRENT}, skipping media download ...")
    PATH_M3_MEDIA_CURRENT.mkdir(exist_ok=True)
    m3_page = "https://www.m3net.jp/event/2004f.php"

    # Retrieve circles
    circles_: list[Circle] = []
    # Fetch the m3_page
    soup = soup_via_fetch_or_local_copy(m3_page, i)

    switch_details = soup.select("div.switchDetail")
    switch_names = soup.select("p.switchTitle")
    # Split sections into indices containing cuts and those that contain the
    # descriptions (used to map circle names -> positions).
    # Keep indices so we can also access the matching switchTitle text.
    cut_indices = [i for i in range(len(switch_details)) if "サークルカット集" in switch_names[i].get_text(strip=True)]
    desc_indices = [i for i in range(len(switch_details)) if "サークルカット集" not in switch_names[i].get_text(strip=True)]
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

    def _normalize_cell_text(tag) -> str:
        # Preserve a space where HTML uses <br> so names keep the same shape
        # between the description table and the cut list.
        return tag.get_text(" ", strip=True)

    circles_: list[Circle] = []
    for di in range(len(cut_indices)):
        orig_cut_i = cut_indices[di]
        d = switch_details[orig_cut_i]
        # Extract genre from the matching switchTitle for this cut section.
        raw_title = switch_names[orig_cut_i].get_text(strip=True)
        genre = _extract_genre(raw_title)
        rows = d.select("table tr")

        def _is_name_row(row) -> bool:
            if row.select_one("img"):
                return False
            if row.select_one("a"):
                return True
            return bool(row.select_one("td.cut01") or row.select_one("td.cut04"))

        rows_image_blocks = [row for row in rows if row.select_one("img")]
        rows_name_blocks = [row for row in rows if _is_name_row(row)]

        # Build a position lookup from the matching description table.
        # This is the same pattern used by M3-03.
        position_table = switch_details[desc_indices[di]].select_one("table")
        position_dict = {}
        for row in position_table.select("tr"):
            cols = row.select("td")
            if len(cols) < 2:
                continue
            position = _normalize_cell_text(cols[0])
            circle_name = _normalize_cell_text(cols[1])
            position_dict[circle_name] = position

        for i_block in range(min(len(rows_image_blocks), len(rows_name_blocks))):
            cut_blocks = rows_image_blocks[i_block].select("td")
            name_blocks = rows_name_blocks[i_block].select("td")

            for j in range(max(len(cut_blocks), len(name_blocks))):
                cut_block = cut_blocks[j] if j < len(cut_blocks) else cut_blocks[-1]
                name_block = name_blocks[j] if j < len(name_blocks) else name_blocks[-1]

                # Collect all images in this cut cell (handles colspan=2 with two images)
                imgs = cut_block.select("img")
                img_names = [re.search(r"/([^/]+)$", img["src"]).group(1) for img in imgs]

                # Collect names: prefer individual <a> anchors if present, otherwise
                # split the cell text on common delimiters like '/', '／', or newline.
                anchor_tags = name_block.select("a")
                if anchor_tags and len(anchor_tags) > 1:
                    names = [a.get_text(strip=True) for a in anchor_tags]
                    links = [a["href"] for a in anchor_tags]
                elif anchor_tags and len(anchor_tags) == 1:
                    anchor_tag = anchor_tags[0]
                    names = [anchor_tag.get_text(strip=True)]
                    links = [anchor_tag["href"]]
                else:
                    cell_text = _normalize_cell_text(name_block)
                    # Split only on separators that actually join plain-text circle names.
                    parts = re.split(r"\s*[／/]\s*|\n", cell_text)
                    names = [p for p in parts if p]
                    # Try to get a single link if present; otherwise None per name.
                    link_tag = name_block.select_one("a")
                    links = [link_tag["href"] if link_tag is not None else None for _ in names]

                if not names:
                    # Some cut slots are intentionally blank in the HTML.
                    # Skip them instead of trying to fabricate a circle name.
                    continue

                # Pair names and images by index. If counts mismatch, reuse last available.
                pair_count = max(len(names), len(img_names))
                for k in range(pair_count):
                    name_text = names[k] if k < len(names) else names[-1]
                    link = links[k] if k < len(links) else links[-1] if links else None
                    img_name = img_names[k] if k < len(img_names) else img_names[-1] if img_names else None

                    img_file_name = f'{i:02d}_cut_{img_name}' if img_name else None

                    position = position_dict.get(name_text, "")
                    if not position and img_name:
                        img_stem = Path(img_name).stem
                        if img_stem.lower() != "na":
                            position = img_stem
                    if name_text in {"■準備会予備スペース■", "予備ブース"}:
                        continue
                    if not position:
                        safe_name = name_text.encode('ascii', errors='backslashreplace').decode('ascii')
                        try:
                            print("WARNING: No position found for circle:", name_text)
                        except Exception:
                            print("WARNING: No position found for circle:", safe_name)
                        # if name_text == "M3準備会":
                        #     position = "09a"
                        #     print(f"For {name_text}, assigning position {position} manually")


                    # download image if available
                    if img_name and not skip_media_dl:
                        img_url = f"https://www.m3net.jp/img/event/m3_{i:02d}/{img_name}"
                        print(f"Fetching image at {img_url}")
                        img_resp = requests.get(img_url)
                        if img_resp.status_code != 200:
                            raise ValueError(f"Failed to fetch image {img_name}, status code: {img_resp.status_code}")
                        img_path = PATH_M3_MEDIA_CURRENT / img_file_name
                        with img_path.open("wb+") as img_file:
                            img_file.write(img_resp.content)

                    media_list = [Medium(f"{i:02d}/{img_file_name}", [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))])] if img_file_name else []

                    circles_.append(Circle(
                        aliases=[f"{name_text}"],
                        media=media_list,
                        links=[link] if link else None,
                        comments=f"Genre: {genre}\n{cut_block.get_text(strip=True)}",
                        position=position
                    ))
    # Print a safe ASCII-escaped summary to avoid UnicodeEncodeError
    summary = f"Retrieved {len(circles_)} circles for {name}."
    print(summary.encode('ascii', errors='backslashreplace').decode('ascii'))

    # Export circles
    circles_output_path = PATH_M3_HELPER_CURRENT / f"circles_{i:02d}.json"
    out = [c.get_json() for c in circles_]
    with circles_output_path.open("w+", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)