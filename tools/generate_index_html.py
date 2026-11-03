import json
import html
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('site_data.json', 'r', encoding='utf-8') as f:
    site_data = json.load(f)

# Build HTML pieces
print("Starting HTML generation...")
