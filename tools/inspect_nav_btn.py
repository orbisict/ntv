with open('styles.css', encoding='utf-8') as f:
    css = f.read()

import re
pos = css.find('.btn-header-cta')
print(css[pos:pos+400])
pos2 = css.find('.nav-container')
print(css[pos2:pos2+300])
