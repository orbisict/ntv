import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('full_document_readable.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Split into appendices based on keywords
idx_app1 = text.find('[P 69] Phụ lục 1.Tờ trình')
idx_app2 = text.find('[P 128] Phụ lục 2 Đơn xin sử dụng địa điểm')
idx_app3 = text.find('[P 163] Phụ lục 3. Biên bản thỏa thuận')
idx_app4 = text.find('[P 223] Phụ lục 4. Công văn thông báo')
idx_app5 = text.find('[P 244] Phụ lục 5. Công văn thông báo')

app1_text = text[idx_app1:idx_app2].strip()
app2_text = text[idx_app2:idx_app3].strip()
app3_text = text[idx_app3:idx_app4].strip()
app4_text = text[idx_app4:idx_app5].strip()
app5_text = text[idx_app5:].strip()

print(f"App 1 len: {len(app1_text)}")
print(f"App 2 len: {len(app2_text)}")
print(f"App 3 len: {len(app3_text)}")
print(f"App 4 len: {len(app4_text)}")
print(f"App 5 len: {len(app5_text)}")

appendices = {
    'app1': app1_text,
    'app2': app2_text,
    'app3': app3_text,
    'app4': app4_text,
    'app5': app5_text
}

with open('appendices_raw.json', 'w', encoding='utf-8') as f:
    json.dump(appendices, f, ensure_ascii=False, indent=2)

print("Saved appendices_raw.json")
