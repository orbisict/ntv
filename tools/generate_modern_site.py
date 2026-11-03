import json
import html
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Ensure tools directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from icons import ICONS

def icon(name, extra_class=''):
    svg = ICONS.get(name, '')
    if extra_class and svg:
        svg = svg.replace('class="v-icon"', f'class="v-icon {extra_class}"')
    return svg

def h(text):
    return html.escape(str(text)) if text is not None else ""

# Load data
with open('tools/site_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load raw appendices
with open('tools/appendices_html.json', 'r', encoding='utf-8') as f:
    apps_raw = json.load(f)

# Clean any emoji in appendices
apps = {}
for k, v in apps_raw.items():
    cleaned = v
    cleaned = cleaned.replace('📋 Sao chép toàn văn', f"{icon('copy', 'v-icon-sm')} Sao chép toàn văn")
    cleaned = cleaned.replace('🖨️ In văn bản này', f"{icon('printer', 'v-icon-sm')} In văn bản này")
    # Clean any remaining emojis
    for em in ['📋', '🖨️', '🌸', '🏛️', '🏢', '👗', '🛡️', '📄', '🎟️', '⭐', '★']:
        cleaned = cleaned.replace(em, '')
    apps[k] = cleaned

# 1. Agenda Timeline
agenda_html = []
for idx, item in enumerate(data['agenda']):
    act_lower = item['activity'].lower()
    item_type = 'all'
    is_highlight = False
    badge_label = "Chương trình"
    
    if 'khai mạc' in act_lower or 'đón khách' in act_lower or 'giới thiệu' in act_lower:
        item_type += ' opening'
        badge_label = "Nghi lễ & Khai mạc"
    if 'tiết mục' in act_lower or 'đờn ca tài tử' in act_lower or 'phương mỹ chi' in act_lower:
        item_type += ' art'
        is_highlight = True
        badge_label = "Biểu diễn nghệ thuật"
    if 'giao lưu' in act_lower:
        item_type += ' talk'
        is_highlight = True
        badge_label = "Giao lưu chia sẻ"
    if 'fashion' in act_lower or 'thời trang' in act_lower:
        item_type += ' fashion'
        is_highlight = True
        badge_label = "Trình diễn thời trang"
    if 'tổng kết' in act_lower or 'tiễn khách' in act_lower:
        item_type += ' closing'
        badge_label = "Tổng kết & Tri ân"

    card_class = "timeline-card card-highlight" if is_highlight else "timeline-card"
    node_class = "timeline-node highlight" if is_highlight else "timeline-node"

    agenda_html.append(f"""
    <div class="{node_class}" data-type="{item_type}">
      <div class="timeline-time-badge">
        <span class="time-text">{h(item['time'])}</span>
      </div>
      <div class="timeline-point"></div>
      <div class="{card_class}">
        <div class="timeline-card-header">
          <div>
            <span class="category-pill">{badge_label}</span>
            <h4 class="timeline-activity">{h(item['activity'])}</h4>
          </div>
          <span class="timeline-team-pill">{icon('users', 'v-icon-sm')} {h(item['team'])}</span>
        </div>
        <p class="timeline-desc">{h(item['content'])}</p>
        <div class="timeline-meta-footer">
          <span>{icon('music', 'v-icon-sm')} <strong>Âm thanh:</strong> {h(item['audio'])}</span>
          <span>{icon('building', 'v-icon-sm')} <strong>Ban thực hiện:</strong> {h(item['team'])}</span>
        </div>
      </div>
    </div>
    """)
agenda_str = "\n".join(agenda_html)

# 2. Media Plans
# Pre-event table
media_pre_rows = []
for idx, r in enumerate(data['media_pre']):
    media_pre_rows.append(f"""
    <tr>
      <td class="text-center font-bold" style="width: 45px;">{idx+1}</td>
      <td class="font-bold">{h(r['activity'])}</td>
      <td>{h(r['objective'])}</td>
      <td>{h(r['content'])}</td>
      <td><span class="channel-tag">{h(r['channel'])}</span></td>
      <td class="whitespace-nowrap font-semibold">{h(r['time'])}</td>
      <td>{h(r['lead'])}</td>
      <td><span class="kpi-target-tag">{h(r['kpi'])}</span></td>
    </tr>
    """)
media_pre_str = "\n".join(media_pre_rows)

# During-event table
media_during_rows = []
for idx, r in enumerate(data['media_during']):
    media_during_rows.append(f"""
    <tr>
      <td class="text-center font-bold" style="width: 45px;">{idx+1}</td>
      <td class="font-bold">{h(r['activity'])}</td>
      <td>{h(r['objective'])}</td>
      <td>{h(r['content'])}</td>
      <td><span class="channel-tag">{h(r['channel'])}</span></td>
      <td class="whitespace-nowrap font-semibold">{h(r['time'])}</td>
      <td>{h(r['lead'])}</td>
    </tr>
    """)
media_during_str = "\n".join(media_during_rows)

# Post-event table
media_post_rows = []
for idx, r in enumerate(data['media_post']):
    media_post_rows.append(f"""
    <tr>
      <td><span class="phase-tag">{h(r['phase'])}</span></td>
      <td class="whitespace-nowrap font-semibold">{h(r['time'])}</td>
      <td class="font-bold">{h(r['activity'])}</td>
      <td>{h(r['content'])}</td>
      <td><span class="channel-tag">{h(r['channel'])}</span></td>
      <td>{h(r['lead'])}</td>
    </tr>
    """)
media_post_str = "\n".join(media_post_rows)

# 3. Risks & Severity Badges
def get_sev_badge(sev):
    s = sev.lower()
    if 'rất cao' in s:
        return f'<span class="badge badge-danger">{h(sev)}</span>'
    elif 'cao' in s:
        return f'<span class="badge badge-warning">{h(sev)}</span>'
    elif 'trung bình' in s:
        return f'<span class="badge badge-caution">{h(sev)}</span>'
    else:
        return f'<span class="badge badge-info">{h(sev)}</span>'

# Risks Plan
risk_plan_rows = []
for r in data['risks_plan']:
    risk_plan_rows.append(f"""
    <tr data-severity="{h(r['severity'])}">
      <td class="font-bold">{h(r['category'])}</td>
      <td class="font-semibold text-primary">{h(r['risk'])}</td>
      <td>{get_sev_badge(r['severity'])}</td>
      <td class="text-sm">{h(r['prevention'])}</td>
      <td class="text-sm">{h(r['contingency'])}</td>
      <td><span class="team-badge">{h(r['team'])}</span></td>
    </tr>
    """)
risk_plan_str = "\n".join(risk_plan_rows)

# Risks Event
risk_event_rows = []
for r in data['risks_event']:
    risk_event_rows.append(f"""
    <tr data-severity="{h(r['severity'])}">
      <td class="font-bold">{h(r['category'])}</td>
      <td class="font-semibold text-primary">{h(r['risk'])}</td>
      <td>{get_sev_badge(r['severity'])}</td>
      <td class="text-sm">{h(r['prevention'])}</td>
      <td class="text-sm">{h(r['contingency'])}</td>
      <td><span class="team-badge">{h(r['team'])}</span></td>
    </tr>
    """)
risk_event_str = "\n".join(risk_event_rows)

# Risks Media
risk_media_rows = []
for r in data['risks_media']:
    risk_media_rows.append(f"""
    <tr data-severity="{h(r['severity'])}">
      <td><span class="category-pill">{h(r['category'])}</span></td>
      <td class="font-semibold text-primary">{h(r['id'])}. {h(r['risk'])}</td>
      <td>{get_sev_badge(r['severity'])}</td>
      <td class="text-sm">{h(r['prevention'])}</td>
      <td class="text-sm">{h(r['contingency'])}</td>
      <td><span class="team-badge">{h(r['team'])}</span></td>
    </tr>
    """)
risk_media_str = "\n".join(risk_media_rows)

# KPIs HTML
kpi_cards = []
for k in data['kpis']:
    kpi_cards.append(f"""
    <div class="kpi-card">
      <div class="kpi-card-top">
        <span class="kpi-group-tag">{h(k['group'])}</span>
        <h5 class="kpi-metric-title">#{h(k['id'])}. {h(k['metric'])}</h5>
        <div class="kpi-target-box">
          <span class="target-label">Mục tiêu:</span>
          <span class="target-value">{h(k['target'])}</span>
        </div>
      </div>
      <div class="kpi-meta-row">
        <span>{icon('clock', 'v-icon-sm')} Hạn: {h(k['deadline'])}</span>
        <span>{icon('file-text', 'v-icon-sm')} Nguồn: {h(k['source'])}</span>
      </div>
    </div>
    """)
kpis_str = "\n".join(kpi_cards)

# 4. Budget Table
budget_rows = []
for g in data['budget_groups']:
    budget_rows.append(f"""
    <tr class="budget-group-header-row">
      <td colspan="6" class="budget-group-title">
        {icon('wallet', 'v-icon-sm')} {h(g['name'])} 
        <span class="group-subtotal">(Tiểu kế: {h(g['subtotal'])})</span>
      </td>
    </tr>
    """)
    for itm in g['items']:
        budget_rows.append(f"""
        <tr class="budget-item-row" data-group-code="{h(g['code'])}">
          <td class="font-semibold">{h(itm['name'])}</td>
          <td class="text-center">{h(itm['quantity'])}</td>
          <td class="text-center">{h(itm['unit'])}</td>
          <td class="text-right text-muted">{h(itm['unit_price'])}</td>
          <td class="text-right font-bold text-primary">{h(itm['total_price'])}</td>
          <td class="text-notes">{h(itm['notes'])}</td>
        </tr>
        """)
budget_table_str = "\n".join(budget_rows)

# Sponsors Table
sponsor_rows = []
for s in data['sponsors']:
    sponsor_rows.append(f"""
    <tr>
      <td class="font-bold">{h(s['source'])}</td>
      <td class="text-center">{h(s['quantity'])}</td>
      <td class="text-right font-bold text-gold">{h(s['value'])}</td>
      <td>{h(s['unit'])}</td>
    </tr>
    """)
sponsors_table_str = "\n".join(sponsor_rows)

# Privileges Table
privilege_rows = []
for p in data['privileges']:
    privilege_rows.append(f"""
    <tr>
      <td class="font-bold">{h(p['item'])}</td>
      <td class="text-center font-bold text-diamond">{h(p['diamond'])}</td>
      <td class="text-center">{h(p['gold'])}</td>
      <td class="text-center">{h(p['silver'])}</td>
      <td class="text-center text-muted">{h(p['partner'])}</td>
    </tr>
    """)
privileges_table_str = "\n".join(privilege_rows)

# Master HTML Template
html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kế hoạch Chương trình Văn hoá & Nghệ thuật Tỉnh Đồng Tháp 2027 | Chạm Một Sắc Sen - Đại học Văn Hiến</title>
  <meta name="description" content="Đề án Kế hoạch tổng thể tổ chức Chương trình Văn hoá & Nghệ thuật tỉnh Đồng Tháp năm 2027 chủ đề 'Chạm một sắc Sen' thực hiện bởi Trường Đại học Văn Hiến.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./styles.css">
  <link rel="icon" href="./assets/images/logo-VHU.png" type="image/png">
</head>
<body>

  <!-- Top Announcement Bar -->
  <aside class="top-announcement" aria-label="Thông tin nhanh">
    <div class="container top-announcement-flex">
      <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
        <span class="announcement-badge">{icon('sparkles', 'v-icon-sm')} ĐỀ ÁN SỰ KIỆN VĂN HÓA VHU 2027</span>
        <span>Hồ sơ Kế hoạch Tổng thể & Đề án Tổ chức Chương trình</span>
      </div>
      <div class="top-contact-info">
        <span>{icon('map-pin', 'v-icon-sm')} HungHau Campus, 13E Nguyễn Văn Linh, Bình Hưng, TP.HCM</span>
        <span>{icon('phone', 'v-icon-sm')} Hotline: 0369.449.925</span>
      </div>
    </div>
  </aside>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="container nav-container">
      <a href="#" class="brand-wrapper" title="Trường Đại học Văn Hiến">
        <img src="./assets/images/logo-VHU.png" alt="Logo Trường Đại học Văn Hiến" class="brand-logo-img">
        <div class="brand-title-box">
          <span class="brand-main-title">TRƯỜNG ĐẠI HỌC VĂN HIẾN</span>
          <span class="brand-sub-title">CHẠM MỘT SẮC SEN • ĐỒNG THÁP 2027</span>
        </div>
      </a>

      <!-- Desktop Navigation -->
      <nav class="desktop-nav" aria-label="Điều hướng trang">
        <a href="#overview" class="nav-link active">Tổng quan</a>
        <a href="#agenda" class="nav-link">Kịch bản</a>
        <a href="#media-plan" class="nav-link">Truyền thông</a>
        <a href="#risks-kpi" class="nav-link">Rủi ro & KPI</a>
        <a href="#budget" class="nav-link">Ngân sách</a>
        <a href="#creative" class="nav-link">Ấn phẩm</a>
        <a href="#appendices" class="nav-link">Hồ sơ pháp lý</a>
      </nav>

      <div class="nav-actions">
        <a href="#register-contact" class="btn-header-cta">
          {icon('ticket', 'v-icon-sm')} Nhận vé tham dự
        </a>
        <button class="mobile-menu-toggle" aria-label="Mở thực đơn điều hướng" aria-expanded="false">
          <svg class="v-icon v-icon-lg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Drawer -->
    <div class="mobile-nav-drawer">
      <a href="#overview" class="nav-link">Tổng quan sự kiện</a>
      <a href="#agenda" class="nav-link">Kịch bản chương trình</a>
      <a href="#media-plan" class="nav-link">Kế hoạch truyền thông</a>
      <a href="#risks-kpi" class="nav-link">Quản trị rủi ro & KPI</a>
      <a href="#budget" class="nav-link">Dự trù kinh phí & Tài trợ</a>
      <a href="#creative" class="nav-link">Thiết kế & Ấn phẩm</a>
      <a href="#appendices" class="nav-link">Hồ sơ pháp lý & 5 Phụ lục</a>
      <a href="#register-contact" class="nav-link" style="color: var(--sen-pink); font-weight: 800;">{icon('ticket', 'v-icon-sm')} Đăng ký vé tham dự</a>
    </div>
  </header>

  <!-- Hero Banner (Expansive Widescreen 2-Column Split Layout) -->
  <section class="hero-banner">
    <div class="container">
      <div class="hero-widescreen-grid">
        <!-- Left Column: Primary Typography, Badges, Metadata, Key Stats & CTAs -->
        <div class="hero-main-col">
          <div class="hero-pill-badge">
            <span class="badge-dot"></span> TRƯỜNG ĐẠI HỌC VĂN HIẾN • KẾ HOẠCH NĂM 2027
          </div>

          <h1 class="hero-main-title">KẾ HOẠCH CHƯƠNG TRÌNH VĂN HOÁ &amp; NGHỆ THUẬT TỈNH ĐỒNG THÁP NĂM 2027</h1>
          <div class="hero-theme-title">CHỦ ĐỀ: CHẠM MỘT SẮC SEN</div>

          <p class="hero-lead-desc">
            Đề án tổng thể chuỗi hoạt động giao lưu văn hóa, trình diễn nghệ thuật dân tộc Nam Bộ và tôn vinh di sản Đồng Tháp Mười trong không gian học đường hiện đại tại cơ sở HungHau Campus.
          </p>

          <!-- Meta Bar -->
          <div class="hero-meta-bar">
            <div class="hero-meta-item">
              <span>{icon('clock', 'v-icon-sm v-icon-gold')} <strong>Thời gian:</strong> 07:30, Chủ Nhật - Ngày 20/06/2027</span>
            </div>
            <div class="hero-meta-item">
              <span>{icon('map-pin', 'v-icon-sm v-icon-gold')} <strong>Địa điểm:</strong> Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus</span>
            </div>
            <div class="hero-meta-item">
              <span>{icon('graduation-cap', 'v-icon-sm v-icon-gold')} <strong>Đơn vị thực hiện:</strong> Trường Đại học Văn Hiến</span>
            </div>
          </div>

          <!-- Highlight metrics row -->
          <div class="hero-quick-highlights">
            <div class="hero-highlight-pill">
              <span class="pill-number">500+</span>
              <span class="pill-text">Khán giả &amp; Khách mời</span>
            </div>
            <div class="hero-highlight-pill">
              <span class="pill-number">08</span>
              <span class="pill-text">Tiết mục nghệ thuật</span>
            </div>
            <div class="hero-highlight-pill">
              <span class="pill-number">30+</span>
              <span class="pill-text">Gian hàng trải nghiệm</span>
            </div>
            <div class="hero-highlight-pill">
              <span class="pill-number">05</span>
              <span class="pill-text">Bộ phụ lục hồ sơ</span>
            </div>
          </div>

          <!-- Balanced Responsive Button Matrix -->
          <div class="hero-cta-group">
            <a href="#register-contact" class="btn-hero btn-pink">
              {icon('ticket', 'v-icon-sm')} Đăng ký vé miễn phí
            </a>
            <a href="#agenda" class="btn-hero btn-gold">
              {icon('clipboard-list', 'v-icon-sm')} Xem kịch bản chương trình
            </a>
            <a href="#budget" class="btn-hero btn-glass">
              {icon('wallet', 'v-icon-sm')} Tra cứu ngân sách &amp; Tài trợ
            </a>
            <a href="#appendices" class="btn-hero btn-glass">
              {icon('file-text', 'v-icon-sm')} Toàn văn Hồ sơ &amp; Phụ lục
            </a>
          </div>
        </div>

        <!-- Right Column: Countdown Box & Stage Showcase Card -->
        <div class="hero-visual-col">
          <!-- Countdown Box -->
          <div class="countdown-container">
            <div class="countdown-header-flex">
              <span class="countdown-live-badge"><span class="pulse-ring"></span> TRỰC TIẾP ĐẾM NGƯỢC</span>
              <span class="countdown-title">NGÀY HỘI VĂN HÓA ĐỒNG THÁP 2027</span>
            </div>
            <div class="countdown-grid">
              <div class="countdown-box">
                <div class="countdown-num" id="days">00</div>
                <div class="countdown-label">Ngày</div>
              </div>
              <div class="countdown-box">
                <div class="countdown-num" id="hours">00</div>
                <div class="countdown-label">Giờ</div>
              </div>
              <div class="countdown-box">
                <div class="countdown-num" id="mins">00</div>
                <div class="countdown-label">Phút</div>
              </div>
              <div class="countdown-box">
                <div class="countdown-num" id="secs">00</div>
                <div class="countdown-label">Giây</div>
              </div>
            </div>
          </div>

          <!-- Dedicated Key Visual Showcase Card -->
          <div class="hero-visual-card">
            <div class="visual-badge-overlay">{icon('lotus', 'v-icon-sm')} Phối cảnh sân khấu chính thức tại Hội trường Trần Hưng Đạo</div>
            <img src="./assets/images/nen-chinh.png" alt="Phối cảnh sân khấu chính thức Chạm một sắc Sen" class="hero-stage-img" data-lightbox data-src="./assets/images/nen-chinh.png" data-title="Phối cảnh sân khấu chính thức" data-caption="Background sân khấu chính màn hình LED Hội trường Trần Hưng Đạo, HungHau Campus">
            <div class="stage-specs-grid">
              <div class="spec-item">
                <span class="spec-label">Quy mô địa điểm</span>
                <span class="spec-val">Hội trường Tầng 9 (800 chỗ)</span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Thời lượng chính</span>
                <span class="spec-val">07:30 - 11:30 (4 tiếng)</span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Khách mời ngôi sao</span>
                <span class="spec-val highlight-gold">Ca sĩ Phương Mỹ Chi</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Stats Ribbon (Spanning full width under the 2-column grid) -->
      <div class="hero-stats-ribbon">
        <div class="hero-stat-card">
          <div class="stat-icon-wrapper">{icon('users', 'v-icon-lg')}</div>
          <div class="stat-value">300+</div>
          <div class="stat-label">Khán giả &amp; Khách mời trực tiếp tại Hội trường</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon-wrapper">{icon('megaphone', 'v-icon-lg')}</div>
          <div class="stat-value">≥ 100.000</div>
          <div class="stat-label">Lượt tiếp cận trên toàn bộ chiến dịch truyền thông</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon-wrapper">{icon('award', 'v-icon-lg')}</div>
          <div class="stat-value">305 Triệu</div>
          <div class="stat-label">Tổng nguồn tài chính tài trợ vận động được</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon-wrapper">{icon('heart', 'v-icon-lg')}</div>
          <div class="stat-value">100% Lợi Nhuận</div>
          <div class="stat-label">Quyên góp TT Bảo trợ Xã hội Đồng Tháp (200,9 Triệu)</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 1: OVERVIEW & 7 OBJECTIVES -->
  <section id="overview" class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">{icon('file-text', 'v-icon-sm')} I. THÔNG TIN SỰ KIỆN & MỤC TIÊU</span>
        <h2 class="section-title">Khái Quát Chương Trình & Tôn Chỉ Nhân Văn</h2>
        <p class="section-desc">Chương trình Văn hoá & Nghệ thuật tỉnh Đồng Tháp năm 2027 là sự kiện văn hóa học đường trọng điểm của Đại học Văn Hiến, kết hợp hài hòa tri thức, văn hóa dân tộc và trách nhiệm phụng sự cộng đồng.</p>
      </div>

      <div class="overview-grid">
        <!-- Event Profile Card -->
        <div class="event-profile-card">
          <h3 class="profile-title">{icon('building', 'v-icon-blue')} Thông Tin Sự Kiện Chính Thức</h3>
          <div class="profile-meta-list">
            <div class="meta-row">
              <div class="meta-icon-box">{icon('tag', 'v-icon-sm')}</div>
              <div>
                <div class="meta-label">Tên chương trình</div>
                <div class="meta-value">Chương trình Văn hoá & Nghệ thuật tỉnh Đồng Tháp năm 2027</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box pink">{icon('lotus', 'v-icon-sm')}</div>
              <div>
                <div class="meta-label">Chủ đề chính thức</div>
                <div class="meta-value" style="color: var(--sen-pink); font-weight: 800;">Chạm một sắc Sen</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box">{icon('calendar', 'v-icon-sm')}</div>
              <div>
                <div class="meta-label">Thời gian tổ chức</div>
                <div class="meta-value">07:30, Chủ Nhật - Ngày 20 tháng 06 năm 2027</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box gold">{icon('map-pin', 'v-icon-sm')}</div>
              <div>
                <div class="meta-label">Địa điểm tổ chức</div>
                <div class="meta-value">Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus, Khu chức năng số 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box">{icon('graduation-cap', 'v-icon-sm')}</div>
              <div>
                <div class="meta-label">Đơn vị thực hiện</div>
                <div class="meta-value">Trường Đại học Văn Hiến (Ban Tổ chức Sự kiện)</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box pink">{icon('sparkles', 'v-icon-sm')}</div>
              <div>
                <div class="meta-label">Tông màu nhận diện</div>
                <div class="meta-value">Hồng Sen Đồng Tháp, Xanh lá Sen & Xanh dương - Vàng Ánh Kim (Đại học Văn Hiến)</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 7 Core Objectives -->
        <div class="objectives-container">
          <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--vhu-navy-base); margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
            {icon('award', 'v-icon-gold')} 07 Mục Tiêu Chiến Lược Cốt Lõi
          </h3>
          
          <div class="objective-item">
            <div class="obj-number">1</div>
            <div class="obj-content">
              <h4>Gắn kết tri thức với văn hóa dân tộc</h4>
              <p>Xây dựng hình ảnh Đại học Văn Hiến là môi trường giáo dục gắn kết tri thức với văn hóa dân tộc, chủ động kết nối và lan tỏa các giá trị văn hóa tỉnh Đồng Tháp.</p>
            </div>
          </div>

          <div class="objective-item">
            <div class="obj-number">2</div>
            <div class="obj-content">
              <h4>Không gian giao lưu doanh nghiệp & sinh viên</h4>
              <p>Tạo không gian giao lưu giữa các nhà tài trợ, doanh nghiệp, giảng viên, sinh viên thông qua các hoạt động biểu diễn văn hoá - nghệ thuật.</p>
            </div>
          </div>

          <div class="objective-item">
            <div class="obj-number">3</div>
            <div class="obj-content">
              <h4>Bảo tồn & phát huy di sản theo phong cách trẻ</h4>
              <p>Kết nối văn hóa Đồng Tháp với thế hệ trẻ, khuyến khích sinh viên tiếp cận, trân trọng và góp phần gìn giữ, phát huy các giá trị văn hóa truyền thống theo hình thức hiện đại, phù hợp với giới trẻ.</p>
            </div>
          </div>

          <div class="objective-item">
            <div class="obj-number">4</div>
            <div class="obj-content">
              <h4>Tăng cường hợp tác chiến lược đa phương</h4>
              <p>Tăng cường sự hợp tác giữa nhà trường với các doanh nghiệp, các đơn vị truyền thông và các cơ quan quản lý văn hóa.</p>
            </div>
          </div>

          <div class="objective-item">
            <div class="obj-number">5</div>
            <div class="obj-content">
              <h4>Giao lưu truyền cảm hứng cùng Chủ tịch Hùng Hậu</h4>
              <p>Tạo cơ hội để sinh viên giao lưu và kết nối với Chủ tịch Tập đoàn Hùng Hậu gắn với hình ảnh gần gũi, qua đó truyền cảm hứng, chia sẻ kinh nghiệm thực tiễn và định hướng phát triển cho thế hệ trẻ.</p>
            </div>
          </div>

          <div class="objective-item">
            <div class="obj-number">6</div>
            <div class="obj-content">
              <h4>Mục tiêu nhân văn: 100% Lợi nhuận làm từ thiện</h4>
              <p>Quyên góp toàn bộ lợi nhuận sau sự kiện cho Trung tâm Bảo trợ xã hội Tổng hợp tỉnh Đồng Tháp, bảo đảm minh bạch và nhân văn.</p>
            </div>
          </div>

          <div class="objective-item">
            <div class="obj-number">7</div>
            <div class="obj-content">
              <h4>Độ phủ truyền thông rộng khắp</h4>
              <p>Đạt chỉ số tiếp cận ≥ 100.000 người trên toàn bộ chiến dịch truyền thông đa kênh (mạng xã hội, báo chí và truyền hình).</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Featured Guests Ribbon -->
      <div class="featured-guests-banner">
        <div class="guests-info">
          <h3>{icon('sparkles', 'v-icon-gold')} Khách Mời Đặc Biệt & Nghệ Sĩ Đồng Hành</h3>
          <p>Chương trình quy tụ dàn khách mời danh dự, nghệ sĩ tên tuổi và các chuyên gia văn hóa hàng đầu, mang đến những phần trình diễn nghệ thuật thăng hoa và những câu chuyện truyền cảm hứng sâu sắc.</p>
          <div class="guest-tags-cloud">
            <span class="guest-tag"><span class="tag-bullet"></span> Ca sĩ Phương Mỹ Chi</span>
            <span class="guest-tag"><span class="tag-bullet"></span> Hoa hậu Nguyễn Thị Yến Nhi</span>
            <span class="guest-tag"><span class="tag-bullet"></span> Á hậu Lê Phan Hạnh Nguyên</span>
            <span class="guest-tag"><span class="tag-bullet"></span> Ông Trần Văn Hậu (Chủ tịch HĐQT Hùng Hậu)</span>
            <span class="guest-tag"><span class="tag-bullet"></span> NTK Nguyễn Minh Công (BST "Miệt Cù Lao")</span>
            <span class="guest-tag"><span class="tag-bullet"></span> Nghệ nhân Đờn ca tài tử Nam Bộ</span>
            <span class="guest-tag"><span class="tag-bullet"></span> PGS.TS Nguyễn Minh Đức (ĐH Văn Hiến)</span>
            <span class="guest-tag"><span class="tag-bullet"></span> Đại biểu Tỉnh Đồng Tháp</span>
          </div>
        </div>
        <div class="guests-banner-img" data-lightbox data-src="./assets/images/khach-moi.png" data-title="Poster Khách mời & Nghệ sĩ" data-caption="Khách mời danh dự và nghệ sĩ tham gia chương trình 'Chạm một sắc Sen'">
          <img src="./assets/images/khach-moi.png" alt="Khách mời chương trình Chạm một sắc Sen">
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: AGENDA TIMELINE -->
  <section id="agenda" class="section bg-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-pink">{icon('clock', 'v-icon-sm')} II. NỘI DUNG CHƯƠNG TRÌNH</span>
        <h2 class="section-title">Kịch Bản Chi Tiết & Dòng Thời Gian Sự Kiện</h2>
        <p class="section-desc">Toàn bộ 11 hoạt động diễn ra từ 07:30 đến 11:10 ngày 20/06/2027 tại Hội trường Trần Hưng Đạo (Tầng 9, HungHau Campus).</p>
      </div>

      <!-- Filters -->
      <div class="agenda-controls">
        <button class="filter-btn active" data-filter="all">Tất cả hoạt động</button>
        <button class="filter-btn" data-filter="opening">Khai mạc & Check-in</button>
        <button class="filter-btn" data-filter="art">Nghệ thuật & Âm nhạc</button>
        <button class="filter-btn" data-filter="talk">Giao lưu & Q&A</button>
        <button class="filter-btn" data-filter="fashion">Fashion Show</button>
        <button class="filter-btn" data-filter="closing">Tổng kết & Bế mạc</button>
      </div>

      <!-- Timeline Stream -->
      <div class="timeline-stream">
        {agenda_str}
      </div>
    </div>
  </section>

  <!-- SECTION 3: MEDIA PLAN -->
  <section id="media-plan" class="section">
    <div class="container tab-wrapper">
      <div class="section-header">
        <span class="section-tag tag-gold">{icon('megaphone', 'v-icon-sm')} III. KẾ HOẠCH TRUYỀN THÔNG</span>
        <h2 class="section-title">Chiến Lược Lan Tỏa Đa Kênh Trong 3 Giai Đoạn</h2>
        <p class="section-desc">Kế hoạch truyền thông bài bản trước, trong và sau sự kiện trên hệ thống Fanpage, TikTok VHU, đối tác công nghệ Orbis ICT, Báo Pháp Luật Việt Nam và Đài PT-TH Đồng Tháp.</p>
      </div>

      <!-- Media Objectives Card -->
      <div class="content-card" style="margin-bottom: 28px; border-left: 4px solid var(--vhu-blue-primary);">
        <h4 style="font-size: 1.1rem; color: var(--vhu-navy-base); margin-bottom: 12px; font-weight: 800; display: flex; align-items: center; gap: 8px;">
          {icon('award', 'v-icon-blue')} 07 Mục Tiêu Truyền Thông Cụ Thể
        </h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; font-size: 0.88rem;">
          <div style="display: flex; gap: 6px;">{icon('check-circle', 'v-icon-sm v-icon-blue')} <span>Gia tăng nhận diện ĐH Văn Hiến thông qua chương trình “Chạm một sắc Sen”.</span></div>
          <div style="display: flex; gap: 6px;">{icon('check-circle', 'v-icon-sm v-icon-blue')} <span>Tôn vinh và lan tỏa tinh thần khát vọng, nỗ lực vươn lên của Chủ tịch Tập đoàn Hùng Hậu.</span></div>
          <div style="display: flex; gap: 6px;">{icon('check-circle', 'v-icon-sm v-icon-blue')} <span>Lan tỏa thông điệp thiện nguyện và bảo đảm minh bạch tuyệt đối cho công tác quyên góp.</span></div>
          <div style="display: flex; gap: 6px;">{icon('check-circle', 'v-icon-sm v-icon-blue')} <span>Tăng cường kết nối bền chặt giữa VHU với doanh nghiệp, nhà tài trợ và báo chí.</span></div>
          <div style="display: flex; gap: 6px;">{icon('check-circle', 'v-icon-sm v-icon-blue')} <span>Khuyến khích người tham gia sáng tạo nội dung chia sẻ kèm hashtag #ChamMotSacSen.</span></div>
          <div style="display: flex; gap: 6px;">{icon('check-circle', 'v-icon-sm v-icon-blue')} <span>Thư cảm ơn và quà tặng 100% gửi đến VIP & người tham dự trong 3 ngày sau sự kiện.</span></div>
          <div style="display: flex; gap: 6px;">{icon('check-circle', 'v-icon-sm v-icon-blue')} <span>Bảo đảm ít nhất 80% số khách mời xác nhận tham dự thông qua hệ thống vé QR code.</span></div>
        </div>
      </div>

      <!-- Tabs Header -->
      <div class="tabs-header" data-tab-group="media">
        <button class="tab-btn active" data-target="media-pre">3.3.1 Trước sự kiện (Tiền kỳ)</button>
        <button class="tab-btn" data-target="media-during">3.3.2 Trong sự kiện (20/06)</button>
        <button class="tab-btn" data-target="media-post">3.3.3 Sau sự kiện (Hậu kỳ)</button>
      </div>

      <div class="table-hint-bar">{icon('chevron-right', 'v-icon-sm')} Vuốt ngang để xem toàn bộ bảng số liệu</div>

      <!-- Tab 1: Pre-event -->
      <div class="tab-panel active" id="media-pre" data-tab-group="media">
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>STT</th>
                <th>Hoạt động truyền thông</th>
                <th>Mục tiêu</th>
                <th>Nội dung triển khai</th>
                <th>Kênh chính</th>
                <th>Thời gian</th>
                <th>Đơn vị phụ trách</th>
                <th>KPI cam kết</th>
              </tr>
            </thead>
            <tbody>
              {media_pre_str}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tab 2: During-event -->
      <div class="tab-panel" id="media-during" data-tab-group="media">
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>STT</th>
                <th>Hoạt động truyền thông</th>
                <th>Mục tiêu</th>
                <th>Nội dung triển khai</th>
                <th>Kênh chính</th>
                <th>Thời gian</th>
                <th>Đơn vị phụ trách</th>
              </tr>
            </thead>
            <tbody>
              {media_during_str}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tab 3: Post-event -->
      <div class="tab-panel" id="media-post" data-tab-group="media">
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Giai đoạn</th>
                <th>Thời gian</th>
                <th>Hoạt động</th>
                <th>Nội dung triển khai</th>
                <th>Kênh chính</th>
                <th>Phụ trách</th>
              </tr>
            </thead>
            <tbody>
              {media_post_str}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: RISK MANAGEMENT & KPIS -->
  <section id="risks-kpi" class="section bg-alt">
    <div class="container tab-wrapper">
      <div class="section-header">
        <span class="section-tag tag-pink">{icon('shield', 'v-icon-sm')} IV. QUẢN TRỊ RỦI RO & MA TRẬN KPI</span>
        <h2 class="section-title">Kế Hoạch Phòng Ngừa, Xử Lý Sự Cố & Đo Lường</h2>
        <p class="section-desc">Hệ thống quản trị rủi ro đa chiều từ khâu lập kế hoạch, vận hành thực địa đến truyền thông khủng hoảng và 29 chỉ số KPI đo lường định lượng toàn chiến dịch.</p>
      </div>

      <!-- Search & Filters -->
      <div class="search-filter-bar">
        <div class="search-input-box">
          <span>{icon('search', 'v-icon-sm')}</span>
          <input type="text" id="risk-search-input" placeholder="Tìm kiếm rủi ro, sự cố hoặc bộ phận phụ trách...">
        </div>
        <div>
          <label for="risk-severity-select" style="font-size: 0.82rem; font-weight: 700; margin-right: 6px;">Mức độ:</label>
          <select id="risk-severity-select" class="select-filter">
            <option value="all">Tất cả mức độ</option>
            <option value="Rất cao">Rất cao</option>
            <option value="Cao">Cao</option>
            <option value="Trung bình">Trung bình</option>
            <option value="Thấp">Thấp</option>
          </select>
        </div>
      </div>

      <!-- Tabs Header -->
      <div class="tabs-header" data-tab-group="risks">
        <button class="tab-btn active" data-target="risk-tab-plan">4.1 Rủi ro Kế hoạch</button>
        <button class="tab-btn" data-target="risk-tab-event">4.2 Rủi ro Sự kiện (Hiện trường)</button>
        <button class="tab-btn" data-target="risk-tab-media">4.3 Rủi ro Truyền thông (19 tình huống)</button>
        <button class="tab-btn" data-target="risk-tab-kpi">4.4 Tổng kết 29 KPI Truyền thông</button>
      </div>

      <div class="table-hint-bar">{icon('chevron-right', 'v-icon-sm')} Vuốt ngang để xem toàn bộ bảng số liệu</div>

      <!-- Tab 1: Plan Risks -->
      <div class="tab-panel active" id="risk-tab-plan" data-tab-group="risks">
        <div class="table-responsive">
          <table class="data-table risk-data-table">
            <thead>
              <tr>
                <th>Hạng mục</th>
                <th>Nhận diện Rủi ro & Bối cảnh</th>
                <th>Mức độ</th>
                <th>Phương án Phòng ngừa (Trước sự kiện)</th>
                <th>Phương án Xử lý & Kịch bản B (Khi xảy ra sự cố)</th>
                <th>Bộ phận Phụ trách</th>
              </tr>
            </thead>
            <tbody>
              {risk_plan_str}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tab 2: Event Risks -->
      <div class="tab-panel" id="risk-tab-event" data-tab-group="risks">
        <div class="table-responsive">
          <table class="data-table risk-data-table">
            <thead>
              <tr>
                <th>Phân loại</th>
                <th>Nhận diện Rủi ro & Bối cảnh</th>
                <th>Đánh giá</th>
                <th>Phương án Phòng ngừa (Trước sự kiện)</th>
                <th>Phương án Xử lý & Kịch bản B</th>
                <th>Bộ phận Phụ trách</th>
              </tr>
            </thead>
            <tbody>
              {risk_event_str}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tab 3: Media Risks -->
      <div class="tab-panel" id="risk-tab-media" data-tab-group="risks">
        <div class="table-responsive">
          <table class="data-table risk-data-table">
            <thead>
              <tr>
                <th>Phân nhóm</th>
                <th>Nhận diện Rủi ro</th>
                <th>Đánh giá</th>
                <th>Biện pháp phòng ngừa</th>
                <th>Phương án xử lý</th>
                <th>Phụ trách</th>
              </tr>
            </thead>
            <tbody>
              {risk_media_str}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tab 4: KPIs Matrix -->
      <div class="tab-panel" id="risk-tab-kpi" data-tab-group="risks">
        <div class="kpi-grid">
          {kpis_str}
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: BUDGET & SPONSORS -->
  <section id="budget" class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-gold">{icon('wallet', 'v-icon-sm')} V. DỰ TRÙ KINH PHÍ & NGUỒN TÀI TRỢ</span>
        <h2 class="section-title">Kế Hoạch Cân Đối Tài Chính & Quỹ Thiện Nguyện</h2>
        <p class="section-desc">Minh bạch ngân sách với 68 hạng mục chi tiết, cơ cấu nguồn tài trợ và cam kết trích toàn bộ lợi nhuận ủng hộ Trung tâm Bảo trợ Xã hội Tổng hợp tỉnh Đồng Tháp.</p>
      </div>

      <!-- 3 Master Finance Cards -->
      <div class="finance-overview-grid">
        <div class="finance-kpi-card card-income">
          <div class="card-finance-label">{icon('award', 'v-icon-sm')} Tổng Nguồn Thu Tài Trợ (5.2)</div>
          <div class="card-finance-value">305.000.000 đ</div>
          <div class="card-finance-note">Gồm Kim Cương (VHU 100tr), Vàng (100tr), Bạc (105tr) + Tài trợ hiện vật</div>
        </div>

        <div class="finance-kpi-card card-expense">
          <div class="card-finance-label">{icon('wallet', 'v-icon-sm')} Tổng Chi Phí Dự Toán (5.1)</div>
          <div class="card-finance-value">104.074.748 đ</div>
          <div class="card-finance-note">Chi trực tiếp: 94.613.408 đ + Dự phòng 10% (Đã gồm 8% VAT)</div>
        </div>

        <div class="finance-kpi-card card-charity">
          <div class="card-finance-label">{icon('heart', 'v-icon-sm')} Chênh Lệch Quỹ Thiện Nguyện (5.3)</div>
          <div class="card-finance-value">+ 200.925.252 đ</div>
          <div class="card-finance-note">100% Chuyển giao trao tặng TT Bảo trợ Xã hội Tổng hợp Tỉnh Đồng Tháp</div>
        </div>
      </div>

      <!-- Visual Budget Stacked Bar -->
      <div class="budget-visual-bar">
        <div class="budget-bar-title">
          <span>{icon('wallet', 'v-icon-sm')} Phân Bổ Tỷ Trọng Chi Phí 09 Nhóm Hạng Mục</span>
          <span style="font-size: 0.88rem; color: var(--vhu-blue-primary); font-weight: 700;">Tổng chi dự toán: 104.074.748 đ</span>
        </div>
        <div class="budget-stacked-bar">
          <div class="bar-segment" style="width: 17.1%; background: #153872;" title="Nhóm A (Địa điểm & Dàn dựng): 17.820.000 đ"></div>
          <div class="bar-segment" style="width: 6.2%; background: #244e96;" title="Nhóm C (Ấn phẩm): 6.447.608 đ"></div>
          <div class="bar-segment" style="width: 31.1%; background: #d49b19;" title="Nhóm D (Truyền thông & Báo chí): 32.400.000 đ"></div>
          <div class="bar-segment" style="width: 8.3%; background: #f7b731;" title="Nhóm E (Nghệ thuật & Biểu diễn): 8.640.000 đ"></div>
          <div class="bar-segment" style="width: 10.4%; background: #d83a6f;" title="Nhóm F (Khách mời & Nghệ sĩ): 10.800.000 đ"></div>
          <div class="bar-segment" style="width: 10.5%; background: #e8437d;" title="Nhóm G (Quà tặng & Tri ân): 10.918.800 đ"></div>
          <div class="bar-segment" style="width: 3.1%; background: #059669;" title="Nhóm H (Hậu cần, An ninh, Y tế): 3.240.000 đ"></div>
          <div class="bar-segment" style="width: 4.2%; background: #0284c7;" title="Nhóm I (Phục vụ & Lưu trú): 4.347.000 đ"></div>
          <div class="bar-segment" style="width: 9.1%; background: #64748b;" title="Nhóm K (Dự phòng 10%): 9.461.340 đ"></div>
        </div>

        <div class="budget-legend-grid">
          <div class="legend-item"><span class="legend-color-dot" style="background: #153872;"></span>Nhóm A: Dàn dựng (17,8M)</div>
          <div class="legend-item"><span class="legend-color-dot" style="background: #244e96;"></span>Nhóm C: Ấn phẩm (6,4M)</div>
          <div class="legend-item"><span class="legend-color-dot" style="background: #d49b19;"></span>Nhóm D: Truyền thông (32,4M)</div>
          <div class="legend-item"><span class="legend-color-dot" style="background: #f7b731;"></span>Nhóm E: Nghệ thuật (8,6M)</div>
          <div class="legend-item"><span class="legend-color-dot" style="background: #d83a6f;"></span>Nhóm F: Khách mời (10,8M)</div>
          <div class="legend-item"><span class="legend-color-dot" style="background: #e8437d;"></span>Nhóm G: Quà tặng (10,9M)</div>
          <div class="legend-item"><span class="legend-color-dot" style="background: #059669;"></span>Nhóm H: An ninh/Y tế (3,2M)</div>
          <div class="legend-item"><span class="legend-color-dot" style="background: #0284c7;"></span>Nhóm I: Phục vụ (4,3M)</div>
          <div class="legend-item"><span class="legend-color-dot" style="background: #64748b;"></span>Nhóm K: Dự phòng (9,4M)</div>
        </div>
      </div>

      <!-- Budget Detail Search & Table -->
      <div style="margin-bottom: 30px;">
        <div class="search-filter-bar">
          <div class="search-input-box">
            <span>{icon('search', 'v-icon-sm')}</span>
            <input type="text" id="budget-search-input" placeholder="Tìm tên hạng mục (vé, hoa, standee, khách sạn...)...">
          </div>
          <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
            <select id="budget-group-select" class="select-filter">
              <option value="all">Tất cả nhóm hạng mục (A - K)</option>
              <option value="A">Nhóm A: Địa điểm - Dàn dựng</option>
              <option value="B">Nhóm B: Âm thanh ánh sáng (0đ)</option>
              <option value="C">Nhóm C: Ấn phẩm</option>
              <option value="D">Nhóm D: Truyền thông & Báo chí</option>
              <option value="E">Nhóm E: Nghệ thuật sân khấu</option>
              <option value="F">Nhóm F: Khách mời - Nghệ sĩ</option>
              <option value="G">Nhóm G: Quà tặng & Kỷ niệm chương</option>
              <option value="H">Nhóm H: Hậu cần, An ninh, Y tế</option>
              <option value="I">Nhóm I: Phục vụ, Nước uống, Khách sạn</option>
            </select>
            <span class="badge badge-info" id="budget-visible-count">68 hạng mục</span>
          </div>
        </div>

        <div class="table-hint-bar">{icon('chevron-right', 'v-icon-sm')} Vuốt ngang để xem toàn bộ bảng số liệu</div>

        <div class="table-responsive" style="max-height: 520px; overflow-y: auto;">
          <table class="data-table budget-data-table">
            <thead style="position: sticky; top: 0; z-index: 5;">
              <tr>
                <th>Tên Hạng mục</th>
                <th style="text-align: center;">Số lượng</th>
                <th style="text-align: center;">Đơn vị</th>
                <th style="text-align: right;">Đơn giá (chưa VAT)</th>
                <th style="text-align: right;">Thành tiền (có VAT 8%)</th>
                <th>Ghi chú & Giải trình nguồn lực</th>
              </tr>
            </thead>
            <tbody>
              {budget_table_str}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Sponsorship Sources & Privileges Grid -->
      <div class="overview-grid" style="margin-top: 36px;">
        <!-- Sponsors Sources -->
        <div class="content-card">
          <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--vhu-navy-base); margin-bottom: 14px; display: flex; align-items: center; gap: 8px;">
            {icon('award', 'v-icon-gold')} Cơ Cấu Nguồn Thu Tài Trợ (5.2)
          </h4>
          <div class="table-responsive">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Nguồn tài chính</th>
                  <th style="text-align: center;">Số lượng</th>
                  <th style="text-align: right;">Giá trị (VNĐ)</th>
                  <th>Hình thức / Đơn vị</th>
                </tr>
              </thead>
              <tbody>
                {sponsors_table_str}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Balance summary -->
        <div class="content-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--vhu-navy-base); margin-bottom: 14px; display: flex; align-items: center; gap: 8px;">
              {icon('wallet', 'v-icon-blue')} Kế Hoạch Cân Đối Thu Chi (5.3)
            </h4>
            <div class="table-responsive" style="margin-bottom: 14px;">
              <table class="data-table" style="min-width: unset;">
                <tbody>
                  <tr>
                    <td><strong>Tổng thu dự kiến:</strong></td>
                    <td style="text-align: right; font-weight: 800; color: var(--vhu-blue-primary);">305.000.000 VNĐ</td>
                  </tr>
                  <tr>
                    <td><strong>Tổng chi phí dự toán:</strong></td>
                    <td style="text-align: right; font-weight: 800; color: var(--text-secondary);">104.074.748 VNĐ</td>
                  </tr>
                  <tr style="background: var(--sen-pink-soft);">
                    <td><strong style="color: var(--sen-pink);">Chênh lệch (Quỹ thiện nguyện):</strong></td>
                    <td style="text-align: right; font-weight: 900; color: var(--sen-pink); font-size: 1.1rem;">+ 200.925.252 VNĐ</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p style="font-size: 0.86rem; color: var(--text-secondary); line-height: 1.5;">
              Toàn bộ số tiền thặng dư <strong>200.925.252 VNĐ</strong> sẽ được trao tận tay Trung tâm Bảo trợ Xã hội Tổng hợp tỉnh Đồng Tháp dưới sự chứng kiến của các cơ quan ban ngành và đối tác tài trợ.
            </p>
          </div>
          <div style="margin-top: 14px;">
            <img src="./assets/images/nha-tai-tro.png" alt="Banner nhà tài trợ" style="border-radius: var(--radius-md); box-shadow: var(--shadow-sm); cursor: pointer;" data-lightbox data-src="./assets/images/nha-tai-tro.png" data-title="Key Visual Nhà Tài Trợ" data-caption="Bộ nhận diện tri ân các Nhà tài trợ đồng hành cùng chương trình">
          </div>
        </div>
      </div>

      <!-- Sponsor Privileges Matrix Table -->
      <div class="content-card" style="margin-top: 32px;">
        <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--vhu-navy-base); margin-bottom: 14px; display: flex; align-items: center; gap: 8px;">
          {icon('sparkles', 'v-icon-gold')} 5.4 Bảng Ma Trận Quyền Lợi Nhà Tài Trợ
        </h4>
        <div class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th>Hạng mục quyền lợi</th>
                <th class="privilege-tier-header diamond">Kim Cương (100 Triệu)</th>
                <th class="privilege-tier-header gold">Vàng (50 Triệu)</th>
                <th class="privilege-tier-header silver">Bạc (35 Triệu)</th>
                <th class="privilege-tier-header partner">Đồng hành (Hiện vật)</th>
              </tr>
            </thead>
            <tbody>
              {privileges_table_str}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 6: CREATIVE SHOWCASE & GALLERY -->
  <section id="creative" class="section bg-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-pink">{icon('sparkles', 'v-icon-sm')} X. THIẾT KẾ VÀ ẤN PHẨM TRUYỀN THÔNG</span>
        <h2 class="section-title">Hệ Thống Nhận Diện Hình Ảnh & Không Gian Sự Kiện</h2>
        <p class="section-desc">Bộ ấn phẩm truyền thông toàn diện gồm Poster, Backdrop, Mascot Bé Sen, Standee, Sơ đồ mặt bằng, Quà tặng và Nhạc độc quyền sự kiện.</p>
      </div>

      <!-- Gallery Grid -->
      <div class="gallery-grid">
        <!-- 1. Poster chính -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image1.png" data-title="H1. Poster chính thức sự kiện" data-caption="Poster quảng bá chính thức chương trình 'Chạm một sắc Sen' năm 2027">
            <img src="./assets/docx_media/image1.png" alt="Poster sự kiện Chạm một sắc Sen" loading="lazy">
            <span class="gallery-overlay-badge">H1. Poster</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Poster Quảng Bá Chính Thức</h4>
              <p class="gallery-item-caption">Thiết kế chủ đạo kết hợp đóa hoa sen Đồng Tháp và biểu tượng Khuê Văn Các Đại học Văn Hiến.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 2. Poster phiên bản 2 -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image2.png" data-title="H1. Poster phiên bản công bố khách mời" data-caption="Poster chi tiết các mốc hoạt động và công bố dàn nghệ sĩ">
            <img src="./assets/docx_media/image2.png" alt="Poster chi tiết sự kiện" loading="lazy">
            <span class="gallery-overlay-badge">H1. Poster Detail</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Poster Lịch Trình Chi Tiết</h4>
              <p class="gallery-item-caption">Thông tin các tiết mục Đờn ca tài tử, Fashion Show và ca sĩ khách mời Phương Mỹ Chi.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 3. Key Visual Nhà tài trợ -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image3.png" data-title="Key Visual Nhà tài trợ" data-caption="Visual vinh danh các nhà tài trợ Kim Cương, Vàng, Bạc và Đơn vị đồng hành">
            <img src="./assets/docx_media/image3.png" alt="Key visual nhà tài trợ" loading="lazy">
            <span class="gallery-overlay-badge">Nhà Tài Trợ</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Ấn Phẩm Tri Ân Nhà Tài Trợ</h4>
              <p class="gallery-item-caption">Vinh danh sự đóng góp của các doanh nghiệp, thương hiệu thời trang và đơn vị kỹ thuật.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 4. Background sân khấu chính -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image4.jpeg" data-title="H2. Background Sân khấu chính" data-caption="Màn hình LED chính tại Hội trường Trần Hưng Đạo">
            <img src="./assets/docx_media/image4.jpeg" alt="Background sân khấu chính" loading="lazy">
            <span class="gallery-overlay-badge">H2. Background LED</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Background Sân Khấu Chính</h4>
              <p class="gallery-item-caption">Đồ họa visual chuyển động trên màn hình LED lớn phục vụ các tiết mục nghệ thuật và Fashion Show.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 5. Backdrop sự kiện -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image5.jpeg" data-title="H4. Backdrop Check-in" data-caption="Backdrop chụp ảnh lưu niệm tại Sảnh Trống Đồng">
            <img src="./assets/docx_media/image5.jpeg" alt="Backdrop check-in" loading="lazy">
            <span class="gallery-overlay-badge">H4. Backdrop Sảnh</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Backdrop Chụp Ảnh Lưu Niệm</h4>
              <p class="gallery-item-caption">Khu vực đón tiếp đại biểu, hoa hậu và sinh viên check-in ghi dấu kỷ niệm ngày hội.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 6. Mascot VHU & Bé Sen -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image6.jpeg" data-title="H3. Mascot Sự kiện" data-caption="Mascot Bé Sen Đồng Tháp kết hợp cùng Mascot VHU">
            <img src="./assets/docx_media/image6.jpeg" alt="Mascot Bé Sen và VHU" loading="lazy">
            <span class="gallery-overlay-badge">H3. Mascot Bé Sen</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Mascot Bé Sen & Mascot VHU</h4>
              <p class="gallery-item-caption">Nhân vật biểu trưng tạo bầu không khí hào hứng, gần gũi cho sinh viên và khách tham quan.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 7. Standee sự kiện -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image7.jpeg" data-title="H5. Standee chỉ dẫn" data-caption="Hệ thống standee đặt tại các sảnh và lối lên thang máy Tầng 9">
            <img src="./assets/docx_media/image7.jpeg" alt="Standee chỉ dẫn" loading="lazy">
            <span class="gallery-overlay-badge">H5. Standee</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Hệ Thống Standee Phân Luồng</h4>
              <p class="gallery-item-caption">Hướng dẫn sinh viên và khách mời đến đúng vị trí bàn check-in, booth tài trợ và hội trường.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 8. Sơ đồ mặt bằng -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image8.jpeg" data-title="H6. Sơ đồ khu vực Sảnh Trống Đồng và Hội trường" data-caption="Sơ đồ bố trí gian hàng, sân khấu, lối thoát hiểm và bàn đón tiếp">
            <img src="./assets/docx_media/image8.jpeg" alt="Sơ đồ mặt bằng sảnh Trống Đồng và Hội trường" loading="lazy">
            <span class="gallery-overlay-badge">H6. Sơ Đồ Mặt Bằng</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Sơ Đồ Mặt Bằng Sảnh & Hội Trường</h4>
              <p class="gallery-item-caption">Bố trí 04 gian hàng nhà tài trợ, Góc Khát vọng VHU, trạm y tế và hành lang an toàn PCCC.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 9. Standee dọc -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image9.jpeg" data-title="H5. Standee dọc cổng Campus" data-caption="Standee dọc kích thước lớn đặt tại cổng vào HungHau Campus">
            <img src="./assets/docx_media/image9.jpeg" alt="Standee dọc cổng campus" loading="lazy">
            <span class="gallery-overlay-badge">H5. Standee Cổng</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Standee Cổng HungHau Campus</h4>
              <p class="gallery-item-caption">Định vị sự kiện ngay từ lối vào khuôn viên số 13E Đại lộ Nguyễn Văn Linh.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 10. Quà tặng sự kiện -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image10.png" data-title="H8. Quà tặng sự kiện" data-caption="Khăn bandana thiết kế độc quyền 50x50cm và kỷ niệm chương tri ân">
            <img src="./assets/docx_media/image10.png" alt="Quà tặng khăn bandana và kỷ niệm chương" loading="lazy">
            <span class="gallery-overlay-badge">H8. Quà Tặng</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Quà Tặng & Kỷ Niệm Chương</h4>
              <p class="gallery-item-caption">320 khăn bandana hoa sen cách điệu dành cho sinh viên và kỷ niệm chương vinh danh VIP.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 11. Thư mời & Thư cảm ơn -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image11.jpeg" data-title="H9. Thư mời & Thư cảm ơn" data-caption="Bộ ấn phẩm thư mời trang trọng gửi Đại biểu VIP và thư tri ân">
            <img src="./assets/docx_media/image11.jpeg" alt="Thư mời và thư cảm ơn sự kiện" loading="lazy">
            <span class="gallery-overlay-badge">H9. Thư Mời</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Thư Mời & Thư Tri Ân Trang Trọng</h4>
              <p class="gallery-item-caption">Thiết kế đồng bộ nhận diện thương hiệu Văn Hiến gửi các đại biểu tỉnh Đồng Tháp và doanh nghiệp.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>

        <!-- 12. Nhạc độc quyền QR -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image12.png" data-title="H9. Nhạc độc quyền sự kiện" data-caption="Mã QR và biểu tượng giai điệu chủ đề 'Chạm một sắc Sen'">
            <img src="./assets/docx_media/image12.png" alt="Mã QR nhạc độc quyền sự kiện" loading="lazy">
            <span class="gallery-overlay-badge">H9/H10. Âm Nhạc</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Nhạc Độc Quyền Sự Kiện</h4>
              <p class="gallery-item-caption">Bản nhạc chủ đề hòa trộn âm sắc đờn ca tài tử sông nước và nhịp điệu tuổi trẻ hiện đại.</p>
            </div>
            <div class="gallery-item-footer">
              <span>{icon('zoom-in', 'v-icon-sm')} Nhấn để xem phóng to</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Audio Box -->
      <div class="audio-card-box">
        <div class="audio-info-side">
          <img src="./assets/docx_media/image12.png" alt="QR Nhạc sự kiện" class="audio-qr-thumb">
          <div class="audio-meta">
            <h4>{icon('music', 'v-icon-gold')} Giai Điệu Chủ Đề: "Chạm Một Sắc Sen"</h4>
            <p>Hòa âm độc quyền: Kết hợp ngũ cung Nam Bộ, đờn kìm, đờn tranh và dàn nhạc hiện đại VHU</p>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 20px;">
          <div class="equalizer-wave">
            <div class="eq-bar" style="animation-play-state: paused;"></div>
            <div class="eq-bar" style="animation-play-state: paused;"></div>
            <div class="eq-bar" style="animation-play-state: paused;"></div>
            <div class="eq-bar" style="animation-play-state: paused;"></div>
            <div class="eq-bar" style="animation-play-state: paused;"></div>
            <div class="eq-bar" style="animation-play-state: paused;"></div>
          </div>
          <button class="btn-play-preview" id="btn-audio-toggle">
            {icon('play', 'v-icon-sm')} Nghe thử giai điệu
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 7: APPENDICES & OFFICIAL DOSSIER -->
  <section id="appendices" class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-gold">{icon('file-text', 'v-icon-sm')} HỒ SƠ PHÁP LÝ & PHỤ LỤC HÀNH CHÍNH</span>
        <h2 class="section-title">Văn Bản Pháp Lý & Tờ Trình Đề Án Chính Thức</h2>
        <p class="section-desc">Bộ 05 văn bản hành chính đầy đủ theo chuẩn thể thức quản lý nhà nước: Tờ trình Ban Giám hiệu, Đơn xin cơ sở vật chất, Thỏa thuận tài trợ thời trang, Công văn gửi Sở VHTT TP.HCM và Công văn phối hợp ANTT địa phương.</p>
      </div>

      <!-- Appendix Nav Pills -->
      <div class="appendix-nav-pill-group">
        <button class="app-pill-btn active" data-target="app1-doc">{icon('file-text', 'v-icon-sm')} Phụ lục 1: Tờ trình Ban Giám hiệu</button>
        <button class="app-pill-btn" data-target="app2-doc">{icon('building', 'v-icon-sm')} Phụ lục 2: Đơn xin sử dụng địa điểm</button>
        <button class="app-pill-btn" data-target="app3-doc">{icon('award', 'v-icon-sm')} Phụ lục 3: Thỏa thuận BST "Miệt Cù Lao"</button>
        <button class="app-pill-btn" data-target="app4-doc">{icon('building', 'v-icon-sm')} Phụ lục 4: Công văn gửi Sở VHTT TP.HCM</button>
        <button class="app-pill-btn" data-target="app5-doc">{icon('shield', 'v-icon-sm')} Phụ lục 5: Công văn ANTT, PCCC & ATGT</button>
      </div>

      <!-- Document Containers -->
      <div class="appendix-content-area">
        {apps['app1']}
        {apps['app2']}
        {apps['app3']}
        {apps['app4']}
        {apps['app5']}
      </div>
    </div>
  </section>

  <!-- SECTION 8: REGISTRATION & CONTACT -->
  <section id="register-contact" class="section bg-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-pink">{icon('ticket', 'v-icon-sm')} ĐĂNG KÝ & LIÊN HỆ BAN TỔ CHỨC</span>
        <h2 class="section-title">Nhận Vé Mời "Passport Sen" & Kết Nối Đồng Hành</h2>
        <p class="section-desc">Số lượng có hạn (300 chỗ ngồi miễn phí dành cho sinh viên và đại biểu khách mời). Đăng ký ngay để nhận vé điện tử kèm mã QR check-in cá nhân.</p>
      </div>

      <div class="reg-contact-grid">
        <!-- Registration Form Card -->
        <div class="ticket-form-card">
          <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--vhu-navy-base); margin-bottom: 18px; display: flex; align-items: center; gap: 8px;">
            {icon('ticket', 'v-icon-pink')} Cổng Đăng Ký Vé Trực Tuyến
          </h3>
          <form id="ticket-reg-form">
            <div class="form-group">
              <label for="reg-fullname" class="form-label">Họ và tên người tham dự *</label>
              <input type="text" id="reg-fullname" class="form-control" placeholder="Ví dụ: Nguyễn Văn A" required>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label for="reg-mssv" class="form-label">Mã số sinh viên (MSSV) *</label>
                <input type="text" id="reg-mssv" class="form-control" placeholder="Ví dụ: 241A010999" required>
              </div>
              <div class="form-group">
                <label for="reg-faculty" class="form-label">Khoa / Đơn vị *</label>
                <select id="reg-faculty" class="form-control" required>
                  <option value="Khoa Nghệ thuật & Thời trang">Khoa Nghệ thuật & Thời trang</option>
                  <option value="Khoa Du lịch">Khoa Du lịch</option>
                  <option value="Khoa Kinh tế - Quản trị">Khoa Kinh tế - Quản trị</option>
                  <option value="Khoa KHXH & Nhân văn">Khoa KHXH & Nhân văn</option>
                  <option value="Khoa CNTT - Viễn thông">Khoa CNTT - Viễn thông</option>
                  <option value="Đại biểu / Khách mời Doanh nghiệp">Đại biểu / Khách mời Doanh nghiệp</option>
                  <option value="Khoa khác thuộc VHU">Khoa khác thuộc VHU</option>
                </select>
              </div>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label for="reg-email" class="form-label">Địa chỉ Email *</label>
                <input type="email" id="reg-email" class="form-control" placeholder="email@vhu.edu.vn" required>
              </div>
              <div class="form-group">
                <label for="reg-phone" class="form-label">Số điện thoại liên lạc *</label>
                <input type="tel" id="reg-phone" class="form-control" placeholder="090xxxxxxx" required>
              </div>
            </div>
            <div class="form-group">
              <label class="form-label">Quyền lợi nhận được khi tham dự:</label>
              <div style="font-size: 0.84rem; color: var(--text-secondary); background: #f1f5f9; padding: 12px 14px; border-radius: var(--radius-md); line-height: 1.5;">
                <div style="display: flex; gap: 6px; margin-bottom: 4px;">{icon('check', 'v-icon-sm v-icon-pink')} <span>01 Cuốn Passport Sen check-in các gian hàng tài trợ</span></div>
                <div style="display: flex; gap: 6px; margin-bottom: 4px;">{icon('check', 'v-icon-sm v-icon-pink')} <span>01 Khăn bandana hoa sen 50x50cm độc quyền sự kiện</span></div>
                <div style="display: flex; gap: 6px;">{icon('check', 'v-icon-sm v-icon-pink')} <span>Giao lưu trực tiếp cùng Chủ tịch Hùng Hậu & Ca sĩ Phương Mỹ Chi, 2 Hoa hậu</span></div>
              </div>
            </div>
            <button type="submit" class="btn-hero btn-gold" style="width: 100%; justify-content: center; margin-top: 8px;">
              {icon('sparkles', 'v-icon-sm')} Xác Nhận Đăng Ký & Tạo Vé QR Code
            </button>
          </form>
        </div>

        <!-- Official Contact Card -->
        <div class="contact-info-card">
          <h3>{icon('building', 'v-icon-gold')} Ban Tổ Chức Sự Kiện</h3>
          <p style="font-size: 0.88rem; color: #e2e8f0; margin-bottom: 22px;">Trường Đại học Văn Hiến trân trọng kính mời Quý Doanh nghiệp, Đối tác truyền thông và các bạn sinh viên cùng tham gia kiến tạo một ngày hội văn hóa ý nghĩa.</p>

          <div class="contact-item-row">
            <div class="contact-icon">{icon('user', 'v-icon-sm')}</div>
            <div>
              <div style="font-size: 0.76rem; text-transform: uppercase; color: var(--vhu-gold-light); font-weight: 700;">Đại diện Ban Tổ chức</div>
              <div style="font-size: 1rem; font-weight: 800;">Bà Trần Thúy Quyên</div>
              <div style="font-size: 0.82rem; opacity: 0.9;">Trưởng Ban Tổ chức Ngày hội</div>
            </div>
          </div>

          <div class="contact-item-row">
            <div class="contact-icon">{icon('phone', 'v-icon-sm')}</div>
            <div>
              <div style="font-size: 0.76rem; text-transform: uppercase; color: var(--vhu-gold-light); font-weight: 700;">Điện thoại liên hệ</div>
              <div style="font-size: 1rem; font-weight: 800;">0369.449.925</div>
              <div style="font-size: 0.82rem; opacity: 0.9;">Hỗ trợ thông tin tài trợ & báo chí</div>
            </div>
          </div>

          <div class="contact-item-row">
            <div class="contact-icon">{icon('map-pin', 'v-icon-sm')}</div>
            <div>
              <div style="font-size: 0.76rem; text-transform: uppercase; color: var(--vhu-gold-light); font-weight: 700;">Địa điểm diễn ra sự kiện</div>
              <div style="font-size: 0.92rem; font-weight: 700; line-height: 1.4;">Tầng 9, Hội trường Trần Hưng Đạo & Sảnh Trống Đồng, HungHau Campus</div>
              <div style="font-size: 0.82rem; opacity: 0.9;">Khu chức năng số 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM</div>
            </div>
          </div>

          <div class="charity-notice-box">
            <h5>{icon('heart', 'v-icon-pink')} Đơn Vị Thụ Hưởng Thiện Nguyện</h5>
            <p><strong>Trung tâm Bảo trợ Xã hội Tổng hợp tỉnh Đồng Tháp</strong><br>
            Toàn bộ thặng dư tài chính sau sự kiện (+200.925.252 đ) sẽ được trao tặng trực tiếp để hỗ trợ chăm lo người già neo đơn, trẻ em có hoàn cảnh đặc biệt khó khăn tại quê hương Đất Sen Hồng.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- LIGHTBOX DIALOG -->
  <dialog id="image-lightbox-dialog" aria-labelledby="modal-title">
    <div class="modal-inner">
      <div class="modal-header-bar">
        <h4 id="modal-title" class="modal-title-text">{icon('zoom-in', 'v-icon-sm')} Chi tiết ấn phẩm</h4>
        <button class="modal-close-btn" aria-label="Đóng">&times;</button>
      </div>
      <div class="modal-body-content">
        <img src="" alt="Hình ảnh phóng to" class="modal-preview-img">
        <p class="modal-caption-text"></p>
      </div>
    </div>
  </dialog>

  <!-- TICKET RESULT DIALOG -->
  <dialog id="ticket-result-dialog" aria-labelledby="ticket-modal-title">
    <div class="modal-inner" style="max-width: 500px;">
      <div class="modal-header-bar" style="background: var(--vhu-navy-dark);">
        <h4 id="ticket-modal-title">{icon('ticket', 'v-icon-gold')} Vé Mời Điện Tử - Passport Sen</h4>
        <button class="modal-close-btn ticket-close-btn" aria-label="Đóng">&times;</button>
      </div>
      <div class="modal-body-content">
        <div class="passport-sen-card">
          <div class="passport-sen-header">
            <div>
              <div style="font-size: 0.72rem; text-transform: uppercase; color: var(--vhu-gold-light); font-weight: 800;">ĐẠI HỌC VĂN HIẾN • HUNGHAU HOLDINGS</div>
              <div style="font-size: 1.1rem; font-weight: 900; color: #fff;">CHẠM MỘT SẮC SEN 2027</div>
            </div>
            <img src="./assets/images/logo-VHU.png" alt="Logo VHU" style="height: 38px; width: auto; background: #fff; padding: 2px; border-radius: 4px;">
          </div>

          <div style="text-align: center;">
            <img src="./assets/docx_media/image12.png" alt="QR Code" class="passport-qr-code">
            <div style="font-size: 1.15rem; font-weight: 900; letter-spacing: 0.1em; color: var(--vhu-gold-light); margin-bottom: 12px;" id="ticket-display-code">VHU-SEN-886699</div>
          </div>

          <div style="border-top: 1px dashed rgba(255,255,255,0.25); padding-top: 12px; font-size: 0.85rem; line-height: 1.6;">
            <div><strong>Khách mời:</strong> <span id="ticket-display-name">Nguyễn Văn A</span></div>
            <div><strong>MSSV / Mã định danh:</strong> <span id="ticket-display-mssv">241A010999</span></div>
            <div><strong>Khoa / Đơn vị:</strong> <span id="ticket-display-faculty">Khoa Du lịch</span></div>
            <div><strong>Thời gian:</strong> 07:30, Ngày 20/06/2027</div>
            <div><strong>Vị trí:</strong> Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus</div>
          </div>
        </div>

        <p style="margin-top: 14px; font-size: 0.82rem; color: var(--text-muted);">
          Vui lòng chụp màn hình hoặc lưu mã vé này để quét QR code tại bàn đón tiếp Tầng 9.
        </p>
      </div>
    </div>
  </dialog>

  <!-- Back to Top Button -->
  <button id="back-to-top-btn" class="back-to-top" aria-label="Lên đầu trang">
    {icon('arrow-up', 'v-icon-sm')}
  </button>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
            <img src="./assets/images/logo-VHU.png" alt="Logo VHU" style="height: 44px; width: auto; background: #fff; padding: 4px; border-radius: 6px;">
            <div>
              <h4 style="margin: 0;">TRƯỜNG ĐẠI HỌC VĂN HIẾN</h4>
              <div style="font-size: 0.76rem; color: #94a3b8;">VAN HIEN UNIVERSITY</div>
            </div>
          </div>
          <div class="footer-slogan">"THÀNH NHÂN TRƯỚC KHI THÀNH DANH"</div>
          <p style="font-size: 0.86rem; line-height: 1.6; color: #cbd5e1; max-width: 480px;">
            Chương trình Văn hoá & Nghệ thuật tỉnh Đồng Tháp năm 2027 - "Chạm một sắc Sen". Sự kiện văn hóa học đường kết hợp tri thức, bảo tồn di sản sông nước Nam Bộ và hoạt động thiện nguyện xã hội ý nghĩa.
          </p>
        </div>

        <div class="footer-col">
          <h5>Liên Kết Nhanh</h5>
          <ul class="footer-links">
            <li><a href="#overview">Tổng quan sự kiện</a></li>
            <li><a href="#agenda">Kịch bản chương trình</a></li>
            <li><a href="#media-plan">Kế hoạch truyền thông</a></li>
            <li><a href="#risks-kpi">Quản trị rủi ro & KPI</a></li>
            <li><a href="#budget">Dự trù kinh phí & Tài trợ</a></li>
            <li><a href="#creative">Bộ nhận diện thiết kế</a></li>
            <li><a href="#appendices">Hồ sơ pháp lý 5 Phụ lục</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>Đơn Vị Đồng Hành</h5>
          <ul class="footer-links">
            <li>Tập đoàn Hùng Hậu (HungHau Holdings)</li>
            <li>Tỉnh Đồng Tháp (Đơn vị kết nối văn hóa)</li>
            <li>NTK Nguyễn Minh Công (BST "Miệt Cù Lao")</li>
            <li>Trang phục biểu diễn DIVIT</li>
            <li>Công ty Công nghệ Orbis ICT</li>
            <li>Báo Pháp Luật Việt Nam</li>
            <li>Đài PT-TH Đồng Tháp</li>
            <li>TT Bảo trợ Xã hội Tổng hợp Đồng Tháp</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 2027 Trường Đại học Văn Hiến (VHU). Toàn bộ nội dung và ấn phẩm thuộc bản quyền của Ban Tổ chức Chương trình "Chạm một sắc Sen".</p>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="./data.js"></script>
  <script src="./script.js"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated clean, responsive index.html successfully!")
