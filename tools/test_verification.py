import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
html = open('index.html', encoding='utf-8').read()

print("--- 1. Testing Tabs ---")
tab_targets = re.findall(r'data-tab-target="([^"]+)"', html)
for t in set(tab_targets):
    assert f'id="{t}"' in html, f"Missing tab target: {t}"
print(f"Verified {len(tab_targets)} tab buttons. Targets: {sorted(list(set(tab_targets)))}")

print("\n--- 2. Testing Appendix Tabs ---")
app_targets = re.findall(r'data-app-target="([^"]+)"', html)
for t in set(app_targets):
    assert f'id="{t}"' in html, f"Missing app target: {t}"
print(f"Verified {len(app_targets)} appendix tab buttons. Targets: {sorted(list(set(app_targets)))}")

print("\n--- 3. Testing Budget Codes & Select Options ---")
select_opts = set(re.findall(r'<option value="([^"]+)"', html))
budget_codes = set(re.findall(r'data-group-code="([^"]+)"', html))
print(f"Budget codes in table: {sorted(list(budget_codes))}")
for b in budget_codes:
    assert b in select_opts, f"Missing select option for budget code: {b}"
print("All 9 budget codes match select dropdown options!")

print("\n--- 4. Testing Agenda Timeline Phases ---")
nodes = re.findall(r'data-type="([^"]+)"', html)
for p in ['phase-1', 'phase-2', 'phase-3']:
    count = sum(1 for n in nodes if p in n)
    print(f" - {p}: {count} items")
print(f"Total timeline nodes: {len(nodes)} (Target: 11)")
assert len(nodes) == 11, f"Expected 11 items, got {len(nodes)}"

print("\nALL VERIFICATION CHECKS PASSED PERFECTLY!")
