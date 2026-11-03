import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('btn-audio-toggle')
print("btn-audio-toggle pos:", pos)
if pos != -1:
    print(text[pos-200:pos+400])
