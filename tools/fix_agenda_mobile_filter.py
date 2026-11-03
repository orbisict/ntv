import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update tools/build_world_class_css.py
with open('tools/build_world_class_css.py', 'r', encoding='utf-8') as f:
    css = f.read()

old_hide = """.timeline-node.hide {
  display: none;
}"""

new_hide = """.timeline-node.hide,
.timeline-node.node-hidden {
  display: none !important;
}"""

assert old_hide in css, "old_hide not found in build_world_class_css.py"
css = css.replace(old_hide, new_hide, 1)

old_768_node = """.timeline-node {
    position: relative !important;
    margin-bottom: 20px !important;
    display: block !important;
    width: 100% !important;
  }"""

new_768_node = """.timeline-node {
    position: relative !important;
    margin-bottom: 20px !important;
    display: block;
    width: 100% !important;
  }
  .timeline-node.hide,
  .timeline-node.node-hidden {
    display: none !important;
  }"""

assert old_768_node in css, "old_768_node not found in build_world_class_css.py"
css = css.replace(old_768_node, new_768_node, 1)

with open('tools/build_world_class_css.py', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Updated build_world_class_css.py!")

# 2. Update tools/build_clean_script_js.py
with open('tools/build_clean_script_js.py', 'r', encoding='utf-8') as f:
    js = f.read()

old_agenda_fn = """function initAgendaFilters() {
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
        const types = typeStr.split(/\\\\s+/);

        if (filter === 'all' || types.includes(filter)) {
          node.style.display = '';
        } else {
          node.style.display = 'none';
        }
      });
    });
  });
}"""

new_agenda_fn = """function initAgendaFilters() {
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
        const types = typeStr.split(/\\\\s+/);

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
}"""

assert old_agenda_fn in js, "old_agenda_fn not found in build_clean_script_js.py"
js = js.replace(old_agenda_fn, new_agenda_fn, 1)

with open('tools/build_clean_script_js.py', 'w', encoding='utf-8') as f:
    f.write(js)

print("SUCCESS: Updated build_clean_script_js.py!")
