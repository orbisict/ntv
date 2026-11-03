import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

print(css[96800:97200])
