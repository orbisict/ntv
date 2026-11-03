import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.top-announcement {')
print(css[pos:pos+400])

import re
matches = re.findall(r'(\.top-announcement[^{]*\{[^}]*\})', css)
for m in matches:
    print("Match:")
    print(m)
