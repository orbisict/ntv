with open('index.html', encoding='utf-8') as f:
    html = f.read()

import re

print("Legend parent:", re.findall(r'<div class="([^"]*)"[^>]*>\s*<div class="legend-item"', html))
print("App tab buttons parent:", re.findall(r'<div class="([^"]*)"[^>]*>\s*<button class="app-tab-btn', html))
print("Budget table parent:", re.findall(r'<div class="([^"]*)"[^>]*>\s*<table class="budget-table', html))
