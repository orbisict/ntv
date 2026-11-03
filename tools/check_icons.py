import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/icons.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
keys = re.findall(r"'([a-zA-Z0-9_-]+)':", text)
print("Available icons:", len(keys))
print(keys)
