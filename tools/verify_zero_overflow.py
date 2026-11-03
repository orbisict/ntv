import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath("index.html").replace(os.sep, '/')
file_url = f"file:///{html_file}"

# We can run headless chrome with a script to check scrollWidth vs innerWidth
script = """
const w = window.innerWidth;
const s = document.documentElement.scrollWidth;
const b = document.body.scrollWidth;
const bad = [];
for (const el of document.querySelectorAll('*')) {
  const r = el.getBoundingClientRect();
  if (r.right > w + 2) {
    bad.push({ tag: el.tagName, cls: el.className, right: r.right, w: r.width });
  }
}
console.log(JSON.stringify({ innerWidth: w, scrollWidth: s, bodyWidth: b, badCount: bad.length, bad: bad.slice(0, 10) }));
"""

# Let's test with node CDP or direct evaluate
print("Zero overflow verification script ready")
