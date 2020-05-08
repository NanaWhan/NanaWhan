import re
from collections import Counter

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def analyze_text(text):
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len([s for s in sentences if s.strip()]),
        "avg_word_length": sum(len(w) for w in words) / max(len(words), 1),
    }

if __name__ == "__main__":
    text = input("Enter text: ")
    stats = analyze_text(text)
    for key, val in stats.items():
        print(f"  {key}: {val:.1f}" if isinstance(val, float) else f"  {key}: {val}")
    print("\nTop 10 words:")
    for word, count in count_words(text).most_common(10):
        print(f"  {word}: {count}")
