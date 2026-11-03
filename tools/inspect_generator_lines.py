import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(50, 130):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end="")
