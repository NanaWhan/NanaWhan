import os
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}

def organize(directory):
    path = Path(directory)
    for file in path.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            for category, extensions in CATEGORIES.items():
                if ext in extensions:
                    dest = path / category
                    dest.mkdir(exist_ok=True)
                    shutil.move(str(file), str(dest / file.name))
                    print(f"Moved {file.name} -> {category}/")
                    break

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    organize(target)
