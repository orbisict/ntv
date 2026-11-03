import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    gen = f.read()

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css = f.read()

print("=== TICKET HTML IN GEN ===")
idx = gen.find('class="live-ticket-card"')
if idx != -1:
    print(gen[idx-50:idx+1500])

print("\n=== ALL TICKET CSS RULES ===")
for m in re.finditer(r'([^{}]*ticket-[^{]*\{[^}]*\})', css):
    print(m.group(0))
