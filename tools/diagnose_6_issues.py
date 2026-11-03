import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    gen = f.read()

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css = f.read()

print("=== 1. PILLAR CARD HTML & CSS ===")
m_pil = re.search(r'<div class="pillar-card"[\s\S]*?</div>\s*</div>', gen)
if m_pil:
    print(m_pil.group(0)[:300])

for m in re.finditer(r'([^{}]*pillar-[^{]*\{[^}]*\})', css):
    print(m.group(0))

print("\n=== 2. TIMELINE JS FILTERING & CSS ===")
with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    js = f.read()

m_filter = re.search(r'agenda-filter-btn[\s\S]*?(?=\n\s*\n\s*/\*|\Z)', js)
if m_filter:
    print(m_filter.group(0)[:600])

print("\n=== 3. APPENDIX TABS HTML & CSS ===")
m_app = re.search(r'<div[^>]*appendix-nav[\s\S]*?</div>', gen)
if not m_app:
    m_app = re.search(r'Phụ Lục 1: Danh sách Nhân sự[\s\S]*?</div>', gen)
if m_app:
    print(m_app.group(0)[:500])

for m in re.finditer(r'([^{}]*appendix-tab[^{]*\{[^}]*\}|[^{}]*appendix-nav[^{]*\{[^}]*\})', css):
    print(m.group(0))

print("\n=== 4. TICKET HTML & CSS ===")
m_tkt = re.search(r'<div[^>]*live-ticket-card[\s\S]*?</div>\s*</div>\s*</div>', gen)
if m_tkt:
    print(m_tkt.group(0)[:600])

for m in re.finditer(r'([^{}]*live-ticket[^{]*\{[^}]*\}|[^{}]*ticket-body[^{]*\{[^}]*\}|[^{}]*ticket-header[^{]*\{[^}]*\})', css):
    print(m.group(0))
