import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('budget-group-header-cell')
print(html[pos-700:pos-250])
