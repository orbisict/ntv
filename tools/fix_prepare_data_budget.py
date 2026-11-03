with open('tools/prepare_data.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''    <tr class="budget-group-header-row" data-group-code="{h(g['code'])}">
      <td colspan="6" class="budget-group-title">
        {icon('wallet', 'v-icon-sm')} {h(g['name'])} 
        <span class="group-subtotal">(Tiểu kế: {h(g['subtotal'])})</span>
      </td>
    </tr>'''

replacement = '''    <tr class="budget-group-header-row" data-group-code="{h(g['code'])}">
      <td colspan="6" class="budget-group-header-cell">
        <div class="budget-group-title">
          {icon('wallet', 'v-icon-sm')} <span>{h(g['name'])}</span> 
          <span class="group-subtotal">(Tiểu kế: {h(g['subtotal'])})</span>
        </div>
      </td>
    </tr>'''

if target in text:
    text = text.replace(target, replacement)
    with open('tools/prepare_data.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated prepare_data.py budget group header structure!")
else:
    print("ERROR: target not found in prepare_data.py")
