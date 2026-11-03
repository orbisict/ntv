import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('ticket-form-card')
print(html[pos-300:pos+300])
