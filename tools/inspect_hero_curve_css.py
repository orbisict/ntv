with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.hero-bottom-curve')
print(css[pos:pos+300])
