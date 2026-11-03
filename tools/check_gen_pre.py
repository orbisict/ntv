import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_modern_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos1 = text.find('html_content = f"""')
print(text[:pos1])
