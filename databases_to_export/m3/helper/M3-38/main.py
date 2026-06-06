
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
    i = 38
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    m3_page = "https://www.m3net.jp/event/2016f.php"

    # Retrieve circles
    circles_: list[Circle] = []
    # Fetch the m3_page
    soup = soup_via_fetch_or_local_copy(m3_page, i)

    switch_details = soup.select("div.switchDetail")
    switch_names = soup.select("p.switchTitle")
    # M3-06 is a direct table listing: each switchDetail block contains circle rows.

    def _extract_genre(full_title: str) -> str:
        # Keep the full switch title, e.g.
        # "[ A ] (音楽：オリジナル・カバー　音響：その他)".
        # Normalizing whitespace keeps the output stable without dropping
        # the category text that distinguishes each block.
        return re.sub(r"\s+", " ", full_title).strip()

    def _normalize_cell_text(tag) -> str:
        # Preserve a space where HTML uses <br> so names like
        # "マリオ音楽グループ<br>岡崎支部" match the cut-side text.
        return tag.get_text(" ", strip=True)

    def _extract_position_from_row(row) -> str:
        # Position is stored in the first column of each row.
        position_cell = row.select_one("td.left")
        return _normalize_cell_text(position_cell) if position_cell is not None else ""
    
    def _extract_primary_name(cell) -> str:
        primary_item = cell.select_one("ul.dropmenu2 > li")
        if primary_item is None:
            return _normalize_cell_text(cell)

        name_parts = []
        for child in primary_item.contents:
            if getattr(child, "name", None) == "ul":
                break
            if getattr(child, "get_text", None) is not None:
                text = child.get_text(" ", strip=True)
            else:
                text = str(child).strip()
            if text:
                name_parts.append(text)

        name_text = " ".join(name_parts).strip()
        return name_text if name_text else _normalize_cell_text(cell)

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
            name_text = _extract_primary_name(cols[1])

            comments = _normalize_cell_text(cols[2])

            # Collect all anchor hrefs in the name cell (handles drop-down / hover links)
            anchors = cols[1].select("a")
            raw_links = [a.get("href") for a in anchors if a.get("href")]
            # Deduplicate while preserving order
            seen = set()
            links = []
            for l in raw_links:
                if l in seen:
                    continue
                if l in ["target=_blank"]:
                    continue
                seen.add(l)
                links.append(l)

            circles_.append(Circle(
                aliases=[name_text],
                links=links if links else None,
                comments=f"Block: {genre}\n{comments}",
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