import json
import html
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('appendices_raw.json', 'r', encoding='utf-8') as f:
    apps = json.load(f)

# Helper to escape
def h(text):
    return html.escape(str(text)) if text else ""

# Let's write dedicated formatters for App 1 to 5

# --- APPENDIX 1: TỜ TRÌNH ---
app1_html = """
<div class="doc-paper-wrapper" id="app1-doc">
  <div class="doc-actions-top">
    <button class="btn-doc-action btn-copy-doc">📋 Sao chép toàn văn</button>
    <button class="btn-doc-action btn-print-doc">🖨️ In văn bản này</button>
  </div>
  
  <div class="doc-admin-header">
    <div class="doc-admin-left">
      <div class="agency-upper">TRƯỜNG ĐẠI HỌC VĂN HIẾN</div>
      <div class="agency-main">BAN TỔ CHỨC SỰ KIỆN</div>
      <div class="doc-number">Số: ....../TTr-BTC-2027</div>
    </div>
    <div class="doc-admin-right">
      <div class="country-title">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</div>
      <div class="motto">Độc lập - Tự do - Hạnh phúc</div>
      <div class="doc-date">TP. Hồ Chí Minh, ngày 01 tháng 05 năm 2027</div>
    </div>
  </div>

  <h2 class="doc-title-main">TỜ TRÌNH</h2>
  <div class="doc-subtitle">Về việc phê duyệt Kế hoạch tổ chức Chương trình Văn hóa & Nghệ thuật tỉnh Đồng Tháp năm 2027 "Chạm một sắc Sen"</div>

  <div class="doc-recipient">Kính gửi: BAN GIÁM HIỆU TRƯỜNG ĐẠI HỌC VĂN HIẾN</div>

  <p class="doc-paragraph">Căn cứ định hướng chiến lược phát triển văn hóa học đường cho sinh viên Trường Đại học Văn Hiến năm 2027;</p>
  <p class="doc-paragraph">Căn cứ nhu cầu giao lưu văn hóa nghệ thuật và kết nối doanh nghiệp, nhà tài trợ với thế hệ trẻ;</p>
  <p class="doc-paragraph">Ban Tổ chức sự kiện kính trình Ban Giám hiệu xem xét và phê duyệt Kế hoạch cùng Dự toán kinh phí chi tiết cho Chương trình Văn hoá – Nghệ thuật tỉnh Đồng Tháp năm 2027 với các nội dung cụ thể như sau:</p>

  <h3 class="doc-section-h1">I. THÔNG TIN CHUNG VỀ SỰ KIỆN</h3>
  <ul class="doc-list">
    <li><strong>Tên sự kiện:</strong> Chương trình Văn hoá – Nghệ thuật tỉnh Đồng Tháp năm 2027</li>
    <li><strong>Chủ đề chính:</strong> Chạm một sắc Sen</li>
    <li><strong>Thời gian tổ chức:</strong> 07h30, Chủ Nhật - Ngày 20/06/2027</li>
    <li><strong>Địa điểm dự kiến:</strong> Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus (Khu chức năng số 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM)</li>
    <li><strong>Đơn vị thực hiện:</strong> Trường Đại học Văn Hiến (Ban Tổ chức Sự kiện)</li>
    <li><strong>Đối tượng tham gia:</strong> Sinh viên Trường Đại học Văn Hiến (Đăng ký trực tuyến hoàn toàn miễn phí)</li>
    <li><strong>Quy mô tham dự:</strong> 300 người tham dự trực tiếp tại Hội trường Trần Hưng Đạo</li>
    <li><strong>Màu sắc chủ đạo:</strong> Hồng Sen, Xanh lá Sen, Xanh dương (Kết hợp bộ nhận diện thương hiệu Đại học Văn Hiến)</li>
  </ul>

  <h3 class="doc-section-h1">II. MỤC TIÊU VÀ Ý NGHĨA TRỌNG TÂM</h3>
  <p class="doc-paragraph"><strong>1. Tôn vinh & Lan tỏa Văn hóa:</strong> Tái hiện không gian văn hóa, nghệ thuật và hình ảnh con người Đồng Tháp qua biểu tượng hoa sen theo phong cách hiện đại, sinh động, phù hợp với giới trẻ.</p>
  <p class="doc-paragraph"><strong>2. Giao lưu & Truyền cảm hứng:</strong> Tạo không gian giao lưu trực tiếp giữa sinh viên với Chủ tịch Tập đoàn Hùng Hậu (Ông Trần Văn Hậu), truyền cảm hứng nỗ lực vươn lên và định hướng phát triển thực tiễn.</p>
  <p class="doc-paragraph"><strong>3. Mục tiêu Thiện nguyện Nhân văn:</strong> Toàn bộ lợi nhuận thu được sau sự kiện sẽ được trích quyên góp cho Trung tâm Bảo trợ xã hội Tổng hợp tỉnh Đồng Tháp.</p>
  <p class="doc-paragraph"><strong>4. Gắn kết Doanh nghiệp & Truyền thông:</strong> Tăng cường mối quan hệ hợp tác chiến lược giữa Trường Đại học Văn Hiến với các doanh nghiệp, nhà tài trợ và các cơ quan báo chí.</p>

  <h3 class="doc-section-h1">III. NỘI DUNG VÀ KỊCH BẢN CHƯƠNG TRÌNH (20/06/2027)</h3>
  <p class="doc-paragraph">Chương trình chính diễn ra tại Tầng 9 Hội trường Trần Hưng Đạo với kịch bản điều hành chi tiết như sau:</p>
  
  <div class="table-scroll-wrapper">
<table class="doc-table">
    <thead>
      <tr>
        <th style="width: 25%;">Khung thời gian</th>
        <th>Nội dung & Tiết mục chính</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>07:30 – 08:10</td><td>Đón khách, check-in bằng mã QR, ổn định hội trường.</td></tr>
      <tr><td>08:10 – 08:20</td><td>Mở màn tiết mục nghệ thuật "Sắc Sen VHU".</td></tr>
      <tr><td>08:20 – 08:30</td><td>Giới thiệu Đại biểu, Khách mời VIP và các Nhà tài trợ.</td></tr>
      <tr><td>08:30 – 08:40</td><td>Phát biểu khai mạc của Đại diện Trường Đại học Văn Hiến.</td></tr>
      <tr><td>08:40 – 09:00</td><td>Trình diễn nghệ thuật "Hồn Sen Đất Việt" kết hợp cùng các nghệ nhân Đờn ca tài tử Nam Bộ.</td></tr>
      <tr><td>09:00 – 09:50</td><td>Giao lưu chia sẻ cùng Chủ tịch HĐQT HungHau Holding.</td></tr>
      <tr><td>09:50 – 10:05</td><td>Sinh viên tương tác và đặt câu hỏi trực tiếp cho Khách mời.</td></tr>
      <tr><td>10:05 – 10:25</td><td>Fashion Show "Sắc Sen” - Trình diễn BST "Miệt Cù Lao" của NTK Nguyễn Minh Công với sự góp mặt của Hoa hậu Yến Nhi và Á hậu Hạnh Nguyên.</td></tr>
      <tr><td>10:25 – 10:40</td><td>Trình diễn âm nhạc “Hồn quê" & "Ếch ngoài đáy giếng" do Ca sĩ khách mời Phương Mỹ Chi biểu diễn.</td></tr>
      <tr><td>10:40 – 10:55</td><td>Lễ Tổng kết: Trao hoa, kỷ niệm chương và thư tri ân các Nhà tài trợ; chụp ảnh lưu niệm.</td></tr>
      <tr><td>10:55 – 11:10</td><td>Tiễn khách và kết thúc chương trình.</td></tr>
    </tbody>
  </table>
</div>

  <h3 class="doc-section-h1">IV. DỰ TRÙ KINH PHÍ VÀ NGUỒN TÀI CHÍNH</h3>
  <p class="doc-paragraph"><strong>1. Tổng hợp dự trù chi phí thực hiện:</strong></p>
  <div class="table-scroll-wrapper">
<table class="doc-table">
    <thead>
      <tr>
        <th>Nhóm hạng mục chi phí</th>
        <th style="text-align: right;">Tổng tiền (đã bao gồm VAT 8%)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Nhóm A: Địa điểm – Dàn dựng không gian</td><td style="text-align: right;">17.820.000 đ</td></tr>
      <tr><td>Nhóm B: Âm thanh – Ánh sáng – Màn hình LED (CSVC có sẵn)</td><td style="text-align: right;">0 đ</td></tr>
      <tr><td>Nhóm C: Ấn phẩm, Passport Sen, Standee, Thẻ Staff</td><td style="text-align: right;">6.447.608 đ</td></tr>
      <tr><td>Nhóm D: Truyền thông, Báo chí & Quảng cáo số</td><td style="text-align: right;">32.400.000 đ</td></tr>
      <tr><td>Nhóm E: Nghệ thuật, Dàn dựng & Biểu diễn Sân khấu</td><td style="text-align: right;">8.640.000 đ</td></tr>
      <tr><td>Nhóm F: Khách mời VIP, Nghệ sĩ & Thù lao đón tiếp</td><td style="text-align: right;">10.800.000 đ</td></tr>
      <tr><td>Nhóm G: Quà tặng Sinh viên, Kỷ niệm chương & Hoa tươi</td><td style="text-align: right;">10.918.800 đ</td></tr>
      <tr><td>Nhóm H: Hậu cần, An ninh, PCCC & Sơ cứu Y tế</td><td style="text-align: right;">3.240.000 đ</td></tr>
      <tr><td>Nhóm I: Phục vụ, Nước uống Aquafina & Lưu trú Khách phương xa</td><td style="text-align: right;">4.347.000 đ</td></tr>
      <tr style="font-weight: bold; background: #fafafa;"><td>TỔNG CHI PHÍ TRỰC TIẾP</td><td style="text-align: right;">94.613.408 đ</td></tr>
      <tr><td>Nhóm K: Chi phí dự phòng phát sinh (10%)</td><td style="text-align: right;">9.461.340 đ</td></tr>
      <tr style="font-weight: bold; background: #f0f7ff; color: #18376b;"><td>TỔNG CỘNG KINH PHÍ DỰ KIẾN (Đã gồm VAT & Dự phòng)</td><td style="text-align: right;">104.074.748 đ</td></tr>
    </tbody>
  </table>
</div>

  <p class="doc-paragraph"><strong>2. Cơ cấu nguồn tài trợ vận động:</strong></p>
  <div class="table-scroll-wrapper">
<table class="doc-table">
    <thead>
      <tr>
        <th>Gói tài trợ / Đơn vị đồng hành</th>
        <th>Hình thức tài trợ</th>
        <th style="text-align: right;">Giá trị tài trợ dự kiến</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Nhà tài trợ Kim Cương (Trường Đại học Văn Hiến)</td><td>Tiền mặt</td><td style="text-align: right;">100.000.000 đ</td></tr>
      <tr><td>Nhà tài trợ Vàng (02 đơn vị Doanh nghiệp)</td><td>Tiền mặt</td><td style="text-align: right;">100.000.000 đ</td></tr>
      <tr><td>Nhà tài trợ Bạc (03 đơn vị Doanh nghiệp)</td><td>Tiền mặt</td><td style="text-align: right;">105.000.000 đ</td></tr>
      <tr><td>Trường ĐH Văn Hiến (CSVC, Hội trường & Âm thanh ánh sáng)</td><td>Hiện vật / Tài trợ 100%</td><td style="text-align: right;">0 đ (Quy đổi)</td></tr>
      <tr><td>NTK Nguyễn Minh Công (BST Thời trang "Miệt Cù Lao")</td><td>Hiện vật / Tài trợ 100%</td><td style="text-align: right;">0 đ (Quy đổi)</td></tr>
      <tr><td>Trang phục biểu diễn DIVIT (Trang phục & Đạo cụ biểu diễn)</td><td>Hiện vật / Tài trợ 100%</td><td style="text-align: right;">0 đ (Quy đổi)</td></tr>
      <tr><td>Orbis ICT (Tài trợ kỹ thuật livestream & truyền thông)</td><td>Dịch vụ / Hỗ trợ 100%</td><td style="text-align: right;">0 đ (Quy đổi)</td></tr>
      <tr style="font-weight: bold; background: #fff9e6;"><td>TỔNG NGUỒN TÀI CHÍNH DỰ KIẾN</td><td>Tiền mặt vận động</td><td style="text-align: right;">305.000.000 đ</td></tr>
    </tbody>
  </table>
</div>

  <p class="doc-paragraph"><strong>3. Kế hoạch cân đối tài chính & Thiện nguyện:</strong></p>
  <p class="doc-paragraph">Tổng thu vận động (305.000.000 đ) trừ Tổng chi dự toán (104.074.748 đ) đạt thặng dư <strong>200.925.252 đ</strong>. Toàn bộ số tiền chênh lệch này sẽ được Nhà trường phối hợp cùng Ban Tổ chức trao tặng trực tiếp cho Trung tâm Bảo trợ xã hội Tổng hợp tỉnh Đồng Tháp theo đúng tôn chỉ nhân văn của chương trình.</p>

  <h3 class="doc-section-h1">V. KẾ HOẠCH VẬN HÀNH VÀ TIẾN ĐỘ THỰC HIỆN</h3>
  <ul class="doc-list">
    <li><strong>Giai đoạn 1 (01/05 – 20/05/2027):</strong> Trình duyệt chủ trương, hoàn thiện hồ sơ pháp lý, gửi văn bản đến Sở VHTT TP.HCM và chính quyền địa phương; ký kết thỏa thuận tài trợ với các đối tác.</li>
    <li><strong>Giai đoạn 2 (21/05 – 15/06/2027):</strong> Triển khai chiến dịch truyền thông đa kênh; mở cổng đăng ký trực tuyến cho sinh viên (300 vé); sản xuất quà tặng và ấn phẩm POSM.</li>
    <li><strong>Giai đoạn 3 (16/06 – 19/06/2027):</strong> Hoàn tất công tác thi công sân khấu Sảnh Trống Đồng & Tầng 9; chạy thử tải hệ thống điện, âm thanh ánh sáng và tổng duyệt sân khấu tối 19/06/2027.</li>
    <li><strong>Giai đoạn 4 (20/06/2027):</strong> Vận hành chính thức sự kiện "Chạm một sắc Sen" (07:30 – 11:10); tiếp đón đại biểu và livestream đa kênh.</li>
    <li><strong>Giai đoạn 5 (21/06 – 04/08/2027):</strong> Hoàn tất chứng từ quyết toán thu chi; công bố báo cáo minh bạch trên truyền thông và tiến hành bàn giao trao tặng tiền từ thiện cho Trung tâm Bảo trợ xã hội Tổng hợp tỉnh Đồng Tháp.</li>
  </ul>

  <h3 class="doc-section-h1">VI. QUẢN TRỊ RỦI RO</h3>
  <p class="doc-paragraph">Ban Tổ chức đã xây dựng ma trận kiểm soát rủi ro toàn diện: chủ động phương án máy phát điện dự phòng, đường truyền Internet cáp quang riêng cho livestream, bố trí lối thoát hiểm và đội ngũ an ninh – y tế túc trực suốt thời gian diễn ra chương trình.</p>

  <h3 class="doc-section-h1">VII. KIẾN NGHỊ VÀ ĐỀ XUẤT</h3>
  <p class="doc-paragraph">Ban Tổ chức kính trình Ban Giám hiệu Trường Đại học Văn Hiến xem xét, chấp thuận chủ trương tổ chức Chương trình Văn hóa & Nghệ thuật tỉnh Đồng Tháp năm 2027 "Chạm một sắc Sen", đồng thời phê duyệt dự toán kinh phí để Ban Tổ chức chủ động triển khai các công tác chuẩn bị đúng tiến độ.</p>
  <p class="doc-paragraph">Kính trình Ban Giám hiệu xem xét, quyết định./.</p>

  <div class="doc-sign-grid">
    <div class="doc-sign-col-left">
      <strong>Nơi nhận:</strong><br>
      - Ban Giám hiệu (để báo cáo);<br>
      - Các Phòng, Khoa liên quan (để p/h);<br>
      - Lưu: VT, BTC.
    </div>
    <div class="doc-sign-col-right">
      <div class="sign-title">TM. BAN TỔ CHỨC SỰ KIỆN</div>
      <div class="sign-title">TRƯỞNG BAN TỔ CHỨC</div>
      <div class="sign-note">(Ký và ghi rõ họ tên)</div>
      <img src="./assets/docx_media/image13.png" alt="Dấu mộc xác thực" class="stamp-seal-img">
      <div class="sign-name">Trần Thúy Quyên</div>
    </div>
  </div>
</div>
"""

# --- APPENDIX 2: ĐƠN XIN SỬ DỤNG ĐỊA ĐIỂM ---
app2_html = """
<div class="doc-paper-wrapper" id="app2-doc" style="display: none;">
  <div class="doc-actions-top">
    <button class="btn-doc-action btn-copy-doc">📋 Sao chép toàn văn</button>
    <button class="btn-doc-action btn-print-doc">🖨️ In văn bản này</button>
  </div>

  <div class="doc-admin-header">
    <div class="doc-admin-left">
      <div class="agency-upper">TRƯỜNG ĐẠI HỌC VĂN HIẾN</div>
      <div class="agency-main">BAN TỔ CHỨC SỰ KIỆN</div>
      <div class="doc-number">Số: ....../ĐN-BTC-2027</div>
    </div>
    <div class="doc-admin-right">
      <div class="country-title">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</div>
      <div class="motto">Độc lập – Tự do – Hạnh phúc</div>
      <div class="doc-date">TP. Hồ Chí Minh, ngày 05 tháng 05 năm 2027</div>
    </div>
  </div>

  <h2 class="doc-title-main">ĐƠN XIN SỬ DỤNG ĐỊA ĐIỂM TỔ CHỨC SỰ KIỆN</h2>
  <div class="doc-subtitle">(V/v: Sử dụng Hội trường và Sảnh tổ chức Chương trình Văn hóa & Nghệ thuật tỉnh Đồng Tháp 2027 “Chạm một sắc Sen”)</div>

  <div class="doc-recipient">
    Kính gửi:<br>
    - Ban Giám hiệu Trường Đại học Văn Hiến;<br>
    - Ban Quản lý Cơ sở HungHau Campus;<br>
    - Phòng Quản trị Cơ sở vật chất & Thiết bị.
  </div>

  <h3 class="doc-section-h1">I. THÔNG TIN ĐƠN VỊ ĐĂNG KÝ & SỰ KIỆN</h3>
  <ul class="doc-list">
    <li><strong>Đơn vị đăng ký:</strong> Trường Đại học Văn Hiến (Ban Tổ chức Sự kiện)</li>
    <li><strong>Người đại diện liên hệ:</strong> Trần Thúy Quyên – Trưởng Ban Tổ chức (SĐT: 0369449925)</li>
    <li><strong>Tên sự kiện:</strong> Chương trình Văn hóa – Nghệ thuật tỉnh Đồng Tháp năm 2027</li>
    <li><strong>Chủ đề chính:</strong> Chạm một sắc Sen</li>
    <li><strong>Quy mô tham dự:</strong> 300 sinh viên Trường Đại học Văn Hiến, các vương miện Hoa hậu, Nghệ sĩ khách mời và đại biểu tỉnh Đồng Tháp.</li>
    <li><strong>Mục đích sử dụng:</strong> Tổ chức không gian trải nghiệm văn hóa, biểu diễn nghệ thuật và khu vực gian hàng nhà tài trợ.</li>
  </ul>

  <h3 class="doc-section-h1">II. ĐỊA ĐIỂM VÀ THỜI GIAN ĐĂNG KÝ SỬ DỤNG (02 NGÀY)</h3>
  <p class="doc-paragraph"><strong>1. Các khu vực đăng ký sử dụng:</strong></p>
  <ul class="doc-list">
    <li><strong>Hội trường Trần Hưng Đạo (Tầng 9, HungHau Campus):</strong> Phục vụ sân khấu chính, âm thanh, ánh sáng, màn hình LED và 300 ghế ngồi.</li>
    <li><strong>Khu vực Sảnh Trống Đồng:</strong> Phục vụ lắp đặt 04-06 gian hàng tài trợ và mô hình check-in "Góc Khát vọng VHU".</li>
    <li><strong>Phòng chức năng / Backstage Tầng 9:</strong> Phục vụ phòng chờ VIP, chuẩn bị cho Nghệ sĩ, Hoa hậu và Ban Tổ chức.</li>
    <li><strong>Hệ thống thang máy:</strong> Sử dụng 02 buồng thang máy bên phải để phân luồng di chuyển an toàn cho đại biểu và người tham gia.</li>
  </ul>

  <p class="doc-paragraph"><strong>2. Lịch trình chi tiết đăng ký sử dụng trong 02 ngày:</strong></p>
  <div class="table-scroll-wrapper">
<table class="doc-table">
    <thead>
      <tr>
        <th style="width: 25%;">Thời gian</th>
        <th>Nội dung công việc</th>
        <th>Khu vực sử dụng</th>
        <th>Yêu cầu CSVC & Kỹ thuật</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>NGÀY 1: 19/06/2027</strong><br>(07h00 - 17h00)</td>
        <td>Thực hiện trang trí không gian; dựng 04 booth tài trợ và góc check-in "Khát vọng VHU".</td>
        <td>Hội trường Tầng 9 & Sảnh Trống Đồng</td>
        <td>Cung cấp nguồn điện thi công, hỗ trợ kỹ thuật tòa nhà.</td>
      </tr>
      <tr>
        <td><strong>NGÀY 1: 19/06/2027</strong><br>(17h00 - 21h00)</td>
        <td>Chạy thử tải thiết bị kỹ thuật, tổng duyệt sân khấu, khớp âm thanh/ánh sáng với dàn nhạc, MC và nghệ sĩ.</td>
        <td>Hội trường Trần Hưng Đạo</td>
        <td>Hệ thống điện áp ổn định, vận hành màn hình LED & loa.</td>
      </tr>
      <tr>
        <td><strong>NGÀY 2: 20/06/2027</strong><br>(06h30 - 07h30)</td>
        <td>Phân luồng và đón tiếp sinh viên, Đại biểu & VIP.</td>
        <td>Sảnh Trống Đồng & Phòng chờ VIP</td>
        <td>Mở cửa thang máy riêng, đảm bảo trật tự sảnh đón.</td>
      </tr>
      <tr>
        <td><strong>NGÀY 2: 20/06/2027</strong><br>(07h30 - 11h00)</td>
        <td>Diễn ra chính thức chương trình "Chạm một sắc Sen".</td>
        <td>Hội trường Trần Hưng Đạo</td>
        <td>Hỗ trợ an ninh, PCCC, máy phát điện dự phòng sẵn sàng.</td>
      </tr>
      <tr>
        <td><strong>NGÀY 2: 20/06/2027</strong><br>(11h30 - 17h30)</td>
        <td>Tháo dỡ, thu dọn tiểu cảnh, gian hàng sảnh Trống Đồng, vệ sinh công nghiệp và bàn giao mặt bằng.</td>
        <td>Hội trường Trần Hưng Đạo, Sảnh Trống Đồng</td>
        <td>Kiểm tra hiện trạng và nghiệm thu bàn giao CSVC.</td>
      </tr>
    </tbody>
  </table>
</div>

  <h3 class="doc-section-h1">III. ĐỀ XUẤT HỖ TRỢ VỀ CƠ SỞ VẬT CHẤT & KỸ THUẬT</h3>
  <ul class="doc-list">
    <li><strong>Kỹ thuật & Điện:</strong> Hỗ trợ cán bộ kỹ thuật trực giám sát hệ thống điện, âm thanh, ánh sáng, màn hình LED trong suốt thời gian tổng duyệt (tối 19/06) và sự kiện chính (sáng 20/06); chuẩn bị sẵn sàng phương án máy phát điện dự phòng.</li>
    <li><strong>An ninh & Vận chuyển:</strong> Hỗ trợ phân luồng giao thông tại bãi xe, mở lối đi thang máy ưu tiên cho đại biểu VIP/nghệ sĩ và cho phép xe tải chở đồ trang thiết bị hậu cần ra vào bãi bốc xếp.</li>
    <li><strong>Vệ sinh & PCCC:</strong> Kiểm tra trang thiết bị PCCC, lối thoát hiểm cầu thang bộ tại Tầng 9 trước 07h00 ngày 20/06/2027 và hỗ trợ tăng cường công tác vệ sinh trước - sau chương trình.</li>
  </ul>

  <h3 class="doc-section-h1">IV. CAM KẾT CỦA BAN TỔ CHỨC</h3>
  <ol class="doc-list">
    <li>Sử dụng địa điểm đúng mục đích, đúng thời gian và khu vực đã đăng ký trong đơn.</li>
    <li>Chịu trách nhiệm hoàn toàn về công tác quản lý sinh viên, đảm bảo an ninh trật tự, an toàn phòng chống cháy nổ và an toàn điện trong suốt 02 ngày sử dụng.</li>
    <li>Bảo quản toàn bộ tài sản, cơ sở vật chất, trang thiết bị của Hội trường và Campus. Trường hợp xảy ra hư hỏng, mất mát do lỗi của Ban Tổ chức, chúng tôi cam kết bồi thường theo đúng quy định của Nhà trường.</li>
    <li>Tiến hành thu dọn vệ sinh, tháo dỡ toàn bộ phông bạt, gian hàng và bàn giao mặt bằng sạch sẽ, nguyên trạng cho Ban Quản lý Campus trước 18h00 ngày 20/06/2027.</li>
  </ol>

  <p class="doc-paragraph">Kính mong Ban Giám hiệu, Ban Quản lý Cơ sở HungHau Campus và Phòng Quản trị CSVC xem xét, chấp thuận cho phép Ban Tổ chức sử dụng địa điểm để triển khai công tác chuẩn bị đúng tiến độ.</p>
  <p class="doc-paragraph">Xin trân trọng cảm ơn!</p>

  <div class="doc-sign-grid">
    <div class="doc-sign-col-left" style="text-align: center;">
      <div class="sign-title">Ý KIẾN BAN GIÁM HIỆU / BQL CƠ SỞ</div>
      <div class="sign-note">(Ký và ghi rõ họ tên)</div>
    </div>
    <div class="doc-sign-col-right">
      <div class="sign-title">TM. BAN TỔ CHỨC SỰ KIỆN</div>
      <div class="sign-title">TRƯỞNG BAN TỔ CHỨC</div>
      <div class="sign-note">(Ký và ghi rõ họ tên)</div>
      <img src="./assets/docx_media/image13.png" alt="Dấu mộc xác thực" class="stamp-seal-img">
      <div class="sign-name">Trần Thúy Quyên</div>
    </div>
  </div>
</div>
"""

# --- APPENDIX 3: BIÊN BẢN THỎA THUẬN TÀI TRỢ & BIỂU DIỄN BST ---
app3_html = """
<div class="doc-paper-wrapper" id="app3-doc" style="display: none;">
  <div class="doc-actions-top">
    <button class="btn-doc-action btn-copy-doc">📋 Sao chép toàn văn</button>
    <button class="btn-doc-action btn-print-doc">🖨️ In văn bản này</button>
  </div>

  <div class="doc-admin-header">
    <div class="doc-admin-left">
      <div class="agency-upper">BỘ GIÁO DỤC VÀ ĐÀO TẠO</div>
      <div class="agency-main">TRƯỜNG ĐẠI HỌC VĂN HIẾN</div>
      <div class="doc-number">Số: ....../BBTT-VHU-NMC</div>
    </div>
    <div class="doc-admin-right">
      <div class="country-title">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</div>
      <div class="motto">Độc lập - Tự do - Hạnh phúc</div>
      <div class="doc-date">TP. Hồ Chí Minh, ngày 10 tháng 05 năm 2027</div>
    </div>
  </div>

  <h2 class="doc-title-main">BIÊN BẢN THỎA THUẬN PHÊ DUYỆT</h2>
  <div class="doc-subtitle">VIỆC TÀI TRỢ VÀ BIỂU DIỄN TRANG PHỤC THỜI TRANG<br>(V/v: Trình diễn Bộ sưu tập "Miệt Cù Lao" của NTK Nguyễn Minh Công tại Chương trình Văn hóa & Nghệ thuật tỉnh Đồng Tháp năm 2027 "Chạm một sắc Sen")</div>

  <p class="doc-paragraph">Căn cứ Kế hoạch tổ chức Chương trình Văn hóa & Nghệ thuật tỉnh Đồng Tháp năm 2027 với chủ đề “Chạm một sắc Sen” do Trường Đại học Văn Hiến phê duyệt;</p>
  <p class="doc-paragraph">Căn cứ nhu cầu hợp tác tôn vinh nghệ thuật và văn hóa sông nước Nam Bộ giữa Trường Đại học Văn Hiến và Nhà thiết kế Nguyễn Minh Công;</p>
  <p class="doc-paragraph">Căn cứ khả năng và sự thống nhất tự nguyện giữa hai Bên.</p>

  <p class="doc-paragraph">Hôm nay, ngày 10 tháng 05 năm 2027, tại Trường Đại học Văn Hiến, hai Bên gồm có:</p>

  <div style="background: #f8faff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 16px 0;">
    <p><strong>BÊN A: TRƯỜNG ĐẠI HỌC VĂN HIẾN (ĐƠN VỊ TỔ CHỨC)</strong></p>
    <p>- Đại diện: Bà Trần Thúy Quyên | Chức vụ: Trưởng Ban Tổ chức</p>
    <p>- Địa chỉ: HungHau Campus, Khu chức năng 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM</p>
    <p>- Điện thoại: 0369449925</p>
    <hr style="margin: 10px 0; border: none; border-top: 1px dashed #cbd5e1;">
    <p><strong>BÊN B: NHÀ THIẾT KẾ NGUYỄN MINH CÔNG (ĐƠN VỊ TÀI TRỢ TRANG PHỤC)</strong></p>
    <p>- Đại diện: Ông Nguyễn Minh Công | Chức danh: Nhà thiết kế Thời trang / Tác giả BST "Miệt Cù Lao"</p>
    <p>- Thương hiệu: Thương hiệu NTK Nguyễn Minh Công</p>
  </div>

  <p class="doc-paragraph">Sau khi bàn bạc và thống nhất, hai Bên cùng ký kết Biên bản thỏa thuận phê duyệt với các điều khoản cụ thể như sau:</p>

  <h3 class="doc-section-h1">ĐIỀU 1: MỤC ĐÍCH VÀ NỘI DUNG PHÊ DUYỆT</h3>
  <p class="doc-paragraph"><strong>1.1. Phê duyệt biểu diễn:</strong> Bên A chính thức phê duyệt đề xuất của Bên B về việc đưa Bộ sưu tập thời trang "Miệt Cù Lao" vào trình diễn trong tiết mục Fashion Show "Sắc Sen" thuộc Chương trình Văn hóa – Nghệ thuật tỉnh Đồng Tháp năm 2027 "Chạm một sắc Sen".</p>
  <p class="doc-paragraph"><strong>1.2. Thời gian và Địa điểm trình diễn:</strong></p>
  <ul class="doc-list">
    <li>Thời gian: Từ 10:05 đến 10:25, ngày 20/06/2027.</li>
    <li>Địa điểm: Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus, Khu chức năng số 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM.</li>
  </ul>
  <p class="doc-paragraph"><strong>1.3. Hình thức tài trợ:</strong> Bên B tham gia với tư cách Nhà tài trợ Đồng hành hỗ trợ hiện vật (toàn bộ trang phục và phụ kiện trình diễn của BST "Miệt Cù Lao"). Sự hợp tác mang tính chất hỗ trợ nghệ thuật văn hóa phi thương mại (không thu phí bản quyền).</p>

  <h3 class="doc-section-h1">ĐIỀU 2: QUYỀN VÀ TRÁCH NHIỆM CỦA BÊN A (ĐƠN VỊ TỔ CHỨC)</h3>
  <ul class="doc-list">
    <li>Bảo đảm sàn diễn (catwalk), hệ thống âm thanh, ánh sáng chuyên nghiệp, màn hình LED hiển thị visual nghệ thuật tương thích với tinh thần BST.</li>
    <li>Phối hợp cùng Bên B điều phối nhân sự người mẫu (Hoa hậu Nguyễn Thị Yến Nhi, Á hậu Lê Phan Hạnh Nguyên và các thành viên CLB Thời trang VHU).</li>
    <li>Bố trí khu vực thay đồ (backstage) riêng biệt, an toàn, có gương soi và nhân sự hỗ trợ bảo quản trang phục.</li>
    <li>Thực hiện đầy đủ các quyền lợi truyền thông cho Bên B theo danh vị Nhà tài trợ Đồng hành.</li>
  </ul>

  <h3 class="doc-section-h1">ĐIỀU 3: QUYỀN VÀ TRÁCH NHIỆM CỦA BÊN B (NHÀ THIẾT KẾ NGUYỄN MINH CÔNG)</h3>
  <ul class="doc-list">
    <li>Cung cấp đầy đủ các mẫu thiết kế thuộc BST "Miệt Cù Lao" đúng số lượng, bảo đảm chất lượng, độ hoàn thiện cao và kích cỡ phù hợp với người mẫu trước ngày 18/06/2027.</li>
    <li>Cử trợ lý hoặc trực tiếp có mặt tại buổi khớp sân khấu tổng duyệt (chiều 19/06/2027) và buổi diễn chính thức (sáng 20/06/2027) để hỗ trợ căn chỉnh trang phục.</li>
    <li>Bảo đảm trang phục đúng tinh thần thuần phong mỹ tục của văn hóa Việt Nam và môi trường giáo dục đại học.</li>
  </ul>

  <h3 class="doc-section-h1">ĐIỀU 4: CAM KẾT VỀ BẢN QUYỀN, AN TOÀN VÀ THUẦN PHONG MỸ TỤC</h3>
  <ul class="doc-list">
    <li>Bên B cam kết BST "Miệt Cù Lao" thuộc quyền sở hữu trí tuệ hợp pháp của Bên B, không có tranh chấp về bản quyền tác giả.</li>
    <li>Cả hai Bên cam kết các thiết kế không mang yếu tố kích động, không có chi tiết phản cảm hoặc vi phạm các quy định hiện hành về biểu diễn nghệ thuật theo Nghị định số 144/2020/NĐ-CP.</li>
  </ul>

  <h3 class="doc-section-h1">ĐIỀU 5: QUYỀN LỢI TRUYỀN THÔNG DÀNH CHO BÊN B</h3>
  <ul class="doc-list">
    <li>Được ghi nhận danh vị chính thức: Đơn vị Tài trợ Trang phục Fashion Show - NTK Nguyễn Minh Công.</li>
    <li>Xuất hiện logo thương hiệu trên Poster, Backdrop, màn hình LED sân khấu chính và Thư cảm ơn sự kiện.</li>
    <li>Được đưa tin trong 05 bài đăng PR trên Fanpage Trường ĐH Văn Hiến và xuất hiện trong Video Recap / After Movie chính thức của chương trình.</li>
    <li>Đại diện Bên B được mời tham dự sự kiện tại hàng ghế VIP và nhận hoa, kỷ niệm chương tri ân trong phần Tổng kết chương trình.</li>
  </ul>

  <h3 class="doc-section-h1">ĐIỀU 6: HIỆU LỰC THI HÀNH</h3>
  <p class="doc-paragraph">Biên bản này có hiệu lực kể từ ngày ký cho đến khi hai Bên hoàn tất toàn bộ nghĩa vụ và chương trình kết thúc thành công. Biên bản được lập thành 04 (bốn) bản có giá trị pháp lý như nhau, mỗi Bên giữ 02 bản.</p>

  <div class="doc-sign-grid">
    <div class="doc-sign-col-left" style="text-align: center;">
      <div class="sign-title">ĐẠI DIỆN BÊN A<br>TRƯỜNG ĐẠI HỌC VĂN HIẾN<br>TRƯỞNG BAN TỔ CHỨC</div>
      <div class="sign-note">(Ký, ghi rõ họ tên và đóng dấu)</div>
      <img src="./assets/docx_media/image13.png" alt="Dấu mộc xác thực" class="stamp-seal-img">
      <div class="sign-name">Trần Thúy Quyên</div>
    </div>
    <div class="doc-sign-col-right">
      <div class="sign-title">ĐẠI DIỆN BÊN B<br>NHÀ THIẾT KẾ THỜI TRANG</div>
      <div class="sign-note">(Ký và ghi rõ họ tên)</div>
      <div style="height: 50px;"></div>
      <div class="sign-name">Nguyễn Minh Công</div>
    </div>
  </div>
</div>
"""

# --- APPENDIX 4: CÔNG VĂN SỞ VHTT TP.HCM ---
app4_html = """
<div class="doc-paper-wrapper" id="app4-doc" style="display: none;">
  <div class="doc-actions-top">
    <button class="btn-doc-action btn-copy-doc">📋 Sao chép toàn văn</button>
    <button class="btn-doc-action btn-print-doc">🖨️ In văn bản này</button>
  </div>

  <div class="doc-admin-header">
    <div class="doc-admin-left">
      <div class="agency-upper">BỘ GIÁO DỤC VÀ ĐÀO TẠO</div>
      <div class="agency-main">TRƯỜNG ĐẠI HỌC VĂN HIẾN</div>
      <div class="doc-number">Số: ....../CV-VHU-2027</div>
    </div>
    <div class="doc-admin-right">
      <div class="country-title">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</div>
      <div class="motto">Độc lập - Tự do - Hạnh phúc</div>
      <div class="doc-date">TP. Hồ Chí Minh, ngày 05 tháng 05 năm 2027</div>
    </div>
  </div>

  <h2 class="doc-title-main">CÔNG VĂN THÔNG BÁO VÀ ĐỀ NGHỊ CHẤP THUẬN<br>TỔ CHỨC HOẠT ĐỘNG BIỂU DIỄN NGHỆ THUẬT VÀ TRÌNH DIỄN THỜI TRANG</h2>
  <div class="doc-subtitle">(V/v: Tổ chức Chương trình Văn hóa & Nghệ thuật tỉnh Đồng Tháp năm 2027 "Chạm một sắc Sen")</div>

  <div class="doc-recipient">Kính gửi: SỞ VĂN HÓA VÀ THỂ THAO THÀNH PHỐ HỒ CHÍ MINH<br>(Phòng Quản lý Nghệ thuật)</div>

  <p class="doc-paragraph">Căn cứ Nghị định số 144/2020/NĐ-CP ngày 14 tháng 12 năm 2020 của Chính phủ quy định về hoạt động nghệ thuật biểu diễn;</p>
  <p class="doc-paragraph">Căn cứ Kế hoạch hoạt động văn hóa học đường của Trường Đại học Văn Hiến năm học 2026 – 2027 nhằm tăng cường kết nối và giáo dục truyền thống văn hóa dân tộc cho sinh viên;</p>
  <p class="doc-paragraph">Trường Đại học Văn Hiến trân trọng gửi văn bản thông báo và đề nghị Quý Sở xem xét, chấp thuận cho Nhà trường tổ chức hoạt động biểu diễn nghệ thuật và trình diễn thời trang trong khuôn khổ Chương trình Văn hóa & Nghệ thuật tỉnh Đồng Tháp năm 2027 với các thông tin chi tiết như sau:</p>

  <h3 class="doc-section-h1">I. ĐƠN VỊ TỔ CHỨC VÀ ĐẠI DIỆN CHÍNH THỨC</h3>
  <ul class="doc-list">
    <li><strong>Đơn vị tổ chức:</strong> TRƯỜNG ĐẠI HỌC VĂN HIẾN</li>
    <li><strong>Người đại diện Ban Tổ chức:</strong> Bà Trần Thúy Quyên – Trưởng Ban Tổ chức (SĐT: 0369449925)</li>
    <li><strong>Địa chỉ trụ sở:</strong> HungHau Campus, Khu chức năng 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM.</li>
  </ul>

  <h3 class="doc-section-h1">II. THÔNG TIN CHƯƠNG TRÌNH SỰ KIỆN</h3>
  <ul class="doc-list">
    <li><strong>Tên chương trình:</strong> Chương trình Văn hóa – Nghệ thuật tỉnh Đồng Tháp năm 2027 với chủ đề "Chạm một sắc Sen"</li>
    <li><strong>Thời gian tổ chức:</strong> Từ 07h30 đến 11h10, Chủ Nhật - Ngày 20 tháng 06 năm 2027.</li>
    <li><strong>Địa điểm tổ chức:</strong> Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus, Khu chức năng số 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM.</li>
    <li><strong>Quy mô tham dự:</strong> Khoảng 300 người (gồm giảng viên, sinh viên VHU và đại biểu khách mời).</li>
    <li><strong>Tính chất chương trình:</strong> Hoạt động giao lưu văn hóa nghệ thuật phi thương mại, không bán vé thu tiền dưới bất kỳ hình thức nào.</li>
  </ul>

  <h3 class="doc-section-h1">III. NỘI DUNG CHƯƠNG TRÌNH BIỂU DIỄN VÀ TRÌNH DIỄN THỜI TRANG</h3>
  <p class="doc-paragraph">Chương trình bao gồm các hoạt động biểu diễn nghệ thuật âm nhạc dân gian và tiết mục trình diễn thời trang tôn vinh văn hóa Nam Bộ với danh mục tiết mục cụ thể như sau:</p>

  <div class="table-scroll-wrapper">
<table class="doc-table">
    <thead>
      <tr>
        <th style="width: 20%;">Thời gian</th>
        <th>Nội dung tiết mục</th>
        <th>Nghệ sĩ / Nhân sự thể hiện</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>08:10 – 08:20</td>
        <td>Mở màn tiết mục nghệ thuật "Sắc Sen VHU" (Hát múa ca ngợi quê hương và hình ảnh hoa sen Đồng Tháp).</td>
        <td>CLB Văn nghệ Trường Đại học Văn Hiến</td>
      </tr>
      <tr>
        <td>08:40 – 09:00</td>
        <td>Trình diễn nghệ thuật "Hồn Sen Đất Việt" kết hợp âm nhạc truyền thống và Đờn ca tài tử Nam Bộ.</td>
        <td>Nghệ nhân Đờn ca tài tử phối hợp cùng CLB Văn nghệ VHU</td>
      </tr>
      <tr>
        <td>10:05 – 10:25</td>
        <td>Fashion Show "Sắc Sen" - Trình diễn Bộ sưu tập thời trang "Miệt Cù Lao" của NTK Nguyễn Minh Công.</td>
        <td>Hoa hậu Nguyễn Thị Yến Nhi, Á hậu Lê Phan Hạnh Nguyên & CLB Thời trang VHU</td>
      </tr>
      <tr>
        <td>10:25 – 10:40</td>
        <td>Trình diễn ca nhạc quê hương: Tiết mục "Hồn quê" và "Ếch ngoài đáy giếng".</td>
        <td>Ca sĩ khách mời Phương Mỹ Chi</td>
      </tr>
    </tbody>
  </table>
</div>

  <h3 class="doc-section-h1">IV. CAM KẾT VỀ AN NINH, TRẬT TỰ VÀ THUẦN PHONG MỸ TỤC</h3>
  <p class="doc-paragraph">Trường Đại học Văn Hiến xin cam kết thực hiện nghiêm túc các quy định pháp luật:</p>
  <ul class="doc-list">
    <li>Tất cả các tiết mục âm nhạc và Bộ sưu tập thời trang "Miệt Cù Lao" trình diễn đều có nội dung lành mạnh, tôn vinh nét đẹp văn hóa truyền thống sông nước miền Tây, không vi phạm thuần phong mỹ tục, không mang yếu tố kích động hay phương hại đến an ninh quốc gia.</li>
    <li>Chương trình diễn ra nội bộ trong khuôn viên cơ sở đào tạo của Nhà trường, chấp hành nghiêm các quy định về an ninh trật tự, phòng chống cháy nổ và cứu nạn cứu hộ.</li>
    <li>Chịu trách nhiệm hoàn toàn trước pháp luật về nội dung biểu diễn trong chương trình.</li>
  </ul>

  <h3 class="doc-section-h1">V. ĐỀ NGHỊ CHẤP THUẬN</h3>
  <p class="doc-paragraph">Kính đề nghị Sở Văn hóa và Thể thao Thành phố Hồ Chí Minh xem xét, chấp thuận cho Trường Đại học Văn Hiến được tổ chức các hoạt động biểu diễn nghệ thuật và trình diễn thời trang nêu trên trong khuôn khổ chương trình "Chạm một sắc Sen".</p>
  <p class="doc-paragraph">Xin trân trọng cảm ơn!</p>

  <div class="doc-sign-grid">
    <div class="doc-sign-col-left">
      <strong>Nơi nhận:</strong><br>
      - Như trên;<br>
      - UBND Xã Bình Hưng (để báo cáo);<br>
      - Công an Xã Bình Hưng (để phối hợp ANTT);<br>
      - Ban Giám hiệu VHU (để b/c);<br>
      - Lưu: VT, BTC.
    </div>
    <div class="doc-sign-col-right">
      <div class="sign-title">TM. BAN TỔ CHỨC</div>
      <div class="sign-title">TRƯỞNG BAN TỔ CHỨC</div>
      <div class="sign-note">(Ký, ghi rõ họ tên và đóng dấu)</div>
      <img src="./assets/docx_media/image13.png" alt="Dấu mộc xác thực" class="stamp-seal-img">
      <div class="sign-name">Trần Thúy Quyên</div>
    </div>
  </div>
</div>
"""

# --- APPENDIX 5: CÔNG VĂN UBND & CÔNG AN XÃ BÌNH HƯNG ---
app5_html = """
<div class="doc-paper-wrapper" id="app5-doc" style="display: none;">
  <div class="doc-actions-top">
    <button class="btn-doc-action btn-copy-doc">📋 Sao chép toàn văn</button>
    <button class="btn-doc-action btn-print-doc">🖨️ In văn bản này</button>
  </div>

  <div class="doc-admin-header">
    <div class="doc-admin-left">
      <div class="agency-upper">BỘ GIÁO DỤC VÀ ĐÀO TẠO</div>
      <div class="agency-main">TRƯỜNG ĐẠI HỌC VĂN HIẾN</div>
      <div class="doc-number">Số: ....../TB-BTC-2027</div>
    </div>
    <div class="doc-admin-right">
      <div class="country-title">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</div>
      <div class="motto">Độc lập - Tự do - Hạnh phúc</div>
      <div class="doc-date">TP. Hồ Chí Minh, ngày 05 tháng 05 năm 2027</div>
    </div>
  </div>

  <h2 class="doc-title-main">CÔNG VĂN THÔNG BÁO VÀ ĐỀ NGHỊ HỖ TRỢ</h2>
  <div class="doc-subtitle">(V/v: Đảm bảo an ninh trật tự, an toàn giao thông và phòng cháy chữa cháy – cứu nạn cứu hộ cho Chương trình Văn hóa – Nghệ thuật tỉnh Đồng Tháp năm 2027 "Chạm một sắc Sen")</div>

  <div class="doc-recipient">
    Kính gửi:<br>
    - Ủy ban nhân dân Xã Bình Hưng, TP.HCM;<br>
    - Công an Xã Bình Hưng, TP. Hồ Chí Minh;<br>
    - Đội Cảnh sát PCCC & CNCH – Công an Huyện Bình Chánh / Xã Bình Hưng.
  </div>

  <h3 class="doc-section-h1">I. CĂN CỨ VÀ MỤC ĐÍCH TỔ CHỨC</h3>
  <p class="doc-paragraph">Căn cứ định hướng chiến lược phát triển văn hóa học đường cho sinh viên Trường Đại học Văn Hiến năm 2027;</p>
  <p class="doc-paragraph">Căn cứ nhu cầu giao lưu văn hóa nghệ thuật và kết nối doanh nghiệp, nhà tài trợ với thế hệ trẻ;</p>
  <p class="doc-paragraph">Trường Đại học Văn Hiến xin trân trọng thông báo đến Quý Cơ quan về việc tổ chức sự kiện và đề nghị phối hợp hỗ trợ công tác đảm bảo an ninh trật tự (ANTT), an toàn giao thông (ATGT) và phòng cháy chữa cháy – cứu nạn cứu hộ (PCCC & CNCH) trên địa bàn.</p>

  <h3 class="doc-section-h1">II. THÔNG TIN CHI TIẾT VỀ SỰ KIỆN</h3>
  <div class="table-scroll-wrapper">
<table class="doc-table">
    <tbody>
      <tr>
        <td style="width: 30%; font-weight: bold;">Tên sự kiện:</td>
        <td>Chương trình Văn hóa – Nghệ thuật tỉnh Đồng Tháp năm 2027<br>Chủ đề: "Chạm một sắc Sen"</td>
      </tr>
      <tr>
        <td style="font-weight: bold;">Thời gian tổ chức:</td>
        <td>Từ 07:30 đến 11:30, Chủ Nhật - Ngày 20 tháng 06 năm 2027<br>(Công tác lắp đặt & tổng duyệt chuẩn bị từ 08:00 ngày 19/06/2027)</td>
      </tr>
      <tr>
        <td style="font-weight: bold;">Địa điểm tổ chức:</td>
        <td>Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus, Trường Đại học Văn Hiến<br>(Khu chức năng số 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM)</td>
      </tr>
      <tr>
        <td style="font-weight: bold;">Quy mô tham dự:</td>
        <td>Khoảng 300 đại biểu, khách mời danh dự, giảng viên và sinh viên</td>
      </tr>
      <tr>
        <td style="font-weight: bold;">Tính chất sự kiện:</td>
        <td>Sự kiện giáo dục, văn hóa nghệ thuật phi thương mại (Không bán vé thu tiền)</td>
      </tr>
    </tbody>
  </table>
</div>

  <h3 class="doc-section-h1">III. PHƯƠNG ÁN TỰ ĐẢM BẢO AN NINH TRẬT TỰ VÀ PCCC CỦA NHÀ TRƯỜNG</h3>
  <p class="doc-paragraph">Để đảm bảo sự kiện diễn ra trang trọng, an toàn tuyệt đối, Ban Tổ chức Trường Đại học Văn Hiến đã chủ động triển khai các phương án nội bộ bao gồm:</p>
  <ul class="doc-list">
    <li><strong>Công tác bảo vệ & An ninh trật tự:</strong> Bố trí lực lượng bảo vệ nội bộ (10 nhân sự) phân luồng phương tiện tại cổng ra vào HungHau Campus, hướng dẫn bãi xe sinh viên/khách mời và túc trực điều phối trật tự tại lối vào Tầng 9 Hội trường.</li>
    <li><strong>Công tác Phòng cháy chữa cháy & CNCH:</strong> Hệ thống báo cháy tự động, chữa cháy vách tường, bình chữa cháy xách tay và lối thoát hiểm tại Tầng 9 HungHau Campus đã được kiểm tra, đảm bảo vận hành tốt. Bố trí tổ PCCC cơ sở túc trực suốt thời gian diễn ra sự kiện.</li>
    <li><strong>Công tác Y tế & Hậu cần:</strong> Bố trí 01 Trạm y tế lưu động với đầy đủ trang thiết bị sơ cấp cứu ban đầu và nhân sự y tế túc trực tại khuôn viên sự kiện.</li>
  </ul>

  <h3 class="doc-section-h1">IV. NỘI DUNG ĐỀ NGHỊ HỖ TRỢ</h3>
  <p class="doc-paragraph">Nhằm hỗ trợ Nhà trường quản lý tốt an ninh địa bàn và phòng ngừa các sự cố phát sinh, Ban Tổ chức kính đề nghị UBND Xã Bình Hưng, Công an Xã Bình Hưng và Đội Cảnh sát PCCC & CNCH hỗ trợ một số nội dung sau:</p>
  <ul class="doc-list">
    <li><strong>UBND Xã Bình Hưng & Công an Xã Bình Hưng:</strong> Ghi nhận thông tin tổ chức sự kiện; hỗ trợ tuần tra, giám sát tình hình an ninh trật tự, an toàn giao thông tại tuyến đường Đại lộ Nguyễn Văn Linh khu vực trước cổng HungHau Campus trong khung giờ cao điểm đón khách và ra về (07:00 – 08:00 và 11:00 – 12:00 ngày 20/06/2027).</li>
    <li><strong>Công an Xã Bình Hưng & Đội Cảnh sát PCCC & CNCH:</strong> Hướng dẫn, hỗ trợ phương án an toàn PCCC & CNCH khi có yêu cầu; tạo điều kiện thuận lợi để sự kiện diễn ra an toàn, tuân thủ đúng quy định pháp luật.</li>
  </ul>

  <div style="background: #f1f5f9; padding: 12px 16px; border-radius: 6px; margin: 16px 0; font-size: 0.95rem;">
    <strong>Liên hệ trực tiếp của Ban Tổ chức sự kiện:</strong><br>
    - Bà Trần Thúy Quyên – Trưởng Ban Tổ chức sự kiện<br>
    - Điện thoại: 0369449925<br>
    - Địa chỉ: HungHau Campus, Khu chức năng 13E, Đại lộ Nguyễn Văn Linh, Xã Bình Hưng, TP.HCM.
  </div>

  <p class="doc-paragraph">Trường Đại học Văn Hiến rất mong nhận được sự quan tâm, hỗ trợ và tạo điều kiện của Quý Cơ quan để Chương trình Văn hóa – Nghệ thuật tỉnh Đồng Tháp năm 2027 được diễn ra thành công tốt đẹp.</p>
  <p class="doc-paragraph">Xin trân trọng cảm ơn!</p>

  <div class="doc-sign-grid">
    <div class="doc-sign-col-left">
      <strong>Nơi nhận:</strong><br>
      - Như trên;<br>
      - Ban Giám hiệu (để b/c);<br>
      - Công an Xã Bình Hưng;<br>
      - Lưu: VT, BTC.
    </div>
    <div class="doc-sign-col-right">
      <div class="sign-title">TM. BAN TỔ CHỨC NGÀY HỘI</div>
      <div class="sign-title">TRƯỞNG BAN TỔ CHỨC</div>
      <div class="sign-note">(Ký, ghi rõ họ tên và đóng dấu)</div>
      <img src="./assets/docx_media/image13.png" alt="Dấu mộc xác thực" class="stamp-seal-img">
      <div class="sign-name">Trần Thúy Quyên</div>
    </div>
  </div>
</div>
"""

with open('appendices_html.json', 'w', encoding='utf-8') as f:
    json.dump({
        'app1': app1_html,
        'app2': app2_html,
        'app3': app3_html,
        'app4': app4_html,
        'app5': app5_html
    }, f, ensure_ascii=False, indent=2)

print("Saved appendices_html.json successfully!")
