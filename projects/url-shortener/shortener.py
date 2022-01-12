import hashlib
import json
import os

DB_FILE = "urls.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE) as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)

def shorten(url, custom_code=None):
    db = load_db()
    if custom_code:
        code = custom_code
    else:
        code = hashlib.md5(url.encode()).hexdigest()[:6]
    db[code] = url
    save_db(db)
    return code

def resolve(code):
    db = load_db()
    return db.get(code)

def list_urls():
    db = load_db()
    for code, url in db.items():
        print(f"  {code} -> {url}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        list_urls()
    elif sys.argv[1] == "add":
        code = shorten(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        print(f"Shortened: {code}")
    elif sys.argv[1] == "get":
        print(resolve(sys.argv[2]) or "Not found")
