import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/appendices_html.json', 'r', encoding='utf-8') as f:
    apps = json.load(f)

classes = set()
for k, v in apps.items():
    found = re.findall(r'class="([^"]+)"', v)
    for c in found:
        for single in c.split():
            classes.add(single)

print("Classes found in appendices_html.json:")
for c in sorted(list(classes)):
    print(" -", c)
