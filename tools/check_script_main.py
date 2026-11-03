import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Script length:", len(text))
pos_main = text.find('document.addEventListener(\'DOMContentLoaded\'')
print("DOMContentLoaded pos:", pos_main)
print(text[pos_main:pos_main+500])
