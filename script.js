/* ============================================================
   TRƯỜNG ĐẠI HỌC VĂN HIẾN - KẾ HOẠCH "CHẠM MỘT SẮC SEN" 2027
   Main Interactive Script
============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  initCountdown();
  initLotusCanvas();
  initMobileNav();
  initAgendaFilters();
  initTabs();
  initAppendixTabs();
  initRiskFilters();
  initBudgetFilters();
  initLightbox();
  initTicketStudio();
  initTicketRegistration();
  initAudioSimulation();
  initBackToTop();
  initMobileFloatingBar();
  initScrollSpy();
  initReadingProgress();
});

/* ============================================================
   1. COUNTDOWN TIMER (20/06/2027 07:30 GMT+7)
============================================================ */
function initCountdown() {
  const targetDate = new Date('2027-06-20T07:30:00+07:00').getTime();

  function update() {
    const now = new Date().getTime();
    const diff = targetDate - now;

    const elD = document.getElementById('days');
    const elH = document.getElementById('hours');
    const elM = document.getElementById('mins');
    const elS = document.getElementById('secs');

    if (!elD || !elH || !elM || !elS) return;

    if (diff <= 0) {
      elD.textContent = '00';
      elH.textContent = '00';
      elM.textContent = '00';
      elS.textContent = '00';
      return;
    }

    const d = Math.floor(diff / (1000 * 60 * 60 * 24));
    const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const s = Math.floor((diff % (1000 * 60)) / 1000);

    const pad = (n) => (n < 10 ? '0' + n : n);

    elD.textContent = d;
    elH.textContent = pad(h);
    elM.textContent = pad(m);
    elS.textContent = pad(s);
  }

  update();
  setInterval(update, 1000);
}

/* ============================================================
   2. AMBIENT LOTUS CANVAS
============================================================ */
function initLotusCanvas() {
  const canvas = document.getElementById('lotus-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  const parent = canvas.parentElement;
  if (!parent) return;

  let width = canvas.width = parent.offsetWidth || window.innerWidth;
  let height = canvas.height = parent.offsetHeight || 600;

  window.addEventListener('resize', () => {
    if (!parent) return;
    width = canvas.width = parent.offsetWidth;
    height = canvas.height = parent.offsetHeight;
  }, { passive: true });

  const petals = [];
  const petalCount = 20;

  const colors = [
    { r: 216, g: 58, b: 111, a: 0.65 },
    { r: 255, g: 117, b: 151, a: 0.6 },
    { r: 247, g: 183, b: 49, a: 0.45 },
    { r: 255, g: 182, b: 193, a: 0.55 }
  ];

  for (let i = 0; i < petalCount; i++) {
    petals.push({
      x: Math.random() * width,
      y: Math.random() * height,
      size: 10 + Math.random() * 12,
      speedY: 0.5 + Math.random() * 1.0,
      speedX: -0.4 + Math.random() * 0.8,
      rotation: Math.random() * 360,
      rotationSpeed: -1 + Math.random() * 2,
      sway: Math.random() * Math.PI * 2,
      swaySpeed: 0.02 + Math.random() * 0.03,
      color: colors[Math.floor(Math.random() * colors.length)]
    });
  }

  let isVisible = true;
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      isVisible = entries[0].isIntersecting;
    });
    observer.observe(parent);
  }

  function drawPetal(p) {
    ctx.save();
    ctx.translate(p.x, p.y);
    ctx.rotate((p.rotation * Math.PI) / 180);

    ctx.beginPath();
    ctx.moveTo(0, -p.size);
    ctx.bezierCurveTo(p.size * 0.8, -p.size * 0.4, p.size * 0.8, p.size * 0.6, 0, p.size);
    ctx.bezierCurveTo(-p.size * 0.8, p.size * 0.6, -p.size * 0.8, -p.size * 0.4, 0, -p.size);
    ctx.closePath();

    const radGrad = ctx.createRadialGradient(0, -p.size * 0.3, p.size * 0.1, 0, 0, p.size);
    radGrad.addColorStop(0, `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, ${p.color.a})`);
    radGrad.addColorStop(1, `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, 0.15)`);

    ctx.fillStyle = radGrad;
    ctx.fill();

    ctx.restore();
  }

  function loop() {
    if (isVisible) {
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < petals.length; i++) {
        const p = petals[i];
        p.sway += p.swaySpeed;
        p.y += p.speedY;
        p.x += p.speedX + Math.sin(p.sway) * 0.7;
        p.rotation += p.rotationSpeed;

        if (p.y > height + p.size) {
          p.y = -p.size;
          p.x = Math.random() * width;
        }
        if (p.x > width + p.size) p.x = -p.size;
        if (p.x < -p.size) p.x = width + p.size;

        drawPetal(p);
      }
    }
    requestAnimationFrame(loop);
  }

  loop();
}

/* ============================================================
   3. MOBILE DRAWER NAVIGATION
============================================================ */
function initMobileNav() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const drawer = document.getElementById('mobile-nav-drawer');
  const backdrop = document.getElementById('mobile-nav-backdrop');
  const closeBtn = document.getElementById('mobile-drawer-close');

  if (!menuBtn || !drawer) return;

  function openDrawer() {
    drawer.classList.add('open');
    if (backdrop) backdrop.classList.add('active');
    document.body.classList.add('menu-open');
    menuBtn.setAttribute('aria-expanded', 'true');
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    if (backdrop) backdrop.classList.remove('active');
    document.body.classList.remove('menu-open');
    menuBtn.setAttribute('aria-expanded', 'false');
  }

  menuBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (drawer.classList.contains('open')) {
      closeDrawer();
    } else {
      openDrawer();
    }
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      closeDrawer();
    });
  }

  if (backdrop) {
    backdrop.addEventListener('click', closeDrawer);
  }

  drawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

/* ============================================================
   4. AGENDA CATEGORY FILTERS (3 PHASES, 11 ITEMS TOTAL)
============================================================ */
function initAgendaFilters() {
  const filterBtns = document.querySelectorAll('.agenda-filter-btn');
  const timelineNodes = document.querySelectorAll('.timeline-node');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter') || 'all';

      timelineNodes.forEach(node => {
        const typeStr = (node.getAttribute('data-type') || '').trim();
        const types = typeStr.split(/\s+/);

        if (filter === 'all' || types.includes(filter)) {
          node.classList.remove('node-hidden');
          node.classList.remove('hide');
          node.style.setProperty('display', '', '');
        } else {
          node.classList.add('node-hidden');
          node.classList.add('hide');
          node.style.setProperty('display', 'none', 'important');
        }
      });
    });
  });
}

/* ============================================================
   5. UNIFIED TAB SWITCHER (.tab-nav-wrapper, .tab-pill-btn, .tab-pane)
============================================================ */
function initTabs() {
  document.querySelectorAll('.tab-nav-wrapper').forEach(nav => {
    const btns = nav.querySelectorAll('.tab-pill-btn');
    const container = nav.closest('section') || nav.parentElement;
    if (!container) return;

    btns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = btn.getAttribute('data-tab-target');
        if (!targetId) return;

        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const panes = container.querySelectorAll('.tab-pane');
        panes.forEach(pane => {
          if (pane.id === targetId) {
            pane.classList.add('active');
          } else {
            pane.classList.remove('active');
          }
        });

        // If in risk section, re-run risk filtering
        if (typeof window.filterRisks === 'function') {
          window.filterRisks();
        }
      });
    });
  });
}

/* ============================================================
   6. APPENDIX TABS SWITCHER (.appendix-nav-pill-group, .app-tab-btn, .app-content-pane)
============================================================ */
function initAppendixTabs() {
  const group = document.querySelector('.appendix-nav-pill-group');
  if (!group) return;

  const btns = group.querySelectorAll('.app-tab-btn');
  const section = group.closest('section') || document;
  const panes = section.querySelectorAll('.app-content-pane');

  btns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = btn.getAttribute('data-app-target');
      if (!targetId) return;

      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      panes.forEach(pane => {
        if (pane.id === targetId) {
          pane.classList.add('active');
        } else {
          pane.classList.remove('active');
        }
      });
    });
  });
}

/* ============================================================
   7. RISK MANAGEMENT SEARCH & EXACT SEVERITY FILTER
============================================================ */
function initRiskFilters() {
  const searchInput = document.getElementById('risk-search-input');
  const severitySelect = document.getElementById('risk-severity-select');
  const tables = [
    document.getElementById('risk-table-plan'),
    document.getElementById('risk-table-event'),
    document.getElementById('risk-table-media')
  ];

  window.filterRisks = function() {
    const q = (searchInput ? searchInput.value : '').toLowerCase().trim();
    const sev = (severitySelect ? severitySelect.value : 'all').toLowerCase().trim();

    tables.forEach(table => {
      if (!table) return;
      const rows = table.querySelectorAll('tbody tr');
      rows.forEach(tr => {
        const rowText = tr.textContent.toLowerCase();
        const rowSev = (tr.getAttribute('data-severity') || '').toLowerCase().trim();

        const matchQ = !q || rowText.includes(q);
        const matchSev = (sev === 'all' || rowSev === sev);

        if (matchQ && matchSev) {
          tr.style.display = '';
        } else {
          tr.style.display = 'none';
        }
      });
    });
  };

  if (searchInput) searchInput.addEventListener('input', window.filterRisks);
  if (severitySelect) severitySelect.addEventListener('change', window.filterRisks);
}

/* ============================================================
   8. BUDGET TABLE SEARCH & CATEGORY FILTER
============================================================ */
function initBudgetFilters() {
  const groupSelect = document.getElementById('budget-group-select');
  const searchInput = document.getElementById('budget-search-input');
  const table = document.getElementById('budget-master-table');
  const countEl = document.getElementById('budget-visible-count');

  if (!table) return;

  function filter() {
    const group = (groupSelect ? groupSelect.value : 'all').trim();
    const q = (searchInput ? searchInput.value : '').toLowerCase().trim();

    const headerRows = table.querySelectorAll('.budget-group-header-row');
    const itemRows = table.querySelectorAll('.budget-item-row');

    let visibleCount = 0;
    const visibleGroups = new Set();

    itemRows.forEach(tr => {
      const code = (tr.getAttribute('data-group-code') || '').trim();
      const text = tr.textContent.toLowerCase();

      const matchGroup = (group === 'all' || code === group);
      const matchQ = (!q || text.includes(q));

      if (matchGroup && matchQ) {
        tr.style.display = '';
        visibleCount++;
        visibleGroups.add(code);
      } else {
        tr.style.display = 'none';
      }
    });

    headerRows.forEach(hr => {
      const code = (hr.getAttribute('data-group-code') || '').trim();
      if (visibleGroups.has(code)) {
        hr.style.display = '';
      } else {
        hr.style.display = 'none';
      }
    });

    if (countEl) countEl.textContent = visibleCount;
  }

  if (groupSelect) groupSelect.addEventListener('change', filter);
  if (searchInput) searchInput.addEventListener('input', filter);
}

/* ============================================================
   9. IMAGE LIGHTBOX MODAL
============================================================ */
function initLightbox() {
  const dialog = document.getElementById('image-lightbox-dialog');
  const imgEl = document.getElementById('lightbox-img');
  const titleEl = document.getElementById('lightbox-title');
  const captionEl = document.getElementById('lightbox-caption');
  const closeBtn = document.getElementById('lightbox-close-btn');

  if (!dialog || !imgEl) return;

  document.querySelectorAll('[data-lightbox]').forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const src = trigger.getAttribute('data-src') || trigger.querySelector('img')?.src;
      const title = trigger.getAttribute('data-title') || '';
      const caption = trigger.getAttribute('data-caption') || '';

      if (src) {
        imgEl.src = src;
        if (titleEl) titleEl.textContent = title;
        if (captionEl) captionEl.textContent = caption;

        if (typeof dialog.showModal === 'function') {
          dialog.showModal();
        } else {
          dialog.setAttribute('open', '');
        }
      }
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      if (typeof dialog.close === 'function') {
        dialog.close();
      } else {
        dialog.removeAttribute('open');
      }
    });
  }

  dialog.addEventListener('click', (e) => {
    if (e.target === dialog) {
      if (typeof dialog.close === 'function') {
        dialog.close();
      } else {
        dialog.removeAttribute('open');
      }
    }
  });
}

/* ============================================================
   10. LIVE VIP TICKET STUDIO (REAL-TIME SYNC)
============================================================ */
function initTicketStudio() {
  const nameInput = document.getElementById('reg-fullname');
  const mssvInput = document.getElementById('reg-mssv');
  const facultySelect = document.getElementById('reg-faculty');

  const displayName = document.getElementById('ticket-display-name');
  const displayMssv = document.getElementById('ticket-display-mssv');
  const displayFaculty = document.getElementById('ticket-display-faculty');
  const displayCode = document.getElementById('ticket-display-code');

  function update() {
    if (displayName && nameInput) {
      displayName.textContent = nameInput.value.trim() || 'Nguyễn Văn A';
    }
    if (displayMssv && mssvInput) {
      const val = mssvInput.value.trim() || '241A010999';
      displayMssv.textContent = val;
      if (displayCode) {
        displayCode.textContent = 'VHU-SEN-' + val.toUpperCase();
      }
    }
    if (displayFaculty && facultySelect) {
      displayFaculty.textContent = facultySelect.value || 'Khoa Du lịch';
    }
  }

  if (nameInput) nameInput.addEventListener('input', update);
  if (mssvInput) mssvInput.addEventListener('input', update);
  if (facultySelect) facultySelect.addEventListener('change', update);

  update();
}

/* ============================================================
   11. TICKET FORM REGISTRATION SUBMISSION
============================================================ */
function initTicketRegistration() {
  const form = document.getElementById('ticket-reg-form');
  const dialog = document.getElementById('ticket-result-dialog');
  const closeBtn = document.getElementById('ticket-close-btn');

  if (!form || !dialog) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('reg-fullname')?.value || 'Nguyễn Văn A';
    const mssv = document.getElementById('reg-mssv')?.value || '241A010999';
    const faculty = document.getElementById('reg-faculty')?.value || 'Khoa Du lịch';

    const mName = document.getElementById('modal-display-name');
    const mMssv = document.getElementById('modal-display-mssv');
    const mFaculty = document.getElementById('modal-display-faculty');
    const mCode = document.getElementById('modal-display-code');

    if (mName) mName.textContent = name;
    if (mMssv) mMssv.textContent = mssv;
    if (mFaculty) mFaculty.textContent = faculty;
    if (mCode) mCode.textContent = 'VHU-SEN-' + mssv.toUpperCase();

    if (typeof dialog.showModal === 'function') {
      dialog.showModal();
    } else {
      dialog.setAttribute('open', '');
    }
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      if (typeof dialog.close === 'function') {
        dialog.close();
      } else {
        dialog.removeAttribute('open');
      }
    });
  }

  dialog.addEventListener('click', (e) => {
    if (e.target === dialog) {
      if (typeof dialog.close === 'function') {
        dialog.close();
      } else {
        dialog.removeAttribute('open');
      }
    }
  });
}

/* ============================================================
   12. AUDIO MELODIC SYNTHESIZER (VIETNAMESE PENTATONIC)
============================================================ */
function initAudioSimulation() {
  const toggleBtn = document.getElementById('btn-audio-toggle');
  const eqBars = document.querySelectorAll('.equalizer-wave .eq-bar');
  if (!toggleBtn) return;

  let isPlaying = false;
  let audioCtx = null;
  let timerId = null;

  const pentatonicScale = [261.63, 293.66, 349.23, 392.00, 440.00, 523.25, 587.33];
  let noteIndex = 0;

  function playTone(freq) {
    if (!audioCtx) return;
    try {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

      gain.gain.setValueAtTime(0, audioCtx.currentTime);
      gain.gain.linearRampToValueAtTime(0.08, audioCtx.currentTime + 0.08);
      gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 1.2);

      osc.connect(gain);
      gain.connect(audioCtx.destination);

      osc.start();
      osc.stop(audioCtx.currentTime + 1.25);
    } catch(e) {}
  }

  function startMelody() {
    function step() {
      if (!isPlaying) return;
      const freq = pentatonicScale[noteIndex % pentatonicScale.length];
      playTone(freq);
      noteIndex = (noteIndex + 1 + Math.floor(Math.random() * 2)) % pentatonicScale.length;
      timerId = setTimeout(step, 900 + Math.random() * 400);
    }
    step();
  }

  toggleBtn.addEventListener('click', () => {
    isPlaying = !isPlaying;

    if (isPlaying) {
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
      } catch(e) {}

      toggleBtn.innerHTML = '<svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg> Tạm dừng giai điệu';
      toggleBtn.classList.add('playing');

      eqBars.forEach(b => b.style.animationPlayState = 'running');
      startMelody();
    } else {
      toggleBtn.innerHTML = '<svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg> Bật giai điệu Sen';
      toggleBtn.classList.remove('playing');

      eqBars.forEach(b => b.style.animationPlayState = 'paused');
      if (timerId) clearTimeout(timerId);
    }
  });
}

/* ============================================================
   13. BACK TO TOP BUTTON
============================================================ */
function initBackToTop() {
  const btn = document.getElementById('back-to-top-btn');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

function initMobileFloatingBar() {
  const bar = document.getElementById('mobile-floating-bar');
  if (!bar) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 280) {
      bar.classList.add('visible');
    } else {
      bar.classList.remove('visible');
    }
  }, { passive: true });
}

/* ============================================================
   14. SCROLL SPY FOR NAVIGATION HIGHLIGHT
============================================================ */
function initScrollSpy() {
  const navLinks = document.querySelectorAll('.desktop-nav .nav-link');
  if (!navLinks.length) return;

  const sections = Array.from(navLinks).map(link => {
    const id = link.getAttribute('href');
    return id && id.startsWith('#') ? document.querySelector(id) : null;
  }).filter(Boolean);

  window.addEventListener('scroll', () => {
    let currentId = '';
    const scrollPos = window.scrollY + 120;

    for (let i = sections.length - 1; i >= 0; i--) {
      const sec = sections[i];
      if (sec.offsetTop <= scrollPos) {
        currentId = '#' + sec.id;
        break;
      }
    }

    navLinks.forEach(link => {
      if (link.getAttribute('href') === currentId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }, { passive: true });
}

/* ============================================================
   15. READING PROGRESS BAR
============================================================ */
function initReadingProgress() {
  const bar = document.getElementById('reading-progress-bar');
  if (!bar) return;

  window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (totalHeight <= 0) return;
    const progress = Math.min(100, Math.max(0, (window.scrollY / totalHeight) * 100));
    bar.style.width = progress + '%';
  }, { passive: true });
}

/* ============================================================
   16. DEDICATED PRINT FUNCTIONS (TICKET & OFFICIAL APPENDICES)
============================================================ */
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

  // Use invisible iframe to bypass popup blocker and prevent printing the full site
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
      position: relative;
    }

    .notch-top {
      position: absolute;
      top: -12px;
      right: -13px;
      width: 24px;
      height: 24px;
      background: #f8fafc;
      border-radius: 50%;
      border: 2px solid #0b1f42;
      z-index: 2;
    }
    .notch-bottom {
      position: absolute;
      bottom: -12px;
      right: -13px;
      width: 24px;
      height: 24px;
      background: #f8fafc;
      border-radius: 50%;
      border: 2px solid #0b1f42;
      z-index: 2;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-logo {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      object-fit: contain;
    }
    .ticket-badge-vip {
      background: #d49b19;
      color: #0b1f42;
      font-size: 12px;
      font-weight: 900;
      padding: 5px 12px;
      border-radius: 20px;
      letter-spacing: 0.06em;
    }

    .event-theme-box {
      margin-bottom: 16px;
    }
    .event-sup-title {
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      color: #d83a6f;
      letter-spacing: 0.05em;
      margin-bottom: 3px;
    }
    .event-grand-title {
      font-family: Georgia, serif;
      font-size: 25px;
      font-weight: 900;
      color: #0b1f42;
      line-height: 1.2;
      margin-bottom: 6px;
    }
    .event-grand-title span {
      color: #d83a6f;
    }
    .event-guest-stars {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #fdf2f8;
      border: 1px solid #fbcfe8;
      color: #be185d;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 20px;
    }

    .info-matrix {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px 16px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 14px;
    }
    .info-item {
      display: flex;
      flex-direction: column;
    }
    .info-item.span-2 {
      grid-column: span 2;
    }
    .info-label {
      font-size: 9.5px;
      font-weight: 700;
      text-transform: uppercase;
      color: #64748b;
      letter-spacing: 0.04em;
      margin-bottom: 2px;
    }
    .info-val {
      font-size: 13.5px;
      font-weight: 800;
      color: #0b1f42;
    }
    .info-val.highlight-name {
      font-size: 16.5px;
      color: #0b1f42;
    }
    .info-val.seat-badge {
      display: inline-block;
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fde68a;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 900;
      width: fit-content;
    }

    .ticket-inner-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 10.5px;
      color: #64748b;
      padding-top: 4px;
    }

    .stub-tag {
      font-size: 11px;
      font-weight: 900;
      color: #0b1f42;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 8px;
      background: #e2e8f0;
      padding: 4px 10px;
      border-radius: 6px;
      width: 100%;
    }
    .stub-qr-container {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      padding: 8px;
      border-radius: 10px;
      margin-bottom: 8px;
    }
    .stub-qr {
      width: 105px;
      height: 105px;
      display: block;
      object-fit: contain;
    }
    .stub-code-text {
      font-family: monospace;
      font-size: 12px;
      font-weight: 900;
      letter-spacing: 0.08em;
      color: #0b1f42;
      margin-bottom: 6px;
    }
    .stub-guest-name {
      font-size: 12px;
      font-weight: 800;
      color: #0b1f42;
      margin-bottom: 2px;
      max-width: 180px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .stub-note {
      font-size: 9.5px;
      color: #64748b;
      line-height: 1.3;
    }

    .guide-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 18px 22px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .guide-header-title {
      font-size: 12px;
      font-weight: 900;
      text-transform: uppercase;
      color: #0b1f42;
      letter-spacing: 0.05em;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 8px;
    }
    .guide-columns {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px 20px;
    }
    .guide-step {
      font-size: 11px;
      line-height: 1.5;
      color: #334155;
    }
    .guide-step strong {
      color: #0b1f42;
      font-weight: 800;
    }
    .guide-footer-note {
      margin-top: 12px;
      padding-top: 10px;
      border-top: 1px dashed #e2e8f0;
      font-size: 10px;
      color: #64748b;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="ticket-sheet">
    <div class="vip-ticket-container">
      <div class="ticket-main-section">
        <div class="notch-top"></div>
        <div class="notch-bottom"></div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 1px solid #f1f5f9;">
          <div class="brand-group">
            <img src="${logoUrl}" class="brand-logo" alt="Logo VHU">
            <div>
              <div style="font-size: 13px; font-weight: 900; color: #0b1f42; letter-spacing: 0.03em;">TRƯỜNG ĐẠI HỌC VĂN HIẾN</div>
              <div style="font-size: 10.5px; color: #64748b;">HUNGHAU CAMPUS &bull; BAN TỔ CHỨC SỰ KIỆN</div>
            </div>
          </div>
          <div class="ticket-badge-vip">★ VÉ MỜI VIP</div>
        </div>

        <div class="event-theme-box">
          <div class="event-sup-title">CHƯƠNG TRÌNH VĂN HÓA &amp; NGHỆ THUẬT TỈNH ĐỒNG THÁP NĂM 2027</div>
          <div class="event-grand-title">CHẠM MỘT SẮC <span>SEN</span></div>
          <div class="event-guest-stars">
            ★ Ca sĩ Phương Mỹ Chi &bull; Di sản Đờn ca tài tử &bull; Fashion Show BST Sen
          </div>
        </div>

        <div class="info-matrix">
          <div class="info-item">
            <span class="info-label">Họ và tên khách mời:</span>
            <span class="info-val highlight-name">${name}</span>
          </div>
          <div class="info-item">
            <span class="info-label">Mã định danh / MSSV:</span>
            <span class="info-val">${mssv}</span>
          </div>
          <div class="info-item">
            <span class="info-label">Khoa / Đơn vị:</span>
            <span class="info-val">${faculty}</span>
          </div>
          <div class="info-item">
            <span class="info-label">Vị trí chỗ ngồi:</span>
            <span class="info-val seat-badge">KHÁN ĐÀI A (HÀNG GHẾ VIP)</span>
          </div>
          <div class="info-item span-2">
            <span class="info-label">Thời gian check-in &amp; Khai mạc:</span>
            <span class="info-val">07:30 – 11:10 &bull; Chủ Nhật, Ngày 20/06/2027</span>
          </div>
          <div class="info-item span-2">
            <span class="info-label">Địa điểm diễn ra:</span>
            <span class="info-val">Tầng 9, Hội trường Trần Hưng Đạo, HungHau Campus (13E Nguyễn Văn Linh, Nam TP.HCM)</span>
          </div>
        </div>

        <div class="ticket-inner-footer">
          <span>* Vé hợp lệ kèm trọn bộ quà tặng Sen Passport &amp; Khăn rằn</span>
          <span style="font-weight: 700; color: #0b1f42;">Hotline BTC: 0369.449.925</span>
        </div>
      </div>

      <div class="ticket-stub-section">
        <div class="stub-tag">CUỐNG VÉ CHECK-IN</div>
        <div class="stub-qr-container">
          <img src="${qrUrl}" alt="QR" class="stub-qr">
        </div>
        <div class="stub-code-text">${code}</div>
        <div class="stub-guest-name">${name}</div>
        <div style="font-size: 10px; color: #64748b; margin-bottom: 6px;">GATE A &bull; KHÁN ĐÀI VIP</div>
        <div class="stub-note">Xuất trình tại Bàn Đón tiếp Tầng 9 để nhận Thẻ đeo sự kiện</div>
      </div>
    </div>

    <div class="guide-card">
      <div class="guide-header-title">
        QUYỀN LỢI ĐẠI BIỂU &amp; HƯỚNG DẪN THAM DỰ SỰ KIỆN
      </div>
      <div class="guide-columns">
        <div class="guide-step">
          <strong>1. Thời gian Check-in:</strong> Có mặt tại Bàn Lễ tân Tầng 9 từ 07:30 đến 08:10 để quét mã QR và ổn định khán đài VIP trước lễ khai mạc.
        </div>
        <div class="guide-step">
          <strong>2. Đặc quyền Vé VIP:</strong> Nhận 01 cuốn Passport Sen đóng dấu lưu niệm, 01 khăn rằn Nam Bộ độc quyền và phiếu trải nghiệm ẩm thực sen.
        </div>
        <div class="guide-step">
          <strong>3. Trang phục tham dự:</strong> Khuyến khích Áo dài truyền thống hoặc trang phục trang trọng, thanh lịch tôn vinh văn hóa học đường.
        </div>
        <div class="guide-step">
          <strong>4. Hỗ trợ đón tiếp:</strong> Đội ngũ Tình nguyện viên và Lễ tân VHU túc trực hỗ trợ suốt chương trình. Hotline: 0369.449.925.
        </div>
      </div>
      <div class="guide-footer-note">
        TRƯỜNG ĐẠI HỌC VĂN HIẾN &bull; "THÀNH NHÂN TRƯỚC KHI THÀNH DANH" &bull; LƯU HÀNH NỘI BỘ NĂM 2027
      </div>
    </div>
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

  printViaIframe(html);
}

function printActiveAppendix() {
  const activePane = document.querySelector('.app-content-pane.active .doc-paper-wrapper');
  if (!activePane) return;

  // Print via isolated iframe

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
  doc.write(html);
  doc.close();
  setTimeout(() => {
    try {
      frame.contentWindow.focus();
      frame.contentWindow.print();
    } catch (e) {
      window.print();
    }
  }, 400);
}

function copyActiveAppendix(btn) {
  const activePane = document.querySelector('.app-content-pane.active .doc-paper-wrapper');
  if (!activePane) return;

  const clone = activePane.cloneNode(true);
  const actions = clone.querySelector('.doc-actions-top');
  if (actions) actions.remove();

  const text = clone.innerText.trim();
  navigator.clipboard.writeText(text).then(() => {
    const originalHtml = btn.innerHTML;
    btn.innerHTML = '<svg class="v-icon v-icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Đã sao chép!';
    btn.style.background = '#dcfce7';
    btn.style.color = '#15803d';
    btn.style.borderColor = '#86efac';

    setTimeout(() => {
      btn.innerHTML = originalHtml;
      btn.style.background = '';
      btn.style.color = '';
      btn.style.borderColor = '';
    }, 2200);
  }).catch(err => {
    alert('Không thể sao chép: ' + err);
  });
}

// Global window assignments
window.printTicket = printTicket;
window.printActiveAppendix = printActiveAppendix;
window.copyActiveAppendix = copyActiveAppendix;
