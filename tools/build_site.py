import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('site_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Building website files...")
# Verify data keys
for k in data.keys():
    print(f"Key: {k}")
