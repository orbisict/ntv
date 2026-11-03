import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update tools/generate_world_class_site.py
with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    site_code = f.read()

# Top announcement bar
old_top_bar = """        <span class="announcement-badge">{icon('sparkles', 'v-icon-sm')} VĂN HÓA HỌC ĐƯỜNG 2027</span>
        <span>Đề án Giao lưu Văn hóa &amp; Nghệ thuật Dân tộc Nam Bộ</span>"""

new_top_bar = """        <span class="announcement-badge">{icon('sparkles', 'v-icon-sm')} HỒ SƠ ĐỀ ÁN SỐ 104/QĐ-ĐHVH</span>
        <span>Kế hoạch Tổng thể &amp; Phương án Phối hợp Tổ chức Chương trình 2027</span>"""

if old_top_bar in site_code:
    site_code = site_code.replace(old_top_bar, new_top_bar, 1)
    print("Updated top_bar in generate_world_class_site.py")

# Hero badges
old_hero_badges = """          <div class="hero-badge-row">
            <div class="hero-partner-badge">
              {icon('lotus', 'v-icon-sm v-icon-pink')} ĐỒNG HÀNH: TỈNH ĐỒNG THÁP &amp; HUNGHAU HOLDINGS
            </div>
            <div class="hero-pill-badge">
              <span class="badge-dot"></span> SỰ KIỆN VĂN HÓA NGHỆ THUẬT 2027
            </div>
          </div>"""

new_hero_badges = """          <div class="hero-badge-row">
            <div class="hero-partner-badge">
              {icon('lotus', 'v-icon-sm v-icon-pink')} ĐƠN VỊ ĐỒNG HÀNH: TỈNH ĐỒNG THÁP &amp; HUNGHAU HOLDINGS
            </div>
            <div class="hero-pill-badge">
              {icon('award', 'v-icon-sm v-icon-gold')} QUY MÔ: 800 ĐẠI BIỂU &amp; SINH VIÊN
            </div>
          </div>"""

if old_hero_badges in site_code:
    site_code = site_code.replace(old_hero_badges, new_hero_badges, 1)
    print("Updated hero_badges in generate_world_class_site.py")

# Hero bottom curve
old_hero_curve = """    <!-- Soft Bottom Curve Transition -->
    <div class="hero-bottom-curve">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="var(--bg-page)"></path>
      </svg>
    </div>"""

new_hero_curve = """    <!-- Soft Bottom Curve Transition -->
    <div class="hero-bottom-curve">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#fbf9f5"></path>
      </svg>
    </div>"""

if old_hero_curve in site_code:
    site_code = site_code.replace(old_hero_curve, new_hero_curve, 1)
    print("Updated hero_curve in generate_world_class_site.py")

# Overview to Navy divider
old_div1 = """    <!-- Organic Flowing Wave Transition to Artists Section (Navy) -->
    <div class="section-wave-divider divider-overview-to-navy">
      <svg viewBox="0 0 1440 40" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,40 960,40 1440,0 L1440,40 L0,40 Z" fill="#071630"/>
      </svg>
    </div>"""

new_div1 = """    <!-- Organic Flowing Wave Transition to Artists Section (Navy) -->
    <div class="section-wave-divider divider-overview-to-navy">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#0c2044"/>
      </svg>
    </div>"""

if old_div1 in site_code:
    site_code = site_code.replace(old_div1, new_div1, 1)
    print("Updated div1 in generate_world_class_site.py")

# Artists to Agenda divider
old_div2 = """    <!-- Organic Flowing Wave Transition to Agenda Section (Cream) -->
    <div class="section-wave-divider divider-artists-to-agenda">
      <svg viewBox="0 0 1440 68" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C320,55 720,10 1120,48 C1280,62 1380,28 1440,0 L1440,68 L0,68 Z" fill="#fdfbf7"/>
      </svg>
    </div>"""

new_div2 = """    <!-- Organic Flowing Wave Transition to Agenda Section (Cream) -->
    <div class="section-wave-divider divider-artists-to-agenda">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#f5f2eb"/>
      </svg>
    </div>"""

if old_div2 in site_code:
    site_code = site_code.replace(old_div2, new_div2, 1)
    print("Updated div2 in generate_world_class_site.py")

# To Footer divider
old_div3 = """    <!-- Organic Flowing Wave Transition to Footer (Navy) -->
    <div class="section-wave-divider divider-to-footer">
      <svg viewBox="0 0 1440 68" fill="none" preserveAspectRatio="none">
        <path d="M0,20 C360,68 1080,68 1440,20 L1440,68 L0,68 Z" fill="#071630"/>
      </svg>
    </div>"""

new_div3 = """    <!-- Organic Flowing Wave Transition to Footer (Navy) -->
    <div class="section-wave-divider divider-to-footer">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#07152d"/>
      </svg>
    </div>"""

if old_div3 in site_code:
    site_code = site_code.replace(old_div3, new_div3, 1)
    print("Updated div3 in generate_world_class_site.py")

with open('tools/generate_world_class_site.py', 'w', encoding='utf-8') as f:
    f.write(site_code)

# 2. Update tools/build_world_class_css.py
with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css_code = f.read()

# Desktop Nav gap and font size
old_css_nav = """.desktop-nav {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-link {
  font-size: 0.88rem;
  font-weight: 600;
  color: #cbd5e1;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  transition: all var(--transition-fast);
  white-space: nowrap;
}"""

new_css_nav = """.desktop-nav {
  display: flex;
  align-items: center;
  gap: clamp(2px, 0.6vw, 8px);
}

.nav-link {
  font-size: clamp(0.80rem, 0.85vw, 0.86rem);
  font-weight: 600;
  color: #cbd5e1;
  padding: 6px clamp(6px, 0.7vw, 10px);
  border-radius: var(--radius-sm);
  transition: all var(--transition-fast);
  white-space: nowrap;
}"""

if old_css_nav in css_code:
    css_code = css_code.replace(old_css_nav, new_css_nav, 1)
    print("Updated desktop_nav in build_world_class_css.py")

# btn-header-cta
old_cta = """.btn-header-cta {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: var(--sen-pink-gradient);
  color: #ffffff !important;
  font-weight: 700;
  font-size: 0.86rem;
  padding: 10px 18px;
  border-radius: var(--radius-full);
  box-shadow: var(--shadow-pink);
  transition: all var(--transition-fast);
  white-space: nowrap;
}"""

new_cta = """.btn-header-cta {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--sen-pink-gradient);
  color: #ffffff !important;
  font-weight: 700;
  font-size: clamp(0.80rem, 0.85vw, 0.86rem);
  padding: 8px clamp(12px, 1.2vw, 16px);
  border-radius: var(--radius-full);
  box-shadow: var(--shadow-pink);
  transition: all var(--transition-fast);
  white-space: nowrap;
  flex-shrink: 0;
}"""

if old_cta in css_code:
    css_code = css_code.replace(old_cta, new_cta, 1)
    print("Updated btn-header-cta in build_world_class_css.py")

# Section Artists Background
old_artists_bg = """.section-artists {
  background: radial-gradient(circle at 50% 15%, #0f2752 0%, #071630 60%, #051024 100%);
  color: #ffffff;
}"""

new_artists_bg = """.section-artists {
  background: linear-gradient(180deg, #0c2044 0%, #071630 40%, #051024 100%);
  color: #ffffff;
}"""

if old_artists_bg in css_code:
    css_code = css_code.replace(old_artists_bg, new_artists_bg, 1)
    print("Updated section-artists background")

# Section wave divider CSS
old_wave_css = """.section-wave-divider {
  width: 100%;
  height: 64px;
  overflow: hidden;
  line-height: 0;
  margin-top: 48px;
  margin-bottom: -1px;
  position: relative;
  z-index: 3;
  pointer-events: none;
}"""

new_wave_css = """.section-wave-divider {
  width: 100%;
  height: 48px;
  overflow: hidden;
  line-height: 0;
  margin-top: 48px;
  margin-bottom: -1px;
  position: relative;
  z-index: 3;
  pointer-events: none;
}"""

if old_wave_css in css_code:
    css_code = css_code.replace(old_wave_css, new_wave_css, 1)
    print("Updated wave css in build_world_class_css.py")

with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
    f.write(css_code)

print("SUCCESS: Updated both files!")
