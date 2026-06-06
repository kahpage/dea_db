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
        raw = local_copy_path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except Exception:
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

    print(f"Fetching M3-{i:02d} at {url} ...")
    response = requests.get(url)
    with local_copy_path.open("wb+") as f:
        f.write(response.content)
    return BeautifulSoup(response.content, "lxml")


def _normalize_cell_text(tag) -> str:
    if tag is None:
        return ""
    return tag.get_text(" ", strip=True)


def _cell_lines(tag) -> list[str]:
    if tag is None:
        return []
    text = tag.get_text("\n", strip=True)
    return [line.strip() for line in text.splitlines() if line.strip()]


def _is_position(value: str) -> bool:
    return bool(re.fullmatch(r"(?:[A-Z]|[ァ-ヶー])\d{2}(?:\s+(?:[A-Z]|[ァ-ヶー])\d{2})*", value.strip()))


if __name__ == '__main__':
    i = 20
    name = f"M3-{i:02d}"
    print(f"Processing {name} ...")
    m3_page = "http://www.ahoge.com/old/2007event.html"

    soup = soup_via_fetch_or_local_copy(m3_page, i)

    target_h2 = None
    for h2 in soup.find_all("h2"):
        h2_text = _normalize_cell_text(h2)
        if "10月8日" in h2_text and "M3" in h2_text:
            target_h2 = h2
            break

    table = None
    if target_h2 is not None:
        for sibling in target_h2.next_siblings:
            if getattr(sibling, "name", None) == "table":
                table = sibling
                break
            if getattr(sibling, "name", None) == "h2":
                break

    if table is None:
        table = soup.find("table")

    circles_: list[Circle] = []
    rows = table.select("tr") if table is not None else []
    last_position = ""

    for row in rows:
        cols = row.select("td")
        if not cols:
            continue

        first_text = _normalize_cell_text(cols[0])
        if first_text == "スペース" or first_text == "":
            continue

        if _is_position(first_text):
            position = first_text
            name_cell_index = 1
            last_position = position
        elif last_position and len(cols) >= 2:
            position = last_position
            name_cell_index = 0
        else:
            continue

        if name_cell_index >= len(cols):
            continue

        name_cell = cols[name_cell_index]
        name_tag = name_cell.select_one("a")
        name_text = _normalize_cell_text(name_cell)
        link = name_tag["href"] if name_tag is not None else None

        comment_cells = cols[name_cell_index + 1:]
        comment_lines: list[str] = []
        for cell in comment_cells:
            comment_lines.extend(_cell_lines(cell))
        comments = "\n".join(line for line in comment_lines if line)

        clean_link = None
        if link:
            clean_link = re.sub(r"^https?://web\.archive\.org/web/[^/]+/", "", link)

        circles_.append(Circle(
            aliases=[name_text],
            links=[clean_link] if clean_link else None,
            comments=comments,
            position=position,
        ))

    summary = f"Retrieved {len(circles_)} circles for {name}."
    print(summary.encode("ascii", errors="backslashreplace").decode("ascii"))

    circles_output_path = PATH_M3_HELPER_CURRENT / f"circles_{i:02d}.json"
    out = [c.get_json() for c in circles_]
    with circles_output_path.open("w+", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)
