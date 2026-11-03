import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css = f.read()

pos = css.find('@media print')
print(css[pos-300:pos+50])
