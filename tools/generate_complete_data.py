import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('document_structure.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

# 1. Timeline (Table 17)
tbl_agenda = elements[17]['rows']
agenda_items = []
for row in tbl_agenda[1:]:
    agenda_items.append({
        'time': row[0]['text'].replace('\n', ' ').strip(),
        'activity': row[1]['text'].replace('\n', ' ').strip(),
        'content': row[2]['text'].strip(),
        'audio': row[3]['text'].replace('\n', ' ').strip(),
        'team': row[4]['text'].replace('\n', ' ').strip()
    })

# 2. Media Plans:
# Table 29: Pre-event
tbl_media_pre = elements[29]['rows']
media_pre = []
for row in tbl_media_pre[1:]:
    media_pre.append({
        'activity': row[0]['text'].replace('\n', ' ').strip(),
        'objective': row[1]['text'].replace('\n', ' ').strip(),
        'content': row[2]['text'].replace('\n', ' ').strip(),
        'channel': row[3]['text'].replace('\n', ' ').strip(),
        'time': row[4]['text'].replace('\n', ' ').strip(),
        'lead': row[5]['text'].replace('\n', ' ').strip(),
        'kpi': row[6]['text'].replace('\n', ' ').strip() if len(row) > 6 else ''
    })

# Table 31: During-event
tbl_media_during = elements[31]['rows']
media_during = []
for row in tbl_media_during[1:]:
    media_during.append({
        'activity': row[0]['text'].replace('\n', ' ').strip(),
        'objective': row[1]['text'].replace('\n', ' ').strip(),
        'content': row[2]['text'].replace('\n', ' ').strip(),
        'channel': row[3]['text'].replace('\n', ' ').strip(),
        'time': row[4]['text'].replace('\n', ' ').strip(),
        'lead': row[5]['text'].replace('\n', ' ').strip()
    })

# Table 33: Post-event
tbl_media_post = elements[33]['rows']
media_post = []
curr_phase = "A. Cảm ơn và lan tỏa"
for row in tbl_media_post[1:]:
    p_text = row[0]['text'].replace('\n', ' ').strip()
    if p_text:
        curr_phase = p_text
    media_post.append({
        'phase': curr_phase,
        'time': row[1]['text'].replace('\n', ' ').strip(),
        'activity': row[2]['text'].replace('\n', ' ').strip(),
        'content': row[3]['text'].replace('\n', ' ').strip(),
        'channel': row[4]['text'].replace('\n', ' ').strip(),
        'lead': row[5]['text'].replace('\n', ' ').strip()
    })

# 3. Risks:
# Table 36: Plan Risks
tbl_risk_plan = elements[36]['rows']
risks_plan = []
curr_cat_plan = ""
for row in tbl_risk_plan[1:]:
    c_text = row[0]['text'].replace('\n', ' ').strip()
    if c_text:
        curr_cat_plan = c_text
    risks_plan.append({
        'category': curr_cat_plan,
        'risk': row[1]['text'].replace('\n', ' ').strip(),
        'severity': row[2]['text'].replace('\n', ' ').strip(),
        'prevention': row[3]['text'].strip(),
        'contingency': row[4]['text'].strip(),
        'team': row[5]['text'].replace('\n', ' ').strip()
    })

# Table 38: Event Risks
tbl_risk_event = elements[38]['rows']
risks_event = []
curr_cat_event = ""
for row in tbl_risk_event[1:]:
    c_text = row[0]['text'].replace('\n', ' ').strip()
    if c_text:
        curr_cat_event = c_text
    risks_event.append({
        'category': curr_cat_event,
        'risk': row[1]['text'].replace('\n', ' ').strip(),
        'severity': row[2]['text'].replace('\n', ' ').strip(),
        'prevention': row[3]['text'].strip(),
        'contingency': row[4]['text'].strip(),
        'team': row[5]['text'].replace('\n', ' ').strip()
    })

# Table 40: Media Risks
tbl_risk_media = elements[40]['rows']
risks_media = []
curr_cat_media = "A. Nội dung và thông điệp"
for row in tbl_risk_media[1:]:
    if len(row) == 1 or len(row) < 5:
        curr_cat_media = row[0]['text'].replace('\n', ' ').strip()
        continue
    risks_media.append({
        'category': curr_cat_media,
        'id': row[0]['text'].replace('\n', ' ').strip(),
        'risk': row[1]['text'].replace('\n', ' ').strip(),
        'severity': row[2]['text'].replace('\n', ' ').strip(),
        'prevention': row[3]['text'].strip(),
        'contingency': row[4]['text'].strip(),
        'team': row[5]['text'].replace('\n', ' ').strip() if len(row) > 5 else ''
    })

# Table 42: Media KPIs
tbl_kpi = elements[42]['rows']
kpis = []
curr_group_kpi = ""
for row in tbl_kpi[1:]:
    cells = [c['text'].replace('\n', ' ').strip() for c in row]
    if len(cells) == 1 or not cells[0].isdigit():
        curr_group_kpi = cells[0]
        continue
    kpis.append({
        'group': curr_group_kpi,
        'id': cells[0],
        'metric': cells[1] if len(cells) > 1 else '',
        'target': cells[2] if len(cells) > 2 else '',
        'deadline': cells[3] if len(cells) > 3 else '',
        'source': cells[4] if len(cells) > 4 else ''
    })

# 4. Budget (Table 45)
tbl_budget = elements[45]['rows']
budget_groups = []
curr_group = None

for row in tbl_budget[1:]:
    cells = [c['text'].replace('\n', ' ').strip() for c in row]
    first_col = cells[0]
    if any(first_col.startswith(p) for p in ['A.', 'B.', 'C.', 'D.', 'E.', 'F.', 'G.', 'H.', 'I.', 'K.']) and len(cells) <= 2:
        curr_group = {
            'code': first_col.split('.')[0].strip(),
            'name': first_col,
            'items': [],
            'subtotal': ''
        }
        budget_groups.append(curr_group)
    elif 'CỘNG NHÓM' in first_col:
        subtotal_val = cells[4] if len(cells) > 4 and cells[4] else (cells[-1] if cells else '')
        if curr_group:
            curr_group['subtotal'] = subtotal_val
    elif 'TỔNG CHI PHÍ TRỰC TIẾP' in first_col or 'TỔNG CỘNG' in first_col:
        continue
    else:
        if len(cells) >= 5 and cells[0]:
            item = {
                'name': cells[0],
                'quantity': cells[1] if len(cells) > 1 else '',
                'unit': cells[2] if len(cells) > 2 else '',
                'unit_price': cells[3] if len(cells) > 3 else '',
                'total_price': cells[4] if len(cells) > 4 else '',
                'notes': cells[5] if len(cells) > 5 else ''
            }
            if curr_group:
                curr_group['items'].append(item)

# Table 47: Sponsorship sources
tbl_sponsor = elements[47]['rows']
sponsors = []
for row in tbl_sponsor[1:]:
    cells = [c['text'].replace('\n', ' ').strip() for c in row]
    if len(cells) >= 4:
        sponsors.append({
            'source': cells[0],
            'quantity': cells[1],
            'value': cells[2],
            'unit': cells[3]
        })

# Table 49: Financial Balance
tbl_balance = elements[49]['rows']
balance = []
for row in tbl_balance[1:]:
    cells = [c['text'].replace('\n', ' ').strip() for c in row]
    if len(cells) >= 2:
        balance.append({'item': cells[0], 'amount': cells[1]})

# Table 51: Sponsor Privileges
tbl_privileges = elements[51]['rows']
privileges = []
for row in tbl_privileges[1:]:
    cells = [c['text'].replace('\n', ' ').strip() for c in row]
    if len(cells) >= 5:
        privileges.append({
            'item': cells[0],
            'diamond': cells[1],
            'gold': cells[2],
            'silver': cells[3],
            'partner': cells[4]
        })

# Load raw appendices
with open('appendices_raw.json', 'r', encoding='utf-8') as f:
    app_data = json.load(f)

site_data = {
    'agenda': agenda_items,
    'media_pre': media_pre,
    'media_during': media_during,
    'media_post': media_post,
    'risks_plan': risks_plan,
    'risks_event': risks_event,
    'risks_media': risks_media,
    'kpis': kpis,
    'budget_groups': budget_groups,
    'sponsors': sponsors,
    'balance': balance,
    'privileges': privileges,
    'appendices_raw': app_data
}

with open('site_data.json', 'w', encoding='utf-8') as f:
    json.dump(site_data, f, ensure_ascii=False, indent=2)

js_content = "window.SITE_DATA = " + json.dumps(site_data, ensure_ascii=False, indent=2) + ";\n"
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Exported site_data.json and data.js successfully!")
print(f"- Agenda: {len(agenda_items)} items")
print(f"- Media Pre: {len(media_pre)}, During: {len(media_during)}, Post: {len(media_post)}")
print(f"- Risks Plan: {len(risks_plan)}, Event: {len(risks_event)}, Media: {len(risks_media)}")
print(f"- KPIs: {len(kpis)}")
print(f"- Budget Groups: {len(budget_groups)}")
print(f"- Sponsors: {len(sponsors)}, Balance: {len(balance)}, Privileges: {len(privileges)}")
