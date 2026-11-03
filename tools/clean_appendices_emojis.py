import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from icons import ICONS

def icon(name, extra_class=''):
    svg = ICONS.get(name, '')
    if extra_class and svg:
        svg = svg.replace('class="v-icon"', f'class="v-icon {extra_class}"')
    return svg

with open('appendices_html.json', 'r', encoding='utf-8') as f:
    apps = json.load(f)

# Replace copy & print emojis in all 5 apps
for k in apps:
    txt = apps[k]
    txt = txt.replace('📋 Sao chép toàn văn', f"{icon('copy', 'v-icon-sm')} Sao chép toàn văn")
    txt = txt.replace('🖨️ In văn bản này', f"{icon('printer', 'v-icon-sm')} In văn bản này")
    apps[k] = txt

with open('appendices_html.json', 'w', encoding='utf-8') as f:
    json.dump(apps, f, ensure_ascii=False, indent=2)

print("Cleaned emojis from appendices_html.json successfully!")
