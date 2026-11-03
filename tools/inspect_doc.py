import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('document_structure.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

print(f"Total elements: {len(elements)}")
for i, el in enumerate(elements):
    if el['type'] == 'p':
        txt = el.get('text', '')
        drw = el.get('drawings', [])
        if txt or drw:
            print(f"[{i:03d}] P: {txt[:80]} {'(IMG: ' + str(drw) + ')' if drw else ''}")
    elif el['type'] == 'tbl':
        num_rows = len(el['rows'])
        first_row_cells = [c['text'].replace('\n', ' ')[:25] for c in el['rows'][0]] if num_rows > 0 else []
        print(f"[{i:03d}] TBL: {num_rows} rows x {len(el['rows'][0]) if num_rows else 0} cols | Header: {' | '.join(first_row_cells)}")
