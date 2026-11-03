import re

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Pattern: move backdrop and drawer after </header>
old_block = '''    <!-- Modern Mobile Backdrop & Slide-over Drawer -->
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

    <!-- Reading Progress Bar -->
    <div id="reading-progress-bar" class="reading-progress-bar"></div>
  </header>'''

new_block = '''    <!-- Reading Progress Bar -->
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
  </div>'''

if old_block in code:
    code = code.replace(old_block, new_block, 1)
    with open('tools/generate_world_class_site.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("SUCCESS: Moved drawer out of header in generate_world_class_site.py!")
else:
    print("ERROR: old_block not found in generate_world_class_site.py")
