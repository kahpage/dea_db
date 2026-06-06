
from db_structs import Circle
from pathlib import Path
import json
from bs4 import BeautifulSoup
from bs4.element import Tag
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
    i = 17
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    m3_page = "https://web.archive.org/web/20061212003031fw_/http://www.m3net.jp/m3_17/"

    # Retrieve circles
    circles_: list[Circle] = []
    # Fetch the m3_page
    soup = soup_via_fetch_or_local_copy(m3_page, i)

    def _normalize_text(text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()

    def _extract_entries_from_circle_column(cell: Tag) -> list[tuple[str, str | None]]:
        entries: list[tuple[str, str | None]] = []
        segment: list[str] = []

        def flush_segment() -> None:
            html = "".join(segment).strip()
            segment.clear()
            if not html:
                return

            frag = BeautifulSoup(html, "lxml")
            if frag.select_one("p") is not None:
                return

            text = _normalize_text(frag.get_text(" ", strip=True))
            if not text:
                return

            link_tag = frag.select_one("a")
            link = link_tag.get("href") if link_tag is not None else None
            entries.append((text, link))

        for node in cell.children:
            if isinstance(node, Tag) and node.name and node.name.lower() == "br":
                flush_segment()
                continue
            segment.append(str(node))
        flush_segment()
        return entries

    circles_: list[Circle] = []
    table = soup.select_one("table[bgcolor='d8e0f0']")
    if table is None:
        raise ValueError("Could not find the main circle table for M3-17")

    circle_columns = table.select("tr > td[valign='TOP']")
    for col in circle_columns:
        for name_text, link in _extract_entries_from_circle_column(col):
            circles_.append(Circle(
                aliases=[name_text],
                links=[link.replace("https://web.archive.org/web/20061212003031/", "")] if link else None,
                position=""
            ))
    # Print a safe ASCII-escaped summary to avoid UnicodeEncodeError
    summary = f"Retrieved {len(circles_)} circles for {name}."
    print(summary.encode('ascii', errors='backslashreplace').decode('ascii'))

    # Export circles
    circles_output_path = PATH_M3_HELPER_CURRENT / f"circles_{i:02d}.json"
    out = [c.get_json() for c in circles_]
    with circles_output_path.open("w+", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)