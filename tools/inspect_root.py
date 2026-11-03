with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('--max-width')
print(css[pos-50:pos+150])
