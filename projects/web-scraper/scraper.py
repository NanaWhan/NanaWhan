import json
import csv
from urllib.request import urlopen, Request
from html.parser import HTMLParser

class SimpleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.headings = []
        self._current_tag = None
        self._current_data = ""
    
    def handle_starttag(self, tag, attrs):
        self._current_tag = tag
        if tag == "a":
            for attr, val in attrs:
                if attr == "href":
                    self.links.append(val)
    
    def handle_data(self, data):
        if self._current_tag in ("h1", "h2", "h3"):
            self._current_data += data
    
    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3") and self._current_data.strip():
            self.headings.append({"level": tag, "text": self._current_data.strip()})
            self._current_data = ""
        self._current_tag = None

def fetch_page(url):
    req = Request(url, headers={"User-Agent": "SimpleScraper/1.0"})
    with urlopen(req) as resp:
        return resp.read().decode("utf-8", errors="replace")

def scrape(url):
    html = fetch_page(url)
    parser = SimpleParser()
    parser.feed(html)
    return {"links": parser.links, "headings": parser.headings}

def export_results(data, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    result = scrape(url)
    print(f"Found {len(result['links'])} links, {len(result['headings'])} headings")
    export_results(result)
