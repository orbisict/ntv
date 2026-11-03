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

import re

# Load raw appendices
with open('tools/appendices_html.json', 'r', encoding='utf-8') as f:
    apps_raw = json.load(f)

apps = {}
for k, v in apps_raw.items():
    cleaned = v
    # Strip any inline display:none on containers
    cleaned = re.sub(r'style=[\'"]display:\s*none;?[\'"]', '', cleaned)
    
    # Wire up copy and print buttons
    cleaned = cleaned.replace('class="btn-doc-action btn-copy-doc"', 'class="btn-doc-action btn-copy-doc" onclick="copyActiveAppendix(this)"')
    cleaned = cleaned.replace('class="btn-doc-action btn-print-doc"', 'class="btn-doc-action btn-print-doc" onclick="printActiveAppendix()"')
    
    cleaned = cleaned.replace('📋 Sao chép toàn văn', f"{icon('copy', 'v-icon-sm')} Sao chép toàn văn")
    cleaned = cleaned.replace('🖨️ In văn bản này', f"{icon('printer', 'v-icon-sm')} In văn bản này")
    sig_replacement = f'''
      <div class="digital-seal-container">
        <div class="official-signature-script">Trần Thúy Quyên</div>
        <div class="digital-qr-verify">
          <img src="./assets/docx_media/image13.png" alt="Mã QR xác thực số" class="stamp-seal-img">
          <span class="qr-label">Mã QR số hóa tra cứu hồ sơ gốc</span>
        </div>
      </div>
    '''
    cleaned = cleaned.replace('<img src="./assets/docx_media/image13.png" alt="Dấu mộc xác thực" class="stamp-seal-img">', sig_replacement)
    for em in ['📋', '🖨️', '🌸', '🏛️', '🏢', '👗', '🛡️', '📄', '🎟️', '⭐', '★']:
        cleaned = cleaned.replace(em, '')
    apps[k] = cleaned

# 1. Agenda Timeline
agenda_html = []
for idx, item in enumerate(data['agenda']):
    item_type = 'all'
    is_highlight = False
    badge_label = "Chương trình"
    
    # Accurate timeline phases matching the 11 items from official proposal
    if idx <= 3:
        item_type += ' phase-1'
    elif idx <= 6:
        item_type += ' phase-2'
    else:
        item_type += ' phase-3'

    if idx == 0:
        badge_label = "Đón tiếp & Check-in"
    elif idx == 1:
        badge_label = "Tiết mục mở màn"
        is_highlight = True
    elif idx == 2:
        badge_label = "Giới thiệu đại biểu"
    elif idx == 3:
        badge_label = "Phát biểu khai mạc"
    elif idx == 4:
        badge_label = "Di sản UNESCO Đờn ca tài tử"
        is_highlight = True
    elif idx == 5:
        badge_label = "Tọa đàm truyền cảm hứng"
        is_highlight = True
    elif idx == 6:
        badge_label = "Đối thoại sinh viên Q&A"
    elif idx == 7:
        badge_label = "Fashion Show Áo Dài Sen"
        is_highlight = True
    elif idx == 8:
        badge_label = "Ngôi sao biểu diễn"
        is_highlight = True
    elif idx == 9:
        badge_label = "Lễ Tổng kết & Tri ân"
    elif idx == 10:
        badge_label = "Bế mạc & Tiễn khách"

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
    <tr class="budget-group-header-row" data-group-code="{h(g['code'])}">
      <td colspan="6" class="budget-group-header-cell">
        <div class="budget-group-title">
          {icon('wallet', 'v-icon-sm')} <span>{h(g['name'])}</span> 
          <span class="group-subtotal">(Tiểu kế: {h(g['subtotal'])})</span>
        </div>
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

print("Data structures parsed ready for HTML assembly!")
