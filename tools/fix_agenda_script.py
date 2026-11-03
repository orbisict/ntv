with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = "node.style.display = 'flex';"
replacement = "node.style.display = '';"

if target in text:
    text = text.replace(target, replacement)
    with open('tools/build_clean_script_js.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated build_clean_script_js.py to use node.style.display = ''!")
else:
    print("ERROR: target not found")
