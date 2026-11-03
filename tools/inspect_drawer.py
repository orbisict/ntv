import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="mobile-nav-drawer"')
if start != -1:
    print("--- DRAWER HTML ---")
    print(html[start-30:start+2500])

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("\n--- DRAWER CSS ---")
for m in re.finditer(r'([^{}]*mobile-[^{]*\{[^}]*\})', css):
    print(m.group(0))
