import re

with open('tools/build_appendices_blocks.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any <table class="doc-table"> ... </table> with <div class="table-scroll-wrapper"><table class="doc-table"> ... </table></div>
# If not already wrapped in table-scroll-wrapper

def wrap_table(match):
    tbl = match.group(0)
    return f'<div class="table-scroll-wrapper">\n{tbl}\n</div>'

new_content = re.sub(r'<table class="doc-table">[\s\S]*?</table>', wrap_table, content)

with open('tools/build_appendices_blocks.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated build_appendices_blocks.py with wrapped tables!")
