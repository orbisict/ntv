import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('document_structure.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

# Rel map from earlier:
# rId9 -> media/image1.png
# rId10 -> media/image2.png
# rId11 -> media/image3.png
# rId12 -> media/image4.jpeg
# rId13 -> media/image5.jpeg
# rId14 -> media/image6.jpeg
# rId15 -> media/image7.jpeg
# rId16 -> media/image8.jpeg
# rId17 -> media/image9.jpeg
# rId18 -> media/image10.png
# rId19 -> media/image11.jpeg
# rId20 -> media/image12.png
# rId21 -> media/image13.png

rel_map = {
    'rId9': 'image1.png',
    'rId10': 'image2.png',
    'rId11': 'image3.png',
    'rId12': 'image4.jpeg',
    'rId13': 'image5.jpeg',
    'rId14': 'image6.jpeg',
    'rId15': 'image7.jpeg',
    'rId16': 'image8.jpeg',
    'rId17': 'image9.jpeg',
    'rId18': 'image10.png',
    'rId19': 'image11.jpeg',
    'rId20': 'image12.png',
    'rId21': 'image13.png',
}

for i, el in enumerate(elements):
    drw = el.get('drawings')
    if drw:
        imgs = [rel_map.get(r, r) for r in drw]
        prev_txt = elements[i-1].get('text', '') if i > 0 and elements[i-1]['type']=='p' else ''
        curr_txt = el.get('text', '')
        next_txt = elements[i+1].get('text', '') if i < len(elements)-1 and elements[i+1]['type']=='p' else ''
        print(f"Element {i}: images={imgs}")
        print(f"   Prev: {prev_txt}")
        print(f"   Curr: {curr_txt}")
        print(f"   Next: {next_txt}")
        print("-" * 60)
