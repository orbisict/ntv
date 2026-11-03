from PIL import Image
import os

im = Image.open('verify_full_page_v9.png')
w, h = im.size

# Let's crop slices of 1500px to see all sections
slice_h = 1600
slices = [
    (0, "slice_0_hero.png"),
    (1400, "slice_1_overview.png"),
    (2800, "slice_2_artists.png"),
    (4200, "slice_3_agenda.png"),
    (5800, "slice_4_media.png"),
    (7400, "slice_5_risks.png"),
    (9000, "slice_6_budget.png"),
    (10600, "slice_7_gallery.png"),
    (12200, "slice_8_appendices.png"),
    (13800, "slice_9_ticket.png")
]

for y, name in slices:
    box = (0, y, w, min(h, y + slice_h))
    cropped = im.crop(box)
    cropped.save(name)
    print(f"Saved {name} at Y={y}")
