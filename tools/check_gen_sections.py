import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_modern_site.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines in generate_modern_site.py:", len(lines))
# Let's see the section outline
for i, l in enumerate(lines):
    if '<!-- SECTION' in l or '<!-- Hero Banner' in l:
        print(f"Line {i+1}: {l.strip()}")
