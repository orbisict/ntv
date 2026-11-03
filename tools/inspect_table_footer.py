import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Đang hiển thị:')
print(html[pos-100:pos+300])
