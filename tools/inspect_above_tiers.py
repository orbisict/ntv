import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('04 Gói Quyền Lợi Tài Trợ')
print(html[pos-1200:pos])
