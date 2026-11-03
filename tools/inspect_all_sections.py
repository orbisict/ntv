with open('styles.css', encoding='utf-8') as f:
    css = f.read()

import re
sections = re.findall(r'(\.section-[a-z\-]+)\s*\{([^}]+)\}', css)
for s, rules in sections:
    if 'background' in rules or 'padding' in rules:
        print(s, rules.strip().replace('\n', ' '))
