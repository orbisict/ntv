import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

classes = set(re.findall(r'class="([^"]*tab[^"]*)"', html))
print("Classes containing 'tab':")
for c in classes:
    print(" -", c)
