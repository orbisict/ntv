import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('@media (max-width: 768px)')
print(code[pos:pos+1500])
