import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect overview section
p1 = text.find('<section id="overview"')
p2 = text.find('<section id="agenda"')
print("=== OVERVIEW SECTION ===")
print(text[p1:p1+1200])

# Let's inspect guests banner
p_guest = text.find('featured-guests-banner')
if p_guest != -1:
    print("=== GUEST BANNER ===")
    print(text[p_guest-100:p_guest+800])
else:
    print("=== NO GUEST BANNER FOUND ===")
