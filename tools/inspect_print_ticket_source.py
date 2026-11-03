import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    js_code = f.read()

pos = js_code.find('function printTicket')
print(js_code[pos:pos+1200])
