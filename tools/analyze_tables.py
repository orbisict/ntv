import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('document_structure.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

print(f"Total elements: {len(elements)}")

# Let's inspect all tables
tables_info = []
for i, el in enumerate(elements):
    if el['type'] == 'tbl':
        rows = el['rows']
        header = [c['text'].replace('\n', ' ') for c in rows[0]] if rows else []
        tables_info.append({
            'index': i,
            'row_count': len(rows),
            'col_count': len(rows[0]) if rows else 0,
            'header': header
        })

print(f"Total tables: {len(tables_info)}")
for t in tables_info:
    print(f"Table at {t['index']}: {t['row_count']} rows x {t['col_count']} cols | Header: {' | '.join(t['header'][:4])}")

