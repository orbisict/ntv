import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/generate_modern_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

p1 = text.find('<!-- Hero Banner')
p2 = text.find('<!-- SECTION 1: OVERVIEW')

if p1 == -1 or p2 == -1:
    print('Error finding indices!')
    sys.exit(1)

new_hero = """<!-- Hero Banner (Expansive Widescreen 2-Column Split Layout) -->
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

  """

updated_text = text[:p1] + new_hero + text[p2:]
with open('tools/generate_modern_site.py', 'w', encoding='utf-8') as f:
    f.write(updated_text)

print('Updated tools/generate_modern_site.py successfully!')
