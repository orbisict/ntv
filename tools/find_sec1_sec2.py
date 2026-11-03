import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Find Section 1 end and Section 2 start
idx1 = text.find('id="overview"')
idx2 = text.find('id="artists"')

print(text[idx1+1000:idx2+300])
