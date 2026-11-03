import subprocess
import os
import json

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
]

chrome = None
for p in chrome_paths:
    if os.path.exists(p):
        chrome = p
        break

if not chrome:
    print("Chrome not found")
    exit(1)

html_file = os.path.abspath("index.html").replace(os.sep, '/')
file_url = f"file:///{html_file}"

viewports = [
    ("mobile_375", 375, 812),
    ("mobile_414", 414, 896),
    ("tablet_768", 768, 1024),
    ("laptop_1024", 1024, 768),
]

for name, w, h in viewports:
    out_png = os.path.abspath(f"responsive_{name}.png")
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={out_png}",
        file_url
    ]
    subprocess.run(cmd, check=True)
    print(f"Captured {name}: {out_png}")
