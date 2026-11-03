import subprocess
import os

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

html_file = os.path.abspath("test_ticket_preview.html")
out_png = os.path.abspath("ticket_rendered_preview.png")

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--window-size=1000,1400",
    f"--screenshot={out_png}",
    f"file:///{html_file.replace(os.sep, '/')}"
]

print("Running chrome screenshot...")
subprocess.run(cmd, check=True)
print(f"Saved {out_png}")
