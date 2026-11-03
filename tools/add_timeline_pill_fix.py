with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '  .timeline-card {'
replacement = '''  .timeline-card-header {
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
  .timeline-card {'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Added timeline-team-pill wrapping rule!")
else:
    print("ERROR: target not found")
