import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_modern_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))
pos1 = text.find('html_content = f"""')
print("html_content starts at:", pos1)
print(text[pos1:pos1+500])
