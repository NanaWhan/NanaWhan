import json
from datetime import datetime
from collections import defaultdict

def load_expenses():
    with open("expenses.json") as f:
        return json.load(f)

def monthly_report():
    expenses = load_expenses()
    months = defaultdict(float)
    for e in expenses:
        month = datetime.fromisoformat(e["date"]).strftime("%Y-%m")
        months[month] += e["amount"]
    
    for month in sorted(months):
        bar = "#" * int(months[month] / 10)
        print(f"  {month}: ${months[month]:>8.2f} {bar}")

def top_expenses(n=5):
    expenses = load_expenses()
    sorted_exp = sorted(expenses, key=lambda e: e["amount"], reverse=True)
    print(f"\nTop {n} expenses:")
    for e in sorted_exp[:n]:
        date = datetime.fromisoformat(e["date"]).strftime("%Y-%m-%d")
        print(f"  ${e['amount']:>8.2f} | {date} | {e['description']}")

if __name__ == "__main__":
    monthly_report()
    top_expenses()
