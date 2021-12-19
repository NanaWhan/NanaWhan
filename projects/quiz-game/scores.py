import json
import os
from datetime import datetime

SCORES_FILE = "highscores.json"

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE) as f:
            return json.load(f)
    return []

def save_score(name, score, total):
    scores = load_scores()
    scores.append({
        "name": name,
        "score": score,
        "total": total,
        "percentage": round(score / total * 100, 1),
        "date": datetime.now().isoformat()
    })
    scores.sort(key=lambda s: s["percentage"], reverse=True)
    with open(SCORES_FILE, "w") as f:
        json.dump(scores[:10], f, indent=2)

def show_leaderboard():
    scores = load_scores()
    print("\n=== LEADERBOARD ===")
    for i, s in enumerate(scores[:10]):
        print(f"  {i+1}. {s['name']} - {s['score']}/{s['total']} ({s['percentage']}%)")

if __name__ == "__main__":
    show_leaderboard()
