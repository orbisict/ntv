import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    js_code = f.read()

pos = js_code.find('const printWindow = window.open')
print(js_code[pos-100:pos+500])
