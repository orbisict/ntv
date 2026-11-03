import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("index.html").replace(os.sep, '/')
file_url = f"file:///{html_file}"

# We can test by injecting script to open drawer and take screenshot
# Or using node CDP
print("Testing mobile drawer screenshot")
