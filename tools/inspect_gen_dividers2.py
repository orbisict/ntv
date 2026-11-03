import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', encoding='utf-8') as f:
    code = f.read()

pos = code.find('divider-artists-to-agenda')
print(code[pos-100:pos+500])
