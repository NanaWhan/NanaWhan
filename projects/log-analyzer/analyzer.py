import re
from collections import Counter, defaultdict
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)'
)

def parse_log(filepath):
    entries = []
    with open(filepath) as f:
        for line in f:
            match = LOG_PATTERN.match(line.strip())
            if match:
                entries.append({
                    "timestamp": match.group(1),
                    "level": match.group(2),
                    "message": match.group(3)
                })
    return entries

def analyze(entries):
    levels = Counter(e["level"] for e in entries)
    hourly = defaultdict(int)
    for e in entries:
        hour = e["timestamp"][:13]
        hourly[hour] += 1
    
    errors = [e for e in entries if e["level"] in ("ERROR", "CRITICAL")]
    
    return {
        "total": len(entries),
        "by_level": dict(levels),
        "errors": errors[:10],
        "peak_hour": max(hourly, key=hourly.get) if hourly else None
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <logfile>")
    else:
        entries = parse_log(sys.argv[1])
        result = analyze(entries)
        print(f"Total entries: {result['total']}")
        for level, count in result["by_level"].items():
            print(f"  {level}: {count}")
        if result["errors"]:
            print(f"\nRecent errors:")
            for e in result["errors"]:
                print(f"  [{e['timestamp']}] {e['message']}")
