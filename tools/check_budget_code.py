import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_modern_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_b = text.find('budget_table_rows')
if pos_b != -1:
    print(text[pos_b-100:pos_b+1000])
else:
    pos_b = text.find('budget_groups')
    print(text[pos_b-100:pos_b+1000])
