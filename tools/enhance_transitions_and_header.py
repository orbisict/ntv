import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update tools/generate_world_class_site.py
with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    site_code = f.read()

# Top announcement bar
old_top_bar = """        <span class="announcement-badge">{icon('sparkles', 'v-icon-sm')} VĂN HÓA HỌC ĐƯỜNG 2027</span>
        <span>Đề án Giao lưu Văn hóa &amp; Nghệ thuật Dân tộc Nam Bộ</span>"""

new_top_bar = """        <span class="announcement-badge">{icon('sparkles', 'v-icon-sm')} HỒ SƠ ĐỀ ÁN SỐ 104/QĐ-ĐHVH</span>
        <span>Kế hoạch Tổng thể &amp; Phương án Phối hợp Tổ chức Chương trình 2027</span>"""

assert old_top_bar in site_code, "old_top_bar not found"
site_code = site_code.replace(old_top_bar, new_top_bar, 1)

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

assert old_hero_badges in site_code, "old_hero_badges not found"
site_code = site_code.replace(old_hero_badges, new_hero_badges, 1)

# Hero bottom curve
old_hero_end = """        <!-- Right Column: Interactive Live Showcase Widget -->
        <div class="hero-showcase-col">
          {hero_widget}
        </div>
      </div>
    </div>
  </section>"""

new_hero_end = """        <!-- Right Column: Interactive Live Showcase Widget -->
        <div class="hero-showcase-col">
          {hero_widget}
        </div>
      </div>
    </div>

    <!-- Smooth Architectural Curve into Section 1 Overview -->
    <div class="section-wave-divider divider-hero-to-overview">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#fbf9f5"/>
      </svg>
    </div>
  </section>"""

assert old_hero_end in site_code, "old_hero_end not found"
site_code = site_code.replace(old_hero_end, new_hero_end, 1)

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

assert old_div1 in site_code, "old_div1 not found"
site_code = site_code.replace(old_div1, new_div1, 1)

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

assert old_div2 in site_code, "old_div2 not found"
site_code = site_code.replace(old_div2, new_div2, 1)

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

assert old_div3 in site_code, "old_div3 not found"
site_code = site_code.replace(old_div3, new_div3, 1)

with open('tools/generate_world_class_site.py', 'w', encoding='utf-8') as f:
    f.write(site_code)

print("SUCCESS: Updated tools/generate_world_class_site.py!")

# 2. Update tools/build_world_class_css.py
with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css_code = f.read()

# Desktop Nav gap and font size
old_css_nav = """/* Desktop Navigation */
.desktop-nav {
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

new_css_nav = """/* Desktop Navigation */
.desktop-nav {
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
    print("SUCCESS: Updated desktop nav CSS in build_world_class_css.py!")

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
    print("SUCCESS: Updated section-artists background!")

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
}

.divider-hero-to-overview {
  margin-top: 0;
  position: absolute;
  bottom: -1px;
  left: 0;
}

.hero-banner {
  padding-bottom: 72px;
}"""

if old_wave_css in css_code:
    css_code = css_code.replace(old_wave_css, new_wave_css, 1)
    print("SUCCESS: Updated section wave divider CSS!")

with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
    f.write(css_code)

print("SUCCESS: Updated tools/build_world_class_css.py!")
