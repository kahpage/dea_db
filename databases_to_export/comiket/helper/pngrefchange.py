from os import name
from pathlib import Path
import shutil
import re

for event_num in range(83, 101):
    PATH_FOLDER = Path(__file__).parent
    PATH_media = PATH_FOLDER.parent / "media"
    PATH_circle_images = PATH_media / f"{event_num}webcatalog" / "circle_images"
    PATH_allcircles = PATH_FOLDER / "catalogs" / f"C{event_num}" / "all_circles_export.json"

    print(f"Processing event number: {event_num}")
    if not PATH_circle_images.exists():
        print(f"Circle images path does not exist: {PATH_circle_images}. Skipping...")
        continue

    # open all_circles.json and load its content
    with PATH_allcircles.open("r", encoding="utf-8") as f:
        all_circles_data = f.read()
    # Iterate over all png of circle_images and replace in the data
    for file in PATH_circle_images.iterdir():
        if file.is_file() and file.suffix == ".png":
            new_path_str = f'"path": "{event_num}webcatalog/circle_images/{file.name}"'
            old_path_str = f'"path": "{event_num}webcatalog/circle_images/{file.with_suffix('.jpg').name}"'
            if old_path_str in all_circles_data:
                all_circles_data = all_circles_data.replace(old_path_str, new_path_str)
                print(f"Updated image path in all_circles.json: {old_path_str} -> {new_path_str}")
            else:
                print(f"Could not find image path {old_path_str} in all_circles.json ! Skipping...")

    # Write back the updated data to all_circles.json
    with PATH_allcircles.open("w", encoding="utf-8") as f:
        f.write(all_circles_data)