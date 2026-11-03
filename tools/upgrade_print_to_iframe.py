import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    js_code = f.read()

# Replace printTicket and printActiveAppendix
target_code = """  const printWindow = window.open('', '_blank', 'width=960,height=720');
  if (!printWindow) {
    alert('Vui lòng cho phép mở pop-up trong trình duyệt để in vé!');
    return;
  }"""

assert target_code in js_code, "target_code not found in build_clean_script_js.py"

# Define the helper function and new printTicket / printActiveAppendix
old_full_print_section = """function printTicket() {
  const nameInput = document.getElementById('reg-fullname');
  const mssvInput = document.getElementById('reg-mssv');
  const facultyInput = document.getElementById('reg-faculty');

  const name = (nameInput?.value || document.getElementById('ticket-display-name')?.textContent || 'Nguyễn Văn A').trim();
  const mssv = (mssvInput?.value || document.getElementById('ticket-display-mssv')?.textContent || '241A010999').trim();
  const faculty = (facultyInput?.value || document.getElementById('ticket-display-faculty')?.textContent || 'Khoa Du lịch').trim();
  const code = 'VHU-SEN-' + mssv.toUpperCase();

  const origin = window.location.origin;
  const logoUrl = origin && origin !== 'null' ? origin + '/assets/images/logo-VHU.png' : './assets/images/logo-VHU.png';
  const qrUrl = origin && origin !== 'null' ? origin + '/assets/docx_media/image12.png' : './assets/docx_media/image12.png';

  const printWindow = window.open('', '_blank', 'width=960,height=720');
  if (!printWindow) {
    alert('Vui lòng cho phép mở pop-up trong trình duyệt để in vé!');
    return;
  }

  const html = `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <title>Vé Mời VIP "Passport Sen" - ĐH Văn Hiến 2027</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 12mm 12mm;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    body {
      background: #f8fafc;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #0b1f42;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 16px;
    }
    .ticket-sheet {
      width: 100%;
      max-width: 820px;
      margin: 0 auto;
    }
    
    .vip-ticket-container {
      background: #ffffff;
      border: 2px solid #0b1f42;
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(11,31,66,0.12);
      display: flex;
      position: relative;
      margin-bottom: 24px;
    }

    .ticket-main-section {
      flex: 1;
      padding: 22px 26px;
      border-right: 2px dashed #cbd5e1;
      position: relative;
      background: #ffffff;
    }
    .ticket-stub-section {
      width: 240px;
      background: #f8fafc;
      padding: 20px 18px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      text-align: center;
      border-left: 2px dashed #cbd5e1;
      margin-left: -2px;
    }

    .ticket-brand {
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 12px;
      margin-bottom: 14px;
    }
    .ticket-logo {
      height: 48px;
      width: auto;
    }
    .ticket-title-group h2 {
      font-size: 1.05rem;
      font-weight: 800;
      color: #0b1f42;
      letter-spacing: 0.02em;
    }
    .ticket-title-group p {
      font-size: 0.72rem;
      color: #d49b19;
      font-weight: 700;
    }

    .ticket-event-name {
      margin-bottom: 14px;
    }
    .ticket-event-label {
      font-size: 0.7rem;
      text-transform: uppercase;
      font-weight: 800;
      letter-spacing: 0.08em;
      color: #d83a6f;
    }
    .ticket-event-title {
      font-size: 1.45rem;
      font-weight: 900;
      color: #0b1f42;
      line-height: 1.2;
    }

    .ticket-details-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      background: #f8fafc;
      padding: 12px 14px;
      border-radius: 12px;
      margin-bottom: 12px;
    }
    .detail-item .label {
      font-size: 0.68rem;
      text-transform: uppercase;
      font-weight: 700;
      color: #64748b;
    }
    .detail-item .value {
      font-size: 0.88rem;
      font-weight: 800;
      color: #0b1f42;
    }

    .ticket-qr-block {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .ticket-qr-block img {
      width: 140px;
      height: 140px;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 4px;
      background: #ffffff;
      margin-bottom: 6px;
    }
    .ticket-code {
      font-family: monospace;
      font-size: 0.82rem;
      font-weight: 800;
      color: #0b1f42;
      letter-spacing: 0.06em;
    }

    .print-tip {
      font-size: 0.75rem;
      color: #64748b;
      margin-top: 10px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="ticket-sheet">
    <div class="vip-ticket-container">
      <div class="ticket-main-section">
        <div class="ticket-brand">
          <img src="${logoUrl}" alt="Logo VHU" class="ticket-logo">
          <div class="ticket-title-group">
            <h2>TRƯỜNG ĐẠI HỌC VĂN HIẾN</h2>
            <p>HUNGHAU CAMPUS • NĂM 2027</p>
          </div>
        </div>

        <div class="ticket-event-name">
          <div class="ticket-event-label">Vé Tham Dự Chính Thức</div>
          <div class="ticket-event-title">CHƯƠNG TRÌNH "CHẠM MỘT SẮC SEN"</div>
        </div>

        <div class="ticket-details-grid">
          <div class="detail-item">
            <div class="label">Khách mời / Sinh viên</div>
            <div class="value">${name}</div>
          </div>
          <div class="detail-item">
            <div class="label">MSSV / Mã định danh</div>
            <div class="value">${mssv}</div>
          </div>
          <div class="detail-item">
            <div class="label">Khoa / Đơn vị</div>
            <div class="value">${faculty}</div>
          </div>
          <div class="detail-item">
            <div class="label">Vị trí chỗ ngồi</div>
            <div class="value" style="color: #d49b19;">Khán Đài A (Ghế VIP Danh Dự)</div>
          </div>
          <div class="detail-item">
            <div class="label">Thời gian check-in</div>
            <div class="value">07:30 - Ngày 20/06/2027</div>
          </div>
          <div class="detail-item">
            <div class="label">Địa điểm diễn ra</div>
            <div class="value">Tầng 9, Hội trường Trần Hưng Đạo</div>
          </div>
        </div>

        <div style="font-size: 0.7rem; color: #64748b;">
          * Quý khách vui lòng xuất trình vé mời này tại bàn check-in Tầng 9 trước 08:00 để nhận Bộ quà tặng "Passport Sen" và thưởng thức Dạ Cổ Hoài Lang đón khách.
        </div>
      </div>

      <div class="ticket-stub-section">
        <div style="font-size: 0.72rem; font-weight: 800; color: #0b1f42; text-transform: uppercase;">
          CUỐNG VÉ CHECK-IN
        </div>
        <div class="ticket-qr-block">
          <img src="${qrUrl}" alt="QR Check-in">
          <div class="ticket-code">${code}</div>
        </div>
        <div style="font-size: 0.65rem; color: #64748b; line-height: 1.3;">
          Xác thực điện tử<br>Ban Tổ Chức VHU 2027
        </div>
      </div>
    </div>

    <p class="print-tip">Hệ thống in vé điện tử chính thức của Trường Đại học Văn Hiến. Bạn có thể in trực tiếp hoặc lưu dưới dạng PDF.</p>
  </div>

  <script>
    window.onload = function() {
      setTimeout(() => {
        window.print();
        window.close();
      }, 350);
    };
  <\/script>
</body>
</html>`;

  printWindow.document.open();
  printWindow.document.write(html);
  printWindow.document.close();
}

function printActiveAppendix() {
  const activePane = document.querySelector('.app-content-pane.active .doc-paper-wrapper');
  if (!activePane) return;

  const printWindow = window.open('', '_blank', 'width=900,height=850');
  if (!printWindow) {
    alert('Vui lòng cho phép mở pop-up trong trình duyệt để in văn bản!');
    return;
  }

  const docClone = activePane.cloneNode(true);
  const actions = docClone.querySelector('.doc-actions-top');
  if (actions) actions.remove();

  const html = `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <title>Hồ sơ pháp lý - Trường Đại học Văn Hiến 2027</title>
  <link rel="stylesheet" href="./styles.css">
  <style>
    @page { size: A4 portrait; margin: 20mm 15mm 20mm 20mm; }
    * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    body {
      background: #ffffff;
      margin: 0;
      padding: 0;
      font-family: 'Times New Roman', Times, serif;
      font-size: 14pt;
      line-height: 1.5;
      color: #000000;
    }
    .doc-paper-wrapper {
      box-shadow: none !important;
      border: none !important;
      padding: 0 !important;
      margin: 0 auto !important;
      max-width: 100% !important;
    }
    .doc-actions-top { display: none !important; }
  </style>
</head>
<body>
  ${docClone.outerHTML}
  <script>
    window.onload = function() {
      setTimeout(() => {
        window.print();
        window.close();
      }, 400);
    };
  <\/script>
</body>
</html>`;

  printWindow.document.open();
  printWindow.document.write(html);
  printWindow.document.close();
}"""

new_full_print_section = """function printHtmlViaFrame(html) {
  // Use invisible iframe: 100% bypasses popup blocker and isolates print strictly to the content
  let printFrame = document.getElementById('print-isolated-iframe');
  if (!printFrame) {
    printFrame = document.createElement('iframe');
    printFrame.id = 'print-isolated-iframe';
    printFrame.style.position = 'fixed';
    printFrame.style.right = '0';
    printFrame.style.bottom = '0';
    printFrame.style.width = '0';
    printFrame.style.height = '0';
    printFrame.style.border = 'none';
    document.body.appendChild(printFrame);
  }

  const frameDoc = printFrame.contentWindow.document;
  frameDoc.open();
  frameDoc.write(html);
  frameDoc.close();

  setTimeout(() => {
    try {
      printFrame.contentWindow.focus();
      printFrame.contentWindow.print();
    } catch (err) {
      const win = window.open('', '_blank');
      if (win) {
        win.document.open();
        win.document.write(html);
        win.document.close();
        win.focus();
        setTimeout(() => { win.print(); win.close(); }, 400);
      }
    }
  }, 400);
}

function printTicket() {
  const nameInput = document.getElementById('reg-fullname');
  const mssvInput = document.getElementById('reg-mssv');
  const facultyInput = document.getElementById('reg-faculty');

  const name = (nameInput?.value || document.getElementById('ticket-display-name')?.textContent || 'Nguyễn Văn A').trim();
  const mssv = (mssvInput?.value || document.getElementById('ticket-display-mssv')?.textContent || '241A010999').trim();
  const faculty = (facultyInput?.value || document.getElementById('ticket-display-faculty')?.textContent || 'Khoa Du lịch').trim();
  const code = 'VHU-SEN-' + mssv.toUpperCase();

  const origin = window.location.origin;
  const logoUrl = origin && origin !== 'null' ? origin + '/assets/images/logo-VHU.png' : './assets/images/logo-VHU.png';
  const qrUrl = origin && origin !== 'null' ? origin + '/assets/docx_media/image12.png' : './assets/docx_media/image12.png';

  const html = `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <title>Vé Mời VIP "Passport Sen" - ĐH Văn Hiến 2027</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 12mm 12mm;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    body {
      background: #f8fafc;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #0b1f42;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 16px;
    }
    .ticket-sheet {
      width: 100%;
      max-width: 820px;
      margin: 0 auto;
    }
    
    .vip-ticket-container {
      background: #ffffff;
      border: 2px solid #0b1f42;
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(11,31,66,0.12);
      display: flex;
      position: relative;
      margin-bottom: 24px;
    }

    .ticket-main-section {
      flex: 1;
      padding: 22px 26px;
      border-right: 2px dashed #cbd5e1;
      position: relative;
      background: #ffffff;
    }
    .ticket-stub-section {
      width: 240px;
      background: #f8fafc;
      padding: 20px 18px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      text-align: center;
      border-left: 2px dashed #cbd5e1;
      margin-left: -2px;
    }

    .ticket-brand {
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 12px;
      margin-bottom: 14px;
    }
    .ticket-logo {
      height: 48px;
      width: auto;
    }
    .ticket-title-group h2 {
      font-size: 1.05rem;
      font-weight: 800;
      color: #0b1f42;
      letter-spacing: 0.02em;
    }
    .ticket-title-group p {
      font-size: 0.72rem;
      color: #d49b19;
      font-weight: 700;
    }

    .ticket-event-name {
      margin-bottom: 14px;
    }
    .ticket-event-label {
      font-size: 0.7rem;
      text-transform: uppercase;
      font-weight: 800;
      letter-spacing: 0.08em;
      color: #d83a6f;
    }
    .ticket-event-title {
      font-size: 1.45rem;
      font-weight: 900;
      color: #0b1f42;
      line-height: 1.2;
    }

    .ticket-details-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      background: #f8fafc;
      padding: 12px 14px;
      border-radius: 12px;
      margin-bottom: 12px;
    }
    .detail-item .label {
      font-size: 0.68rem;
      text-transform: uppercase;
      font-weight: 700;
      color: #64748b;
    }
    .detail-item .value {
      font-size: 0.88rem;
      font-weight: 800;
      color: #0b1f42;
    }

    .ticket-qr-block {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .ticket-qr-block img {
      width: 140px;
      height: 140px;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 4px;
      background: #ffffff;
      margin-bottom: 6px;
    }
    .ticket-code {
      font-family: monospace;
      font-size: 0.82rem;
      font-weight: 800;
      color: #0b1f42;
      letter-spacing: 0.06em;
    }

    .print-tip {
      font-size: 0.75rem;
      color: #64748b;
      margin-top: 10px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="ticket-sheet">
    <div class="vip-ticket-container">
      <div class="ticket-main-section">
        <div class="ticket-brand">
          <img src="${logoUrl}" alt="Logo VHU" class="ticket-logo">
          <div class="ticket-title-group">
            <h2>TRƯỜNG ĐẠI HỌC VĂN HIẾN</h2>
            <p>HUNGHAU CAMPUS • NĂM 2027</p>
          </div>
        </div>

        <div class="ticket-event-name">
          <div class="ticket-event-label">Vé Tham Dự VIP Chính Thức</div>
          <div class="ticket-event-title">CHƯƠNG TRÌNH "CHẠM MỘT SẮC SEN"</div>
        </div>

        <div class="ticket-details-grid">
          <div class="detail-item">
            <div class="label">Khách mời / Sinh viên</div>
            <div class="value">${name}</div>
          </div>
          <div class="detail-item">
            <div class="label">MSSV / Mã định danh</div>
            <div class="value">${mssv}</div>
          </div>
          <div class="detail-item">
            <div class="label">Khoa / Đơn vị</div>
            <div class="value">${faculty}</div>
          </div>
          <div class="detail-item">
            <div class="label">Vị trí chỗ ngồi</div>
            <div class="value" style="color: #d49b19;">Khán Đài A (Ghế VIP Danh Dự)</div>
          </div>
          <div class="detail-item">
            <div class="label">Thời gian check-in</div>
            <div class="value">07:30 - Ngày 20/06/2027</div>
          </div>
          <div class="detail-item">
            <div class="label">Địa điểm diễn ra</div>
            <div class="value">Tầng 9, Hội trường Trần Hưng Đạo</div>
          </div>
        </div>

        <div style="font-size: 0.7rem; color: #64748b;">
          * Quý khách vui lòng xuất trình vé mời này tại bàn check-in Tầng 9 trước 08:00 để nhận Bộ quà tặng "Passport Sen" và thưởng thức Dạ Cổ Hoài Lang đón khách.
        </div>
      </div>

      <div class="ticket-stub-section">
        <div style="font-size: 0.72rem; font-weight: 800; color: #0b1f42; text-transform: uppercase;">
          CUỐNG VÉ CHECK-IN
        </div>
        <div class="ticket-qr-block">
          <img src="${qrUrl}" alt="QR Check-in">
          <div class="ticket-code">${code}</div>
        </div>
        <div style="font-size: 0.65rem; color: #64748b; line-height: 1.3;">
          Xác thực điện tử<br>Ban Tổ Chức VHU 2027
        </div>
      </div>
    </div>

    <p class="print-tip">Hệ thống in vé điện tử chính thức của Trường Đại học Văn Hiến. Bạn có thể in trực tiếp hoặc lưu dưới dạng PDF.</p>
  </div>
</body>
</html>`;

  printHtmlViaFrame(html);
}

function printActiveAppendix() {
  const activePane = document.querySelector('.app-content-pane.active .doc-paper-wrapper');
  if (!activePane) return;

  const docClone = activePane.cloneNode(true);
  const actions = docClone.querySelector('.doc-actions-top');
  if (actions) actions.remove();

  const html = `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <title>Hồ sơ pháp lý - Trường Đại học Văn Hiến 2027</title>
  <link rel="stylesheet" href="./styles.css">
  <style>
    @page { size: A4 portrait; margin: 20mm 15mm 20mm 20mm; }
    * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    body {
      background: #ffffff;
      margin: 0;
      padding: 0;
      font-family: 'Times New Roman', Times, serif;
      font-size: 14pt;
      line-height: 1.5;
      color: #000000;
    }
    .doc-paper-wrapper {
      box-shadow: none !important;
      border: none !important;
      padding: 0 !important;
      margin: 0 auto !important;
      max-width: 100% !important;
    }
    .doc-actions-top { display: none !important; }
  </style>
</head>
<body>
  ${docClone.outerHTML}
</body>
</html>`;

  printHtmlViaFrame(html);
}"""

assert old_full_print_section in js_code, "old_full_print_section not found"
js_code = js_code.replace(old_full_print_section, new_full_print_section, 1)

with open('tools/build_clean_script_js.py', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("SUCCESS: Updated build_clean_script_js.py with iframe print!")
