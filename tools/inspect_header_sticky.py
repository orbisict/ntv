import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.site-header {')
print(css[pos:pos+400])

import re
matches = re.findall(r'(\.site-header[^{]*\{[^}]*\})', css)
for m in matches:
    print("Match:")
    print(m)
