# Đề Án Văn Hoá & Nghệ Thuật: "Chạm Một Sắc Sen" (2027)
### Trường Đại Học Văn Hiến • Đồng Hành Cùng Tỉnh Đồng Tháp & Hùng Hậu Holdings

Website chính thức công bố và số hóa toàn bộ Đề án Kế hoạch Tổng thể & Đề án Tổ chức Chương trình Giao lưu Văn hóa Dân tộc Tỉnh Đồng Tháp năm 2027 chủ đề **"Chạm Một Sắc Sen"**.

---

## 🌟 Tổng Quan Chương Trình
- **Thời gian tổ chức:** 07:30 – 11:30, Chủ Nhật, Ngày 20/06/2027 (Thời lượng 4 tiếng)
- **Địa điểm:** Hội trường Trần Hưng Đạo (Tầng 9), HungHau Campus (13E Nguyễn Văn Linh, Phong Phú, Nam TP.HCM)
- **Quy mô:** 800 chỗ ngồi (300 đại biểu & sinh viên dự trực tiếp, phủ sóng đa kênh trực tuyến)
- **Khách mời ngôi sao & nghệ nhân:** Ca sĩ Phương Mỹ Chi, Nhà thiết kế Nguyễn Minh Công (BST Áo dài Sen độc quyền), Nghệ nhân CLB Đờn ca tài tử Nam Bộ.
- **Mục tiêu thiện nguyện:** Quyên góp 100% lợi nhuận (dự kiến **200,9 triệu đồng**) trao tặng Trung tâm Bảo trợ Xã hội Tổng hợp Tỉnh Đồng Tháp.

---

## 🎨 Bộ Nhận Diện Thương Hiệu VHU (Brand Guidelines)
- **VHU Navy (Chủ đạo):** `#051024` (Dark), `#0b1f42` (Base), `#153872` (Light)
- **Khuê Văn Các Sun Gold (Biểu tượng tri thức):** `#d49b19`, `#fcd34d`, `#fff9ed`
- **Đồng Tháp Lotus Pink (Sắc Sen hồng):** `#d83a6f`, `#ff7597`, `#fdf2f6`
- **Typography:** *Playfair Display* (Editorial & Cultural Headline) kết hợp *Plus Jakarta Sans* (Body text hiện đại, rõ nét).

---

## 📂 Cấu Trúc Dự Án
```
NTV/
├── index.html            # Trang chủ hoàn chỉnh, tích hợp 8 phần đề án
├── styles.css            # Hệ thống CSS chuẩn quốc tế, Responsive đa thiết bị
├── script.js             # Logic tương tác: Audio soundscape, Bộ lọc kịch bản,
│                         # Tra cứu ngân sách, In vé VIP, Modal toàn văn phụ lục
├── data.js               # Dữ liệu số hóa đầy đủ từ hồ sơ Word gốc (web.docx)
├── assets/
│   ├── docs/             # File đề án gốc (web.docx)
│   ├── docx_media/       # Toàn bộ hình ảnh, poster, standee, phác thảo trích xuất
│   └── images/           # Logo VHU, backdrop sân khấu 3D chính thức
├── tools/                # Bộ công cụ build tự động bằng Python
│   ├── prepare_data.py
│   ├── generate_world_class_site.py
│   ├── build_world_class_css.py
│   └── build_clean_script_js.py
├── .gitignore            # Cấu hình bỏ qua file rác, cache và thư mục tạm
└── README.md             # Tài liệu hướng dẫn dự án
```

---

## 🚀 Hướng Dẫn Chạy & Build Lại Dự Án

### 1. Xem trực tiếp trên trình duyệt
Bạn chỉ cần mở file `index.html` bằng trình duyệt web bất kỳ hoặc dùng extension **Live Server** trong VS Code / IDE.

### 2. Tự động build lại mã nguồn (nếu có chỉnh sửa dữ liệu)
```bash
# 1. Trích xuất và chuẩn bị dữ liệu
python tools/prepare_data.py

# 2. Biên dịch CSS tối ưu
python tools/build_world_class_css.py

# 3. Biên dịch JS tương tác và cơ chế In vé VIP iframe
python tools/build_clean_script_js.py

# 4. Lắp ráp trang HTML tổng thể
python tools/generate_world_class_site.py
```

---

## 💻 Git & Đẩy Mã Nguồn (Push Code)
```bash
git init
git add .
git commit -m "feat: complete Cham Mot Sac Sen 2027 cultural event website"
git branch -M main
git remote add origin <URL_REPOSITORY_CUA_BAN>
git push -u origin main
```
