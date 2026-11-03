import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

p_head = text.find('<head>')
p_head_end = text.find('</head>')
print(text[p_head:p_head_end])
