import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'@media[^{]+\{(?:[^{}]*\{[^{}]*\})*\.tab-nav-wrapper[^{]*\{[^}]*\}', css)
print("Matches in media query:", matches)
pos = css.find('.tab-nav-wrapper', css.find('@media (max-width: 768px)'))
print("Pos in 768px:", pos)
