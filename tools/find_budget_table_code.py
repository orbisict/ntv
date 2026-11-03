import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    gen = f.read()

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css = f.read()

print("=== BUDGET MASTER TABLE IN GEN ===")
idx = gen.find('id="budget-master-table"')
if idx != -1:
    print(gen[idx-200:idx+800])

print("\n=== BUDGET TABLE CSS ===")
for m in re.finditer(r'([^{}]*budget-table[^{]*\{[^}]*\})', css):
    print(m.group(0))

for m in re.finditer(r'([^{}]*table-category[^{]*\{[^}]*\}|[^{}]*group-header[^{]*\{[^}]*\})', css):
    print(m.group(0))
