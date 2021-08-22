import json
import os

CONTACTS_FILE = "contacts.json"

def load():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE) as f:
            return json.load(f)
    return {}

def save(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(name, phone=None, email=None):
    contacts = load()
    contacts[name] = {"phone": phone, "email": email}
    save(contacts)

def search(query):
    contacts = load()
    results = {}
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in str(info.get("phone", "")) or query.lower() in str(info.get("email", "")).lower():
            results[name] = info
    return results

def list_all():
    for name, info in sorted(load().items()):
        parts = [name]
        if info.get("phone"):
            parts.append(info["phone"])
        if info.get("email"):
            parts.append(info["email"])
        print(" | ".join(parts))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        list_all()
    elif sys.argv[1] == "add":
        add_contact(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None, sys.argv[4] if len(sys.argv) > 4 else None)
    elif sys.argv[1] == "search":
        for name, info in search(sys.argv[2]).items():
            print(f"{name}: {info}")
