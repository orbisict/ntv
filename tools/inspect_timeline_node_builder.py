import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('.timeline-node {')
while pos != -1:
    print("Found at", pos)
    print(code[pos-20:pos+150])
    print("="*40)
    pos = code.find('.timeline-node {', pos+1)
