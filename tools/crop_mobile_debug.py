from PIL import Image

im0 = Image.open('mobile_slice_0.png')
print('im0 size:', im0.size)

# Crop 1: Top & Hero (0 to 800)
im0.crop((0, 0, 375, 800)).save('m_crop_hero.png')

# Crop 2: Hero bottom, countdown & specs (700 to 1600)
im0.crop((0, 700, 375, 1600)).save('m_crop_hero_bottom.png')

# Crop 3: Overview & Pillars (1500 to 2400)
im0.crop((0, 1500, 375, 2400)).save('m_crop_overview.png')

# Crop 4: Artists (2300 to 3000)
im0.crop((0, 2300, 375, 3000)).save('m_crop_artists.png')

im1 = Image.open('mobile_slice_1.png')
# Crop 5: Timeline / Agenda (3000 to 4000)
im1.crop((0, 3000, 375, 4000)).save('m_crop_agenda.png')

# Crop 6: Budget Table (4800 to 5800)
im1.crop((0, 4800, 375, 5800)).save('m_crop_budget.png')

im2 = Image.open('mobile_slice_2.png')
# Crop 7: Registration & Ticket preview (7500 to 8800)
im2.crop((0, 7500, 375, 8800)).save('m_crop_ticket.png')

print("All crops saved.")
