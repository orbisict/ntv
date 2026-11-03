with open('index.html', encoding='utf-8') as f:
    html = f.read()

import re
pos = [m.start() for m in re.finditer(r'section-wave-divider', html)]
print("Found", len(pos), "wave dividers at:")
for p in pos:
    print("--- around", p, "---")
    print(html[max(0, p-100):min(len(html), p+150)])
