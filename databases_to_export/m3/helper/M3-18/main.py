
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
    i = 18
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    m3_page = "https://web.archive.org/web/20061212003359fw_/http://www.m3net.jp/m3_18/circle.html"

    # Retrieve circles
    circles_: list[Circle] = []
    # Fetch the m3_page
    soup = soup_via_fetch_or_local_copy(m3_page, i)

    # The M3-18 page lists circles in a single table where genre header rows
    # look like: <td colspan="3" align="center" bgcolor="e8e8e8">...<td>
    # and each subsequent circle row contains three columns: position, name, description.

    def _normalize_cell_text(tag) -> str:
        if tag is None:
            return ""
        return tag.get_text(" ", strip=True)

    # Find the table that contains genre header rows (colspan=3)
    table = None
    for t in soup.select("table"):
        if t.select_one("td[colspan='3']"):
            table = t
            break
    if table is None:
        # Fallback to a likely candidate
        table = soup.select_one("table[width='95%']") or soup.find("table")

    circles_: list[Circle] = []
    current_genre = ""
    rows = table.select("tr") if table is not None else []
    for row in rows:
        header = row.select_one("td[colspan='3']")
        if header:
            # Header row: set current genre for following circle rows
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

        circles_.append(Circle(
            aliases=[name_text],
            links=[link.replace("https://web.archive.org/web/20061212003359/", "")] if link else None,
            comments=full_comments,
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