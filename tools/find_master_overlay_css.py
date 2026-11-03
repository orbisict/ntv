import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

for m in re.finditer(r'([^{}]*(?:master-banner-overlay|master-badge|artist-master|banner-main-name)[^{]*\{[^}]*\})', css):
    print(m.group(0))
