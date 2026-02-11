import re
import sys
from collections import Counter
from pathlib import Path

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def analyze_text(text):
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    paragraphs = text.split('\n\n')
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len([s for s in sentences if s.strip()]),
        "paragraphs": len([p for p in paragraphs if p.strip()]),
        "avg_word_length": sum(len(w) for w in words) / max(len(words), 1),
        "reading_time_min": len(words) / 200,
    }

def analyze_file(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"File not found: {filepath}")
        return
    text = path.read_text()
    print(f"\nAnalysis of: {path.name}")
    print("-" * 40)
    stats = analyze_text(text)
    for key, val in stats.items():
        label = key.replace("_", " ").title()
        print(f"  {label}: {val:.1f}" if isinstance(val, float) else f"  {label}: {val}")
    print(f"\nTop 10 words:")
    for word, count in count_words(text).most_common(10):
        print(f"  {word}: {count}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for f in sys.argv[1:]:
            analyze_file(f)
    else:
        text = input("Enter text: ")
        stats = analyze_text(text)
        for key, val in stats.items():
            print(f"  {key}: {val}")
