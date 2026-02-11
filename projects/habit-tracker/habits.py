import json
import os
from datetime import datetime, timedelta

HABITS_FILE = "habits.json"

def load():
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE) as f:
            return json.load(f)
    return {}

def save(habits):
    with open(HABITS_FILE, "w") as f:
        json.dump(habits, f, indent=2)

def add_habit(name, frequency="daily"):
    habits = load()
    habits[name] = {"frequency": frequency, "log": [], "created": datetime.now().isoformat()}
    save(habits)

def log_habit(name):
    habits = load()
    if name in habits:
        habits[name]["log"].append(datetime.now().strftime("%Y-%m-%d"))
        save(habits)

def get_streak(name):
    habits = load()
    if name not in habits:
        return 0
    dates = sorted(set(habits[name]["log"]), reverse=True)
    if not dates:
        return 0
    streak = 1
    for i in range(len(dates) - 1):
        d1 = datetime.strptime(dates[i], "%Y-%m-%d")
        d2 = datetime.strptime(dates[i+1], "%Y-%m-%d")
        if (d1 - d2).days == 1:
            streak += 1
        else:
            break
    return streak

def show_habits():
    for name, data in load().items():
        streak = get_streak(name)
        total = len(set(data["log"]))
        print(f"  {name} ({data['frequency']}): {total} days, streak: {streak}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        show_habits()
    elif sys.argv[1] == "add":
        add_habit(sys.argv[2])
    elif sys.argv[1] == "log":
        log_habit(sys.argv[2])
