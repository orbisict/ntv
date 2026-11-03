import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css = f.read()

print("has table-footer-status:", "table-footer-status" in css)
print("has clip in html, body:", "overflow-x: clip" in css)
print("has position: fixed in site-header:", "position: fixed !important;\n    top: 0 !important;" in css)
