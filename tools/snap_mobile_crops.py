import subprocess
import os
from PIL import Image

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("index.html").replace(os.sep, '/')
file_url = f"file:///{html_file}"

viewports = [
    ("m_hero", 375, 1000),
    ("m_full1", 375, 3000),
    ("m_full2", 375, 6000),
]

for name, w, h in viewports:
    out = os.path.abspath(f"mobile_{name}.png")
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={out}",
        file_url
    ]
    subprocess.run(cmd, check=True)
    print(f"Captured {out}, size={os.path.getsize(out)}")

# Now crop key regions
im1 = Image.open("mobile_m_full1.png")
im1.crop((0, 0, 375, 800)).save(os.path.abspath("crop_hero_view.png"))
im1.crop((0, 750, 375, 1600)).save(os.path.abspath("crop_specs_stats.png"))
im1.crop((0, 1500, 375, 2300)).save(os.path.abspath("crop_pillars_view.png"))
im1.crop((0, 2200, 375, 3000)).save(os.path.abspath("crop_artists_view.png"))

im2 = Image.open("mobile_m_full2.png")
im2.crop((0, 3000, 375, 3900)).save(os.path.abspath("crop_timeline_view.png"))
im2.crop((0, 3900, 375, 5000)).save(os.path.abspath("crop_budget_view.png"))
im2.crop((0, 5000, 375, 6000)).save(os.path.abspath("crop_ticket_view.png"))

print("All crops generated successfully!")
