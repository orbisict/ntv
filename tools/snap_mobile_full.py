import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("index.html").replace(os.sep, '/')
file_url = f"file:///{html_file}"

# We can take screenshots of different scroll heights or test different viewport widths
# Let's write an HTML test runner with iframe or use CDP
# Better yet, let's use node with CDP to take full page screenshot at 375px
print("Ready to run node CDP full page capture")
