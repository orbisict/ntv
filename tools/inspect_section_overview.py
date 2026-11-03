with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.section-overview {')
print(css[pos:pos+300])
