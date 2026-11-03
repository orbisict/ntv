import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', encoding='utf-8') as f:
    html = f.read()

btns = re.findall(r'<button[^>]*class="[^"]*agenda-filter-btn[^"]*"[^>]*>.*?</button>', html, re.DOTALL)
print("--- BUTTONS ---")
for b in btns:
    print(b)

nodes = re.findall(r'<div[^>]*class="[^"]*timeline-node[^"]*"[^>]*>', html)
print("\n--- NODES ---")
for n in nodes:
    print(n)
