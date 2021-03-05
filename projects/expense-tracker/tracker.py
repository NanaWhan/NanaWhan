import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(amount, description, category="general"):
    expenses = load_expenses()
    expenses.append({
        "amount": amount,
        "description": description,
        "category": category,
        "date": datetime.now().isoformat()
    })
    save_expenses(expenses)

def get_total(category=None):
    expenses = load_expenses()
    if category:
        expenses = [e for e in expenses if e["category"] == category]
    return sum(e["amount"] for e in expenses)

def get_summary():
    expenses = load_expenses()
    categories = {}
    for e in expenses:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]
    return categories

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python tracker.py add <amount> <desc> [category]")
        print("       python tracker.py summary")
    elif sys.argv[1] == "add":
        amount = float(sys.argv[2])
        desc = sys.argv[3]
        cat = sys.argv[4] if len(sys.argv) > 4 else "general"
        add_expense(amount, desc, cat)
        print(f"Added: ${amount} - {desc} [{cat}]")
    elif sys.argv[1] == "summary":
        for cat, total in get_summary().items():
            print(f"  {cat}: ${total:.2f}")
        print(f"\n  Total: ${get_total():.2f}")
