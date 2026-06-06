
from db_structs import Circle
from pathlib import Path
import json
from bs4 import BeautifulSoup
import re
import requests
import lxml

PATH_M3_HELPER_CURRENT = Path(__file__).parent
PATH_M3_HELPER = PATH_M3_HELPER_CURRENT.parent
PATH_M3 = PATH_M3_HELPER.parent

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
    i = 16
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    m3_page = "https://www.m3net.jp/event/2005f.php"

    # Retrieve circles
    circles_: list[Circle] = []
    # Fetch the m3_page
    soup = soup_via_fetch_or_local_copy(m3_page, i)

    switch_details = soup.select("div.switchDetail")
    switch_names = soup.select("p.switchTitle")
    # M3-06 is a direct table listing: each switchDetail block contains circle rows.

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

    def _extract_position_from_row(row) -> str:
        # Position is stored in the first column of each row.
        position_cell = row.select_one("td.left")
        return _normalize_cell_text(position_cell) if position_cell is not None else ""

    circles_: list[Circle] = []
    for di in range(len(switch_details)):
        d = switch_details[di]
        raw_title = switch_names[di].get_text(strip=True)
        genre = _extract_genre(raw_title)
        rows = d.select("table.tblCircleList tr")

        for row in rows:
            cols = row.select("td")
            if len(cols) < 3:
                continue

            position = _extract_position_from_row(row)
            name_tag = cols[1].select_one("a")
            name_text = _normalize_cell_text(cols[1])
            comments = _normalize_cell_text(cols[2])
            link = name_tag["href"] if name_tag is not None else None

            circles_.append(Circle(
                aliases=[name_text],
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