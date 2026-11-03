import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('budget-master-table')
print(html[pos-1000:pos])
