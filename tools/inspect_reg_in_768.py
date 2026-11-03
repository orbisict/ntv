import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.reg-contact-grid', css.find('@media (max-width: 768px)'))
print("reg-contact-grid in 768px pos:", pos)
if pos != -1:
    print(css[pos:pos+300])
