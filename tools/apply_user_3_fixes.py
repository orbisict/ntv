import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update tools/generate_world_class_site.py
with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    site_code = f.read()

old_footer_str = """        <div style="padding: 12px 20px; font-size: 0.82rem; color: var(--text-muted); background: #f8fafc; border-top: 1px solid var(--border-subtle); display: flex; justify-content: space-between;">
          <span>Đang hiển thị: <strong id="budget-visible-count">68</strong> hạng mục</span>
          <span>Đơn vị tính: Việt Nam Đồng (VNĐ)</span>
        </div>"""

new_footer_str = """        <div class="table-footer-status">
          <span class="status-count-tag">{icon('layers', 'v-icon-xs')} Đang hiển thị: <strong id="budget-visible-count">68</strong> hạng mục</span>
          <span class="status-currency-tag">{icon('wallet', 'v-icon-xs')} Đơn vị tính: <strong>Việt Nam Đồng (VNĐ)</strong></span>
        </div>"""

if old_footer_str in site_code:
    site_code = site_code.replace(old_footer_str, new_footer_str, 1)
    with open('tools/generate_world_class_site.py', 'w', encoding='utf-8') as f:
        f.write(site_code)
    print("SUCCESS: Updated tools/generate_world_class_site.py with table-footer-status!")
else:
    print("NOTE: old_footer_str already replaced or not found.")

# 2. Update tools/build_world_class_css.py
with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css_code = f.read()

# Add global table-footer-status CSS before responsive media queries
table_footer_global_css = """/* Table Footer Status Bar */
.table-footer-status {
  padding: 14px 20px;
  font-size: 0.82rem;
  color: var(--text-muted);
  background: #f8fafc;
  border-top: 1px solid var(--border-subtle);
  border-radius: 0 0 var(--radius-md) var(--radius-md);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px 24px;
}

.status-count-tag,
.status-currency-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}

.status-count-tag strong,
.status-currency-tag strong {
  color: var(--vhu-navy-base);
  font-weight: 700;
}
"""

if "/* Table Footer Status Bar */" not in css_code:
    pos_insert = css_code.find("/* === 1. LAPTOP & COMPACT DESKTOP")
    assert pos_insert != -1, "pos_insert not found"
    css_code = css_code[:pos_insert] + table_footer_global_css + "\n" + css_code[pos_insert:]
    print("SUCCESS: Added table_footer_global_css to build_world_class_css.py")

# Update @media (max-width: 768px) block start
old_768_start = """@media (max-width: 768px) {
  :root {
    --container-padding: 16px;
  }
  html, body {
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  body {
    padding-bottom: calc(92px + env(safe-area-inset-bottom, 16px)) !important; /* Generous clearance for mobile floating bar */
  }"""

new_768_start = """@media (max-width: 768px) {
  :root {
    --container-padding: 16px;
    --header-height: 64px;
  }
  html, body {
    overflow-x: clip !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  html {
    scroll-padding-top: 76px !important;
  }
  body {
    padding-top: 64px !important; /* Fixed header spacing */
    padding-bottom: calc(92px + env(safe-area-inset-bottom, 16px)) !important; /* Generous clearance for mobile floating bar */
  }"""

assert old_768_start in css_code, "old_768_start not found in build_world_class_css.py"
css_code = css_code.replace(old_768_start, new_768_start, 1)

# Add mobile sticky/fixed header styles
old_header_rule = """  /* Header & Navigation */
  .top-announcement {
    display: none;
  }
  .btn-header-cta {
    display: none;
  }"""

new_header_rule = """  /* Header & Navigation (Always Fixed at Top of Mobile Viewport) */
  .site-header {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 64px !important;
    z-index: 1000 !important;
    background: rgba(5, 16, 36, 0.98) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.45) !important;
    border-bottom: 1px solid rgba(212, 155, 25, 0.3) !important;
  }
  .nav-container {
    height: 64px !important;
  }
  .top-announcement {
    display: none !important;
  }
  .btn-header-cta {
    display: none !important;
  }"""

assert old_header_rule in css_code, "old_header_rule not found in build_world_class_css.py"
css_code = css_code.replace(old_header_rule, new_header_rule, 1)

# Add sponsor tier 1-column, tab wrapper horizontal swipe, and table footer status in 768px query
additional_768_rules = """
  /* 04 Gói Quyền Lợi Tài Trợ Doanh Nghiệp (1 Full-width Column on Mobile) */
  .sponsor-tier-grid {
    grid-template-columns: 1fr !important;
    gap: 16px !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  .sponsor-tier-card {
    padding: 22px 18px !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }
  .tier-price {
    font-size: 1.65rem !important;
    white-space: nowrap !important;
  }

  /* Universal Tab Nav Swipe Capsules (Media Plan & Risks/KPI) */
  .tab-nav-wrapper {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    gap: 8px !important;
    justify-content: flex-start !important;
    padding: 4px 16px 12px !important;
    margin-left: -16px !important;
    margin-right: -16px !important;
    scrollbar-width: none;
  }
  .tab-nav-wrapper::-webkit-scrollbar {
    display: none;
  }
  .tab-pill-btn {
    white-space: nowrap !important;
    flex: 0 0 auto !important;
    padding: 8px 16px !important;
    font-size: 0.82rem !important;
  }

  /* Table Footer Status Bar (Mobile Stacked with generous gap) */
  .table-footer-status {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 8px !important;
    padding: 12px 14px !important;
  }

  /* Ticket Registration Card (Mobile Fit) */
  .ticket-form-card,
  .reg-form-card {
    padding: 20px 16px !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }
"""

pos_end_768 = css_code.find("/* ------------------------------------------------------------\n   16. PRINT OPTIMIZATION")
assert pos_end_768 != -1, "pos_end_768 not found"

# Find the last closing brace before print optimization
pos_last_brace = css_code.rfind("}", 0, pos_end_768)
assert pos_last_brace != -1, "pos_last_brace not found"

css_code = css_code[:pos_last_brace] + additional_768_rules + css_code[pos_last_brace:]

with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
    f.write(css_code)

print("SUCCESS: Updated tools/build_world_class_css.py!")
