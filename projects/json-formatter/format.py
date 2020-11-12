import json
import sys

def format_json(data, indent=2, sort_keys=False):
    if isinstance(data, str):
        data = json.loads(data)
    return json.dumps(data, indent=indent, sort_keys=sort_keys)

def minify_json(data):
    if isinstance(data, str):
        data = json.loads(data)
    return json.dumps(data, separators=(',', ':'))

def validate_json(data):
    try:
        json.loads(data)
        return True, "Valid JSON"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python format.py <file.json> [--minify] [--sort]")
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        content = f.read()
    
    if "--minify" in sys.argv:
        print(minify_json(content))
    else:
        print(format_json(content, sort_keys="--sort" in sys.argv))
