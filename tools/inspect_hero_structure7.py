import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    site_code = f.read()

pos = site_code.find('hero-stats-ribbon')
print(site_code[pos+500:pos+1500])
