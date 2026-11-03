import re

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css_py = f.read()

# 1. Update Drawer CSS in build_world_class_css.py
old_drawer_css = '''/* Modern App-grade Mobile Navigation Drawer & Backdrop */
.mobile-nav-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(5, 16, 36, 0.75);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 1040;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.mobile-nav-backdrop.active {
  opacity: 1;
  pointer-events: auto;
}

.mobile-nav-drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: min(88vw, 360px);
  background: linear-gradient(180deg, #071936 0%, #051024 100%);
  border-left: 1px solid rgba(247, 183, 49, 0.3);
  box-shadow: -10px 0 36px rgba(0, 0, 0, 0.6);
  z-index: 1050;
  display: flex;
  flex-direction: column;
  transform: translateX(100%);
  transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1);
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: 24px 20px 32px;
}

.mobile-nav-drawer.open {
  transform: translateX(0);
}

.mobile-drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 18px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 16px;
}

.mobile-drawer-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.mobile-drawer-logo {
  height: 38px;
  width: auto;
  border-radius: 50%;
  background: #ffffff;
  padding: 2px;
}

.mobile-drawer-close {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #ffffff;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.mobile-drawer-close:hover {
  background: rgba(216, 58, 111, 0.3);
  color: #ff94b2;
}

.mobile-drawer-links {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.mobile-drawer-links .nav-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 14px;
  border-radius: 10px;
  font-size: 0.95rem;
  font-weight: 600;
  color: #e2e8f0;
  text-decoration: none;
  transition: all 0.2s ease;
  border-bottom: none;
}

.mobile-drawer-links .nav-link:hover,
.mobile-drawer-links .nav-link.active {
  background: rgba(212, 155, 25, 0.15);
  color: var(--vhu-gold-light);
}

.mobile-drawer-footer {
  margin-top: 20px;
  padding-top: 18px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.mobile-drawer-cta {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: linear-gradient(135deg, #d83a6f 0%, #e11d48 100%);
  color: #ffffff;
  padding: 13px 20px;
  border-radius: 9999px;
  font-weight: 800;
  font-size: 0.92rem;
  text-decoration: none;
  box-shadow: 0 4px 14px rgba(216, 58, 111, 0.4);
}

.mobile-drawer-hotline {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #fcd34d;
  padding: 10px 16px;
  border-radius: 9999px;
  font-size: 0.85rem;
  font-weight: 700;
  text-decoration: none;
}'''

new_drawer_css = '''/* Modern App-grade Mobile Navigation Drawer & Backdrop */
.mobile-nav-backdrop {
  position: fixed !important;
  inset: 0 !important;
  background: rgba(5, 16, 36, 0.82) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  z-index: 99998 !important;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.3s !important;
}

.mobile-nav-backdrop.active {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}

.mobile-nav-drawer {
  position: fixed !important;
  top: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: min(85vw, 340px) !important;
  background: #071936 !important;
  background: linear-gradient(180deg, #071936 0%, #051024 100%) !important;
  border-left: 1px solid rgba(247, 183, 49, 0.35) !important;
  box-shadow: -12px 0 40px rgba(0, 0, 0, 0.75) !important;
  z-index: 99999 !important;
  display: flex !important;
  flex-direction: column !important;
  transform: translateX(100%) !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.32s !important;
  overflow-y: auto !important;
  -webkit-overflow-scrolling: touch !important;
  padding: 22px 18px 28px !important;
  box-sizing: border-box !important;
}

.mobile-nav-drawer.open {
  transform: translateX(0) !important;
  visibility: visible !important;
  pointer-events: auto !important;
}

.mobile-drawer-header {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding-bottom: 16px !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12) !important;
  margin-bottom: 14px !important;
  background: transparent !important;
}

.mobile-drawer-brand {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  background: transparent !important;
}

.mobile-drawer-logo {
  height: 38px !important;
  width: 38px !important;
  border-radius: 50% !important;
  background: #ffffff !important;
  padding: 2px !important;
  flex-shrink: 0 !important;
}

.mobile-drawer-close {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  color: #ffffff !important;
  width: 36px !important;
  height: 36px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  flex-shrink: 0 !important;
  transition: all 0.2s ease !important;
}

.mobile-drawer-close:hover {
  background: rgba(216, 58, 111, 0.4) !important;
  color: #ff94b2 !important;
}

.mobile-drawer-links {
  display: flex !important;
  flex-direction: column !important;
  gap: 6px !important;
  flex: 1 !important;
  background: transparent !important;
}

.mobile-drawer-links .nav-link {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 12px 14px !important;
  border-radius: 10px !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #f1f5f9 !important;
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.06) !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}

.mobile-drawer-links .nav-link:hover,
.mobile-drawer-links .nav-link.active {
  background: rgba(212, 155, 25, 0.2) !important;
  border-color: rgba(247, 183, 49, 0.4) !important;
  color: #fcd34d !important;
}

.mobile-drawer-footer {
  margin-top: 18px !important;
  padding-top: 16px !important;
  border-top: 1px solid rgba(255, 255, 255, 0.12) !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
  background: transparent !important;
}

.mobile-drawer-cta {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  background: linear-gradient(135deg, #d83a6f 0%, #e11d48 100%) !important;
  color: #ffffff !important;
  padding: 12px 18px !important;
  border-radius: 9999px !important;
  font-weight: 800 !important;
  font-size: 0.9rem !important;
  text-decoration: none !important;
  box-shadow: 0 4px 14px rgba(216, 58, 111, 0.4) !important;
}

.mobile-drawer-hotline {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  color: #fcd34d !important;
  padding: 10px 16px !important;
  border-radius: 9999px !important;
  font-size: 0.85rem !important;
  font-weight: 700 !important;
  text-decoration: none !important;
}'''

if old_drawer_css in css_py:
    css_py = css_py.replace(old_drawer_css, new_drawer_css, 1)
    print("SUCCESS: Replaced drawer CSS in build_world_class_css.py!")
else:
    print("ERROR: old_drawer_css not matched in build_world_class_css.py!")

with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
    f.write(css_py)
