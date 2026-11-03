with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.container {')
print(css[pos:pos+250])
pos = css.find('.desktop-nav {')
print(css[pos:pos+300])
