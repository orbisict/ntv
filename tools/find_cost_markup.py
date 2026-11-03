import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Cơ Cấu Phân Bổ Chi Phí Sự Kiện')
if idx != -1:
    print(text[idx-200:idx+1500])
else:
    print("Not found by exact title")
