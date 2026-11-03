import re

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "/* === 4. MOBILE LANDSCAPE & STANDARD PHONES (<= 768px) === */"
end_marker = "/* === 5. COMPACT MOBILE & SMALL SMARTPHONES (<= 420px) === */"

idx1 = content.find(start_marker)
idx2 = content.find(end_marker, idx1)

if idx1 == -1 or idx2 == -1:
    print("Markers not found", idx1, idx2)
    exit(1)

new_block = '''/* === 4. MOBILE LANDSCAPE & PHONES (<= 768px) - WORLD-CLASS MOBILE APP EXPERIENCE === */
@media (max-width: 768px) {
  :root {
    --container-padding: 14px;
  }
  body {
    padding-bottom: 74px; /* Space for mobile floating bar */
  }
  body.menu-open {
    overflow: hidden;
  }
  .section {
    padding: 38px 0;
  }
  .section-header {
    margin-bottom: 20px;
    text-align: center;
  }
  .section-tag {
    font-size: 0.7rem;
    padding: 3px 9px;
  }
  .section-title {
    font-size: clamp(1.4rem, 5.2vw, 1.85rem);
    line-height: 1.22;
    margin: 6px 0 8px;
    letter-spacing: -0.01em;
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
    padding: 24px 0 28px;
  }
  .hero-badge-row {
    gap: 6px;
    margin-bottom: 8px;
  }
  .hero-partner-badge,
  .hero-pill-badge {
    font-size: 0.68rem;
    padding: 4px 8px;
  }
  .theme-label-small {
    font-size: 0.7rem;
    letter-spacing: 0.12em;
  }
  .theme-title-grand {
    font-size: clamp(2rem, 7.5vw, 2.5rem);
    line-height: 1.12;
    margin: 4px 0 6px;
  }
  .hero-theme-sub-line {
    font-size: 0.88rem;
    line-height: 1.35;
    margin: 4px 0 8px;
    color: #fde68a;
  }
  .theme-lotus-divider {
    display: none;
  }
  .hero-lead-desc {
    font-size: 0.88rem;
    line-height: 1.5;
    color: #cbd5e1;
    margin-bottom: 16px;
  }

  /* Compact 3-in-1 Meta Ribbon */
  .hero-meta-bar {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 16px;
    width: 100%;
  }
  .hero-meta-item {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: rgba(11, 31, 66, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    font-size: 0.82rem;
  }
  .hero-meta-item .meta-label {
    display: none;
  }
  .hero-meta-item .meta-val {
    font-size: 0.82rem;
    font-weight: 700;
  }

  /* Hero CTA Cluster */
  .hero-cta-group {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    width: 100%;
    margin-bottom: 18px;
  }
  .hero-cta-group .btn-hero-pink {
    grid-column: span 2;
    justify-content: center;
    padding: 13px 18px;
    font-size: 0.95rem;
    font-weight: 800;
    background: linear-gradient(135deg, #d83a6f 0%, #e11d48 100%);
    box-shadow: 0 4px 16px rgba(216, 58, 111, 0.4);
  }
  .hero-cta-group .btn-hero {
    justify-content: center;
    padding: 10px 8px;
    font-size: 0.78rem;
    font-weight: 700;
    text-align: center;
  }
  .hero-cta-group .btn-hero:last-child {
    grid-column: span 2;
  }

  /* Right Showcase Master Card on Mobile */
  .hero-showcase-master-card {
    margin-top: 10px;
    border-radius: 14px;
    border: 1px solid rgba(247, 183, 49, 0.3);
    background: rgba(7, 25, 54, 0.75);
    backdrop-filter: blur(10px);
    overflow: hidden;
  }
  .showcase-countdown-header {
    padding: 10px 12px;
    font-size: 0.76rem;
  }
  .countdown-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 4px;
    padding: 8px 10px;
  }
  .countdown-box {
    padding: 6px 2px;
    border-radius: 6px;
  }
  .countdown-num {
    font-size: 1.35rem;
    font-weight: 900;
  }
  .countdown-label {
    font-size: 0.6rem;
  }
  .stage-photo-img {
    height: 170px;
    object-fit: cover;
  }
  .stage-specs-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 4px;
    padding: 8px 10px;
  }
  .spec-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 6px 10px;
    background: rgba(255, 255, 255, 0.04);
    border-radius: 6px;
    font-size: 0.76rem;
  }
  .spec-label {
    font-size: 0.72rem;
  }
  .spec-val {
    font-size: 0.8rem;
    font-weight: 700;
  }
  .hero-audio-capsule {
    padding: 8px 12px;
    gap: 8px;
  }
  .audio-capsule-title {
    font-size: 0.78rem;
    max-width: 170px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* 2x2 Hero Stats Micro-Dashboard */
  .hero-stats-ribbon {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 6px;
    margin-top: 14px;
  }
  .hero-stat-card {
    padding: 10px 8px;
    border-radius: 10px;
    background: rgba(11, 31, 66, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.08);
    text-align: center;
  }
  .stat-icon-wrapper {
    display: none;
  }
  .stat-value {
    font-size: 1.25rem;
    font-weight: 900;
    color: #fcd34d;
    margin-bottom: 2px;
  }
  .stat-label {
    font-size: 0.68rem;
    color: #cbd5e1;
    line-height: 1.25;
  }

  /* Native App-grade Horizontal Swipable Filter Bars */
  .timeline-filter-bar,
  .kpi-tabs-bar,
  .appendix-tabs-bar {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
    gap: 6px !important;
    padding: 4px 2px 10px !important;
    margin-bottom: 16px !important;
    scrollbar-width: none;
    -ms-overflow-style: none;
  }
  .timeline-filter-bar::-webkit-scrollbar,
  .kpi-tabs-bar::-webkit-scrollbar,
  .appendix-tabs-bar::-webkit-scrollbar {
    display: none;
  }
  .timeline-filter-bar button,
  .kpi-tabs-bar button,
  .appendix-tabs-bar button,
  .appendix-tab-btn,
  .kpi-tab-btn,
  .agenda-filter-btn {
    flex: 0 0 auto !important;
    white-space: nowrap !important;
    font-size: 0.78rem !important;
    padding: 7px 12px !important;
    border-radius: 9999px !important;
  }

  /* Section 1: 7 Pillars (Compact Cultural List) */
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
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  }
  .pillar-num {
    width: 32px;
    height: 32px;
    font-size: 0.85rem;
    font-weight: 900;
    background: #fef3c7;
    color: #92400e;
    border: 1px solid #fde68a;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .pillar-title {
    font-size: 0.9rem;
    font-weight: 800;
    color: #0b1f42;
    line-height: 1.35;
    margin-bottom: 2px;
  }
  .pillar-desc {
    font-size: 0.78rem;
    color: #64748b;
    line-height: 1.4;
  }

  /* Section 2: Artists & Heritage */
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
    background: #071936;
    border: 1px solid rgba(255, 255, 255, 0.1);
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

  /* Section 3: Timeline */
  .timeline-stream {
    padding-left: 24px;
    position: relative;
  }
  .timeline-stream::before {
    left: 6px;
    width: 2px;
  }
  .timeline-point {
    left: -22px;
    top: 16px;
    width: 12px;
    height: 12px;
  }
  .timeline-node {
    margin-bottom: 14px;
  }
  .timeline-time-badge {
    position: static;
    text-align: left;
    margin-bottom: 6px;
  }
  .timeline-time-badge .time-text {
    display: inline-flex;
    background: #e0f2fe;
    color: #0369a1;
    padding: 2px 7px;
    border-radius: 5px;
    font-size: 0.75rem;
    font-weight: 800;
  }
  .timeline-card {
    padding: 12px 14px;
    border-radius: 10px;
  }
  .timeline-card-title {
    font-size: 0.95rem;
    font-weight: 800;
    margin-bottom: 3px;
  }
  .timeline-card-desc {
    font-size: 0.8rem;
    color: #475569;
    line-height: 1.4;
    margin-bottom: 6px;
  }
  .timeline-tag {
    font-size: 0.7rem;
    padding: 2px 6px;
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

  /* Section 5: Budget & 68 Rows Table (Bounded Touch Scroll) */
  .finance-overview-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
    margin-bottom: 16px;
  }
  .finance-stat-card {
    padding: 10px 10px;
    border-radius: 10px;
  }
  .finance-val {
    font-size: 1.25rem;
    font-weight: 900;
  }
  .finance-label {
    font-size: 0.7rem;
  }
  .budget-toolbar {
    flex-direction: column !important;
    gap: 8px !important;
    width: 100% !important;
  }
  .budget-toolbar .select-filter,
  .budget-toolbar .search-input-box {
    width: 100% !important;
    max-width: 100% !important;
    height: 42px !important;
    font-size: 0.85rem !important;
    border-radius: 8px !important;
  }
  .table-scroll-wrapper {
    max-height: 440px;
    overflow-y: auto;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    border-radius: 10px;
    border: 1px solid var(--border-subtle);
  }
  .table-scroll-wrapper th {
    position: sticky;
    top: 0;
    background: #071936;
    color: #ffffff;
    z-index: 5;
  }
  .mobile-scroll-hint {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.74rem;
    color: #64748b;
    padding: 7px 10px;
    background: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
  }
  .budget-table,
  .data-table {
    min-width: 620px;
    font-size: 0.8rem;
  }
  .budget-table td,
  .budget-table th,
  .data-table td,
  .data-table th {
    padding: 8px 10px;
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
  .kpi-metric-badge {
    font-size: 1.15rem;
    font-weight: 900;
  }
  .kpi-label {
    font-size: 0.7rem;
    line-height: 1.25;
  }

  /* Section 8: Official Documents */
  .doc-paper-wrapper {
    padding: 16px 12px;
    border-radius: 8px;
    overflow-x: auto;
  }
  .doc-admin-header {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 10px;
  }
  .doc-title-main {
    font-size: 1.15rem;
    margin: 12px 0 4px;
  }
  .doc-paragraph {
    text-indent: 0;
    font-size: 0.88rem;
    line-height: 1.55;
  }
  .doc-actions-bar {
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 6px;
    margin-bottom: 12px;
  }
  .doc-actions-bar button {
    width: 100%;
    justify-content: center;
    height: 40px;
    font-size: 0.82rem;
  }
  .doc-content-area table {
    display: table;
    width: 100%;
    min-width: 540px;
    font-size: 0.78rem;
  }

  /* Section 9: Registration & Ticket Simulator */
  .reg-contact-grid {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .reg-form-card {
    padding: 16px 14px;
    border-radius: 12px;
  }
  .form-row-2 {
    grid-template-columns: 1fr;
    gap: 10px;
  }
  .form-group input,
  .form-group select,
  .form-group textarea {
    font-size: 16px !important;
    height: 44px;
    border-radius: 8px;
  }
  .live-ticket-card {
    max-width: 330px;
    margin: 0 auto;
    border-radius: 12px;
  }
  .ticket-holo-header {
    padding: 12px 14px;
    flex-wrap: wrap;
    gap: 6px;
  }
  .ticket-event-name {
    font-size: 0.95rem;
  }
  .ticket-body-grid {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 14px 12px;
    align-items: center;
    text-align: center;
  }
  .ticket-qr-block {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .ticket-qr-img {
    width: 105px;
    height: 105px;
  }
  .ticket-details-block {
    width: 100%;
    text-align: left;
  }
  .ticket-info-line {
    padding-bottom: 4px;
    font-size: 0.8rem;
  }
  .ticket-footer-bar {
    flex-direction: column;
    gap: 8px;
    align-items: stretch;
    padding: 10px 12px;
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
  .footer-bottom {
    flex-direction: column;
    gap: 6px;
    text-align: center;
    font-size: 0.75rem;
  }
}

'''

content = content[:idx1] + new_block + content[idx2:]
with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated tools/build_world_class_css.py successfully!")
