import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'(<header[\s\S]*?</header>)', html)
if m:
    header_html = m.group(0)
    print("HEADER HTML LENGTH:", len(header_html))
    print(header_html)
