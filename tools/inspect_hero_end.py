import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    site_code = f.read()

pos = site_code.find('hero-showcase-col')
print(site_code[pos:pos+300])
