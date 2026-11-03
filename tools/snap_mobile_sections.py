import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("index.html").replace(os.sep, '/')
file_url = f"file:///{html_file}"

# We can take screenshots with window sizes:
# 375, 4000
# and another at 375, 8000
for i, h in enumerate([3000, 6000, 9000, 15000]):
    out_png = os.path.abspath(f"mobile_slice_{i}.png")
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        f"--window-size=375,{h}",
        f"--screenshot={out_png}",
        file_url
    ]
    subprocess.run(cmd, check=True)
    print(f"Captured mobile_slice_{i}.png with height {h}")
