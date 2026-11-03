import json
import html
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import icons
from icons import ICONS

def icon(name, extra_class=''):
    svg = ICONS.get(name, '')
    if extra_class and svg:
        svg = svg.replace('class="v-icon"', f'class="v-icon {extra_class}"')
    return svg

def h(text):
    return html.escape(str(text)) if text is not None else ""

# Load data
with open('site_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Agenda HTML
agenda_html = []
for idx, item in enumerate(data['agenda']):
    act_lower = item['activity'].lower()
    item_type = 'all'
    is_highlight = False
    badge_label = "Chương trình"
    
    if 'khai mạc' in act_lower or 'đón khách' in act_lower or 'giới thiệu' in act_lower:
        item_type += ' opening'
        badge_label = "Nghi lễ & Khai mạc"
    if 'tiết mục' in act_lower or 'đờn ca tài tử' in act_lower or 'phương mỹ chi' in act_lower:
        item_type += ' art'
        is_highlight = True
        badge_label = "Biểu diễn nghệ thuật"
    if 'giao lưu' in act_lower:
        item_type += ' talk'
        is_highlight = True
        badge_label = "Giao lưu chia sẻ"
    if 'fashion' in act_lower or 'thời trang' in act_lower:
        item_type += ' fashion'
        is_highlight = True
        badge_label = "Trình diễn thời trang"
    if 'tổng kết' in act_lower or 'tiễn khách' in act_lower:
        item_type += ' closing'
        badge_label = "Tổng kết & Tri ân"

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

# 2. Media Plans HTML
# Pre-event table
media_pre_rows = []
for idx, r in enumerate(data['media_pre']):
    media_pre_rows.append(f"""
    <tr>
      <td class="text-center font-bold">{idx+1}</td>
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

# During-event table
media_during_rows = []
for idx, r in enumerate(data['media_during']):
    media_during_rows.append(f"""
    <tr>
      <td class="text-center font-bold">{idx+1}</td>
      <td class="font-bold">{h(r['activity'])}</td>
      <td>{h(r['objective'])}</td>
      <td>{h(r['content'])}</td>
      <td><span class="channel-tag">{h(r['channel'])}</span></td>
      <td class="whitespace-nowrap font-semibold">{h(r['time'])}</td>
      <td>{h(r['lead'])}</td>
    </tr>
    """)
media_during_str = "\n".join(media_during_rows)

# Post-event table
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

# 3. Risks HTML
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

# Risks Plan
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

# Risks Event
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

# Risks Media
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

# 4. Budget Table HTML
budget_rows = []
for g in data['budget_groups']:
    budget_rows.append(f"""
    <tr class="budget-group-header-row">
      <td colspan="6" class="budget-group-title">
        {icon('wallet', 'v-icon-sm')} {h(g['name'])} 
        <span class="group-subtotal">(Tiểu kế: {h(g['subtotal'])})</span>
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

print("HTML modules compiled cleanly without emojis!")
