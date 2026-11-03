import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    js_code = f.read()

pos1 = js_code.find('function printTicket()')
pos2 = js_code.find('// Global window assignments')

assert pos1 != -1 and pos2 != -1, f"pos1={pos1}, pos2={pos2}"

# Extract the existing printTicket and printActiveAppendix to preserve all styles and HTML
section_to_replace = js_code[pos1:pos2]

# In printTicket, change the printWindow logic to use printHtmlViaFrame
# Let's inspect the exact lines to replace
old_window_open_ticket = """  const printWindow = window.open('', '_blank', 'width=960,height=720');
  if (!printWindow) {
    alert('Vui lòng cho phép mở pop-up trong trình duyệt để in vé!');
    return;
  }"""

new_window_open_ticket = """  // Use invisible iframe to bypass popup blocker and prevent printing the full site
  function printViaIframe(content) {
    let frame = document.getElementById('print-isolated-iframe');
    if (!frame) {
      frame = document.createElement('iframe');
      frame.id = 'print-isolated-iframe';
      frame.style.position = 'fixed';
      frame.style.right = '0';
      frame.style.bottom = '0';
      frame.style.width = '0';
      frame.style.height = '0';
      frame.style.border = 'none';
      document.body.appendChild(frame);
    }
    const doc = frame.contentWindow.document;
    doc.open();
    doc.write(content);
    doc.close();
    setTimeout(() => {
      try {
        frame.contentWindow.focus();
        frame.contentWindow.print();
      } catch (e) {
        const win = window.open('', '_blank');
        if (win) {
          win.document.open();
          win.document.write(content);
          win.document.close();
          win.focus();
          setTimeout(() => { win.print(); win.close(); }, 400);
        }
      }
    }, 400);
  }"""

old_window_write_ticket = """  printWindow.document.open();
  printWindow.document.write(html);
  printWindow.document.close();"""

new_window_write_ticket = """  printViaIframe(html);"""

old_window_open_app = """  const printWindow = window.open('', '_blank', 'width=900,height=850');
  if (!printWindow) {
    alert('Vui lòng cho phép mở pop-up trong trình duyệt để in văn bản!');
    return;
  }"""

new_window_open_app = """  // Print via isolated iframe"""

old_window_write_app = """  printWindow.document.open();
  printWindow.document.write(html);
  printWindow.document.close();"""

new_window_write_app = """  let frame = document.getElementById('print-isolated-iframe');
  if (!frame) {
    frame = document.createElement('iframe');
    frame.id = 'print-isolated-iframe';
    frame.style.position = 'fixed';
    frame.style.right = '0';
    frame.style.bottom = '0';
    frame.style.width = '0';
    frame.style.height = '0';
    frame.style.border = 'none';
    document.body.appendChild(frame);
  }
  const doc = frame.contentWindow.document;
  doc.open();
  doc.write(html);
  doc.close();
  setTimeout(() => {
    try {
      frame.contentWindow.focus();
      frame.contentWindow.print();
    } catch (e) {
      window.print();
    }
  }, 400);"""

section_updated = section_to_replace
assert old_window_open_ticket in section_updated, "old_window_open_ticket not found"
section_updated = section_updated.replace(old_window_open_ticket, new_window_open_ticket, 1)

assert old_window_write_ticket in section_updated, "old_window_write_ticket not found"
section_updated = section_updated.replace(old_window_write_ticket, new_window_write_ticket, 1)

assert old_window_open_app in section_updated, "old_window_open_app not found"
section_updated = section_updated.replace(old_window_open_app, new_window_open_app, 1)

assert old_window_write_app in section_updated, "old_window_write_app not found"
section_updated = section_updated.replace(old_window_write_app, new_window_write_app, 1)

js_code = js_code[:pos1] + section_updated + js_code[pos2:]

with open('tools/build_clean_script_js.py', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("SUCCESS: Updated tools/build_clean_script_js.py with iframe printing!")
