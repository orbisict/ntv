import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('budget-visible-count')
print(code[pos-200:pos+300])
