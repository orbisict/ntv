import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all tables and see if they are wrapped in .table-scroll-wrapper
matches = re.finditer(r'<table[^>]*>', html)
for i, m in enumerate(matches):
    start = m.start()
    snippet = html[max(0, start-250):start]
    print(f"Table {i+1} opening: {m.group(0)}")
    has_scroll_wrapper = 'table-scroll-wrapper' in snippet
    print(f"  Has table-scroll-wrapper in preceding 250 chars: {has_scroll_wrapper}")
    if not has_scroll_wrapper:
        print(f"  Preceding code: {snippet.strip().splitlines()[-2:]}")
