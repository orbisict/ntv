import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('sponsor-tier-grid')
while pos != -1:
    print("Found sponsor-tier-grid at", pos)
    print(code[pos-50:pos+200])
    print("="*40)
    pos = code.find('sponsor-tier-grid', pos+1)
