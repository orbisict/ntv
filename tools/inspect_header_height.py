import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('--header-height')
while pos != -1:
    print("Found --header-height at", pos)
    print(css[pos-50:pos+100])
    print("="*40)
    pos = css.find('--header-height', pos+1)
