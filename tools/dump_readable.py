import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('document_structure.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

with open('full_document_readable.txt', 'w', encoding='utf-8') as out:
    for i, el in enumerate(elements):
        if el['type'] == 'p':
            t = el.get('text', '')
            drw = el.get('drawings', [])
            if t:
                out.write(f"\n[P {i}] {t}\n")
            if drw:
                out.write(f"  [MEDIA {drw}]\n")
        elif el['type'] == 'tbl':
            out.write(f"\n--- [TABLE {i} ({len(el['rows'])} rows x {len(el['rows'][0]) if el['rows'] else 0} cols)] ---\n")
            for r_idx, row in enumerate(el['rows']):
                row_str = " | ".join(c['text'].replace('\n', ' // ') for c in row)
                out.write(f"R{r_idx+1}: {row_str}\n")
            out.write("--- [END TABLE] ---\n\n")

print("Dumped full readable document to full_document_readable.txt")
