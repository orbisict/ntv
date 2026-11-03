import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('full_document_readable.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(110, 225):
    print(f"{i:03d}: {lines[i]}", end='')
