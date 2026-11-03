import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('class="live-ticket-card"')
if idx != -1:
    print(html[idx-50:idx+2000])
