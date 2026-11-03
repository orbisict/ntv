import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/site_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Keys in site_data.json:", list(data.keys()))
for k in data.keys():
    val = data[k]
    if isinstance(val, list):
        print(f"  {k}: list of {len(val)} items")
    elif isinstance(val, dict):
        print(f"  {k}: dict of {len(val)} keys")
    else:
        print(f"  {k}: {type(val)}")
