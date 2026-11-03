import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', encoding='utf-8') as f:
    code = f.read()

pos = code.find('top-banner')
if pos == -1: pos = code.find('top-notice')
if pos == -1: pos = code.find('top-bar')
if pos == -1: pos = code.find('navbar-brand')

print("Pos:", pos)
print(code[pos-200:pos+1500])
