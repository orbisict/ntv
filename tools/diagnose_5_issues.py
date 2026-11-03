import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    gen = f.read()

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css = f.read()

print("=== 1. AGENDA CONTROLS ===")
m1 = re.search(r'<div[^>]*agenda-controls[\s\S]*?</div>', gen)
if m1:
    print(m1.group(0))

print("\n=== CSS FOR AGENDA CONTROLS ===")
for m in re.finditer(r'([^{}]*agenda-controls[^{]*\{[^}]*\})', css):
    print(m.group(0))
for m in re.finditer(r'([^{}]*agenda-filter-btn[^{]*\{[^}]*\})', css):
    print(m.group(0))

print("\n=== 2. FINANCE OVERVIEW CARDS ===")
m2 = re.search(r'<div[^>]*finance-overview-grid[\s\S]*?</div>\s*</div>\s*</div>', gen)
if m2:
    print(m2.group(0))

print("\n=== 3. PROGRESS / DISTRIBUTION BAR ===")
m3 = re.search(r'<div[^>]*cost-distribution[\s\S]*?</div>\s*</div>', gen)
if not m3:
    m3 = re.search(r'<div[^>]*progress[\s\S]*?</div>\s*</div>', gen)
if not m3:
    m3 = re.search(r'Cơ Cấu Phân Bổ Chi Phí Sự Kiện[\s\S]*?</div>\s*</div>\s*</div>\s*</div>', gen)
if m3:
    print(m3.group(0)[:1000])

print("\n=== 4. SECTION TRANSITION CURVES ===")
for m in re.finditer(r'(<div[^>]*curve[\s\S]*?</div>|<svg[^>]*curve[\s\S]*?</svg>)', gen):
    print(m.group(0)[:300])

print("\n=== 5. ARTIST HEADER & FLOATING BAR PADDING ===")
m5 = re.search(r'<div[^>]*artist-card-hero[\s\S]*?</div>\s*</div>', gen)
if m5:
    print(m5.group(0)[:600])
