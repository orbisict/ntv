import re

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Global Budget Group Header CSS
old_group_header_css = '''.budget-group-header-row td {
  background: #f1f5f9 !important;
  color: var(--vhu-navy-base);
  font-weight: 800;
  font-size: 0.92rem;
  padding: 12px 18px;
}

.budget-group-title {
  display: flex;
  align-items: center;
  gap: 6px;
}'''

new_group_header_css = '''.budget-group-header-cell {
  background: #edf2f7 !important;
  color: var(--vhu-navy-base);
  padding: 12px 18px !important;
  border-top: 2px solid #cbd5e1 !important;
  border-bottom: 1px solid #cbd5e1 !important;
}

.budget-group-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 800;
  color: #0b1f42;
  font-size: 0.92rem;
}

.budget-group-title .group-subtotal {
  color: #b45309;
  font-weight: 700;
  font-size: 0.85rem;
  margin-left: 6px;
}'''

if old_group_header_css in code:
    code = code.replace(old_group_header_css, new_group_header_css, 1)
    print("SUCCESS: Updated global budget group header CSS!")
else:
    print("WARNING: old_group_header_css not matched exactly")

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

  /* 1. ISSUE 1 FIX: 7 PILLARS (Clean Flex Layout with 0 Overlap) */
  .pillars-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 10px !important;
    width: 100% !important;
  }
  .pillar-card {
    display: flex !important;
    align-items: flex-start !important;
    gap: 14px !important;
    padding: 14px 16px !important;
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .pillar-number {
    width: 38px !important;
    height: 38px !important;
    min-width: 38px !important;
    max-width: 38px !important;
    flex-shrink: 0 !important;
    font-size: 0.95rem !important;
    font-weight: 800 !important;
    margin-top: 2px !important;
    border-radius: 50% !important;
    background: var(--vhu-blue-soft) !important;
    color: var(--vhu-navy-light) !important;
    border: 1.5px solid var(--vhu-blue-border) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }
  .pillar-card-wide .pillar-number {
    background: var(--vhu-gold-soft) !important;
    color: var(--vhu-gold-primary) !important;
    border-color: var(--vhu-gold-border) !important;
  }
  .pillar-content {
    flex: 1 !important;
    min-width: 0 !important;
  }
  .pillar-title {
    font-size: 0.94rem !important;
    font-weight: 800 !important;
    line-height: 1.35 !important;
    margin-bottom: 4px !important;
    color: var(--vhu-navy-base) !important;
  }
  .pillar-desc {
    font-size: 0.8rem !important;
    line-height: 1.45 !important;
    color: #475569 !important;
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

  /* 2. ISSUE 2 FIX: AGENDA CONTROLS & TIMELINE (Zero Bloating & Natural Card Flow) */
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
  .agenda-filter-btn {
    flex: 0 0 auto !important;
    white-space: nowrap !important;
    font-size: 0.82rem !important;
    padding: 8px 14px !important;
    box-sizing: border-box !important;
  }
  .timeline-stream {
    padding-left: 24px !important;
    position: relative !important;
    max-width: 100% !important;
  }
  .timeline-stream::before {
    left: 6px !important;
    top: 10px !important;
    bottom: 10px !important;
    width: 2px !important;
  }
  .timeline-node {
    position: relative !important;
    margin-bottom: 20px !important;
    display: block !important;
    width: 100% !important;
  }
  .timeline-point {
    position: absolute !important;
    left: -24px !important;
    top: 10px !important;
    width: 12px !important;
    height: 12px !important;
  }
  .timeline-time-badge {
    position: static !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 5px !important;
    font-size: 0.78rem !important;
    font-weight: 800 !important;
    color: #92400e !important;
    background: #fef3c7 !important;
    border: 1px solid #fde68a !important;
    padding: 3px 10px !important;
    border-radius: 9999px !important;
    margin-bottom: 8px !important;
    width: auto !important;
    text-align: left !important;
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
    padding: 14px 16px !important;
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

  /* 3. ISSUE 3 FIX: FINANCE OVERVIEW & EXPENDITURE BREAKDOWN ROWS */
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
    width: 100% !important;
  }
  .legend-item {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    gap: 8px !important;
    padding: 8px 12px !important;
    background: #f8fafc !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 8px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .legend-item-title {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    color: var(--vhu-navy-base) !important;
    min-width: 0 !important;
    flex: 1 !important;
  }
  .legend-item-val {
    white-space: nowrap !important;
    font-size: 0.82rem !important;
    flex-shrink: 0 !important;
    text-align: right !important;
  }
  .legend-item-val .val-money {
    font-weight: 800 !important;
    color: #0b1f42 !important;
  }
  .legend-item-val .val-pct {
    font-size: 0.76rem !important;
    color: #64748b !important;
    margin-left: 2px !important;
  }

  /* 4. ISSUE 4 FIX: 68-ROW BUDGET TABLE MOBILE REFINEMENT */
  .table-card-container {
    border-radius: 14px !important;
    border: 1px solid #e2e8f0 !important;
    overflow: hidden !important;
    background: #ffffff !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05) !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  .table-scroll-wrapper {
    max-height: 480px !important;
    overflow-y: auto !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    border-radius: 0 !important;
    border: none !important;
    width: 100% !important;
    display: block !important;
  }
  .mobile-scroll-hint {
    background: #f1f5f9 !important;
    color: #475569 !important;
    font-size: 0.74rem !important;
    font-weight: 600 !important;
    padding: 8px 12px !important;
    border-bottom: 1px solid #e2e8f0 !important;
  }
  .budget-table,
  .data-table {
    min-width: 660px !important;
    font-size: 0.8rem !important;
    border-collapse: collapse !important;
  }
  .data-table th {
    background: #071936 !important;
    color: #ffffff !important;
    padding: 10px 12px !important;
    font-size: 0.76rem !important;
    white-space: nowrap !important;
    position: sticky !important;
    top: 0 !important;
    z-index: 5 !important;
  }
  .data-table td {
    padding: 10px 12px !important;
    font-size: 0.8rem !important;
    line-height: 1.4 !important;
    border-bottom: 1px solid #edf2f7 !important;
  }
  .budget-group-header-cell {
    background: #edf2f7 !important;
    padding: 10px 14px !important;
    border-top: 2px solid #cbd5e1 !important;
    border-bottom: 1px solid #cbd5e1 !important;
  }
  .budget-group-title {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    font-weight: 800 !important;
    color: #0b1f42 !important;
    font-size: 0.88rem !important;
  }
  .budget-group-title .group-subtotal {
    color: #b45309 !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    margin-left: 4px !important;
  }

  /* Section 6: Risks & 29 KPIs (2-Column Micro Tiles) */
  .kpi-tabs-bar,
  .timeline-filter-bar {
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
    scrollbar-width: none !important;
    gap: 8px !important;
  }
  .kpi-tabs-bar button,
  .timeline-filter-bar button {
    flex: 0 0 auto !important;
    white-space: nowrap !important;
    font-size: 0.82rem !important;
    padding: 8px 14px !important;
  }
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

  /* 5. ISSUE 5 FIX: APPENDIX TABS (Horizontal Swipeable Pills, Zero Vertical Eggs) */
  .appendix-nav-pill-group {
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
    padding-bottom: 10px !important;
    margin-bottom: 18px !important;
    scrollbar-width: none !important;
    gap: 8px !important;
  }
  .appendix-nav-pill-group::-webkit-scrollbar {
    display: none !important;
  }
  .app-tab-btn {
    flex: 0 0 auto !important;
    white-space: nowrap !important;
    padding: 9px 18px !important;
    border-radius: 9999px !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    border: 1px solid #cbd5e1 !important;
    background: #ffffff !important;
    color: #334155 !important;
    height: auto !important;
    line-height: 1.3 !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    transition: all 0.2s ease !important;
  }
  .app-tab-btn.active {
    background: #0b1f42 !important;
    color: #ffffff !important;
    border-color: #0b1f42 !important;
    box-shadow: 0 4px 12px rgba(11, 31, 66, 0.25) !important;
  }
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

  /* 6. ISSUE 6 FIX: VIP TICKET BOARDING PASS REFINEMENT */
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
    background: linear-gradient(135deg, #071936 0%, #0d2650 50%, #071936 100%) !important;
    border: 1.5px solid rgba(247, 183, 49, 0.6) !important;
    border-radius: 16px !important;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35) !important;
    max-width: 340px !important;
    width: 100% !important;
    margin: 0 auto !important;
    overflow: hidden !important;
  }
  .ticket-holo-header {
    padding: 12px 16px !important;
    background: rgba(0, 0, 0, 0.35) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 10px !important;
  }
  .ticket-header-left {
    flex: 1 !important;
    min-width: 0 !important;
  }
  .ticket-org-tag {
    font-size: 0.62rem !important;
    color: #fcd34d !important;
    letter-spacing: 0.06em !important;
  }
  .ticket-event-name {
    font-size: 0.88rem !important;
    font-weight: 800 !important;
    line-height: 1.25 !important;
    color: #ffffff !important;
  }
  .ticket-logo-badge {
    height: 34px !important;
    width: 34px !important;
    flex-shrink: 0 !important;
  }
  .ticket-body-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 14px !important;
    padding: 16px 16px !important;
    align-items: center !important;
    text-align: left !important;
  }
  .ticket-qr-block {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    background: #ffffff !important;
    padding: 8px 12px !important;
    border-radius: 10px !important;
    border: 1.5px solid #d49b19 !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25) !important;
  }
  .ticket-qr-img {
    width: 100px !important;
    height: 100px !important;
  }
  .ticket-code-tag {
    font-size: 0.68rem !important;
    font-weight: 900 !important;
    color: #0b1f42 !important;
    margin-top: 4px !important;
    letter-spacing: 0.05em !important;
  }
  .ticket-details-block {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 6px !important;
  }
  .ticket-info-line {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    padding: 6px 0 !important;
    border-bottom: 1px dashed rgba(255, 255, 255, 0.12) !important;
    font-size: 0.8rem !important;
    gap: 10px !important;
  }
  .ticket-info-line .info-label {
    color: #94a3b8 !important;
    font-size: 0.74rem !important;
    flex-shrink: 0 !important;
  }
  .ticket-info-line .info-val {
    color: #f1f5f9 !important;
    font-weight: 700 !important;
    text-align: right !important;
    word-break: break-word !important;
  }
  .ticket-info-line .info-val.highlight-gold {
    color: #fcd34d !important;
    font-weight: 800 !important;
  }
  .ticket-footer-bar {
    padding: 10px 16px !important;
    background: rgba(0, 0, 0, 0.4) !important;
    border-top: 1px dashed rgba(255, 255, 255, 0.16) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
  }
  .ticket-footer-bar .btn-ticket-print {
    padding: 8px 14px !important;
    font-size: 0.8rem !important;
    height: auto !important;
    width: auto !important;
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
}

'''

    code = code[:idx] + enhanced_768 + code[end_idx:]
    with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("SUCCESS: Replaced 768px block in build_world_class_css.py with all 6 fixes!")
else:
    print(f"ERROR: Could not find media query markers (idx={idx}, end_idx={end_idx})")
