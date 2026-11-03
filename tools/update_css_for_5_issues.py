import re

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update .stacked-bar & .bar-segment (Global)
old_stacked_css = '''.stacked-bar {
  display: flex;
  height: 28px;
  border-radius: var(--radius-full);
  overflow: hidden;
  margin-bottom: 16px;
}

.bar-segment {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 800;
  color: #ffffff;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 0 4px;
}'''

new_stacked_css = '''.stacked-bar {
  display: flex;
  height: 14px;
  border-radius: var(--radius-full);
  overflow: hidden;
  background: #e2e8f0;
  margin: 14px 0 18px;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}

.bar-segment {
  height: 100%;
  transition: width 0.4s ease;
}'''

if old_stacked_css in code:
    code = code.replace(old_stacked_css, new_stacked_css, 1)
    print("SUCCESS: Updated global .stacked-bar CSS!")
else:
    print("WARNING: old_stacked_css not found exactly")

# 2. Update @media (max-width: 768px) block
start_marker = '@media (max-width: 768px) {'
end_marker = '/* ------------------------------------------------------------\n   16. PRINT OPTIMIZATION'

idx = code.find(start_marker)
end_idx = code.find(end_marker, idx)

if idx != -1 and end_idx != -1:
    print("Found 768px block in build_world_class_css.py")
    
    enhanced_768 = '''@media (max-width: 768px) {
  :root {
    --container-padding: 16px;
  }
  html, body {
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  body {
    padding-bottom: calc(92px + env(safe-area-inset-bottom, 16px)) !important; /* Generous clearance for mobile floating bar */
  }
  body.menu-open {
    overflow: hidden;
  }
  .container {
    padding-left: 16px !important;
    padding-right: 16px !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }
  .section {
    padding: 36px 0;
  }
  .section-header {
    margin-bottom: 18px;
    text-align: center;
  }
  .section-tag {
    font-size: 0.7rem;
    padding: 3px 9px;
  }
  .section-title {
    font-size: clamp(1.35rem, 5.2vw, 1.8rem);
    line-height: 1.22;
    margin: 6px 0 8px;
    letter-spacing: -0.01em;
    word-break: break-word;
    overflow-wrap: break-word;
  }
  .section-desc {
    font-size: 0.86rem;
    line-height: 1.5;
    color: #64748b;
  }

  /* Header & Navigation */
  .top-announcement {
    display: none;
  }
  .btn-header-cta {
    display: none;
  }
  .header-brand {
    gap: 8px;
  }
  .brand-logo-img {
    height: 36px;
  }
  .brand-main-title {
    font-size: 0.85rem;
    line-height: 1.2;
  }
  .brand-sub-title {
    font-size: 0.6rem;
    letter-spacing: 0.04em;
  }

  /* Mobile Floating Action Bar */
  .mobile-floating-bar {
    display: flex;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1020;
    background: rgba(7, 25, 54, 0.94);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-top: 1px solid rgba(247, 183, 49, 0.3);
    padding: 8px 12px;
    padding-bottom: calc(8px + env(safe-area-inset-bottom, 0px));
    gap: 8px;
    align-items: center;
    box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.4);
    transform: translateY(100%);
    transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .mobile-floating-bar.visible {
    transform: translateY(0);
  }
  .floating-btn-call,
  .floating-btn-agenda {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 2px;
    color: #e2e8f0;
    text-decoration: none;
    font-size: 0.66rem;
    font-weight: 700;
    padding: 6px 10px;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.1);
    min-width: 56px;
    cursor: pointer;
  }
  .floating-btn-ticket {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    background: linear-gradient(135deg, #d83a6f 0%, #e11d48 100%);
    color: #ffffff;
    text-decoration: none;
    font-size: 0.88rem;
    font-weight: 800;
    padding: 10px 16px;
    border-radius: 9999px;
    box-shadow: 0 4px 14px rgba(216, 58, 111, 0.4);
  }

  /* Hero Banner - Compact, High-Impact Editorial */
  .hero-banner {
    padding: 22px 0 26px !important;
    width: 100% !important;
    max-width: 100% !important;
    overflow: hidden !important;
  }
  .hero-widescreen-grid {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    max-width: 100% !important;
    gap: 16px !important;
  }
  .hero-main-col {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
  }
  .hero-badge-row {
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 6px !important;
    margin-bottom: 8px !important;
    width: 100% !important;
  }
  .hero-partner-badge,
  .hero-pill-badge {
    font-size: 0.68rem !important;
    padding: 5px 10px !important;
    max-width: 100% !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.35 !important;
    box-sizing: border-box !important;
  }
  .theme-label-small {
    font-size: 0.7rem !important;
    letter-spacing: 0.1em !important;
    margin-bottom: 2px !important;
  }
  .theme-title-grand {
    font-size: clamp(1.95rem, 8vw, 2.5rem) !important;
    line-height: 1.15 !important;
    margin: 4px 0 6px !important;
    word-break: break-word !important;
    overflow-wrap: break-word !important;
    max-width: 100% !important;
  }
  .hero-theme-sub-line {
    font-size: 0.88rem !important;
    line-height: 1.4 !important;
    margin: 4px 0 8px !important;
    color: #fde68a !important;
    word-break: break-word !important;
    overflow-wrap: break-word !important;
    max-width: 100% !important;
  }
  .theme-lotus-divider {
    display: none !important;
  }
  .hero-lead-desc {
    font-size: 0.88rem !important;
    line-height: 1.5 !important;
    color: #cbd5e1 !important;
    margin-bottom: 16px !important;
    word-break: break-word !important;
    overflow-wrap: break-word !important;
    max-width: 100% !important;
  }

  /* Compact 3-in-1 Meta Ribbon */
  .hero-meta-bar {
    display: flex !important;
    flex-direction: column !important;
    gap: 7px !important;
    margin-bottom: 16px !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  .hero-meta-item {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 9px 12px !important;
    background: rgba(11, 31, 66, 0.75) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 10px !important;
    font-size: 0.82rem !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }
  .hero-meta-item .meta-label {
    display: none !important;
  }
  .hero-meta-item .meta-val {
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    word-break: break-word !important;
    overflow-wrap: break-word !important;
  }

  /* Hero CTA Cluster - Vertically Stacked Full Width for Zero Truncation */
  .hero-cta-group {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    width: 100% !important;
    max-width: 100% !important;
    margin-bottom: 18px !important;
  }
  .hero-cta-group .btn-hero {
    width: 100% !important;
    max-width: 100% !important;
    justify-content: center !important;
    text-align: center !important;
    padding: 12px 16px !important;
    font-size: 0.86rem !important;
    font-weight: 700 !important;
    box-sizing: border-box !important;
    border-radius: 9999px !important;
  }
  .hero-cta-group .btn-hero-pink {
    padding: 14px 18px !important;
    font-size: 0.95rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #d83a6f 0%, #e11d48 100%) !important;
    box-shadow: 0 4px 16px rgba(216, 58, 111, 0.4) !important;
  }

  /* Right Showcase Master Card on Mobile */
  .hero-showcase-master-card {
    margin-top: 10px !important;
    border-radius: 14px !important;
    border: 1px solid rgba(247, 183, 49, 0.35) !important;
    background: rgba(7, 25, 54, 0.85) !important;
    backdrop-filter: blur(10px) !important;
    overflow: hidden !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }
  .showcase-countdown-header {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    gap: 4px !important;
    padding: 10px 12px !important;
    font-size: 0.76rem !important;
    text-align: center !important;
  }
  .countdown-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 4px !important;
    padding: 8px 8px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .countdown-box {
    padding: 6px 2px !important;
    border-radius: 6px !important;
    min-width: 0 !important;
  }
  .countdown-num {
    font-size: 1.25rem !important;
    font-weight: 900 !important;
  }
  .countdown-label {
    font-size: 0.6rem !important;
  }
  .stage-photo-img {
    height: 170px !important;
    width: 100% !important;
    object-fit: cover !important;
  }
  .stage-specs-grid {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 4px !important;
    padding: 8px 10px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .hero-audio-capsule {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    padding: 10px 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .hero-audio-capsule .btn-play-soundscape {
    width: 100% !important;
    justify-content: center !important;
  }

  /* 2x2 Hero Stats Micro-Dashboard */
  .hero-stats-ribbon {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 8px !important;
    margin-top: 14px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .hero-stat-card {
    padding: 12px 14px !important;
    border-radius: 10px !important;
    background: rgba(11, 31, 66, 0.75) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    text-align: center !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  /* All Horizontal Scrolling Touch Filter Bars - Strict flex-start to prevent left truncation */
  .timeline-filter-bar,
  .kpi-tabs-bar,
  .appendix-tabs-bar,
  .appendix-nav-pill-group,
  .agenda-controls {
    display: flex !important;
    justify-content: flex-start !important;
    align-items: center !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    width: 100% !important;
    max-width: 100% !important;
    padding-left: 2px !important;
    padding-right: 16px !important;
    padding-bottom: 8px !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    box-sizing: border-box !important;
    scrollbar-width: none !important;
    gap: 8px !important;
  }
  .agenda-controls button,
  .timeline-filter-bar button,
  .kpi-tabs-bar button,
  .appendix-tabs-bar button,
  .appendix-tab-btn,
  .kpi-tab-btn,
  .agenda-filter-btn {
    flex: 0 0 auto !important;
    white-space: nowrap !important;
    font-size: 0.82rem !important;
    padding: 8px 14px !important;
    box-sizing: border-box !important;
  }

  /* Section 1: 7 Pillars */
  .pillars-grid {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .pillar-card {
    display: grid;
    grid-template-columns: 34px 1fr;
    gap: 10px;
    align-items: center;
    padding: 10px 12px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
  }
  .pillar-num {
    width: 34px;
    height: 34px;
    font-size: 0.85rem;
  }
  .pillar-content h4 {
    font-size: 0.88rem;
    font-weight: 700;
    margin-bottom: 2px;
  }
  .pillar-content p {
    font-size: 0.78rem;
    line-height: 1.35;
    color: #475569;
  }

  /* Organic Wave Divider on Mobile */
  .section-wave-divider {
    height: 32px !important;
    margin-top: 24px !important;
    margin-bottom: -1px !important;
  }

  /* Section 2: Artists & Heritage */
  .section-artists {
    padding-bottom: 28px !important;
  }
  .artist-master-banner {
    border-radius: 14px !important;
    margin-bottom: 20px !important;
    overflow: hidden !important;
  }
  .artist-master-img {
    height: 220px !important;
    min-height: 220px !important;
    object-fit: cover !important;
    object-position: center 20% !important;
  }
  .master-banner-overlay {
    padding: 16px 14px 14px !important;
    background: linear-gradient(to top, rgba(5, 16, 36, 0.96) 0%, rgba(5, 16, 36, 0.72) 65%, transparent 100%) !important;
  }
  .master-badge {
    font-size: 0.65rem !important;
    padding: 3px 8px !important;
    margin-bottom: 4px !important;
  }
  .banner-main-name {
    font-size: 1.05rem !important;
    line-height: 1.3 !important;
  }
  .artist-three-grid {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .artist-card-hero {
    border-radius: 14px;
    overflow: hidden;
    background: #0b1f42;
    border: 1px solid rgba(247, 183, 49, 0.35);
  }
  .artist-card-hero .artist-hero-photo {
    height: 190px;
    object-fit: cover;
    object-position: 50% 12%;
  }
  .artist-three-grid .artist-card:not(.artist-card-hero) {
    display: grid;
    grid-template-columns: 70px 1fr;
    gap: 12px;
    align-items: center;
    padding: 10px 12px;
    border-radius: 12px;
  }
  .artist-three-grid .artist-card:not(.artist-card-hero) img {
    width: 70px;
    height: 70px;
    border-radius: 10px;
    object-fit: cover;
  }
  .artist-three-grid .artist-card:not(.artist-card-hero) h4 {
    font-size: 0.92rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 2px;
  }
  .artist-card-quote {
    font-size: 0.82rem !important;
    line-height: 1.5 !important;
    padding: 10px 12px !important;
    margin-bottom: 14px !important;
  }

  /* Section 3: Timeline & Agenda (Expanded Mobile Width) */
  .timeline-stream {
    padding-left: 28px !important;
    max-width: 100% !important;
  }
  .timeline-stream::before {
    left: 8px !important;
    top: 10px !important;
    bottom: 10px !important;
  }
  .timeline-point {
    left: -26px !important;
    top: 14px !important;
    width: 12px !important;
    height: 12px !important;
  }
  .timeline-node {
    margin-bottom: 18px !important;
  }
  .timeline-time-badge {
    position: static !important;
    width: auto !important;
    text-align: left !important;
    margin-bottom: 6px !important;
    display: inline-flex !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    color: var(--vhu-gold-primary) !important;
    background: rgba(212, 155, 25, 0.1) !important;
    padding: 2px 8px !important;
    border-radius: 6px !important;
    border: 1px solid rgba(212, 155, 25, 0.25) !important;
  }
  .timeline-card-header {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 6px !important;
  }
  .timeline-team-pill {
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.35 !important;
    display: inline-flex !important;
    max-width: 100% !important;
  }
  .timeline-card {
    padding: 14px 14px !important;
    border-radius: 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .timeline-card-title,
  .timeline-activity {
    font-size: 0.95rem !important;
    font-weight: 800 !important;
    margin-bottom: 3px !important;
  }
  .timeline-card-desc,
  .timeline-desc {
    font-size: 0.82rem !important;
    color: #475569 !important;
    line-height: 1.45 !important;
    margin-bottom: 6px !important;
  }

  /* Section 4: Media Phases */
  .media-phase-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .media-phase-card {
    padding: 14px 12px;
    border-radius: 10px;
  }

  /* Section 5: Budget & 68 Rows Table (Full-Width Master Cards & Clean Progress) */
  .finance-overview-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
    margin-bottom: 20px !important;
    width: 100% !important;
  }
  .finance-kpi-card {
    width: 100% !important;
    box-sizing: border-box !important;
    padding: 16px 18px !important;
    border-radius: 12px !important;
  }
  .card-finance-value {
    font-size: 1.65rem !important;
    white-space: nowrap !important;
    line-height: 1.25 !important;
    margin: 6px 0 8px !important;
  }
  .budget-visual-bar {
    padding: 16px 14px !important;
    border-radius: 12px !important;
    margin-bottom: 24px !important;
  }
  .budget-bar-title {
    font-size: 0.92rem !important;
    font-weight: 800 !important;
    line-height: 1.35 !important;
  }
  .budget-legend-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
  }
  .budget-legend-grid .legend-item {
    font-size: 0.82rem !important;
    line-height: 1.4 !important;
  }
  .sponsor-tiers-container {
    padding-bottom: 20px !important;
  }
  .sponsor-tier-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .sponsor-card {
    padding: 16px 14px;
    border-radius: 12px;
  }

  /* Section 6: Risks & 29 KPIs (2-Column Micro Tiles) */
  .kpi-items-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
  }
  .kpi-card {
    padding: 10px 10px;
    border-radius: 8px;
  }

  /* Section 7: Creative Identity & Key Visuals */
  .creative-master-grid {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .creative-card {
    border-radius: 12px;
  }

  /* Section 8: Legal Documentation & 5 Appendices */
  .doc-container {
    border-radius: 12px;
  }
  .doc-paper-sheet {
    padding: 16px 12px !important;
    font-size: 0.88rem !important;
    line-height: 1.6 !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    overflow-x: auto !important;
  }
  table.doc-table {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }

  /* Section 9: Registration & Ticket Simulator */
  .reg-contact-grid {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding-bottom: 24px !important;
  }
  .reg-form-card {
    padding: 16px 14px;
    border-radius: 12px;
  }
  .live-ticket-card {
    max-width: 330px;
    margin: 0 auto;
    border-radius: 12px;
  }
  .ticket-body-grid {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 14px 12px;
    align-items: center;
    text-align: center;
  }
  .ticket-footer-bar .btn-ticket-print {
    width: 100%;
    justify-content: center;
    height: 42px;
    font-size: 0.88rem;
  }
  .contact-info-card {
    padding: 16px 14px;
    border-radius: 12px;
  }

  /* Footer */
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  /* Universal Table and Scroll Wrapper Security */
  .table-scroll-wrapper {
    max-height: 440px;
    overflow-y: auto;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    border-radius: 10px;
    border: 1px solid var(--border-subtle);
    width: 100% !important;
    max-width: 100% !important;
    display: block !important;
  }
  .table-card-container {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    overflow: hidden !important;
  }
  .table-scroll-wrapper th {
    position: sticky;
    top: 0;
    background: #071936;
    color: #ffffff;
    z-index: 5;
  }
  .budget-table,
  .data-table {
    min-width: 580px;
    font-size: 0.8rem;
  }
  .budget-table td,
  .budget-table th,
  .data-table td,
  .data-table th {
    padding: 8px 10px;
  }
}

'''

    code = code[:idx] + enhanced_768 + code[end_idx:]
    with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("SUCCESS: Updated 768px media query with all 5 issue fixes!")
else:
    print(f"ERROR: Could not find media query markers (idx={idx}, end_idx={end_idx})")
