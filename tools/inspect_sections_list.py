import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', encoding='utf-8') as f:
    code = f.read()

import re
matches = re.findall(r'<section[^>]+>', code)
for m in matches:
    print(m)
