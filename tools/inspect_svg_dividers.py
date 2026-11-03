import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

import re
for m in re.finditer(r'<div class="section-wave-divider[^"]*"[^>]*>[\s\S]*?</div>', html):
    print("Match:")
    print(m.group(0))
    print("="*40)
