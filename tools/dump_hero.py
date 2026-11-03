import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'(<section class="hero-banner"[\s\S]*?</section>)', html)
if m:
    print(m.group(0))
