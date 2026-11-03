import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['tools/prepare_data.py', 'tools/generate_world_class_site.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'budget-visible-count' in content:
        print(f"Found in {fname}")
        pos = content.find('budget-visible-count')
        print(content[pos-200:pos+300])
