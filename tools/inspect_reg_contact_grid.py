import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.reg-contact-grid')
print(css[pos:pos+400])
