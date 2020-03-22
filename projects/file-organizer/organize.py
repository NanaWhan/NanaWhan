import os
import shutil
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}

def get_category(ext):
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Other"

def organize(directory, dry_run=False):
    path = Path(directory)
    moved = 0
    for file in path.iterdir():
        if file.is_file() and file.name != "organizer.log":
            category = get_category(file.suffix.lower())
            dest = path / category
            if dry_run:
                print(f"[DRY RUN] {file.name} -> {category}/")
            else:
                dest.mkdir(exist_ok=True)
                shutil.move(str(file), str(dest / file.name))
                logging.info(f"Moved {file.name} -> {category}/")
                print(f"Moved {file.name} -> {category}/")
            moved += 1
    print(f"\nTotal: {moved} files {'would be ' if dry_run else ''}organized")

if __name__ == "__main__":
    import sys
    dry = "--dry-run" in sys.argv
    target = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else "."
    organize(target, dry_run=dry)
