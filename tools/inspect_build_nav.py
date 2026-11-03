with open('tools/build_world_class_css.py', encoding='utf-8') as f:
    code = f.read()

pos = code.find('.desktop-nav {')
print(code[pos:pos+400])
