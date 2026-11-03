import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('@media (max-width: 768px)')
print("768px pos:", pos)
sub_css = css[pos:]

import re
matches = re.findall(r'(\.site-header[^{]*\{[^}]*\})', sub_css)
for m in matches:
    print("Match in 768px:")
    print(m)
