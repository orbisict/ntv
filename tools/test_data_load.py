import json
import html
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Ensure tools directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from icons import ICONS

def icon(name, extra_class=''):
    svg = ICONS.get(name, '')
    if extra_class and svg:
        svg = svg.replace('class="v-icon"', f'class="v-icon {extra_class}"')
    return svg

def h(text):
    return html.escape(str(text)) if text is not None else ""

# Load data
with open('tools/site_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load raw appendices
with open('tools/appendices_html.json', 'r', encoding='utf-8') as f:
    apps_raw = json.load(f)

apps = {}
for k, v in apps_raw.items():
    cleaned = v
    cleaned = cleaned.replace('📋 Sao chép toàn văn', f"{icon('copy', 'v-icon-sm')} Sao chép toàn văn")
    cleaned = cleaned.replace('🖨️ In văn bản này', f"{icon('printer', 'v-icon-sm')} In văn bản này")
    for em in ['📋', '🖨️', '🌸', '🏛️', '🏢', '👗', '🛡️', '📄', '🎟️', '⭐', '★']:
        cleaned = cleaned.replace(em, '')
    apps[k] = cleaned

print("Loaded data successfully! Total agenda:", len(data['agenda']), "Budget rows:", len(data['budget_all']))
