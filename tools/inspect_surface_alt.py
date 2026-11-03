with open('styles.css', encoding='utf-8') as f:
    css = f.read()

pos = css.find('--bg-surface-alt')
print(css[pos-50:pos+150])
