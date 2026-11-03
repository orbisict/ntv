import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

ids = set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", js))
for i in sorted(ids):
    found = f'id="{i}"' in h or f"id='{i}'" in h
    print(f"{'OK' if found else 'MISSING'} : #{i}")
