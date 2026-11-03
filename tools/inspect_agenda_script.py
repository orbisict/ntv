import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('agenda-filter-btn')
if idx != -1:
    print(text[idx-50:idx+600])
