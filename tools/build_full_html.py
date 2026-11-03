import json
import html
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('site_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Helper function to escape html
def h(text):
    if text is None:
        return ""
    return html.escape(str(text))

# 1. Agenda HTML
agenda_html = []
for idx, item in enumerate(data['agenda']):
    # Determine type for filtering
    act_lower = item['activity'].lower()
    item_type = 'all'
    is_highlight = False
    if 'khai mạc' in act_lower or 'đón khách' in act_lower or 'giới thiệu' in act_lower:
        item_type += ' opening'
    if 'tiết mục' in act_lower or 'đờn ca tài tử' in act_lower or 'phương mỹ chi' in act_lower:
        item_type += ' art'
        is_highlight = True
    if 'giao lưu' in act_lower:
        item_type += ' talk'
        is_highlight = True
    if 'fashion' in act_lower or 'thời trang' in act_lower:
        item_type += ' fashion'
        is_highlight = True
    if 'tổng kết' in act_lower or 'tiễn khách' in act_lower:
        item_type += ' closing'

    card_class = "timeline-card card-highlight" if is_highlight else "timeline-card"
    node_class = "timeline-node highlight" if is_highlight else "timeline-node"

    agenda_html.append(f"""
    <div class="{node_class}" data-type="{item_type}">
      <div class="timeline-time-badge">{h(item['time'])}</div>
      <div class="timeline-point"></div>
      <div class="{card_class}">
        <div class="timeline-card-header">
          <h4 class="timeline-activity">{h(item['activity'])}</h4>
          <span class="timeline-team-pill">{h(item['team'])}</span>
        </div>
        <p class="timeline-desc">{h(item['content'])}</p>
        <div class="timeline-meta-footer">
          <span>🎵 <strong>Âm thanh:</strong> {h(item['audio'])}</span>
          <span>👥 <strong>Phụ trách:</strong> {h(item['team'])}</span>
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
      <td><strong>{idx+1}</strong></td>
      <td><strong>{h(r['activity'])}</strong></td>
      <td>{h(r['objective'])}</td>
      <td>{h(r['content'])}</td>
      <td><span class="badge badge-info">{h(r['channel'])}</span></td>
      <td><strong>{h(r['time'])}</strong></td>
      <td>{h(r['lead'])}</td>
      <td><span class="badge badge-success">{h(r['kpi'])}</span></td>
    </tr>
    """)
media_pre_str = "\n".join(media_pre_rows)

# During-event table
media_during_rows = []
for idx, r in enumerate(data['media_during']):
    media_during_rows.append(f"""
    <tr>
      <td><strong>{idx+1}</strong></td>
      <td><strong>{h(r['activity'])}</strong></td>
      <td>{h(r['objective'])}</td>
      <td>{h(r['content'])}</td>
      <td><span class="badge badge-info">{h(r['channel'])}</span></td>
      <td><strong>{h(r['time'])}</strong></td>
      <td>{h(r['lead'])}</td>
    </tr>
    """)
media_during_str = "\n".join(media_during_rows)

# Post-event table
media_post_rows = []
for idx, r in enumerate(data['media_post']):
    media_post_rows.append(f"""
    <tr>
      <td><span class="badge badge-primary">{h(r['phase'])}</span></td>
      <td><strong>{h(r['time'])}</strong></td>
      <td><strong>{h(r['activity'])}</strong></td>
      <td>{h(r['content'])}</td>
      <td><span class="badge badge-info">{h(r['channel'])}</span></td>
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
      <td><strong>{h(r['category'])}</strong></td>
      <td><strong>{h(r['risk'])}</strong></td>
      <td>{get_sev_badge(r['severity'])}</td>
      <td>{h(r['prevention'])}</td>
      <td>{h(r['contingency'])}</td>
      <td>{h(r['team'])}</td>
    </tr>
    """)
risk_plan_str = "\n".join(risk_plan_rows)

# Risks Event
risk_event_rows = []
for r in data['risks_event']:
    risk_event_rows.append(f"""
    <tr data-severity="{h(r['severity'])}">
      <td><strong>{h(r['category'])}</strong></td>
      <td><strong>{h(r['risk'])}</strong></td>
      <td>{get_sev_badge(r['severity'])}</td>
      <td>{h(r['prevention'])}</td>
      <td>{h(r['contingency'])}</td>
      <td>{h(r['team'])}</td>
    </tr>
    """)
risk_event_str = "\n".join(risk_event_rows)

# Risks Media
risk_media_rows = []
for r in data['risks_media']:
    risk_media_rows.append(f"""
    <tr data-severity="{h(r['severity'])}">
      <td><span class="badge badge-info">{h(r['category'])}</span></td>
      <td><strong>{h(r['id'])}. {h(r['risk'])}</strong></td>
      <td>{get_sev_badge(r['severity'])}</td>
      <td>{h(r['prevention'])}</td>
      <td>{h(r['contingency'])}</td>
      <td>{h(r['team'])}</td>
    </tr>
    """)
risk_media_str = "\n".join(risk_media_rows)

# KPIs HTML
kpi_cards = []
for k in data['kpis']:
    kpi_cards.append(f"""
    <div class="kpi-card">
      <div>
        <div class="kpi-group-tag">{h(k['group'])}</div>
        <div class="kpi-metric-title">#{h(k['id'])}. {h(k['metric'])}</div>
        <div class="kpi-target-badge">🎯 {h(k['target'])}</div>
      </div>
      <div class="kpi-meta-row">
        <span>⏰ Hạn: {h(k['deadline'])}</span>
        <span>📊 Nguồn: {h(k['source'])}</span>
      </div>
    </div>
    """)
kpis_str = "\n".join(kpi_cards)

# 4. Budget Table HTML
budget_rows = []
for g in data['budget_groups']:
    budget_rows.append(f"""
    <tr class="budget-group-header-row">
      <td colspan="6" style="background: var(--vhu-blue-soft); color: var(--vhu-blue-primary); font-weight: 800; font-size: 0.95rem;">
        📂 {h(g['name'])} (Tiểu kế: <span style="color: var(--sen-pink);">{h(g['subtotal'])}</span>)
      </td>
    </tr>
    """)
    for itm in g['items']:
        budget_rows.append(f"""
        <tr class="budget-item-row" data-group-code="{h(g['code'])}">
          <td><strong>{h(itm['name'])}</strong></td>
          <td style="text-align: center;">{h(itm['quantity'])}</td>
          <td style="text-align: center;">{h(itm['unit'])}</td>
          <td style="text-align: right;">{h(itm['unit_price'])}</td>
          <td style="text-align: right; font-weight: 700; color: var(--vhu-blue-primary);">{h(itm['total_price'])}</td>
          <td style="font-size: 0.82rem; color: var(--text-muted);">{h(itm['notes'])}</td>
        </tr>
        """)
budget_table_str = "\n".join(budget_rows)

# Sponsors Table
sponsor_rows = []
for s in data['sponsors']:
    sponsor_rows.append(f"""
    <tr>
      <td><strong>{h(s['source'])}</strong></td>
      <td style="text-align: center;">{h(s['quantity'])}</td>
      <td style="font-weight: 800; color: var(--vhu-gold-primary); text-align: right;">{h(s['value'])}</td>
      <td>{h(s['unit'])}</td>
    </tr>
    """)
sponsors_table_str = "\n".join(sponsor_rows)

# Privileges Table
privilege_rows = []
for p in data['privileges']:
    privilege_rows.append(f"""
    <tr>
      <td><strong>{h(p['item'])}</strong></td>
      <td style="text-align: center; font-weight: 700; color: #b45309;">{h(p['diamond'])}</td>
      <td style="text-align: center;">{h(p['gold'])}</td>
      <td style="text-align: center;">{h(p['silver'])}</td>
      <td style="text-align: center;">{h(p['partner'])}</td>
    </tr>
    """)
privileges_table_str = "\n".join(privilege_rows)

print("Parsed operations data successfully!")

with open('html_parts.json', 'w', encoding='utf-8') as f:
    json.dump({
        'agenda': agenda_str,
        'media_pre': media_pre_str,
        'media_during': media_during_str,
        'media_post': media_post_str,
        'risk_plan': risk_plan_str,
        'risk_event': risk_event_str,
        'risk_media': risk_media_str,
        'kpis': kpis_str,
        'budget': budget_table_str,
        'sponsors': sponsors_table_str,
        'privileges': privileges_table_str
    }, f, ensure_ascii=False, indent=2)

print("Saved html_parts.json")
