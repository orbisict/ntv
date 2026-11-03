import re

with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update stacked-bar in generate_world_class_site.py
old_stacked_bar = '''        <div class="stacked-bar">
          <div class="bar-segment seg-1" style="width: 38.9%;" title="Sân khấu & Kỹ thuật: 38.9%">38.9% Sân khấu &amp; LED</div>
          <div class="bar-segment seg-2" style="width: 27.9%;" title="Nghệ sĩ & Nhân sự: 27.9%">27.9% Nghệ sĩ</div>
          <div class="bar-segment seg-3" style="width: 20.4%;" title="Ấn phẩm & Quà tặng: 20.4%">20.4% Trải nghiệm</div>
          <div class="bar-segment seg-4" style="width: 12.8%;" title="Truyền thông & Dự phòng: 12.8%">12.8% Dự phòng</div>
        </div>'''

new_stacked_bar = '''        <div class="stacked-bar" role="progressbar" aria-label="Cơ cấu phân bổ chi phí 104.100.000 VNĐ">
          <div class="bar-segment seg-1" style="width: 38.9%;" title="Sân khấu &amp; Kỹ thuật LED: 40.500.000đ (38.9%)"></div>
          <div class="bar-segment seg-2" style="width: 27.9%;" title="Nghệ sĩ &amp; Khách mời: 29.000.000đ (27.9%)"></div>
          <div class="bar-segment seg-3" style="width: 20.4%;" title="Quà tặng &amp; Ấn phẩm sen: 21.200.000đ (20.4%)"></div>
          <div class="bar-segment seg-4" style="width: 12.8%;" title="Truyền thông &amp; Dự phòng 10%: 13.400.000đ (12.8%)"></div>
        </div>'''

if old_stacked_bar in code:
    code = code.replace(old_stacked_bar, new_stacked_bar, 1)
    print("SUCCESS: Updated stacked-bar in generator!")
else:
    print("WARNING: old_stacked_bar not found exactly")

# 2. Update divider-overview-to-navy wave curve
old_wave = '''    <!-- Organic Flowing Wave Transition to Artists Section (Navy) -->
    <div class="section-wave-divider divider-overview-to-navy">
      <svg viewBox="0 0 1440 68" fill="none" preserveAspectRatio="none">
        <path d="M0,24 C320,68 720,10 1120,52 C1280,66 1380,38 1440,24 L1440,68 L0,68 Z" fill="#071630"/>
      </svg>
    </div>'''

new_wave = '''    <!-- Organic Flowing Wave Transition to Artists Section (Navy) -->
    <div class="section-wave-divider divider-overview-to-navy">
      <svg viewBox="0 0 1440 40" fill="none" preserveAspectRatio="none">
        <path d="M0,0 C480,40 960,40 1440,0 L1440,40 L0,40 Z" fill="#071630"/>
      </svg>
    </div>'''

if old_wave in code:
    code = code.replace(old_wave, new_wave, 1)
    print("SUCCESS: Updated wave transition in generator!")
else:
    print("WARNING: old_wave not found exactly")

# 3. Update finance card values to VNĐ
old_finance = '''      <div class="finance-overview-grid">
        <div class="finance-kpi-card card-income">
          <div class="card-finance-label">{icon('wallet', 'v-icon-sm')} Tổng Nguồn Thu Vận Động</div>
          <div class="card-finance-value">305.000.000 đ</div>
          <div class="card-finance-note">Gồm 260.000.000đ tài trợ doanh nghiệp &amp; 45.000.000đ từ gian hàng, vé</div>
        </div>
        <div class="finance-kpi-card card-expense">
          <div class="card-finance-label">{icon('clipboard-list', 'v-icon-sm')} Tổng Dự Toán Chi Phí</div>
          <div class="card-finance-value">104.100.000 đ</div>
          <div class="card-finance-note">Tổng định mức chi phí tổ chức 9 nhóm (Đã gồm 10% dự phòng)</div>
        </div>
        <div class="finance-kpi-card card-charity">
          <div class="card-finance-label">{icon('heart', 'v-icon-sm')} Quỹ Thiện Nguyện Đồng Tháp</div>
          <div class="card-finance-value">200.900.000 đ</div>
          <div class="card-finance-note">100% Lợi nhuận trao tặng Trung tâm Bảo trợ Xã hội Đồng Tháp</div>
        </div>
      </div>'''

new_finance = '''      <div class="finance-overview-grid">
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
      </div>'''

if old_finance in code:
    code = code.replace(old_finance, new_finance, 1)
    print("SUCCESS: Updated finance cards in generator!")
else:
    print("WARNING: old_finance not found exactly")

with open('tools/generate_world_class_site.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved tools/generate_world_class_site.py!")
