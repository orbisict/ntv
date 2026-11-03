import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's inspect DOMContentLoaded in script.js
pos_dcl = js.find("document.addEventListener('DOMContentLoaded', () => {")
print("pos_dcl:", pos_dcl)

new_dcl = """document.addEventListener('DOMContentLoaded', () => {
  initLotusCanvas();
  initCountdown();
  initMobileNav();
  initAgendaFilters();
  initTabs();
  initRiskFilters();
  initBudgetFilters();
  initAppendices();
  initLightbox();
  initTicketStudio();
  initTicketRegistration();
  initAudioSimulation();
  initBackToTop();
  initScrollSpy();
  initReadingProgress();
  initFloatingDock();
});
"""

# Replace DOMContentLoaded block
pos_dcl_end = js.find('});', pos_dcl)
js = js[:pos_dcl] + new_dcl + js[pos_dcl_end+4:]

# Add implementations for new functions
extra_js = """
/* ============================================================
   MASTERPIECE UPGRADES: LOTUS CANVAS, TICKET STUDIO, AUDIO
============================================================ */

/* 1. Ambient Falling Lotus Petal Canvas */
function initLotusCanvas() {
  const canvas = document.getElementById('lotus-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  let width = canvas.width = canvas.parentElement.offsetWidth || window.innerWidth;
  let height = canvas.height = canvas.parentElement.offsetHeight || 600;

  window.addEventListener('resize', () => {
    if (!canvas.parentElement) return;
    width = canvas.width = canvas.parentElement.offsetWidth;
    height = canvas.height = canvas.parentElement.offsetHeight;
  });

  const petals = [];
  const petalCount = 22;

  // Soft palette: Lotus Pink, Blush Pink, Gold shimmer
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
      size: 10 + Math.random() * 14,
      speedY: 0.6 + Math.random() * 1.2,
      speedX: -0.4 + Math.random() * 0.8,
      rotation: Math.random() * 360,
      rotationSpeed: -1 + Math.random() * 2,
      sway: Math.random() * Math.PI * 2,
      swaySpeed: 0.02 + Math.random() * 0.03,
      color: colors[Math.floor(Math.random() * colors.length)]
    });
  }

  let isVisible = true;
  const observer = new IntersectionObserver((entries) => {
    isVisible = entries[0].isIntersecting;
  });
  observer.observe(canvas.parentElement);

  function drawPetal(p) {
    ctx.save();
    ctx.translate(p.x, p.y);
    ctx.rotate((p.rotation * Math.PI) / 180);

    ctx.beginPath();
    // Beautiful stylized lotus petal curve
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

/* 2. Interactive VIP Ticket Studio (Real-time Typing Sync) */
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

/* 3. Audio Melodic Synthesizer (Vietnamese Pentatonic Scale) */
function initAudioSimulation() {
  const toggleBtn = document.getElementById('btn-audio-toggle');
  const eqBars = document.querySelectorAll('.equalizer-wave .eq-bar');
  if (!toggleBtn) return;

  let isPlaying = false;
  let audioCtx = null;
  let timerId = null;

  // Pentatonic notes in Hz (C4, D4, F4, G4, A4, C5, D5)
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
    } catch(e) {
      // AudioContext policy
    }
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

/* 4. Reading Progress Bar */
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

/* 5. Floating Quick Navigation Dock Active Spy */
function initFloatingDock() {
  const dockItems = document.querySelectorAll('.floating-quick-dock .dock-item');
  if (!dockItems.length) return;

  const sections = Array.from(dockItems).map(item => {
    const id = item.getAttribute('href');
    return id && id.startsWith('#') ? document.querySelector(id) : null;
  }).filter(Boolean);

  window.addEventListener('scroll', () => {
    let currentId = '';
    const scrollPos = window.scrollY + 200;

    for (let i = sections.length - 1; i >= 0; i--) {
      const sec = sections[i];
      if (sec.offsetTop <= scrollPos) {
        currentId = '#' + sec.id;
        break;
      }
    }

    dockItems.forEach(item => {
      if (item.getAttribute('href') === currentId) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  }, { passive: true });
}
"""

if 'initLotusCanvas' not in js:
    js = js + '\n' + extra_js

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated script.js with Masterpiece interactive scripts successfully!")
