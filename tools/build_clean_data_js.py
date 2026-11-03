import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load site_data.json
with open('site_data.json', 'r', encoding='utf-8') as f:
    site_data = json.load(f)

# Load raw appendices
with open('appendices_raw.json', 'r', encoding='utf-8') as f:
    app_data = json.load(f)

site_data['appendices_raw'] = app_data

js_content = "window.SITE_DATA = " + json.dumps(site_data, ensure_ascii=False, indent=2) + ";\n"

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated data.js successfully ({len(js_content)} chars)")
