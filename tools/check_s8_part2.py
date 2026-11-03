import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_modern_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

p_s8 = text.find('id="register-contact"')
print(text[p_s8+1200:p_s8+2400])
