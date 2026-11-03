import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.tab-nav-wrapper')
print(css[pos:pos+600])

import re
matches = re.findall(r'(\.tab-nav-wrapper[^{]*\{[^}]*\})', css)
for m in matches:
    print("Match:")
    print(m)
