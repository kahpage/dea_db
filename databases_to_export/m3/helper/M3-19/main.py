"""M3-19 importer: parse circle table (genre headers with colspan=3)

This file follows the same robust pattern used for other M3 importers:
- Use local rawNN.htm if present (robust decoding: utf-8, shift_jis fallback)
- Find the table with genre header rows (<td colspan="3">)
- Parse rows with 3 columns: position, name (links), description
"""

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
    local_copy_path = PATH_M3_HELPER_CURRENT / f"raw{i:02d}.htm"
    if local_copy_path.exists():
        print(f"Using local copy for M3-{i:02d} at {local_copy_path} ...")
        with local_copy_path.open("rb") as f:
            raw = f.read()
        try:
            text = raw.decode("utf-8")
        except Exception:
            # prefer cp932 (Windows-31J) for archived Japanese pages, then fallbacks
            try:
                text = raw.decode("cp932")
            except Exception:
                try:
                    text = raw.decode("shift_jis")
                except Exception:
                    try:
                        text = raw.decode("euc_jp")
                    except Exception:
                        text = raw.decode("utf-8", errors="replace")
        return BeautifulSoup(text, "lxml")
    else:
        print(f"Fetching M3-{i:02d} at {url} ...")
        response = requests.get(url)
        with local_copy_path.open("wb+") as f:
            f.write(response.content)
        return BeautifulSoup(response.content, "lxml")


def _normalize_cell_text(tag) -> str:
    if tag is None:
        return ""
    return tag.get_text(" ", strip=True)


if __name__ == '__main__':
    i = 19
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    m3_page = "https://web.archive.org/web/20070714203329fw_/http://www.m3net.jp/m3_19/"

    soup = soup_via_fetch_or_local_copy(m3_page, i)

    # Find the table that contains genre header rows (colspan=3)
    table = None
    tables = soup.select("table")
    print(f"DEBUG: total candidate tables={len(tables)}")
    for idx, t in enumerate(tables):
        has_header = bool(t.select_one("td[colspan='3']"))
        tr_count = len(t.select("tr"))
        print(f"DEBUG: table[{idx}] has_header={has_header} tr_count={tr_count}")
        try:
            snippet = str(t)[:400]
        except Exception:
            snippet = "<unserializable table>"
        print("DEBUG: table snippet:", repr(snippet))
        if has_header:
            table = t
            break
    if table is None:
        table = soup.select_one("table[width='95%']") or soup.find("table")

    circles_: list[Circle] = []
    current_genre = ""
    rows = table.select("tr") if table is not None else []
    print(f"DEBUG: candidate table rows={len(rows)}")
    for row in rows:
        header = row.select_one("td[colspan='3']")
        if header:
            current_genre = _normalize_cell_text(header)
            continue

        cols = row.select("td")
        if len(cols) < 3:
            continue

        position = _normalize_cell_text(cols[0])
        name_tag = cols[1].select_one("a")
        name_text = _normalize_cell_text(cols[1])
        comments = _normalize_cell_text(cols[2])
        link = name_tag["href"] if name_tag is not None else None

        full_comments = f"Block: {current_genre}\n{comments}" if current_genre else comments

        clean_link = None
        if link:
            clean_link = re.sub(r"^https?://web\.archive\.org/web/[^/]+/", "", link)

        circles_.append(Circle(
            aliases=[name_text],
            links=[clean_link] if clean_link else None,
            comments=full_comments,
            position=position
        ))

    summary = f"Retrieved {len(circles_)} circles for {name}."
    print(summary.encode("ascii", errors="backslashreplace").decode("ascii"))

    # Debug: show first circle comments repr to verify encoding
    if circles_:
        print('DEBUG: first comment repr:', repr(circles_[0].comments)[:200])

    circles_output_path = PATH_M3_HELPER_CURRENT / f"circles_{i:02d}.json"
    out = [c.get_json() for c in circles_]
    with circles_output_path.open("w+", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)
