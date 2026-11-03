import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    js_code = f.read()

pos1 = js_code.find('function printTicket()')
pos2 = js_code.find('// Toast notification helper')
print(f"pos1={pos1}, pos2={pos2}")
print(js_code[pos1:pos1+300])
print("...")
print(js_code[pos2-300:pos2])
