import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('full_document_readable.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect headings and their line ranges
lines = text.split('\n')
for i, l in enumerate(lines):
    if l.startswith('[P ') or l.startswith('--- [TABLE'):
        # Check if it looks like a heading
        if any(keyword in l for keyword in ['KẾ HOẠCH', 'THÔNG TIN', 'NỘI DUNG', 'TRUYỀN THÔNG', 'QUẢN TRỊ RỦI RO', 'DỰ TRÙ KINH PHÍ', 'NGUỒN TÀI TRỢ', 'QUYỀN LỢI', 'Thiết kế', 'Phụ lục', 'TỜ TRÌNH', 'PHIẾU ĐĂNG KÝ', 'HỢP ĐỒNG', 'CÔNG VĂN', 'CAM KẾT']):
            print(f"L{i:03d}: {l[:100]}")
