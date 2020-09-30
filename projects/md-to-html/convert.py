import re

def markdown_to_html(md):
    html = md
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
    html = re.sub(r'^\- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
    
    lines = html.split('\n')
    result = []
    for line in lines:
        if line.strip() and not line.strip().startswith('<'):
            result.append(f'<p>{line}</p>')
        else:
            result.append(line)
    return '\n'.join(result)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            print(markdown_to_html(f.read()))
    else:
        print("Usage: python convert.py <file.md>")
