import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add font variables in :root
if '--font-heading:' not in css:
    css = css.replace(
        ':root {',
        ':root {\n  /* Masterpiece Editorial Typography */\n  --font-heading: \'Playfair Display\', Georgia, \'Times New Roman\', serif;\n  --font-body: \'Plus Jakarta Sans\', system-ui, -apple-system, sans-serif;'
    )

# 2. Apply font-heading
font_rule = """
h1, h2, .hero-main-title, .hero-theme-title, .section-title, .artist-name, .sponsor-tiers-title, .ticket-event-name {
  font-family: var(--font-heading);
}
"""
if 'font-family: var(--font-heading);' not in css:
    css = css + '\n' + font_rule

# 3. Add Masterpiece CSS styles
masterpiece_css = """
/* ============================================================
   MASTERPIECE UPGRADES: LOTUS CANVAS, PROGRESS BAR, AUDIO CAPSULE
============================================================ */
.hero-lotus-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.hero-content-relative {
  position: relative;
  z-index: 2;
}

.reading-progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  width: 0%;
  background: linear-gradient(90deg, #d49b19 0%, #d83a6f 100%);
  z-index: 1001;
  transition: width 0.08s ease-out;
  box-shadow: 0 0 10px rgba(216, 58, 111, 0.6);
}

/* Audio Capsule in Hero */
.hero-audio-capsule {
  background: rgba(6, 19, 41, 0.88);
  border: 1px solid rgba(216, 58, 111, 0.45);
  border-radius: var(--radius-lg);
  padding: 14px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  backdrop-filter: blur(12px);
  box-shadow: 0 8px 28px rgba(0,0,0,0.4);
}

.audio-capsule-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.audio-capsule-badge {
  font-size: 0.68rem;
  font-weight: 800;
  color: var(--sen-pink);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.audio-capsule-title {
  font-size: 0.86rem;
  font-weight: 700;
  color: #ffffff;
}

.equalizer-wave {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 18px;
}

.eq-bar {
  width: 3px;
  background: linear-gradient(to top, var(--vhu-gold-light), var(--sen-pink));
  border-radius: 2px;
  height: 100%;
  animation: eqWave 1s ease-in-out infinite alternate;
  animation-play-state: paused;
}

.eq-bar:nth-child(1) { height: 30%; animation-delay: 0.1s; }
.eq-bar:nth-child(2) { height: 75%; animation-delay: 0.3s; }
.eq-bar:nth-child(3) { height: 100%; animation-delay: 0.2s; }
.eq-bar:nth-child(4) { height: 50%; animation-delay: 0.4s; }
.eq-bar:nth-child(5) { height: 80%; animation-delay: 0.15s; }

@keyframes eqWave {
  0% { height: 20%; }
  100% { height: 100%; }
}

.btn-play-soundscape {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--sen-pink);
  color: #ffffff;
  font-size: 0.82rem;
  font-weight: 700;
  padding: 8px 14px;
  border-radius: var(--radius-full);
  border: none;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  box-shadow: 0 4px 14px rgba(216, 58, 111, 0.35);
}

.btn-play-soundscape:hover {
  background: var(--sen-pink-hover);
  transform: translateY(-1px);
}

.btn-play-soundscape.playing {
  background: var(--vhu-gold-gradient);
  color: var(--vhu-navy-dark) !important;
}

/* ============================================================
   ARTIST SPOTLIGHT SECTION
============================================================ */
.artist-spotlight-section {
  position: relative;
  background: linear-gradient(180deg, #f8fafc 0%, #edf3fc 50%, #f8fafc 100%);
}

.artist-showcase-grid {
  display: grid;
  grid-template-columns: 1.25fr 0.85fr;
  gap: 28px;
  align-items: stretch;
}

.artist-card-primary {
  background: #ffffff;
  border: 1px solid rgba(212, 155, 25, 0.35);
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: var(--shadow-lg);
  display: grid;
  grid-template-columns: 1fr 1.25fr;
  grid-row: span 2;
  position: relative;
}

.artist-img-frame {
  position: relative;
  background: #061329;
  overflow: hidden;
  cursor: pointer;
}

.artist-img-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-normal);
}

.artist-img-frame:hover img {
  transform: scale(1.04);
}

.artist-frame-badge {
  position: absolute;
  top: 14px;
  left: 14px;
  background: rgba(6, 19, 41, 0.85);
  color: var(--vhu-gold-light);
  border: 1px solid rgba(247, 183, 49, 0.4);
  font-size: 0.72rem;
  font-weight: 800;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  backdrop-filter: blur(8px);
}

.artist-bio-content {
  padding: 32px 28px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.artist-role-tag {
  font-size: 0.74rem;
  font-weight: 800;
  color: var(--sen-pink);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.artist-name {
  font-family: var(--font-heading);
  font-size: 1.85rem;
  font-weight: 800;
  color: var(--vhu-navy-base);
  margin-bottom: 6px;
  line-height: 1.2;
}

.artist-title-sub {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-bottom: 16px;
  font-weight: 500;
}

.artist-quote {
  font-style: italic;
  font-size: 0.92rem;
  color: var(--vhu-blue-primary);
  line-height: 1.6;
  background: var(--vhu-blue-soft);
  border-left: 3px solid var(--vhu-gold-primary);
  padding: 12px 16px;
  border-radius: 0 var(--radius-md) var(--radius-md) 0;
  margin-bottom: 20px;
}

.setlist-title {
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--vhu-navy-base);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
  letter-spacing: 0.04em;
}

.setlist-items {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 0.86rem;
  color: var(--text-secondary);
}

.setlist-items li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.artist-sub-card {
  background: #ffffff;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform var(--transition-fast), border-color var(--transition-fast);
}

.artist-sub-card:hover {
  transform: translateY(-2px);
  border-color: var(--vhu-blue-primary);
  box-shadow: var(--shadow-md);
}

.sub-card-header h4 {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--vhu-navy-base);
  margin: 8px 0 6px;
}

.sub-card-desc {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 14px;
}

.performance-highlight {
  background: #f8fafc;
  padding: 10px 14px;
  border-radius: var(--radius-md);
  font-size: 0.84rem;
  color: var(--vhu-blue-primary);
  border: 1px dashed var(--border-subtle);
}

.heritage-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #fff9ed;
  color: #b45309;
  border: 1px solid rgba(212, 155, 25, 0.4);
  font-size: 0.72rem;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: var(--radius-full);
}

.fashion-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #fdf2f6;
  color: var(--sen-pink);
  border: 1px solid rgba(216, 58, 111, 0.3);
  font-size: 0.72rem;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: var(--radius-full);
}

/* ============================================================
   METALLIC SPONSOR TIERS
============================================================ */
.sponsor-tiers-container {
  margin-top: 36px;
}

.sponsor-tiers-title {
  font-family: var(--font-heading);
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--vhu-navy-base);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.sponsor-tier-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.sponsor-tier-card {
  border-radius: var(--radius-lg);
  padding: 26px 22px;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition-normal), box-shadow var(--transition-normal);
  position: relative;
}

.sponsor-tier-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.sponsor-tier-card.card-diamond {
  background: linear-gradient(145deg, #061329 0%, #102a5c 100%);
  color: #ffffff;
  border: 2px solid rgba(247, 183, 49, 0.6);
  box-shadow: 0 10px 30px rgba(6, 19, 41, 0.25);
}

.sponsor-tier-card.card-gold {
  background: linear-gradient(145deg, #fffcf5 0%, #fff6e0 100%);
  border: 2px solid #eab308;
  color: var(--text-main);
}

.sponsor-tier-card.card-silver {
  background: linear-gradient(145deg, #f8fafc 0%, #f1f5f9 100%);
  border: 2px solid #94a3b8;
  color: var(--text-main);
}

.sponsor-tier-card.card-bronze {
  background: linear-gradient(145deg, #fff7ed 0%, #ffedd5 100%);
  border: 2px solid #ea580c;
  color: var(--text-main);
}

.tier-badge {
  align-self: flex-start;
  font-size: 0.74rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  margin-bottom: 12px;
}

.diamond-badge {
  background: linear-gradient(135deg, #f7b731 0%, #d49b19 100%);
  color: #061329;
}

.gold-badge {
  background: #eab308;
  color: #ffffff;
}

.silver-badge {
  background: #64748b;
  color: #ffffff;
}

.bronze-badge {
  background: #c2410c;
  color: #ffffff;
}

.tier-price {
  font-size: 1.6rem;
  font-weight: 900;
  line-height: 1.1;
  margin-bottom: 4px;
}

.card-diamond .tier-price {
  color: var(--vhu-gold-light);
}

.tier-quota {
  font-size: 0.8rem;
  margin-bottom: 18px;
  opacity: 0.85;
}

.tier-privileges {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 0.84rem;
  line-height: 1.45;
  margin-top: auto;
  padding-top: 14px;
  border-top: 1px solid rgba(0,0,0,0.08);
}

.card-diamond .tier-privileges {
  border-top-color: rgba(255,255,255,0.15);
}

.tier-privileges li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

/* ============================================================
   LIVE VIP TICKET SIMULATOR (PASSPORT SEN)
============================================================ */
.ticket-preview-column {
  display: flex;
  flex-direction: column;
}

.live-ticket-card {
  background: radial-gradient(circle at 80% 20%, #1e427e 0%, #0c2146 60%, #061329 100%);
  border: 2px solid rgba(247, 183, 49, 0.6);
  border-radius: var(--radius-xl);
  padding: 24px;
  color: #ffffff;
  box-shadow: 0 16px 36px rgba(6, 19, 41, 0.35);
  position: relative;
  overflow: hidden;
}

.live-ticket-card::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(60deg, transparent 40%, rgba(255, 255, 255, 0.08) 50%, transparent 60%);
  transform: rotate(35deg);
  animation: holoShimmer 6s infinite;
  pointer-events: none;
}

@keyframes holoShimmer {
  0% { transform: translateX(-100%) rotate(35deg); }
  25%, 100% { transform: translateX(100%) rotate(35deg); }
}

.ticket-holo-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 16px;
  border-bottom: 1px dashed rgba(255, 255, 255, 0.2);
  margin-bottom: 18px;
}

.ticket-org-tag {
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--vhu-gold-light);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.ticket-event-name {
  font-family: var(--font-heading);
  font-size: 1.35rem;
  font-weight: 900;
  color: #ffffff;
  margin-top: 2px;
}

.ticket-logo-badge {
  height: 42px;
  width: auto;
  background: #ffffff;
  padding: 3px;
  border-radius: var(--radius-sm);
}

.ticket-body-grid {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 20px;
  align-items: center;
  margin-bottom: 18px;
}

.ticket-qr-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.ticket-qr-img {
  width: 100px;
  height: 100px;
  background: #ffffff;
  padding: 6px;
  border-radius: var(--radius-md);
  margin-bottom: 8px;
}

.ticket-code-tag {
  font-family: monospace;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  color: var(--vhu-gold-light);
  background: rgba(0,0,0,0.3);
  padding: 2px 6px;
  border-radius: 4px;
}

.ticket-details-block {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 0.86rem;
}

.ticket-info-line {
  display: flex;
  flex-direction: column;
}

.ticket-info-line .info-label {
  font-size: 0.7rem;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.ticket-info-line .info-val {
  color: #f1f5f9;
  font-weight: 700;
}

.ticket-footer-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  padding-top: 14px;
  border-top: 1px dashed rgba(255, 255, 255, 0.2);
}

.ticket-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.74rem;
  font-weight: 700;
  color: var(--vhu-gold-light);
}

.btn-ticket-action {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.25);
  font-size: 0.8rem;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.btn-ticket-action:hover {
  background: var(--sen-pink);
  border-color: var(--sen-pink);
}

/* ============================================================
   SMART FLOATING QUICK NAVIGATION DOCK
============================================================ */
.floating-quick-dock {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 950;
  background: rgba(6, 19, 41, 0.88);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(247, 183, 49, 0.35);
  border-radius: var(--radius-full);
  padding: 6px 12px;
  display: flex;
  align-items: center;
  gap: 4px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

.dock-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #cbd5e1;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: var(--radius-full);
  transition: all var(--transition-fast);
  white-space: nowrap;
}

.dock-item:hover, .dock-item.active {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.12);
}

.dock-item.dock-item-highlight {
  background: var(--sen-pink);
  color: #ffffff !important;
  box-shadow: 0 2px 10px rgba(216, 58, 111, 0.4);
}

.dock-item.dock-item-highlight:hover {
  background: var(--sen-pink-hover);
}

@media (max-width: 900px) {
  .floating-quick-dock {
    display: none;
  }
  .artist-showcase-grid {
    grid-template-columns: 1fr;
  }
  .artist-card-primary {
    grid-template-columns: 1fr;
    grid-row: auto;
  }
  .artist-img-frame {
    height: 320px;
  }
}
"""

if '.hero-lotus-canvas' not in css:
    css = css + '\n' + masterpiece_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated styles.css with Masterpiece styles successfully!")
