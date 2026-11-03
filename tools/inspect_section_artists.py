with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.section-artists {')
print(css[pos:pos+300])
