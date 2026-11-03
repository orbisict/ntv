import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('printTicket')
while pos != -1:
    print("Found printTicket at", pos)
    print(html[pos-100:pos+200])
    print("="*40)
    pos = html.find('printTicket', pos+1)
