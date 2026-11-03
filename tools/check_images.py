import os
from PIL import Image

media_files = sorted(os.listdir('assets/docx_media'))
for f in media_files:
    p = os.path.join('assets/docx_media', f)
    with Image.open(p) as img:
        print(f"{f}: format={img.format}, size={img.size}, mode={img.mode}")
