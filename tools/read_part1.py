import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('full_document_readable.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def print_range(start, end):
    for i in range(start, min(end, len(lines))):
        print(f"{i:03d}: {lines[i]}", end='')

print("=== PART 1: 0 to 110 ===")
print_range(0, 110)
