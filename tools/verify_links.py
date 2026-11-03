import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

sources = re.findall(r'(?:src|data-src)="([^"]+)"', content)
print(f"Total image references: {len(sources)}")

missing = []
valid = []
for src in sorted(set(sources)):
    clean_src = src.lstrip('./').replace('/', os.sep)
    if not os.path.exists(clean_src):
        missing.append((src, clean_src))
    else:
        valid.append(src)

print(f"Valid files ({len(valid)}):")
for v in valid:
    print(f"  ✓ {v}")

if missing:
    print(f"MISSING FILES ({len(missing)}):")
    for m in missing:
        print(f"  ✗ {m[0]} -> {m[1]}")
else:
    print("ALL REFERENCED ASSETS EXIST PERFECTLY ON DISK!")
