import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.timeline-node[^{]*\{[^}]*\})', css)
for m in matches:
    print("Match:")
    print(m)
