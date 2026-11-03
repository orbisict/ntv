import sys

with open('script.js', 'r', encoding='utf-8') as f:
    c = f.read()

start_marker = 'const html = `'
end_marker = '`;\n\n  printWindow.document.open();'

idx1 = c.find(start_marker)
idx2 = c.find(end_marker, idx1)

if idx1 != -1 and idx2 != -1:
    template = c[idx1 + len(start_marker):idx2]
    # replace template literals
    content = template.replace('${origin}', '.')
    content = content.replace('${logoUrl}', './assets/images/logo-VHU.png')
    content = content.replace('${qrUrl}', './assets/docx_media/image12.png')
    content = content.replace('${name}', 'Nguyễn Văn A')
    content = content.replace('${mssv}', '241A010999')
    content = content.replace('${faculty}', 'Khoa Du lịch')
    content = content.replace('${code}', 'VHU-SEN-241A010999')
    with open('test_ticket_preview.html', 'w', encoding='utf-8') as out:
        out.write(content)
    print('Generated test_ticket_preview.html successfully')
else:
    print('Markers not found', idx1, idx2)
