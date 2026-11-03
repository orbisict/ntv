import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('tab-pill-btn')
while pos != -1:
    print("Found tab-pill-btn at", pos)
    print(html[pos-100:pos+300])
    print("="*40)
    pos = html.find('tab-pill-btn', pos+1)
