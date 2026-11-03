import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/* Modern App-grade Mobile Navigation Drawer & Backdrop */')
end_idx = text.find('/* ==========================================================================\n   SECTION 0: GLOBAL TICKER', idx)
if end_idx == -1:
    end_idx = idx + 2500

print(text[idx:end_idx])
