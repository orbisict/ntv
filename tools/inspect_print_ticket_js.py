import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('script.js', encoding='utf-8') as f:
    js = f.read()

pos = js.find('printTicket')
print(js[pos+800:pos+2500])
