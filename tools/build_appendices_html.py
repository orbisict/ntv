import json
import re

with open('appendices_raw.json', 'r', encoding='utf-8') as f:
    apps = json.load(f)

# Let's inspect the raw text of each appendix and create structured HTML
print("Loaded appendices raw")
