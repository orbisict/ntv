import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css_code = f.read()

# Fix hero-banner and hero-bottom-curve
target_hero = """.hero-banner {
  position: relative;
  background-color: #051024;
  background-image: 
    radial-gradient(circle at 75% 25%, rgba(13, 37, 82, 0.7) 0%, rgba(5, 16, 36, 0.94) 65%, #051024 100%),
    url('./assets/images/nen-chinh.png');
  background-size: cover;
  background-position: center top;
  background-repeat: no-repeat;
  color: #ffffff;
  padding: 60px 0 64px;
  overflow: hidden;
}"""

replacement_hero = """.hero-banner {
  position: relative;
  background-color: #051024;
  background-image: 
    radial-gradient(circle at 75% 25%, rgba(13, 37, 82, 0.7) 0%, rgba(5, 16, 36, 0.94) 65%, #051024 100%),
    url('./assets/images/nen-chinh.png');
  background-size: cover;
  background-position: center top;
  background-repeat: no-repeat;
  color: #ffffff;
  padding: 60px 0 0 !important;
  overflow: hidden;
}"""

if target_hero in css_code:
    css_code = css_code.replace(target_hero, replacement_hero, 1)
    print("Updated hero-banner padding")

target_curve = """.hero-bottom-curve {
  position: relative;
  width: 100%;
  overflow: hidden;
  line-height: 0;
  transform: translateY(1px);
}"""

replacement_curve = """.hero-bottom-curve {
  position: relative;
  width: 100%;
  overflow: hidden;
  line-height: 0;
  margin-top: 48px;
  margin-bottom: -1px;
  z-index: 3;
  pointer-events: none;
}"""

if target_curve in css_code:
    css_code = css_code.replace(target_curve, replacement_curve, 1)
    print("Updated hero-bottom-curve margins")

# Also remove any conflicting .hero-banner { padding-bottom: 72px; }
css_code = css_code.replace(".hero-banner {\n  padding-bottom: 72px;\n}", "")

with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
    f.write(css_code)

print("SUCCESS: Updated build_world_class_css.py!")
