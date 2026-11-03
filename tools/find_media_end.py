import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css = f.read()

pos = css.find('@media (max-width: 480px)')
print("480px pos:", pos)
if pos != -1:
    print(css[pos-200:pos+200])
else:
    pos = css.rfind('@media')
    print("Last @media pos:", pos)
    print(css[pos:pos+300])
