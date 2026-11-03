import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    js = f.read()

pos = js.find('function initAgendaFilters')
print(js[pos:pos+700])
