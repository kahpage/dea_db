
from db_structs import Medium, Circle, Source, ReliabilityTypes, OriginTypes
from pathlib import Path
import json
from bs4 import BeautifulSoup
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
    i = 11
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    PATH_M3_MEDIA_CURRENT = PATH_M3_MEDIA / f"{i:02d}"
    skip_media_dl = False
    if PATH_M3_MEDIA_CURRENT.exists():
        skip_media_dl = True
        print(f"Media folder for {name} already exists at {PATH_M3_MEDIA_CURRENT}, skipping media download ...")
    PATH_M3_MEDIA_CURRENT.mkdir(exist_ok=True)
    m3_page = "https://www.m3net.jp/event/2003s.php"

    # Retrieve circles
    circles_: list[Circle] = []
    # Fetch the m3_page
    soup = soup_via_fetch_or_local_copy(m3_page, i)

    switch_details = soup.select("div.switchDetail")
    switch_names = soup.select("p.switchTitle")
    # The first five sections are the circle tables. The remaining sections are
    # cut-image pages, which map to circles by position ranges.

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
        # Preserve a space where HTML uses <br> so names like
        # "マリオ音楽グループ<br>岡崎支部" match the cut-side text.
        return tag.get_text(" ", strip=True)

    def _extract_media_name(position: str) -> str | None:
        # M3-11 cut images represent chunks of roughly 20 circle slots.
        # The original importer used the same position ranges below.
        normalized = position.strip()
        if not normalized:
            return None
        if normalized[-1] not in ["a", "b"]:
            normalized = f"{normalized}0"

        pos_value = int(normalized, 16)
        cut_ranges = [
            ("11_cut01.jpg", "10b"),
            ("11_cut02.jpg", "20b"),
            ("11_cut03.jpg", "30b"),
            ("11_cut04.jpg", "40b"),
            ("11_cut05.jpg", "50b"),
            ("11_cut06.jpg", "60b"),
            ("11_cut07.jpg", "70b"),
            ("11_cut08.jpg", "80b"),
            ("11_cut09.jpg", "90b"),
            ("11_cut10.jpg", "100b"),
            ("11_cut11.jpg", "110b"),
        ]
        for media_name, threshold in cut_ranges:
            if pos_value < int(threshold, 16):
                return media_name
        return None

    circles_: list[Circle] = []
    downloaded_media: set[str] = set()
    category_indices = [idx for idx, title in enumerate(switch_names) if "サークルカット集" not in title.get_text(strip=True)]
    for di in category_indices:
        d = switch_details[di]
        raw_title = switch_names[di].get_text(strip=True)
        genre = _extract_genre(raw_title)
        rows = d.select("table.tblCircleList tr")

        for row in rows:
            cols = row.select("td")
            if len(cols) < 3:
                continue

            position = _normalize_cell_text(cols[0])
            name_tag = cols[1].select_one("a")
            name_text = _normalize_cell_text(cols[1])
            comments = _normalize_cell_text(cols[2])
            link = name_tag["href"] if name_tag is not None else None

            media_name = _extract_media_name(position)
            media_list = []
            if media_name:
                img_path = PATH_M3_MEDIA_CURRENT / media_name
                if (not skip_media_dl) and (media_name not in downloaded_media) and (not img_path.exists()):
                    img_url = f"https://www.m3net.jp/img/event/m3_{i:02d}/{media_name.split('_', 1)[1]}"
                    print(f"Fetching image at {img_url} ...")
                    img_resp = requests.get(img_url)
                    if img_resp.status_code != 200:
                        raise ValueError(f"Failed to fetch image {media_name}, status code: {img_resp.status_code}")
                    with img_path.open("wb+") as img_file:
                        img_file.write(img_resp.content)
                    downloaded_media.add(media_name)
                else:
                    downloaded_media.add(media_name)
                media_list = [Medium(f"{i:02d}/{media_name}", [Source(m3_page, (ReliabilityTypes.Reliable, OriginTypes.Official))])]

            circles_.append(Circle(
                aliases=[name_text],
                media=media_list,
                links=[link] if link else None,
                comments=f"Genre: {genre}\n{comments}",
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