with open('tools/generate_world_class_site.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''        <div class="budget-legend-grid">
          <div class="legend-item"><span class="legend-color-dot dot-1"></span> <strong>Sân khấu &amp; Kỹ thuật LED:</strong> 40.500.000đ (38.9%)</div>
          <div class="legend-item"><span class="legend-color-dot dot-2"></span> <strong>Nghệ sĩ &amp; Khách mời:</strong> 29.000.000đ (27.9%)</div>
          <div class="legend-item"><span class="legend-color-dot dot-3"></span> <strong>Quà tặng &amp; Ấn phẩm sen:</strong> 21.200.000đ (20.4%)</div>
          <div class="legend-item"><span class="legend-color-dot dot-4"></span> <strong>Truyền thông &amp; Dự phòng 10%:</strong> 13.400.000đ (12.8%)</div>
        </div>'''

replacement = '''        <div class="budget-legend-grid">
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
        </div>'''

if target in text:
    text = text.replace(target, replacement)
    with open('tools/generate_world_class_site.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated legend in generate_world_class_site.py!")
else:
    print("ERROR: target not found in generate_world_class_site.py")
