with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('.bg-alt')
print(css[pos:pos+300])
