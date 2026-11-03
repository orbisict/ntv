with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.hero-banner {')
print(css[pos:pos+400])
pos = css.find('.hero-banner::')
print(css[pos:pos+400])
