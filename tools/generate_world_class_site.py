import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Ensure tools directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prepare_data import (
    icon, h, data, apps, agenda_str, media_pre_str, media_during_str, 
    media_post_str, risk_plan_str, risk_event_str, risk_media_str, 
    kpis_str, budget_table_str, sponsors_table_str, privileges_table_str
)

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kế hoạch Chương trình Văn hoá & Nghệ thuật Tỉnh Đồng Tháp 2027 | Chạm Một Sắc Sen - Đại học Văn Hiến</title>
  <meta name="description" content="Đề án Kế hoạch tổng thể tổ chức Chương trình Văn hoá & Nghệ thuật tỉnh Đồng Tháp năm 2027 chủ đề 'Chạm một sắc Sen' thực hiện bởi Trường Đại học Văn Hiến.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./styles.css">
  <link rel="icon" href="./assets/images/logo-VHU.png" type="image/png">
</head>
<body>

  <!-- Top Announcement Bar -->
  <aside class="top-announcement" aria-label="Thông báo sự kiện">
    <div class="container top-announcement-flex">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span class="announcement-badge">{icon('sparkles', 'v-icon-sm')} HỒ SƠ ĐỀ ÁN SỐ 104/QĐ-ĐHVH</span>
        <span>Kế hoạch Tổng thể &amp; Phương án Phối hợp Tổ chức Chương trình 2027</span>
      </div>
      <div class="top-contact-info">
        <span>{icon('map-pin', 'v-icon-sm')} HungHau Campus, 13E Nguyễn Văn Linh, Nam TP.HCM</span>
        <span>{icon('phone', 'v-icon-sm')} Hotline BTC: 0369.449.925</span>
      </div>
    </div>
  </aside>

  <!-- Sticky Header (Glassmorphic Deep Navy Integration) -->
  <header class="site-header" id="site-header">
    <div class="container nav-container">
      <a href="#" class="brand-wrapper" aria-label="Trang chủ Kế hoạch Chạm Một Sắc Sen">
        <img src="./assets/images/logo-VHU.png" alt="Logo Đại học Văn Hiến" class="brand-logo-img">
        <div class="brand-title-box">
          <span class="brand-main-title">TRƯỜNG ĐẠI HỌC VĂN HIẾN</span>
          <span class="brand-sub-title">THÀNH NHÂN TRƯỚC KHI THÀNH DANH</span>
        </div>
      </a>

      <!-- Desktop Navigation -->
      <nav class="desktop-nav" aria-label="Điều hướng chính">
        <a href="#overview" class="nav-link">Tổng quan</a>
        <a href="#artists" class="nav-link">Nghệ sĩ &amp; Di sản</a>
        <a href="#agenda" class="nav-link">Kịch bản</a>
        <a href="#media-plan" class="nav-link">Truyền thông</a>
        <a href="#risks-kpi" class="nav-link">Rủi ro &amp; KPI</a>
        <a href="#budget" class="nav-link">Ngân sách &amp; Tài trợ</a>
        <a href="#creative" class="nav-link">Ấn phẩm</a>
        <a href="#appendices" class="nav-link">Hồ sơ pháp lý</a>
      </nav>

      <div class="nav-actions">
        <a href="#register-contact" class="btn-header-cta">
          {icon('ticket', 'v-icon-sm')} Nhận vé VIP
        </a>
        <button id="mobile-menu-btn" class="mobile-menu-toggle" aria-label="Mở menu điều hướng">
          <svg class="v-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>
    </div>

    <!-- Reading Progress Bar -->
    <div id="reading-progress-bar" class="reading-progress-bar"></div>
  </header>

  <!-- Modern Mobile Backdrop & Slide-over Drawer (Top-level under body to escape stacking context) -->
  <div id="mobile-nav-backdrop" class="mobile-nav-backdrop" aria-hidden="true"></div>
  <div id="mobile-nav-drawer" class="mobile-nav-drawer" role="dialog" aria-modal="true" aria-label="Menu điều hướng sự kiện">
    <div class="mobile-drawer-header">
      <div class="mobile-drawer-brand">
        <img src="./assets/images/logo-VHU.png" alt="Logo Đại học Văn Hiến" class="mobile-drawer-logo">
        <div>
          <div style="font-size: 0.92rem; font-weight: 800; color: #ffffff;">ĐẠI HỌC VĂN HIẾN</div>
          <div style="font-size: 0.68rem; color: #fcd34d; letter-spacing: 0.04em; font-weight: 700;">THÀNH NHÂN TRƯỚC KHI THÀNH DANH</div>
        </div>
      </div>
      <button id="mobile-drawer-close" class="mobile-drawer-close" aria-label="Đóng menu">
        <svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>
    <div class="mobile-drawer-links">
      <a href="#overview" class="nav-link"><span>Tổng quan sự kiện</span><svg class="v-icon v-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
      <a href="#artists" class="nav-link"><span>Nghệ sĩ &amp; Di sản</span><svg class="v-icon v-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
      <a href="#agenda" class="nav-link"><span>Kịch bản chi tiết</span><svg class="v-icon v-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
      <a href="#media-plan" class="nav-link"><span>Kế hoạch truyền thông</span><svg class="v-icon v-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
      <a href="#risks-kpi" class="nav-link"><span>Rủi ro &amp; KPI đo lường</span><svg class="v-icon v-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
      <a href="#budget" class="nav-link"><span>Ngân sách &amp; Quyền lợi tài trợ</span><svg class="v-icon v-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
      <a href="#creative" class="nav-link"><span>Bộ nhận diện &amp; Ấn phẩm</span><svg class="v-icon v-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
      <a href="#appendices" class="nav-link"><span>Hồ sơ pháp lý 5 Phụ lục</span><svg class="v-icon v-icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
    </div>
    <div class="mobile-drawer-footer">
      <a href="#register-contact" class="mobile-drawer-cta">
        {icon('ticket', 'v-icon-sm')} Đăng Ký Vé VIP Miễn Phí
      </a>
      <a href="tel:0369449925" class="mobile-drawer-hotline">
        {icon('phone', 'v-icon-sm')} Hotline BTC: 0369.449.925
      </a>
    </div>
  </div>

  <!-- Hero Banner (Cinematic, Grand Editorial & Cultural Majesty) -->
  <section class="hero-banner">
    <!-- Ambient Canvas (subtle gentle golden stardust & lotus glow) -->
    <canvas id="lotus-canvas" class="hero-lotus-canvas"></canvas>

    <div class="container hero-content-relative">
      <div class="hero-widescreen-grid">
        <!-- Left Column: Prestigious Typography, Cultural Heritage & Action Buttons -->
        <div class="hero-main-col">
          <div class="hero-badge-row">
            <div class="hero-partner-badge">
              {icon('lotus', 'v-icon-sm v-icon-pink')} ĐƠN VỊ ĐỒNG HÀNH: TỈNH ĐỒNG THÁP &amp; HUNGHAU HOLDINGS
            </div>
            <div class="hero-pill-badge">
              {icon('award', 'v-icon-sm v-icon-gold')} QUY MÔ: 800 ĐẠI BIỂU &amp; SINH VIÊN
            </div>
          </div>

          <div class="hero-theme-display">
            <span class="theme-label-small">CHỦ ĐỀ CHÍNH THỨC</span>
            <h1 class="theme-title-grand">Chạm Một Sắc Sen</h1>
            <p class="hero-theme-sub-line">Chương Trình Giao Lưu Văn Hóa &amp; Nghệ Thuật Dân Tộc Nam Bộ</p>
            <div class="theme-lotus-divider">
              <span class="divider-line"></span>
              <span class="divider-icon">{icon('lotus', 'v-icon-sm v-icon-pink')}</span>
              <span class="divider-line"></span>
            </div>
          </div>

          <p class="hero-lead-desc">
            Không gian giao lưu văn hóa học đường đỉnh cao tôn vinh di sản sen Đồng Tháp Mười, nghệ thuật Đờn ca tài tử Nam Bộ và tinh thần phụng sự cộng đồng của tuổi trẻ Đại học Văn Hiến tại HungHau Campus.
          </p>

          <!-- Sleek 3-Column Meta Bar -->
          <div class="hero-meta-bar">
            <div class="hero-meta-item">
              {icon('clock', 'v-icon-sm v-icon-gold')}
              <div>
                <span class="meta-label">Thời gian tổ chức</span>
                <span class="meta-val">07:30, Chủ Nhật - 20/06/2027</span>
              </div>
            </div>
            <div class="hero-meta-item">
              {icon('map-pin', 'v-icon-sm v-icon-gold')}
              <div>
                <span class="meta-label">Địa điểm diễn ra</span>
                <span class="meta-val">Hội trường Trần Hưng Đạo (Tầng 9)</span>
              </div>
            </div>
            <div class="hero-meta-item">
              {icon('graduation-cap', 'v-icon-sm v-icon-gold')}
              <div>
                <span class="meta-label">Đơn vị chủ trì</span>
                <span class="meta-val">Trường Đại học Văn Hiến (VHU)</span>
              </div>
            </div>
          </div>

          <!-- Primary CTA Button Cluster -->
          <div class="hero-cta-group">
            <a href="#register-contact" class="btn-hero btn-hero-pink">
              {icon('ticket', 'v-icon-sm')} Đăng ký vé VIP miễn phí
            </a>
            <a href="#agenda" class="btn-hero btn-hero-gold">
              {icon('clipboard-list', 'v-icon-sm')} Xem kịch bản chương trình
            </a>
            <a href="#budget" class="btn-hero btn-hero-glass">
              {icon('wallet', 'v-icon-sm')} Tra cứu ngân sách
            </a>
            <a href="#appendices" class="btn-hero btn-hero-glass">
              {icon('file-text', 'v-icon-sm')} Toàn văn 5 Phụ lục
            </a>
          </div>
        </div>

        <!-- Right Column: Glassmorphic Visual Showcase & Live Countdown -->
        <div class="hero-visual-col">
          <div class="hero-showcase-master-card">
            <!-- Countdown Section -->
            <div class="showcase-countdown-header">
              <span class="countdown-live-badge"><span class="pulse-ring"></span> TRỰC TIẾP ĐẾM NGƯỢC</span>
              <span class="countdown-title">KHAI MẠC: 20/06/2027</span>
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

            <!-- Stage 3D Visual Preview Image with Lightbox -->
            <div class="showcase-stage-frame" data-lightbox data-src="./assets/images/nen-chinh.png" data-title="Phối cảnh sân khấu chính thức Chạm Một Sắc Sen" data-caption="Background sân khấu chính màn hình LED Hội trường Trần Hưng Đạo, HungHau Campus">
              <img src="./assets/images/nen-chinh.png" alt="Phối cảnh sân khấu chính thức Chạm một sắc Sen" class="hero-stage-img">
              <div class="stage-tag-badge">
                {icon('sparkles', 'v-icon-sm v-icon-gold')} Phối cảnh sân khấu chính thức tại Hội trường Trần Hưng Đạo
              </div>
            </div>

            <!-- Specs Grid -->
            <div class="stage-specs-grid">
              <div class="spec-item">
                <span class="spec-label">Quy mô địa điểm</span>
                <span class="spec-val">Tầng 9 (800 chỗ ngồi)</span>
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

            <!-- Audio Soundscape Capsule -->
            <div class="hero-audio-capsule">
              <div class="audio-capsule-info">
                <span class="audio-capsule-badge">{icon('music', 'v-icon-sm v-icon-pink')} ÂM SẮC ĐỒNG THÁP MƯỜI</span>
                <div class="audio-capsule-title">Dạ Cổ Hoài Lang &amp; Hồn Sen Nam Bộ</div>
              </div>
              <div class="equalizer-wave">
                <span class="eq-bar"></span>
                <span class="eq-bar"></span>
                <span class="eq-bar"></span>
                <span class="eq-bar"></span>
                <span class="eq-bar"></span>
              </div>
              <button class="btn-play-soundscape" id="btn-audio-toggle" aria-label="Bật tắt nhạc nền sự kiện">
                {icon('play', 'v-icon-sm')} Bật giai điệu Sen
              </button>
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

    <!-- Soft Bottom Curve Transition -->
    <div class="hero-bottom-curve">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#fbf9f5"></path>
      </svg>
    </div>
  </section>

  <!-- SECTION 1: OVERVIEW & 7 PILLARS -->
  <section id="overview" class="section section-overview">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">{icon('file-text', 'v-icon-sm')} I. TỔNG QUAN ĐỀ ÁN &amp; TÔN CHỈ NHÂN VĂN</span>
        <h2 class="section-title">Khái Quát Chương Trình &amp; Sứ Mệnh Giáo Dục</h2>
        <p class="section-desc">Chương trình Văn hoá &amp; Nghệ thuật tỉnh Đồng Tháp năm 2027 là sự kiện văn hóa học đường quy mô lớn của Đại học Văn Hiến, kết hợp tri thức học thuật, nghệ thuật dân gian và nghĩa cử xã hội cao đẹp.</p>
      </div>

      <!-- University Motto Callout Banner -->
      <div class="motto-banner">
        <div class="motto-crest">{icon('graduation-cap', 'v-icon-lg v-icon-gold')}</div>
        <div class="motto-text-box">
          <div class="motto-quote">"THÀNH NHÂN TRƯỚC KHI THÀNH DANH"</div>
          <p class="motto-sub">Triết lý giáo dục cốt lõi định hình nhân cách và bản sắc của hơn 30.000 sinh viên Đại học Văn Hiến qua từng thế hệ.</p>
        </div>
      </div>

      <!-- 7 Strategic Pillars Grid -->
      <h3 class="subsection-title">{icon('award', 'v-icon-gold')} 07 Mục Tiêu Chiến Lược Của Đề Án</h3>
      <div class="pillars-grid">
        <div class="pillar-card">
          <div class="pillar-number">01</div>
          <div class="pillar-content">
            <h4 class="pillar-title">{icon('lotus', 'v-icon-sm v-icon-pink')} Tôn vinh giá trị văn hóa sen Đồng Tháp</h4>
            <p class="pillar-desc">Khẳng định hình tượng hoa sen là biểu tượng văn hóa đặc sắc, gắn bó với đời sống tâm hồn người dân vùng Đất Sen Hồng.</p>
          </div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">02</div>
          <div class="pillar-content">
            <h4 class="pillar-title">{icon('music', 'v-icon-sm v-icon-gold')} Gìn giữ nghệ thuật Đờn ca tài tử</h4>
            <p class="pillar-desc">Bảo tồn loại hình nghệ thuật Đờn ca tài tử Nam Bộ – Di sản văn hóa phi vật thể của nhân loại được UNESCO vinh danh.</p>
          </div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">03</div>
          <div class="pillar-content">
            <h4 class="pillar-title">{icon('users', 'v-icon-sm')} Không gian giao lưu học đường</h4>
            <p class="pillar-desc">Xây dựng sân chơi lành mạnh, ý nghĩa cho sinh viên các khoa và khách mời thông qua các hoạt động trải nghiệm thực tế.</p>
          </div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">04</div>
          <div class="pillar-content">
            <h4 class="pillar-title">{icon('sparkles', 'v-icon-sm v-icon-gold')} Quảng bá bản lĩnh sinh viên VHU</h4>
            <p class="pillar-desc">Thể hiện sự năng động, sáng tạo, nhiệt huyết cùng tinh thần bảo tồn và phát huy bản sắc văn hóa dân tộc.</p>
          </div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">05</div>
          <div class="pillar-content">
            <h4 class="pillar-title">{icon('heart', 'v-icon-sm v-icon-pink')} Phụng sự cộng đồng &amp; Thiện nguyện</h4>
            <p class="pillar-desc">Quyên góp toàn bộ lợi nhuận (dự kiến 200,9 triệu) cho Trung tâm Bảo trợ Xã hội Tổng hợp Tỉnh Đồng Tháp.</p>
          </div>
        </div>
        <div class="pillar-card">
          <div class="pillar-number">06</div>
          <div class="pillar-content">
            <h4 class="pillar-title">{icon('graduation-cap', 'v-icon-sm v-icon-gold')} Khẳng định triết lý Thành Nhân</h4>
            <p class="pillar-desc">Hiện thực hóa sứ mệnh giáo dục toàn diện của Đại học Văn Hiến qua các hoạt động trải nghiệm thực tiễn.</p>
          </div>
        </div>
        <div class="pillar-card pillar-card-wide">
          <div class="pillar-number">07</div>
          <div class="pillar-content">
            <h4 class="pillar-title">{icon('award', 'v-icon-sm v-icon-gold')} Tăng cường kết nối mạng lưới đối tác bền vững</h4>
            <p class="pillar-desc">Thắt chặt quan hệ hợp tác chiến lược giữa Nhà trường, Doanh nghiệp tài trợ, Tỉnh Đồng Tháp và mạng lưới Cựu sinh viên.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Organic Flowing Wave Transition to Artists Section (Navy) -->
    <div class="section-wave-divider divider-overview-to-navy">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#0c2044"/>
      </svg>
    </div>
  </section>

  <!-- SECTION 2: GUEST STARS & HERITAGE SPOTLIGHT (#artists) -->
  <section id="artists" class="section section-artists">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-pink">{icon('star', 'v-icon-sm v-icon-pink')} II. KHÁCH MỜI DANH DỰ &amp; NGHỆ THUẬT ĐỒNG HÀNH</span>
        <h2 class="section-title">Hội Ngộ Âm Sắc Dân Tộc &amp; Khát Vọng Tuổi Trẻ</h2>
        <p class="section-desc">Chương trình vinh dự đón chào sự hiện diện của các nghệ sĩ tên tuổi, các nghệ nhân di sản Nam Bộ và các nhà thiết kế đồng hành, mang đến những thanh âm thăng hoa của miền sông nước Đồng Tháp Mười.</p>
      </div>

      <!-- Master Artist Poster Banner -->
      <div class="artist-master-banner" data-lightbox data-src="./assets/images/khach-moi.png" data-title="Dàn Khách mời Ngôi sao &amp; Nghệ sĩ Đồng hành" data-caption="Ca sĩ Phương Mỹ Chi, Hoa hậu Miss Grand Vietnam 2024 Nguyễn Thị Yến Nhi, Á hậu 1 Lê Phan Hạnh Nguyên và các nghệ sĩ">
        <img src="./assets/images/khach-moi.png" alt="Dàn khách mời danh dự chương trình Chạm một sắc Sen" class="artist-master-img">
        <div class="master-banner-overlay">
          <span class="master-badge">{icon('sparkles', 'v-icon-sm')} DÀN KHÁCH MỜI NGÔI SAO &amp; ĐẠI SỨ VĂN HÓA</span>
          <h3 class="banner-main-name">Ca Sĩ Phương Mỹ Chi • Hoa Hậu Yến Nhi • Á Hậu Hạnh Nguyên</h3>
        </div>
      </div>

      <!-- Artist Highlights 3-Card Grid -->
      <div class="artist-three-grid">
        <!-- Card 1: Phương Mỹ Chi -->
        <div class="artist-feature-card card-pmc">
          <div class="artist-card-header">
            <span class="role-pill-gold">NGHỆ SĨ NGÔI SAO BIỂU DIỄN</span>
            <h4 class="artist-card-title">Ca Sĩ Phương Mỹ Chi</h4>
            <div class="artist-card-sub">Đại sứ truyền cảm hứng văn hóa dân gian Nam Bộ thế hệ Gen Z</div>
          </div>
          <blockquote class="artist-card-quote">
            "Đến với 'Chạm một sắc Sen' tại Đại học Văn Hiến, Mỹ Chi mong muốn gửi gắm trọn vẹn tình yêu quê hương xứ sở và hồn sen Đồng Tháp Mười đến các bạn sinh viên – những người trẻ sẽ tiếp nối và gìn giữ nét đẹp văn hóa Việt Nam."
          </blockquote>
          <div class="artist-setlist-box">
            <div class="setlist-header">{icon('music', 'v-icon-sm v-icon-pink')} TIẾT MỤC ĐẶC BIỆT:</div>
            <ul class="setlist-ul">
              <li>{icon('check-circle', 'v-icon-sm v-icon-gold')} <strong>08:35:</strong> Tiết mục mở màn "Sắc Sen VHU" chào mừng Đại biểu</li>
              <li>{icon('check-circle', 'v-icon-sm v-icon-gold')} <strong>10:15:</strong> Trình diễn đơn ca ca khúc chủ đề <em>"Chạm Một Sắc Sen"</em> &amp; Giao lưu cùng NTK Nguyễn Minh Công</li>
            </ul>
          </div>
        </div>

        <!-- Card 2: Đờn ca tài tử -->
        <div class="artist-feature-card">
          <div class="artist-card-header">
            <span class="role-pill-blue">DI SẢN UNESCO VĂN HÓA</span>
            <h4 class="artist-card-title">CLB Đờn Ca Tài Tử Nam Bộ</h4>
            <div class="artist-card-sub">Nghệ nhân dân gian &amp; Dàn nhạc cụ cổ truyền Nam Bộ</div>
          </div>
          <p class="card-body-text">
            Không gian âm nhạc mộc mạc mà sâu lắng với dàn ngũ tuyệt cổ truyền: Đàn Kìm, Đàn Tranh, Đàn Bầu, Đàn Cò và Song Lang, kết nối mạch nguồn văn hóa Đồng bằng sông Cửu Long qua các bản Bắc, bản Hạ kinh điển.
          </p>
          <div class="performance-highlight-box">
            <strong>Tiết mục biểu diễn:</strong> Hoà tấu nhạc tài tử Nam Bộ đón khách &amp; Tiết mục <em>"Hồn Sen Đất Việt"</em> (08:40).
          </div>
        </div>

        <!-- Card 3: NTK Nguyễn Minh Công -->
        <div class="artist-feature-card">
          <div class="artist-card-header">
            <span class="role-pill-pink">FASHION SHOW ÁO DÀI SEN</span>
            <h4 class="artist-card-title">NTK Nguyễn Minh Công</h4>
            <div class="artist-card-sub">Bộ sưu tập Áo Dài Sen độc quyền <em>"Miệt Cù Lao"</em></div>
          </div>
          <p class="card-body-text">
            Sự kết hợp độc đáo giữa chất liệu tơ sen Đồng Tháp và lụa truyền thống, được trình diễn bởi chính các sinh viên Khoa Du lịch và Khoa Nghệ thuật Trường Đại học Văn Hiến.
          </p>
          <div class="performance-highlight-box">
            <strong>Trình diễn thời trang:</strong> Fashion Show "Sắc Sen" (10:05) với 12 mẫu thiết kế độc quyền lấy cảm hứng từ đầm sen Tháp Mười.
          </div>
        </div>
      </div>
    </div>

    <!-- Organic Flowing Wave Transition to Agenda Section (Cream) -->
    <div class="section-wave-divider divider-artists-to-agenda">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#f5f2eb"/>
      </svg>
    </div>
  </section>

  <!-- SECTION 3: DETAILED AGENDA TIMELINE -->
  <section id="agenda" class="section section-agenda bg-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">{icon('clock', 'v-icon-sm')} III. KỊCH BẢN TỔ CHỨC CHI TIẾT</span>
        <h2 class="section-title">Timeline Diễn Biến Sự Kiện (07:30 – 11:10)</h2>
        <p class="section-desc">Kế hoạch điều phối 220 phút chi tiết theo từng phút với 11 mốc hoạt động, tích hợp âm thanh, ánh sáng màn hình LED và dàn nhạc dân tộc trực tiếp.</p>
      </div>

      <!-- Filter Controls -->
      <div class="agenda-controls">
        <button class="agenda-filter-btn active" data-filter="all">Tất cả hoạt động (11 mốc)</button>
        <button class="agenda-filter-btn" data-filter="phase-1">07:30 – 08:40: Đón khách &amp; Khai mạc (4 mốc)</button>
        <button class="agenda-filter-btn" data-filter="phase-2">08:40 – 10:05: Giao lưu &amp; Di sản (3 mốc)</button>
        <button class="agenda-filter-btn" data-filter="phase-3">10:05 – 11:10: Fashion Show &amp; Bế mạc (4 mốc)</button>
      </div>

      <!-- Timeline Stream -->
      <div class="timeline-stream">
        {agenda_str}
      </div>
    </div>
  </section>

  <!-- SECTION 4: INTEGRATED MEDIA PLAN -->
  <section id="media-plan" class="section section-media">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">{icon('megaphone', 'v-icon-sm')} IV. KẾ HOẠCH TRUYỀN THÔNG &amp; QUẢNG BÁ</span>
        <h2 class="section-title">Chiến Dịch Truyền Thông Đa Kênh Tích Hợp</h2>
        <p class="section-desc">Kế hoạch truyền thông 3 giai đoạn (Tiền sự kiện, Trong sự kiện và Hậu sự kiện) nhằm đạt tối thiểu 100.000 lượt tiếp cận trên mạng xã hội.</p>
      </div>

      <!-- Phase Tabs -->
      <div class="tab-nav-wrapper">
        <button class="tab-pill-btn active" data-tab-target="tab-pre">1. Tiền Sự Kiện (Trước 20/06)</button>
        <button class="tab-pill-btn" data-tab-target="tab-during">2. Trong Sự Kiện (20/06/2027)</button>
        <button class="tab-pill-btn" data-tab-target="tab-post">3. Hậu Sự Kiện &amp; Thiện Nguyện</button>
      </div>

      <!-- Tab 1: Pre-event -->
      <div id="tab-pre" class="tab-pane active">
        <div class="table-card-container">
          <div class="table-header-title">
            <h4>{icon('calendar', 'v-icon-sm')} Kế Hoạch Truyền Thông Giai Đoạn Tiền Sự Kiện (8 Hạng Mục)</h4>
          </div>
          <div class="table-scroll-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>STT</th>
                  <th>Hoạt động truyền thông</th>
                  <th>Mục tiêu chiến dịch</th>
                  <th>Nội dung triển khai</th>
                  <th>Kênh truyền thông</th>
                  <th>Thời gian</th>
                  <th>Người phụ trách</th>
                  <th>Chỉ số KPI cam kết</th>
                </tr>
              </thead>
              <tbody>
                {media_pre_str}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Tab 2: During-event -->
      <div id="tab-during" class="tab-pane">
        <div class="table-card-container">
          <div class="table-header-title">
            <h4>{icon('calendar', 'v-icon-sm')} Kế Hoạch Truyền Thông Trong Ngày Diễn Ra Sự Kiện (4 Hạng Mục)</h4>
          </div>
          <div class="table-scroll-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>STT</th>
                  <th>Hoạt động truyền thông</th>
                  <th>Mục tiêu chiến dịch</th>
                  <th>Nội dung triển khai</th>
                  <th>Kênh truyền thông</th>
                  <th>Thời gian</th>
                  <th>Người phụ trách</th>
                </tr>
              </thead>
              <tbody>
                {media_during_str}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Tab 3: Post-event -->
      <div id="tab-post" class="tab-pane">
        <div class="table-card-container">
          <div class="table-header-title">
            <h4>{icon('calendar', 'v-icon-sm')} Kế Hoạch Truyền Thông Sau Sự Kiện &amp; Thiện Nguyện (7 Hạng Mục)</h4>
          </div>
          <div class="table-scroll-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Giai đoạn</th>
                  <th>Thời gian</th>
                  <th>Hoạt động chính</th>
                  <th>Nội dung thông điệp</th>
                  <th>Kênh đăng tải</th>
                  <th>Đơn vị phụ trách</th>
                </tr>
              </thead>
              <tbody>
                {media_post_str}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: RISK MANAGEMENT & KPIS -->
  <section id="risks-kpi" class="section section-risks bg-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-pink">{icon('shield', 'v-icon-sm')} V. QUẢN TRỊ RỦI RO &amp; HỆ THỐNG CHỈ SỐ KPI</span>
        <h2 class="section-title">Kịch Bản Ứng Phó Rủi Ro &amp; Đo Lường Hiệu Quả</h2>
        <p class="section-desc">Phương án nhận diện, phòng ngừa và xử lý khẩn cấp 40 rủi ro tiềm ẩn cùng 29 chỉ số KPI đo lường định lượng thành công của chương trình.</p>
      </div>

      <!-- Risk Sub-tabs -->
      <div class="tab-nav-wrapper">
        <button class="tab-pill-btn active" data-tab-target="risk-plan">Rủi ro Kế hoạch &amp; Pháp lý (9)</button>
        <button class="tab-pill-btn" data-tab-target="risk-event">Rủi ro Tổ chức &amp; Sự kiện (12)</button>
        <button class="tab-pill-btn" data-tab-target="risk-media">Rủi ro Truyền thông &amp; Khủng hoảng (19)</button>
        <button class="tab-pill-btn" data-tab-target="tab-kpi">29 Chỉ Số KPI Đo Lường Chi Tiết</button>
      </div>

      <!-- Risk Filter Bar -->
      <div class="search-filter-bar">
        <div class="search-input-box">
          {icon('search', 'v-icon-sm')}
          <input type="text" id="risk-search-input" placeholder="Tìm kiếm rủi ro, nguyên nhân, biện pháp phòng ngừa..." aria-label="Tìm kiếm rủi ro">
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
          <label for="risk-severity-select" style="font-size: 0.85rem; font-weight: 600;">Mức độ:</label>
          <select id="risk-severity-select" class="select-filter">
            <option value="all">Tất cả mức độ</option>
            <option value="rất cao">Rất cao</option>
            <option value="cao">Cao</option>
            <option value="trung bình">Trung bình</option>
            <option value="thấp">Thấp</option>
          </select>
        </div>
      </div>

      <!-- Risk Table 1: Plan -->
      <div id="risk-plan" class="tab-pane active">
        <div class="table-card-container">
          <div class="table-scroll-wrapper">
            <table class="data-table" id="risk-table-plan">
              <thead>
                <tr>
                  <th>Hạng mục</th>
                  <th>Rủi ro nhận diện</th>
                  <th>Mức độ</th>
                  <th>Biện pháp phòng ngừa</th>
                  <th>Phương án xử lý khi xảy ra</th>
                  <th>Đơn vị chịu trách nhiệm</th>
                </tr>
              </thead>
              <tbody>
                {risk_plan_str}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Risk Table 2: Event -->
      <div id="risk-event" class="tab-pane">
        <div class="table-card-container">
          <div class="table-scroll-wrapper">
            <table class="data-table" id="risk-table-event">
              <thead>
                <tr>
                  <th>Hạng mục</th>
                  <th>Rủi ro nhận diện</th>
                  <th>Mức độ</th>
                  <th>Biện pháp phòng ngừa</th>
                  <th>Phương án xử lý khi xảy ra</th>
                  <th>Đơn vị chịu trách nhiệm</th>
                </tr>
              </thead>
              <tbody>
                {risk_event_str}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Risk Table 3: Media -->
      <div id="risk-media" class="tab-pane">
        <div class="table-card-container">
          <div class="table-scroll-wrapper">
            <table class="data-table" id="risk-table-media">
              <thead>
                <tr>
                  <th>Nhóm rủi ro</th>
                  <th>Rủi ro truyền thông</th>
                  <th>Mức độ</th>
                  <th>Biện pháp phòng ngừa</th>
                  <th>Phương án xử lý khủng hoảng</th>
                  <th>Đơn vị chịu trách nhiệm</th>
                </tr>
              </thead>
              <tbody>
                {risk_media_str}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Tab 4: KPIs Grid -->
      <div id="tab-kpi" class="tab-pane">
        <div class="kpi-grid">
          {kpis_str}
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 6: BUDGET & SPONSORS -->
  <section id="budget" class="section section-budget">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">{icon('wallet', 'v-icon-sm')} VI. DỰ TRÙ KINH PHÍ &amp; VẬN ĐỘNG TÀI TRỢ</span>
        <h2 class="section-title">Minh Bạch Tài Chính &amp; Gói Quyền Lợi Nhà Tài Trợ</h2>
        <p class="section-desc">Tổng dự toán 305.000.000 VNĐ cho 68 hạng mục chi tiết. Toàn bộ doanh thu sau khi trừ chi phí vận hành sẽ được quyên góp vào quỹ thiện nguyện Đồng Tháp.</p>
      </div>

      <!-- Financial Balance 3-Card Grid -->
      <div class="finance-overview-grid">
        <div class="finance-kpi-card card-income">
          <div class="card-finance-label">{icon('wallet', 'v-icon-sm')} Tổng Nguồn Thu Vận Động</div>
          <div class="card-finance-value">305.000.000 VNĐ</div>
          <div class="card-finance-note">Gồm 260.000.000đ tài trợ doanh nghiệp &amp; 45.000.000đ từ gian hàng, vé</div>
        </div>
        <div class="finance-kpi-card card-expense">
          <div class="card-finance-label">{icon('clipboard-list', 'v-icon-sm')} Tổng Dự Toán Chi Phí</div>
          <div class="card-finance-value">104.100.000 VNĐ</div>
          <div class="card-finance-note">Tổng định mức chi phí tổ chức 9 nhóm (Đã gồm 10% dự phòng)</div>
        </div>
        <div class="finance-kpi-card card-charity">
          <div class="card-finance-label">{icon('heart', 'v-icon-sm')} Quỹ Thiện Nguyện Đồng Tháp</div>
          <div class="card-finance-value">200.900.000 VNĐ</div>
          <div class="card-finance-note">100% Lợi nhuận trao tặng Trung tâm Bảo trợ Xã hội Đồng Tháp</div>
        </div>
      </div>

      <!-- Expenditure Breakdown Progress Bar -->
      <div class="budget-visual-bar">
        <div class="budget-bar-title">{icon('chart-pie', 'v-icon-sm v-icon-gold')} Cơ Cấu Phân Bổ Chi Phí Sự Kiện (Tổng 104.100.000 VNĐ)</div>
        <div class="stacked-bar" role="progressbar" aria-label="Cơ cấu phân bổ chi phí 104.100.000 VNĐ">
          <div class="bar-segment seg-1" style="width: 38.9%;" title="Sân khấu &amp; Kỹ thuật LED: 40.500.000đ (38.9%)"></div>
          <div class="bar-segment seg-2" style="width: 27.9%;" title="Nghệ sĩ &amp; Khách mời: 29.000.000đ (27.9%)"></div>
          <div class="bar-segment seg-3" style="width: 20.4%;" title="Quà tặng &amp; Ấn phẩm sen: 21.200.000đ (20.4%)"></div>
          <div class="bar-segment seg-4" style="width: 12.8%;" title="Truyền thông &amp; Dự phòng 10%: 13.400.000đ (12.8%)"></div>
        </div>
        <div class="budget-legend-grid">
          <div class="legend-item">
            <div class="legend-item-title">
              <span class="legend-color-dot dot-1"></span>
              <span>Sân khấu &amp; Kỹ thuật LED</span>
            </div>
            <div class="legend-item-val">
              <span class="val-money">40.500.000đ</span> <span class="val-pct">(38.9%)</span>
            </div>
          </div>
          <div class="legend-item">
            <div class="legend-item-title">
              <span class="legend-color-dot dot-2"></span>
              <span>Nghệ sĩ &amp; Khách mời</span>
            </div>
            <div class="legend-item-val">
              <span class="val-money">29.000.000đ</span> <span class="val-pct">(27.9%)</span>
            </div>
          </div>
          <div class="legend-item">
            <div class="legend-item-title">
              <span class="legend-color-dot dot-3"></span>
              <span>Quà tặng &amp; Ấn phẩm sen</span>
            </div>
            <div class="legend-item-val">
              <span class="val-money">21.200.000đ</span> <span class="val-pct">(20.4%)</span>
            </div>
          </div>
          <div class="legend-item">
            <div class="legend-item-title">
              <span class="legend-color-dot dot-4"></span>
              <span>Truyền thông &amp; Dự phòng 10%</span>
            </div>
            <div class="legend-item-val">
              <span class="val-money">13.400.000đ</span> <span class="val-pct">(12.8%)</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 4 Metallic Sponsor Tier Cards -->
      <div class="sponsor-tiers-container">
        <h3 class="sponsor-tiers-title">{icon('award', 'v-icon-gold')} 04 Gói Quyền Lợi Tài Trợ Doanh Nghiệp</h3>
        <div class="sponsor-tier-grid">
          <!-- Diamond Tier -->
          <div class="sponsor-tier-card card-diamond">
            <div class="tier-badge diamond-badge">TÀI TRỢ KIM CƯƠNG</div>
            <div class="tier-price">150.000.000 đ</div>
            <div class="tier-quota">Chỉ duy nhất 01 Đơn vị độc quyền</div>
            <ul class="tier-privileges">
              <li>{icon('check', 'v-icon-sm')} Logo vị trí VIP số 1 trên tất cả Backdrop, Poster &amp; Màn hình LED</li>
              <li>{icon('check', 'v-icon-sm')} Đại diện phát biểu chúc mừng tại Nghi lễ Khai mạc chính thức</li>
              <li>{icon('check', 'v-icon-sm')} Trao kỷ niệm chương &amp; Hoa tri ân trực tiếp từ Lãnh đạo VHU</li>
              <li>{icon('check', 'v-icon-sm')} 01 Gian hàng quảng bá sản phẩm thương hiệu vị trí trung tâm sảnh Tầng 9</li>
              <li>{icon('check', 'v-icon-sm')} Bài viết PR chuyên sâu trên Báo Pháp Luật &amp; Đài PT-TH Đồng Tháp</li>
              <li>{icon('check', 'v-icon-sm')} 20 Vé mời VIP Khán đài A hàng ghế danh dự</li>
            </ul>
          </div>

          <!-- Gold Tier -->
          <div class="sponsor-tier-card card-gold">
            <div class="tier-badge gold-badge">TÀI TRỢ VÀNG</div>
            <div class="tier-price">80.000.000 đ</div>
            <div class="tier-quota">Số lượng: 02 Đơn vị</div>
            <ul class="tier-privileges">
              <li>{icon('check', 'v-icon-sm')} Logo nổi bật trên Backdrop, Standee và toàn bộ Video Clip giới thiệu</li>
              <li>{icon('check', 'v-icon-sm')} Vinh danh trao hoa và Kỷ niệm chương tri ân trên sân khấu chính</li>
              <li>{icon('check', 'v-icon-sm')} 01 Bàn trưng bày giới thiệu doanh nghiệp tại không gian văn hóa</li>
              <li>{icon('check', 'v-icon-sm')} Đăng tin bài cảm ơn trên Cổng thông tin &amp; Fanpage Đại học Văn Hiến</li>
              <li>{icon('check', 'v-icon-sm')} 10 Vé mời VIP Khán đài danh dự</li>
            </ul>
          </div>

          <!-- Silver Tier -->
          <div class="sponsor-tier-card card-silver">
            <div class="tier-badge silver-badge">TÀI TRỢ BẠC</div>
            <div class="tier-price">40.000.000 đ</div>
            <div class="tier-quota">Số lượng: 03 Đơn vị</div>
            <ul class="tier-privileges">
              <li>{icon('check', 'v-icon-sm')} Logo trên các ấn phẩm truyền thông, Standee &amp; Cuốn Passport Sen</li>
              <li>{icon('check', 'v-icon-sm')} Đại diện nhận hoa tri ân tại chương trình</li>
              <li>{icon('check', 'v-icon-sm')} Đặt ấn phẩm tờ rơi tại túi quà tặng lưu niệm của khách mời</li>
              <li>{icon('check', 'v-icon-sm')} 05 Vé tham dự VIP sự kiện</li>
            </ul>
          </div>

          <!-- Bronze Tier -->
          <div class="sponsor-tier-card card-bronze">
            <div class="tier-badge bronze-badge">ĐỒNG HÀNH / ĐỒNG</div>
            <div class="tier-price">20.000.000 đ</div>
            <div class="tier-quota">Không giới hạn số lượng</div>
            <ul class="tier-privileges">
              <li>{icon('check', 'v-icon-sm')} Tên đơn vị trên Backdrop vinh danh Nhà tài trợ đồng hành</li>
              <li>{icon('check', 'v-icon-sm')} Nhận Giấy chứng nhận tri ân đóng góp vì cộng đồng từ VHU</li>
              <li>{icon('check', 'v-icon-sm')} 02 Vé mời tham dự chương trình</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Master 68-row Budget Table -->
      <div class="table-card-container" style="margin-top: 36px;">
        <div class="table-header-title" style="flex-wrap: wrap; gap: 14px;">
          <div>
            <h4>{icon('wallet', 'v-icon-sm')} Bảng Dự Toán Chi Tiết Toàn Bộ 68 Hạng Mục Ngân Sách</h4>
            <div style="font-size: 0.78rem; color: #94a3b8;">Có thể lọc theo từng nhóm hạng mục hoặc tìm kiếm theo từ khóa</div>
          </div>
          <div class="budget-toolbar" style="display: flex; gap: 10px; flex-wrap: wrap;">
            <select id="budget-group-select" class="select-filter">
              <option value="all">Tất cả 9 nhóm kinh phí (68 hạng mục)</option>
              <option value="A">Nhóm A: Địa điểm – Dàn dựng (5 mục)</option>
              <option value="B">Nhóm B: Âm thanh – Ánh sáng – LED (3 mục)</option>
              <option value="C">Nhóm C: Ấn phẩm &amp; Nhận diện (5 mục)</option>
              <option value="D">Nhóm D: Truyền thông &amp; Báo chí (3 mục)</option>
              <option value="E">Nhóm E: Nghệ thuật &amp; Sân khấu (8 mục)</option>
              <option value="F">Nhóm F: Khách mời – Đón tiếp &amp; Tri ân (6 mục)</option>
              <option value="G">Nhóm G: Quà tặng &amp; Kỷ niệm (5 mục)</option>
              <option value="H">Nhóm H: Hậu cần – An toàn – Y tế (7 mục)</option>
              <option value="I">Nhóm I: Phục vụ – Ăn uống (4 mục)</option>
            </select>
            <div class="search-input-box" style="max-width: 260px;">
              {icon('search', 'v-icon-sm')}
              <input type="text" id="budget-search-input" placeholder="Tìm hạng mục chi..." aria-label="Tìm kiếm hạng mục chi ngân sách">
            </div>
          </div>
        </div>

        <div class="table-scroll-wrapper">
          <div class="mobile-scroll-hint">
            {icon('arrow-right', 'v-icon-xs')} Vuốt ngang để xem đủ 6 cột chi phí, đơn giá và tiêu chuẩn kỹ thuật
          </div>
          <table class="data-table" id="budget-master-table">
            <thead>
              <tr>
                <th>Nội dung hạng mục</th>
                <th class="text-center">Số lượng</th>
                <th class="text-center">Đơn vị</th>
                <th class="text-right">Đơn giá (VNĐ)</th>
                <th class="text-right">Thành tiền (VNĐ)</th>
                <th>Ghi chú triển khai</th>
              </tr>
            </thead>
            <tbody>
              {budget_table_str}
            </tbody>
          </table>
        </div>
        <div class="table-footer-status">
          <span class="status-count-tag">{icon('layers', 'v-icon-xs')} Đang hiển thị: <strong id="budget-visible-count">68</strong> hạng mục</span>
          <span class="status-currency-tag">{icon('wallet', 'v-icon-xs')} Đơn vị tính: <strong>Việt Nam Đồng (VNĐ)</strong></span>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 7: CREATIVE GALLERY -->
  <section id="creative" class="section section-gallery bg-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-pink">{icon('sparkles', 'v-icon-sm')} VII. BỘ NHẬN DIỆN THIẾT KẾ &amp; ẤN PHẨM</span>
        <h2 class="section-title">Hệ Thống Ấn Phẩm Nhận Diện &amp; Không Gian Triển Lãm</h2>
        <p class="section-desc">Toàn bộ 13 ấn phẩm trực quan được trích xuất từ đề án chính thức: Poster, Standee, Backdrop, Vé mời, Phối cảnh sân khấu, Quà tặng và Nhạc độc quyền sự kiện.</p>
      </div>

      <!-- Gallery Grid (13 Items) -->
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
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Bộ nhận diện</span>
              <span class="font-bold text-primary">Kích thước A1</span>
            </div>
          </div>
        </div>

        <!-- 2. Standee -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image2.png" data-title="H2. Standee sự kiện" data-caption="Standee đặt tại các sảnh và lối vào HungHau Campus">
            <img src="./assets/docx_media/image2.png" alt="Standee sự kiện Chạm một sắc Sen" loading="lazy">
            <span class="gallery-overlay-badge">H2. Standee</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Standee Đặt Tại Sảnh Campus</h4>
              <p class="gallery-item-caption">Đặt tại sảnh tầng trệt và trước cửa Hội trường Trần Hưng Đạo Tầng 9.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Chỉ dẫn</span>
              <span class="font-bold text-primary">0.8m x 1.8m</span>
            </div>
          </div>
        </div>

        <!-- 3. Backdrop chính -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image3.png" data-title="H3. Backdrop sân khấu chính" data-caption="Backdrop hiển thị trên màn hình LED sân khấu Tầng 9">
            <img src="./assets/docx_media/image3.png" alt="Backdrop sân khấu chính" loading="lazy">
            <span class="gallery-overlay-badge">H3. Backdrop LED</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Backdrop Màn Hình LED Sân Khấu</h4>
              <p class="gallery-item-caption">Độ phân giải 4K sắc nét đồng bộ cùng hệ thống ánh sáng chuyển động.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Sân khấu</span>
              <span class="font-bold text-primary">Màn hình P3</span>
            </div>
          </div>
        </div>

        <!-- 4. Thư mời VIP -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image4.jpeg" data-title="H4. Thư mời đại biểu danh dự" data-caption="Thiết kế thiệp mời trang trọng gửi tới lãnh đạo tỉnh và đối tác">
            <img src="./assets/docx_media/image4.jpeg" alt="Thư mời đại biểu danh dự" loading="lazy">
            <span class="gallery-overlay-badge">H4. Thư mời</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Thư Mời Đại Biểu &amp; Doanh Nghiệp</h4>
              <p class="gallery-item-caption">Chất liệu giấy mỹ thuật ép kim vàng đồng, mang dấu ấn văn hóa thanh tao.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Lễ tân</span>
              <span class="font-bold text-primary">In offset ép kim</span>
            </div>
          </div>
        </div>

        <!-- 5. Vé tham dự -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image5.jpeg" data-title="H5. Vé tham dự Passport Sen" data-caption="Vé tích hợp mã QR cá nhân cho sinh viên check-in">
            <img src="./assets/docx_media/image5.jpeg" alt="Vé tham dự Passport Sen" loading="lazy">
            <span class="gallery-overlay-badge">H5. Vé mời</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Vé Tham Dự / Passport Sen</h4>
              <p class="gallery-item-caption">Tích hợp mã QR định danh và các ô đóng dấu trải nghiệm tại ngày hội.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Kiểm soát vé</span>
              <span class="font-bold text-primary">QR Check-in</span>
            </div>
          </div>
        </div>

        <!-- 6. Phối cảnh sân khấu 3D -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image6.jpeg" data-title="H6. Phối cảnh sân khấu 3D Hội trường" data-caption="Phối cảnh sân khấu Tầng 9 quy mô 800 chỗ ngồi">
            <img src="./assets/docx_media/image6.jpeg" alt="Phối cảnh sân khấu 3D" loading="lazy">
            <span class="gallery-overlay-badge">H6. Phối cảnh 3D</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Phối Cảnh Sân Khấu 3D</h4>
              <p class="gallery-item-caption">Bố cục không gian phân tầng tối ưu góc nhìn cho 500-800 khán giả tham gia.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Kỹ thuật</span>
              <span class="font-bold text-primary">Tầng 9 Campus</span>
            </div>
          </div>
        </div>

        <!-- 7. Nón lá sen -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image7.jpeg" data-title="H7. Nón lá vẽ hoa sen lưu niệm" data-caption="Nón lá vẽ tay thủ công làm quà tặng khách mời danh dự">
            <img src="./assets/docx_media/image7.jpeg" alt="Nón lá sen lưu niệm" loading="lazy">
            <span class="gallery-overlay-badge">H7. Quà tặng</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Nón Lá Sen Vẽ Thủ Công</h4>
              <p class="gallery-item-caption">Món quà đậm chất Nam Bộ vẽ tay bởi các nghệ nhân Làng nghề Đồng Tháp.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Thủ công</span>
              <span class="font-bold text-primary">Quà tặng VIP</span>
            </div>
          </div>
        </div>

        <!-- 8. Túi vải canvas -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image8.jpeg" data-title="H8. Túi vải canvas họa tiết sen" data-caption="Túi canvas thân thiện môi trường dành cho người tham gia">
            <img src="./assets/docx_media/image8.jpeg" alt="Túi vải canvas sen" loading="lazy">
            <span class="gallery-overlay-badge">H8. Quà tặng</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Túi Canvas "Chạm Một Sắc Sen"</h4>
              <p class="gallery-item-caption">Vải bố mộc thân thiện môi trường, in họa tiết đóa sen hồng độc quyền.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Eco-friendly</span>
              <span class="font-bold text-primary">Quà sinh viên</span>
            </div>
          </div>
        </div>

        <!-- 9. Quà tặng đặc sản sen -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image9.jpeg" data-title="H9. Hộp quà đặc sản Đồng Tháp" data-caption="Hộp quà hạt sen sấy, trà sen và tinh dầu sen Đồng Tháp">
            <img src="./assets/docx_media/image9.jpeg" alt="Hộp quà đặc sản sen" loading="lazy">
            <span class="gallery-overlay-badge">H9. Đặc sản</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Hộp Quà Đặc Sản Tháp Mười</h4>
              <p class="gallery-item-caption">Gồm hạt sen sấy giòn, trà tim sen thượng hạng và mứt sen truyền thống.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Đặc sản</span>
              <span class="font-bold text-primary">OCOP Đồng Tháp</span>
            </div>
          </div>
        </div>

        <!-- 10. Gian hàng ẩm thực -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image10.png" data-title="H10. Gian hàng ẩm thực văn hóa sen" data-caption="Khu vực gian hàng trải nghiệm các món ăn thức uống từ sen">
            <img src="./assets/docx_media/image10.png" alt="Gian hàng ẩm thực sen" loading="lazy">
            <span class="gallery-overlay-badge">H10. Gian hàng</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Khu Trải Nghiệm Ẩm Thực Sen</h4>
              <p class="gallery-item-caption">30 gian hàng do sinh viên Khoa Du lịch và doanh nghiệp địa phương vận hành.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Trải nghiệm</span>
              <span class="font-bold text-primary">Sảnh Tầng 9</span>
            </div>
          </div>
        </div>

        <!-- 11. Khu check-in hoa sen -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image11.jpeg" data-title="H11. Tiểu cảnh check-in hoa sen" data-caption="Không gian chụp ảnh tương tác hoa sen và xuồng ba lá Nam Bộ">
            <img src="./assets/docx_media/image11.jpeg" alt="Tiểu cảnh check-in hoa sen" loading="lazy">
            <span class="gallery-overlay-badge">H11. Check-in</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Tiểu Cảnh Xuồng Ba Lá &amp; Hồ Sen</h4>
              <p class="gallery-item-caption">Tái hiện đầm sen rực rỡ và chiếc xuồng ba lá mộc mạc giữa lòng thành phố.</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('tag', 'v-icon-sm')} Tương tác</span>
              <span class="font-bold text-primary">Check-in Photo</span>
            </div>
          </div>
        </div>

        <!-- 12. Mã QR Nhạc độc quyền sự kiện -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper qr-wrapper" data-lightbox data-src="./assets/docx_media/image12.png" data-title="H12. Mã QR Nhạc độc quyền sự kiện" data-caption="Quét mã QR để nghe ca khúc chủ đề 'Chạm Một Sắc Sen' độc quyền trên điện thoại">
            <img src="./assets/docx_media/image12.png" alt="Mã QR Nhạc độc quyền" class="qr-centered-img" loading="lazy">
            <span class="gallery-overlay-badge">H12. QR Nhạc Sen</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Mã QR Ca Khúc Chủ Đề</h4>
              <p class="gallery-item-caption">Quét mã QR trực tiếp trên điện thoại để thưởng thức bản phối độc quyền ca khúc chủ đề "Chạm Một Sắc Sen".</p>
            </div>
            <div class="gallery-item-meta">
              <span>{icon('music', 'v-icon-sm')} Âm nhạc độc quyền</span>
              <span class="font-bold text-primary">Scan QR Code</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 8: LEGAL APPENDICES DOSSIER -->
  <section id="appendices" class="section section-appendices">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">{icon('file-text', 'v-icon-sm')} VIII. HỒ SƠ PHÁP LÝ &amp; VĂN BẢN ĐÍNH KÈM</span>
        <h2 class="section-title">Toàn Văn 05 Bộ Phụ Lục Kèm Theo Đề Án</h2>
        <p class="section-desc">Hệ thống văn bản phê duyệt, phụ lục phân công nhân sự, dự toán chi tiết và phương án bảo đảm an toàn chính thức của Trường Đại học Văn Hiến.</p>
      </div>

      <!-- Appendix Pill Navigation -->
      <div class="appendix-nav-pill-group">
        <button class="app-tab-btn active" data-app-target="app-1">Phụ Lục 1: Danh sách Nhân sự</button>
        <button class="app-tab-btn" data-app-target="app-2">Phụ Lục 2: Dự toán Chi tiết</button>
        <button class="app-tab-btn" data-app-target="app-3">Phụ Lục 3: Khung Truyền thông</button>
        <button class="app-tab-btn" data-app-target="app-4">Phụ Lục 4: Phương án Rủi ro</button>
        <button class="app-tab-btn" data-app-target="app-5">Phụ Lục 5: Giấy tờ &amp; Thẩm duyệt</button>
      </div>

      <!-- Document Reading Container -->
      <div class="doc-stage-container">
        <div id="app-1" class="app-content-pane active">
          {apps['app1']}
        </div>

        <div id="app-2" class="app-content-pane">
          {apps['app2']}
        </div>

        <div id="app-3" class="app-content-pane">
          {apps['app3']}
        </div>

        <div id="app-4" class="app-content-pane">
          {apps['app4']}
        </div>

        <div id="app-5" class="app-content-pane">
          {apps['app5']}
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 9: REGISTRATION & LIVE TICKET STUDIO -->
  <section id="register-contact" class="section section-register bg-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-pink">{icon('ticket', 'v-icon-sm')} IX. ĐĂNG KÝ VÉ THAM DỰ &amp; LIÊN HỆ BAN TỔ CHỨC</span>
        <h2 class="section-title">Nhận Vé Mời VIP "Passport Sen" Trực Tiếp</h2>
        <p class="section-desc">Số lượng có hạn (300 chỗ ngồi miễn phí dành cho sinh viên và đại biểu khách mời). Nhập thông tin để tạo ngay vé điện tử kèm mã QR cá nhân.</p>
      </div>

      <div class="reg-contact-grid">
        <!-- Registration Form Card -->
        <div class="ticket-form-card">
          <h3 class="form-card-title">
            {icon('ticket', 'v-icon-pink')} Cổng Đăng Ký Vé Trực Tuyến
          </h3>
          <form id="ticket-reg-form">
            <div class="form-group">
              <label for="reg-fullname" class="form-label">Họ và tên người tham dự *</label>
              <input type="text" id="reg-fullname" class="form-control" placeholder="Ví dụ: Nguyễn Văn A" value="Nguyễn Văn A" required>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label for="reg-mssv" class="form-label">Mã số sinh viên (MSSV) *</label>
                <input type="text" id="reg-mssv" class="form-control" placeholder="Ví dụ: 241A010999" value="241A010999" required>
              </div>
              <div class="form-group">
                <label for="reg-faculty" class="form-label">Khoa / Đơn vị *</label>
                <select id="reg-faculty" class="form-control" required>
                  <option value="Khoa Nghệ thuật & Thời trang">Khoa Nghệ thuật &amp; Thời trang</option>
                  <option value="Khoa Du lịch" selected>Khoa Du lịch</option>
                  <option value="Khoa Kinh tế - Quản trị">Khoa Kinh tế - Quản trị</option>
                  <option value="Khoa KHXH & Nhân văn">Khoa KHXH &amp; Nhân văn</option>
                  <option value="Khoa CNTT - Viễn thông">Khoa CNTT - Viễn thông</option>
                  <option value="Đại biểu / Khách mời Doanh nghiệp">Đại biểu / Khách mời Doanh nghiệp</option>
                  <option value="Khoa khác thuộc VHU">Khoa khác thuộc VHU</option>
                </select>
              </div>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label for="reg-email" class="form-label">Địa chỉ Email *</label>
                <input type="email" id="reg-email" class="form-control" placeholder="email@vhu.edu.vn" value="sinhvien@vhu.edu.vn" required>
              </div>
              <div class="form-group">
                <label for="reg-phone" class="form-label">Số điện thoại liên lạc *</label>
                <input type="tel" id="reg-phone" class="form-control" placeholder="090xxxxxxx" value="0908889999" required>
              </div>
            </div>
            <div class="form-group">
              <label class="form-label">Quyền lợi nhận được khi tham dự:</label>
              <div class="privileges-box-small">
                <div class="privilege-line">{icon('check', 'v-icon-sm v-icon-pink')} <span>01 Cuốn Passport Sen check-in các gian hàng tài trợ</span></div>
                <div class="privilege-line">{icon('check', 'v-icon-sm v-icon-pink')} <span>01 Khăn bandana hoa sen 50x50cm độc quyền sự kiện</span></div>
                <div class="privilege-line">{icon('check', 'v-icon-sm v-icon-pink')} <span>Giao lưu trực tiếp cùng Ca sĩ Phương Mỹ Chi &amp; Dàn khách mời danh dự</span></div>
              </div>
            </div>
            <button type="submit" class="btn-hero btn-hero-gold" style="width: 100%; justify-content: center; margin-top: 8px;">
              {icon('sparkles', 'v-icon-sm')} Xác Nhận Đăng Ký &amp; Tạo Vé QR Code
            </button>
          </form>
        </div>

        <!-- Right Side: Live VIP Ticket Simulator & BTC Contact -->
        <div class="ticket-preview-column">
          <!-- Live VIP Ticket Simulator -->
          <div class="live-ticket-card">
            <div class="ticket-holo-header">
              <div class="ticket-header-left">
                <span class="ticket-org-tag">ĐẠI HỌC VĂN HIẾN • HUNGHAU CAMPUS</span>
                <div class="ticket-event-name">CHƯƠNG TRÌNH "CHẠM MỘT SẮC SEN" 2027</div>
              </div>
              <img src="./assets/images/logo-VHU.png" alt="Logo VHU" class="ticket-logo-badge">
            </div>

            <div class="ticket-body-grid">
              <div class="ticket-qr-block">
                <img src="./assets/docx_media/image12.png" alt="QR Code Check-in" class="ticket-qr-img">
                <span class="ticket-code-tag" id="ticket-display-code">VHU-SEN-241A010999</span>
              </div>
              <div class="ticket-details-block">
                <div class="ticket-info-line">
                  <span class="info-label">Khách mời / Sinh viên:</span>
                  <span class="info-val font-bold text-primary" id="ticket-display-name">Nguyễn Văn A</span>
                </div>
                <div class="ticket-info-line">
                  <span class="info-label">MSSV / Mã định danh:</span>
                  <span class="info-val" id="ticket-display-mssv">241A010999</span>
                </div>
                <div class="ticket-info-line">
                  <span class="info-label">Khoa / Đơn vị:</span>
                  <span class="info-val" id="ticket-display-faculty">Khoa Du lịch</span>
                </div>
                <div class="ticket-info-line">
                  <span class="info-label">Vị trí chỗ ngồi:</span>
                  <span class="info-val highlight-gold">Khán Đài A (Ghế VIP Danh Dự)</span>
                </div>
                <div class="ticket-info-line">
                  <span class="info-label">Thời gian check-in:</span>
                  <span class="info-val">07:30 - Ngày 20/06/2027</span>
                </div>
              </div>
            </div>

            <div class="ticket-footer-bar">
              <div class="ticket-status-pill">
                <span class="badge-dot"></span> VÉ MỜI HỢP LỆ • VẬN HÀNH BỞI VHU
              </div>
              <div style="display: flex; gap: 8px;">
                <button type="button" class="btn-ticket-action btn-ticket-print" onclick="printTicket()">
                  {icon('printer', 'v-icon-sm')} In vé này
                </button>
              </div>
            </div>
          </div>

          <!-- Official BTC Contact Card -->
          <div class="contact-info-card" style="margin-top: 24px;">
            <h3>{icon('building', 'v-icon-gold')} Ban Tổ Chức Sự Kiện</h3>
            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 18px;">Trường Đại học Văn Hiến trân trọng kính mời Quý Doanh nghiệp, Đối tác truyền thông và các bạn sinh viên cùng tham gia kiến tạo một ngày hội văn hóa ý nghĩa.</p>

            <div class="contact-item-row">
              <div class="contact-icon">{icon('user', 'v-icon-sm')}</div>
              <div>
                <div style="font-size: 0.74rem; text-transform: uppercase; color: var(--vhu-gold-primary); font-weight: 700;">Đại diện Ban Tổ chức</div>
                <div style="font-size: 0.95rem; font-weight: 800; color: var(--vhu-navy-base);">Bà Trần Thúy Quyên</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">Trưởng Ban Tổ chức Ngày hội</div>
              </div>
            </div>

            <div class="contact-item-row">
              <div class="contact-icon">{icon('phone', 'v-icon-sm')}</div>
              <div>
                <div style="font-size: 0.74rem; text-transform: uppercase; color: var(--vhu-gold-primary); font-weight: 700;">Hotline Hỗ Trợ 24/7</div>
                <div style="font-size: 0.95rem; font-weight: 800; color: var(--vhu-navy-base);">0369.449.925</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">Phòng Công tác Sinh viên &amp; Truyền thông VHU</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Organic Flowing Wave Transition to Footer (Navy) -->
    <div class="section-wave-divider divider-to-footer">
      <svg viewBox="0 0 1440 48" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,48 960,48 1440,0 L1440,48 L0,48 Z" fill="#07152d"/>
      </svg>
    </div>
  </section>

  <!-- Image Lightbox Modal -->
  <dialog id="image-lightbox-dialog" class="lightbox-dialog" aria-label="Xem ảnh phóng to">
    <div class="lightbox-content">
      <button id="lightbox-close-btn" class="lightbox-close" aria-label="Đóng cửa sổ ảnh">&times;</button>
      <img id="lightbox-img" src="" alt="Ảnh phóng to" class="modal-preview-img">
      <div class="lightbox-info">
        <h4 id="lightbox-title">Tiêu đề ảnh</h4>
        <p id="lightbox-caption">Mô tả chi tiết ảnh</p>
      </div>
    </div>
  </dialog>

  <!-- Ticket Result Success Modal -->
  <dialog id="ticket-result-dialog" class="ticket-dialog" aria-label="Thông báo vé sự kiện">
    <div class="ticket-dialog-box">
      <button id="ticket-close-btn" class="lightbox-close" aria-label="Đóng thông báo">&times;</button>
      <div style="text-align: center; margin-bottom: 16px;">
        <div style="display: inline-flex; align-items: center; justify-content: center; width: 56px; height: 56px; border-radius: 50%; background: #dcfce7; color: #166534; margin-bottom: 12px;">
          {icon('check-circle', 'v-icon-lg')}
        </div>
        <h3 style="font-size: 1.35rem; font-weight: 900; color: var(--vhu-navy-base); margin-bottom: 4px;">Đăng Ký Thành Công!</h3>
        <p style="font-size: 0.88rem; color: var(--text-secondary);">Chúc mừng bạn đã sở hữu vé tham dự chương trình "Chạm một sắc Sen" 2027.</p>
      </div>

      <div class="ticket-card-popup">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <div style="font-size: 0.72rem; text-transform: uppercase; color: var(--vhu-gold-light); font-weight: 800;">ĐẠI HỌC VĂN HIẾN • HUNGHAU HOLDINGS</div>
            <div style="font-size: 1.1rem; font-weight: 900; color: #fff;">CHẠM MỘT SẮC SEN 2027</div>
          </div>
          <img src="./assets/images/logo-VHU.png" alt="Logo VHU" style="height: 38px; width: auto; border-radius: 50%;">
        </div>

        <div style="text-align: center;">
          <img src="./assets/docx_media/image12.png" alt="QR Code" class="passport-qr-code">
          <div style="font-size: 1.15rem; font-weight: 900; letter-spacing: 0.1em; color: var(--vhu-gold-light); margin-bottom: 12px;" id="modal-display-code">VHU-SEN-241A010999</div>
        </div>

        <div style="border-top: 1px dashed rgba(255,255,255,0.25); padding-top: 12px; font-size: 0.85rem; line-height: 1.6;">
          <div><strong>Khách mời:</strong> <span id="modal-display-name">Nguyễn Văn A</span></div>
          <div><strong>MSSV / Mã định danh:</strong> <span id="modal-display-mssv">241A010999</span></div>
          <div><strong>Khoa / Đơn vị:</strong> <span id="modal-display-faculty">Khoa Du lịch</span></div>
          <div><strong>Thời gian:</strong> 07:30, Ngày 20/06/2027</div>
          <div><strong>Vị trí:</strong> Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus</div>
        </div>
      </div>

      <div style="display: flex; gap: 10px; margin-top: 14px;">
        <button type="button" class="btn btn-primary" onclick="printTicket()" style="flex: 1; padding: 10px 16px; font-size: 0.88rem; justify-content: center;">
          {icon('printer', 'v-icon-sm')} In vé này
        </button>
      </div>

      <p style="margin-top: 12px; font-size: 0.82rem; color: var(--text-muted); text-align: center;">
        Vui lòng chụp màn hình hoặc lưu mã vé này để quét QR code tại bàn đón tiếp Tầng 9.
      </p>
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
            <img src="./assets/images/logo-VHU.png" alt="Logo VHU" style="height: 48px; width: auto; border-radius: 50%;">
            <div>
              <h4 style="margin: 0; color: #fff;">TRƯỜNG ĐẠI HỌC VĂN HIẾN</h4>
              <div style="font-size: 0.76rem; color: #94a3b8;">VAN HIEN UNIVERSITY</div>
            </div>
          </div>
          <div class="footer-slogan">"THÀNH NHÂN TRƯỚC KHI THÀNH DANH"</div>
          <p style="font-size: 0.86rem; line-height: 1.6; color: #cbd5e1; max-width: 480px;">
            Chương trình Văn hoá &amp; Nghệ thuật tỉnh Đồng Tháp năm 2027 - "Chạm một sắc Sen". Sự kiện văn hóa học đường kết hợp tri thức, bảo tồn di sản sông nước Nam Bộ và hoạt động thiện nguyện xã hội ý nghĩa.
          </p>
        </div>

        <div class="footer-col">
          <h5>Liên Kết Nhanh</h5>
          <ul class="footer-links">
            <li><a href="#overview">Tổng quan sự kiện</a></li>
            <li><a href="#artists">Nghệ sĩ &amp; Di sản</a></li>
            <li><a href="#agenda">Kịch bản chương trình</a></li>
            <li><a href="#media-plan">Kế hoạch truyền thông</a></li>
            <li><a href="#risks-kpi">Quản trị rủi ro &amp; KPI</a></li>
            <li><a href="#budget">Dự trù kinh phí &amp; Tài trợ</a></li>
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

  <!-- Mobile Floating Action Bar (Bottom Navigation) -->
  <div id="mobile-floating-bar" class="mobile-floating-bar">
    <a href="tel:0369449925" class="floating-btn-call" aria-label="Gọi hotline ban tổ chức">
      <svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
      <span>Hotline</span>
    </a>
    <a href="#register-contact" class="floating-btn-ticket">
      <svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg>
      <span>Đăng Ký Vé VIP</span>
    </a>
    <a href="#agenda" id="floating-btn-agenda" class="floating-btn-agenda" aria-label="Xem kịch bản">
      <svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>Kịch bản</span>
    </a>
  </div>

  <!-- Scripts -->
  <script src="./data.js"></script>
  <script src="./script.js"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated index.html successfully! Length: {len(html_content)} chars")
