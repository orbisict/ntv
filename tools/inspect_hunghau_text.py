import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

import re
pos = html.find('HungHau Campus')
while pos != -1:
    print("Found at", pos)
    print(html[pos-100:pos+200])
    print("="*40)
    pos = html.find('HungHau Campus', pos+1)
