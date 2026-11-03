import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('html_parts.json', 'r', encoding='utf-8') as f:
    parts = json.load(f)

with open('appendices_html.json', 'r', encoding='utf-8') as f:
    apps = json.load(f)

html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chương trình Văn hoá & Nghệ thuật Tỉnh Đồng Tháp 2027 | Chạm Một Sắc Sen - Đại học Văn Hiến</title>
  <meta name="description" content="Kế hoạch tổng thể và hồ sơ tổ chức Chương trình Văn hoá & Nghệ thuật tỉnh Đồng Tháp năm 2027 'Chạm một sắc Sen' thực hiện bởi Trường Đại học Văn Hiến (VHU).">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./styles.css">
  <link rel="icon" href="./assets/images/logo-VHU.png" type="image/png">
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="top-announcement">
    <div class="container">
      <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
        <span class="announcement-badge">★ SỰ KIỆN VĂN HÓA VHU 2027</span>
        <span>Hồ sơ Kế hoạch Tổng thể & Đề án Tổ chức Chương trình</span>
      </div>
      <div class="top-contact-info">
        <span>📍 HungHau Campus, 13E Nguyễn Văn Linh, Bình Hưng, TP.HCM</span>
        <span>📞 Hotline BTC: 0369.449.925</span>
      </div>
    </div>
  </div>

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

      <!-- Desktop Nav -->
      <nav class="desktop-nav" aria-label="Điều hướng chính">
        <a href="#overview" class="nav-link active">Tổng quan</a>
        <a href="#agenda" class="nav-link">Kịch bản</a>
        <a href="#media-plan" class="nav-link">Truyền thông</a>
        <a href="#risks-kpi" class="nav-link">Rủi ro & KPI</a>
        <a href="#budget" class="nav-link">Ngân sách & Tài trợ</a>
        <a href="#creative" class="nav-link">Thiết kế & Ấn phẩm</a>
        <a href="#appendices" class="nav-link">Hồ sơ & Phụ lục</a>
      </nav>

      <div class="nav-actions">
        <a href="#register-contact" class="btn-header-cta">🎟️ Nhận vé tham dự</a>
        <button class="mobile-menu-toggle" aria-label="Mở thực đơn">☰</button>
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
      <a href="#appendices" class="nav-link">Hồ sơ pháp lý & Phụ lục</a>
      <a href="#register-contact" class="nav-link" style="color: var(--sen-pink); font-weight: bold;">Đăng ký tham dự</a>
    </div>
  </header>

  <!-- Hero Banner -->
  <section class="hero-banner">
    <div class="container hero-content-wrapper">
      <div class="hero-pill-badge">
        🌸 TRƯỜNG ĐẠI HỌC VĂN HIẾN • KẾ HOẠCH TỔ CHỨC 2027
      </div>
      <h1 class="hero-main-title">KẾ HOẠCH CHƯƠNG TRÌNH VĂN HOÁ & NGHỆ THUẬT TỈNH ĐỒNG THÁP NĂM 2027</h1>
      <div class="hero-theme-title">CHỦ ĐỀ: CHẠM MỘT SẮC SEN</div>

      <div class="hero-meta-bar">
        <div class="hero-meta-item">
          <span>⏰ <strong>Thời gian:</strong> 07:30, Chủ Nhật - Ngày 20/06/2027</span>
        </div>
        <div class="hero-meta-item">
          <span>📍 <strong>Địa điểm:</strong> Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus</span>
        </div>
        <div class="hero-meta-item">
          <span>🎓 <strong>Đơn vị thực hiện:</strong> Trường Đại học Văn Hiến</span>
        </div>
      </div>

      <!-- Countdown -->
      <div class="countdown-container">
        <div class="countdown-title">ĐẾM NGƯỢC THỜI GIAN ĐẾN NGÀY HỘI VĂN HÓA</div>
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

      <!-- Hero Buttons -->
      <div class="hero-cta-group">
        <a href="#agenda" class="btn-primary-gold">📋 Xem kịch bản chương trình</a>
        <a href="#budget" class="btn-outline-white">💰 Tra cứu ngân sách & Tài trợ</a>
        <a href="#appendices" class="btn-outline-white">📜 Toàn văn Hồ sơ & Phụ lục</a>
        <a href="#register-contact" class="btn-primary-gold" style="background: var(--sen-pink); color: #fff; box-shadow: var(--shadow-pink);">🎟️ Đăng ký vé miễn phí</a>
      </div>

      <!-- Stats Ribbon -->
      <div class="hero-stats-ribbon">
        <div class="hero-stat-card">
          <div class="stat-icon">👥</div>
          <div class="stat-value">300+</div>
          <div class="stat-label">Khán giả & Khách mời trực tiếp tại Hội trường</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon">📢</div>
          <div class="stat-value">≥ 100.000</div>
          <div class="stat-label">Lượt tiếp cận trên toàn bộ chiến dịch truyền thông</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon">💎</div>
          <div class="stat-value">305 Triệu</div>
          <div class="stat-label">Tổng nguồn tài chính tài trợ vận động được</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon">❤️</div>
          <div class="stat-value">100% Lợi Nhuận</div>
          <div class="stat-label">Quyên góp TT Bảo trợ Xã hội Tổng hợp Đồng Tháp (200,9 Triệu)</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 1: OVERVIEW & OBJECTIVES -->
  <section id="overview" class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">I. THÔNG TIN SỰ KIỆN & MỤC TIÊU</span>
        <h2 class="section-title">Khái Quát Chương Trình & Tôn Chỉ Nhân Văn</h2>
        <p class="section-desc">Chương trình Văn hoá & Nghệ thuật tỉnh Đồng Tháp năm 2027 là sự kiện văn hóa học đường trọng điểm của Đại học Văn Hiến, kết hợp hài hòa tri thức, văn hóa dân tộc và trách nhiệm phụng sự cộng đồng.</p>
      </div>

      <div class="overview-grid">
        <!-- Event Profile Card -->
        <div class="event-profile-card">
          <h3 class="profile-title">🏛️ Thông Tin Sự Kiện Chính Thức</h3>
          <div class="profile-meta-list">
            <div class="meta-row">
              <div class="meta-icon-box">🏷️</div>
              <div>
                <div class="meta-label">Tên chương trình</div>
                <div class="meta-value">Chương trình Văn hoá & Nghệ thuật tỉnh Đồng Tháp năm 2027</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box pink">🌸</div>
              <div>
                <div class="meta-label">Chủ đề chính thức</div>
                <div class="meta-value" style="color: var(--sen-pink); font-weight: 800;">Chạm một sắc Sen</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box">📅</div>
              <div>
                <div class="meta-label">Thời gian tổ chức</div>
                <div class="meta-value">07:30, Chủ Nhật - Ngày 20 tháng 06 năm 2027</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box gold">📍</div>
              <div>
                <div class="meta-label">Địa điểm tổ chức</div>
                <div class="meta-value">Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus, Khu chức năng số 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box">🎓</div>
              <div>
                <div class="meta-label">Đơn vị thực hiện</div>
                <div class="meta-value">Trường Đại học Văn Hiến (Ban Tổ chức Sự kiện)</div>
              </div>
            </div>
            <div class="meta-row">
              <div class="meta-icon-box pink">🎨</div>
              <div>
                <div class="meta-label">Tông màu nhận diện</div>
                <div class="meta-value">Hồng Sen Đồng Tháp, Xanh lá Sen & Xanh dương - Vàng Ánh Kim (Đại học Văn Hiến)</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 7 Core Objectives -->
        <div class="objectives-container">
          <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--vhu-blue-primary); margin-bottom: 4px;">🎯 07 Mục Tiêu Chiến Lược Cốt Lõi</h3>
          
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
          <h3>🌟 Khách Mời Đặc Biệt & Nghệ Sĩ Đồng Hành</h3>
          <p>Chương trình quy tụ dàn khách mời danh dự, nghệ sĩ tên tuổi và các chuyên gia văn hóa hàng đầu, mang đến những phần trình diễn nghệ thuật thăng hoa và những câu chuyện truyền cảm hứng sâu sắc.</p>
          <div class="guest-tags-cloud">
            <span class="guest-tag">🎤 Ca sĩ Phương Mỹ Chi</span>
            <span class="guest-tag">👑 Hoa hậu Nguyễn Thị Yến Nhi</span>
            <span class="guest-tag">👑 Á hậu Lê Phan Hạnh Nguyên</span>
            <span class="guest-tag">👔 Ông Trần Văn Hậu (Chủ tịch HĐQT Hùng Hậu)</span>
            <span class="guest-tag">👗 NTK Nguyễn Minh Công (BST "Miệt Cù Lao")</span>
            <span class="guest-tag">🎶 Nghệ nhân Đờn ca tài tử Nam Bộ</span>
            <span class="guest-tag">🏛️ PGS.TS Nguyễn Minh Đức (ĐH Văn Hiến)</span>
            <span class="guest-tag">🌾 Đại biểu Tỉnh Đồng Tháp</span>
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
        <span class="section-tag tag-pink">II. NỘI DUNG CHƯƠNG TRÌNH</span>
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
        {parts['agenda']}
      </div>
    </div>
  </section>

  <!-- SECTION 3: MEDIA PLAN -->
  <section id="media-plan" class="section">
    <div class="container tab-wrapper">
      <div class="section-header">
        <span class="section-tag tag-gold">III. KẾ HOẠCH TRUYỀN THÔNG</span>
        <h2 class="section-title">Chiến Lược Lan Tỏa Đa Kênh Trong 3 Giai Đoạn</h2>
        <p class="section-desc">Kế hoạch truyền thông bài bản trước, trong và sau sự kiện trên hệ thống Fanpage, TikTok VHU, đối tác công nghệ Orbis ICT, Báo Pháp Luật Việt Nam và Đài PT-TH Đồng Tháp.</p>
      </div>

      <!-- Media Objectives Card -->
      <div class="content-card" style="margin-bottom: 32px; border-left: 4px solid var(--vhu-blue-primary);">
        <h4 style="font-size: 1.15rem; color: var(--vhu-blue-primary); margin-bottom: 12px; font-weight: 800;">🎯 07 Mục Tiêu Truyền Thông Cụ Thể</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; font-size: 0.9rem;">
          <div>✓ Gia tăng nhận diện ĐH Văn Hiến thông qua chương trình “Chạm một sắc Sen”.</div>
          <div>✓ Tôn vinh và lan tỏa tinh thần khát vọng, nỗ lực vươn lên của Chủ tịch Tập đoàn Hùng Hậu.</div>
          <div>✓ Lan tỏa thông điệp thiện nguyện và bảo đảm minh bạch tuyệt đối cho công tác quyên góp.</div>
          <div>✓ Tăng cường kết nối bền chặt giữa VHU với doanh nghiệp, nhà tài trợ và báo chí.</div>
          <div>✓ Khuyến khích người tham gia sáng tạo nội dung chia sẻ kèm hashtag #ChamMotSacSen.</div>
          <div>✓ Thư cảm ơn và quà tặng 100% gửi đến VIP & người tham dự trong 3 ngày sau sự kiện.</div>
          <div>✓ Bảo đảm ít nhất 80% số khách mời xác nhận tham dự thông qua hệ thống vé QR code.</div>
        </div>
      </div>

      <!-- Tabs Header -->
      <div class="tabs-header" data-tab-group="media">
        <button class="tab-btn active" data-target="media-pre">3.3.1 Trước sự kiện (Tiền kỳ)</button>
        <button class="tab-btn" data-target="media-during">3.3.2 Trong sự kiện (20/06)</button>
        <button class="tab-btn" data-target="media-post">3.3.3 Sau sự kiện (Hậu kỳ)</button>
      </div>

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
              {parts['media_pre']}
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
              {parts['media_during']}
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
              {parts['media_post']}
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
        <span class="section-tag tag-pink">IV. QUẢN TRỊ RỦI RO & MA TRẬN KPI</span>
        <h2 class="section-title">Kế Hoạch Phòng Ngừa, Xử Lý Sự Cố & Đo Lường</h2>
        <p class="section-desc">Hệ thống quản trị rủi ro đa chiều từ khâu lập kế hoạch, vận hành thực địa đến truyền thông khủng hoảng và 29 chỉ số KPI đo lường định lượng toàn chiến dịch.</p>
      </div>

      <!-- Search & Filters -->
      <div class="search-filter-bar">
        <div class="search-input-box">
          <span>🔍</span>
          <input type="text" id="risk-search-input" placeholder="Tìm kiếm rủi ro, sự cố hoặc bộ phận phụ trách...">
        </div>
        <div>
          <label for="risk-severity-select" style="font-size: 0.85rem; font-weight: 700; margin-right: 8px;">Mức độ:</label>
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
              {parts['risk_plan']}
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
              {parts['risk_event']}
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
              {parts['risk_media']}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tab 4: KPIs Matrix -->
      <div class="tab-panel" id="risk-tab-kpi" data-tab-group="risks">
        <div class="kpi-grid">
          {parts['kpis']}
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: BUDGET & SPONSORS -->
  <section id="budget" class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag tag-gold">V. DỰ TRÙ KINH PHÍ & NGUỒN TÀI TRỢ</span>
        <h2 class="section-title">Kế Hoạch Cân Đối Tài Chính & Quỹ Thiện Nguyện</h2>
        <p class="section-desc">Minh bạch ngân sách với 68 hạng mục chi tiết, cơ cấu nguồn tài trợ và cam kết trích toàn bộ lợi nhuận ủng hộ Trung tâm Bảo trợ Xã hội Tổng hợp tỉnh Đồng Tháp.</p>
      </div>

      <!-- 3 Master Finance Cards -->
      <div class="finance-overview-grid">
        <div class="finance-kpi-card card-income">
          <div class="card-finance-label">Tổng Nguồn Thu Tài Trợ (5.2)</div>
          <div class="card-finance-value">305.000.000 đ</div>
          <div class="card-finance-note">Gồm Kim Cương (VHU 100tr), Vàng (100tr), Bạc (105tr) + Tài trợ hiện vật</div>
        </div>

        <div class="finance-kpi-card card-expense">
          <div class="card-finance-label">Tổng Chi Phí Dự Toán (5.1)</div>
          <div class="card-finance-value">104.074.748 đ</div>
          <div class="card-finance-note">Chi trực tiếp: 94.613.408 đ + Dự phòng 10% (Đã gồm 8% VAT)</div>
        </div>

        <div class="finance-kpi-card card-charity">
          <div class="card-finance-label">Chênh Lệch Quỹ Thiện Nguyện (5.3)</div>
          <div class="card-finance-value">+ 200.925.252 đ</div>
          <div class="card-finance-note">100% Chuyển giao trao tặng TT Bảo trợ Xã hội Tổng hợp Tỉnh Đồng Tháp</div>
        </div>
      </div>

      <!-- Budget Detail Search & Table -->
      <div style="margin-bottom: 30px;">
        <div class="search-filter-bar">
          <div class="search-input-box">
            <span>🔍</span>
            <input type="text" id="budget-search-input" placeholder="Tìm tên hạng mục (vé, hoa, standee, khách sạn...)...">
          </div>
          <div style="display: flex; align-items: center; gap: 12px;">
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
            <span class="badge badge-primary" id="budget-visible-count">68 hạng mục</span>
          </div>
        </div>

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
              {parts['budget']}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Sponsorship Sources & Privileges Grid -->
      <div class="overview-grid" style="margin-top: 40px;">
        <!-- Sponsors Sources -->
        <div class="content-card">
          <h4 style="font-size: 1.2rem; font-weight: 800; color: var(--vhu-blue-dark); margin-bottom: 16px;">💎 Cơ Cấu Nguồn Thu Tài Trợ (5.2)</h4>
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
                {parts['sponsors']}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Balance summary -->
        <div class="content-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h4 style="font-size: 1.2rem; font-weight: 800; color: var(--vhu-blue-dark); margin-bottom: 16px;">⚖️ Kế Hoạch Cân Đối Thu Chi (5.3)</h4>
            <div class="table-responsive" style="margin-bottom: 16px;">
              <table class="data-table">
                <tbody>
                  <tr>
                    <td><strong>Tổng thu dự kiến:</strong></td>
                    <td style="text-align: right; font-weight: 800; color: var(--vhu-blue-primary);">305.000.000 VNĐ</td>
                  </tr>
                  <tr>
                    <td><strong>Tổng chi phí dự toán:</strong></td>
                    <td style="text-align: right; font-weight: 800; color: var(--text-secondary);">104.074.748 VNĐ</td>
                  </tr>
                  <tr style="background: var(--sen-pink-light);">
                    <td><strong style="color: var(--sen-pink);">Chênh lệch (Quỹ thiện nguyện):</strong></td>
                    <td style="text-align: right; font-weight: 900; color: var(--sen-pink); font-size: 1.15rem;">+ 200.925.252 VNĐ</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p style="font-size: 0.88rem; color: var(--text-secondary); line-height: 1.5;">
              Toàn bộ số tiền thặng dư <strong>200.925.252 VNĐ</strong> sẽ được trao tận tay Trung tâm Bảo trợ Xã hội Tổng hợp tỉnh Đồng Tháp dưới sự chứng kiến của các cơ quan ban ngành và đối tác tài trợ.
            </p>
          </div>
          <div style="margin-top: 14px;">
            <img src="./assets/images/nha-tai-tro.png" alt="Banner nhà tài trợ" style="border-radius: var(--radius-md); box-shadow: var(--shadow-sm); cursor: pointer;" data-lightbox data-src="./assets/images/nha-tai-tro.png" data-title="Key Visual Nhà Tài Trợ" data-caption="Bộ nhận diện tri ân các Nhà tài trợ đồng hành cùng chương trình">
          </div>
        </div>
      </div>

      <!-- Sponsor Privileges Matrix Table -->
      <div class="content-card" style="margin-top: 36px;">
        <h4 style="font-size: 1.2rem; font-weight: 800; color: var(--vhu-blue-dark); margin-bottom: 16px;">🌟 5.4 Bảng Ma Trận Quyền Lợi Nhà Tài Trợ</h4>
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
              {parts['privileges']}
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
        <span class="section-tag tag-pink">X. THIẾT KẾ VÀ ẤN PHẨM TRUYỀN THÔNG</span>
        <h2 class="section-title">Hệ Thống Nhận Diện Hình Ảnh & Không Gian Sự Kiện</h2>
        <p class="section-desc">Bộ ấn phẩm truyền thông toàn diện gồm Poster, Backdrop, Mascot Bé Sen, Standee, Sơ đồ mặt bằng, Quà tặng và Nhạc độc quyền sự kiện.</p>
      </div>

      <!-- Gallery Grid -->
      <div class="gallery-grid">
        <!-- 1. H1. Poster -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image1.png" data-title="H1. Poster" data-caption="Poster quảng bá chính thức Chương trình Văn hóa &amp; Nghệ thuật tỉnh Đồng Tháp năm 2027 'Chạm một sắc Sen'">
            <img src="./assets/docx_media/image1.png" alt="H1. Poster" loading="lazy">
            <span class="gallery-overlay-badge">H1. Poster</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H1. Poster</h4>
              <p class="gallery-item-caption">Poster quảng bá chính thức kết hợp đóa sen Đồng Tháp và biểu tượng Khuê Văn Các Đại học Văn Hiến.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Bộ nhận diện</span>
              <span class="font-bold text-primary">Kích thước A1</span>
            </div>
          </div>
        </div>

        <!-- 2. H1. Poster (Key Visual) -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image2.png" data-title="H1. Poster (Key Visual)" data-caption="Key Visual hình ảnh hoa sen Đồng Tháp kết hợp các nghệ sĩ khách mời và bộ sưu tập áo dài">
            <img src="./assets/docx_media/image2.png" alt="H1. Poster (Key Visual)" loading="lazy">
            <span class="gallery-overlay-badge">H1. Key Visual</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H1. Poster (Key Visual)</h4>
              <p class="gallery-item-caption">Key Visual tôn vinh vẻ đẹp áo dài truyền thống và hình ảnh các nghệ sĩ khách mời đồng hành.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Key Visual</span>
              <span class="font-bold text-primary">Kích thước ngang</span>
            </div>
          </div>
        </div>

        <!-- 3. Danh sách Nhà tài trợ -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image3.png" data-title="Danh sách Nhà tài trợ" data-caption="Bảng nhận diện và tri ân các Nhà tài trợ Kim Cương, Vàng, Bạc và Đơn vị đồng hành">
            <img src="./assets/docx_media/image3.png" alt="Danh sách Nhà tài trợ" loading="lazy">
            <span class="gallery-overlay-badge">Nhà tài trợ</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">Danh sách Nhà tài trợ</h4>
              <p class="gallery-item-caption">Bảng vinh danh và tri ân các đơn vị, doanh nghiệp và đối tác tài trợ đồng hành cùng chương trình.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Quyền lợi</span>
              <span class="font-bold text-primary">Màn hình LED &amp; Backdrop</span>
            </div>
          </div>
        </div>

        <!-- 4. H2. Background sân khấu chính -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image5.jpeg" data-title="H2. Background sân khấu chính" data-caption="Màn hình LED sân khấu chính Hội trường Trần Hưng Đạo quy mô 800 chỗ ngồi Tầng 9">
            <img src="./assets/docx_media/image5.jpeg" alt="H2. Background sân khấu chính" loading="lazy">
            <span class="gallery-overlay-badge">H2. Background</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H2. Background sân khấu chính</h4>
              <p class="gallery-item-caption">Background hiển thị trên màn hình LED lớn tại Hội trường Trần Hưng Đạo cho các tiết mục nghệ thuật.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Sân khấu</span>
              <span class="font-bold text-primary">Màn hình P3</span>
            </div>
          </div>
        </div>

        <!-- 5. H3. Matcos -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image6.jpeg" data-title="H3. Matcos" data-caption="Linh vật sự kiện Bé Gấu VHU &amp; Bé Sen Đồng Tháp">
            <img src="./assets/docx_media/image6.jpeg" alt="H3. Matcos" loading="lazy">
            <span class="gallery-overlay-badge">H3. Matcos</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H3. Matcos</h4>
              <p class="gallery-item-caption">Bộ đôi linh vật biểu trưng Bé Gấu VHU và Bé Sen Đồng Tháp tạo không khí gần gũi, sôi nổi cho sinh viên.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Tương tác</span>
              <span class="font-bold text-primary">Linh vật sự kiện</span>
            </div>
          </div>
        </div>

        <!-- 6. H4. Backdrop -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image4.jpeg" data-title="H4. Backdrop" data-caption="Backdrop check-in và chụp ảnh lưu niệm tại Sảnh đón tiếp">
            <img src="./assets/docx_media/image4.jpeg" alt="H4. Backdrop" loading="lazy">
            <span class="gallery-overlay-badge">H4. Backdrop</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H4. Backdrop</h4>
              <p class="gallery-item-caption">Backdrop chụp ảnh check-in thiết kế 3D cánh sen lớn dành cho khách mời danh dự và sinh viên.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Sảnh đón tiếp</span>
              <span class="font-bold text-primary">Check-in Photo</span>
            </div>
          </div>
        </div>

        <!-- 7. H5. Standee -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image9.jpeg" data-title="H5. Standee" data-caption="Standee chỉ dẫn và phân luồng đặt tại sảnh Campus">
            <img src="./assets/docx_media/image9.jpeg" alt="H5. Standee" loading="lazy">
            <span class="gallery-overlay-badge">H5. Standee</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H5. Standee</h4>
              <p class="gallery-item-caption">Hệ thống standee dọc chỉ dẫn lối vào Hội trường Tầng 9 và thông tin các mốc thời gian chương trình.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Chỉ dẫn</span>
              <span class="font-bold text-primary">0.8m x 1.8m</span>
            </div>
          </div>
        </div>

        <!-- 8. H6. Sơ đồ khu vực Sảnh Trống Đồng -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image8.jpeg" data-title="H6. Sơ đồ khu vực Sảnh Trống Đồng" data-caption="Phối cảnh 3D tổng thể không gian Sảnh Trống Đồng và khu vực gian hàng trải nghiệm">
            <img src="./assets/docx_media/image8.jpeg" alt="H6. Sơ đồ khu vực Sảnh Trống Đồng" loading="lazy">
            <span class="gallery-overlay-badge">H6. Sơ đồ Sảnh</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H6. Sơ đồ khu vực Sảnh Trống Đồng</h4>
              <p class="gallery-item-caption">Phối cảnh tổng thể không gian đón tiếp, các gian hàng doanh nghiệp và khu trải nghiệm văn hóa.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Không gian</span>
              <span class="font-bold text-primary">Phối cảnh 3D</span>
            </div>
          </div>
        </div>

        <!-- 9. H6. Sơ đồ bố trí hội trường Trần Hưng Đạo -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image7.jpeg" data-title="H6. Sơ đồ bố trí hội trường Trần Hưng Đạo" data-caption="Mặt bằng kỹ thuật bố trí sân khấu, phân khu chỗ ngồi đại biểu và lối thoát hiểm">
            <img src="./assets/docx_media/image7.jpeg" alt="H6. Sơ đồ bố trí hội trường Trần Hưng Đạo" loading="lazy">
            <span class="gallery-overlay-badge">H6. Sơ đồ HT</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H6. Sơ đồ bố trí hội trường Trần Hưng Đạo</h4>
              <p class="gallery-item-caption">Sơ đồ kỹ thuật phân khu chỗ ngồi 800 khách, vị trí điều phối âm thanh ánh sáng và an toàn PCCC.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Kỹ thuật</span>
              <span class="font-bold text-primary">Bản vẽ mặt bằng</span>
            </div>
          </div>
        </div>

        <!-- 10. H8. Quà tặng sự kiện -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image10.png" data-title="H8. Quà tặng sự kiện" data-caption="Bộ quà tặng Sen Passport, khăn rằn Nam Bộ độc quyền và ấn phẩm lưu niệm">
            <img src="./assets/docx_media/image10.png" alt="H8. Quà tặng sự kiện" loading="lazy">
            <span class="gallery-overlay-badge">H8. Quà tặng sự kiện</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H8. Quà tặng sự kiện</h4>
              <p class="gallery-item-caption">Bộ ấn phẩm Sen Passport, khăn rằn và các phần quà lưu niệm văn hóa Sen trao tặng khách mời &amp; sinh viên.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Lưu niệm</span>
              <span class="font-bold text-primary">Bộ quà tặng Sen</span>
            </div>
          </div>
        </div>

        <!-- 11. H9. Thư mời & thư cảm ơn -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper" data-lightbox data-src="./assets/docx_media/image11.jpeg" data-title="H9. Thư mời &amp; thư cảm ơn" data-caption="Bộ thiệp Thư Mời đại biểu trang trọng và Thư Cảm Ơn tri ân các đơn vị tài trợ">
            <img src="./assets/docx_media/image11.jpeg" alt="H9. Thư mời &amp; thư cảm ơn" loading="lazy">
            <span class="gallery-overlay-badge">H9. Thư mời</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H9. Thư mời &amp; thư cảm ơn</h4>
              <p class="gallery-item-caption">Thiết kế đồng bộ nhận diện thương hiệu Văn Hiến gửi Lãnh đạo tỉnh, Doanh nghiệp và Đối tác.</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg> Đối ngoại</span>
              <span class="font-bold text-primary">In offset ép kim</span>
            </div>
          </div>
        </div>

        <!-- 12. H9. Nhạc độc quyền sự kiện -->
        <div class="gallery-item-card">
          <div class="gallery-img-wrapper qr-wrapper" data-lightbox data-src="./assets/docx_media/image12.png" data-title="H9. Nhạc độc quyền sự kiện" data-caption="Quét mã QR để nghe ca khúc chủ đề 'Chạm Một Sắc Sen' độc quyền trên điện thoại">
            <img src="./assets/docx_media/image12.png" alt="H9. Nhạc độc quyền sự kiện" class="qr-centered-img" loading="lazy">
            <span class="gallery-overlay-badge">H9. Nhạc sự kiện</span>
          </div>
          <div class="gallery-card-body">
            <div>
              <h4 class="gallery-item-title">H9. Nhạc độc quyền sự kiện</h4>
              <p class="gallery-item-caption">Quét mã QR trực tiếp trên điện thoại để thưởng thức bản phối độc quyền ca khúc chủ đề "Chạm Một Sắc Sen".</p>
            </div>
            <div class="gallery-item-meta">
              <span><svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg> Âm nhạc độc quyền</span>
              <span class="font-bold text-primary">Scan QR Code</span>
            </div>
          </div>
        </div></div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="./data.js"></script>
  <script src="./script.js"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated index.html successfully!")
