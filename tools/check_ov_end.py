import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_modern_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect overview section end
p_ov_end = text.find('<!-- SECTION 2: AGENDA TIMELINE')
print("Overview ends at:", p_ov_end)
print(text[p_ov_end-300:p_ov_end])
