from PIL import Image

im = Image.open('verify_full_28k.png')
w, h = im.size
print('Total 28k dimensions:', w, h)

# Slices from 16000 to end
for y in range(15500, h, 1400):
    im.crop((0, y, w, min(h, y+1400))).save(f'slice_app_{y}.png')
    print(f'Saved slice_app_{y}.png')
