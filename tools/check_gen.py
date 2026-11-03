import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_modern_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

p_guest = text.find('khach-moi.png')
print("khach-moi.png pos:", p_guest)
if p_guest != -1:
    print(text[p_guest-200:p_guest+400])
