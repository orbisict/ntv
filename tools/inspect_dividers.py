with open('styles.css', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.[a-zA-Z0-9_\-]+divider[a-zA-Z0-9_\-]*|\.[a-zA-Z0-9_\-]+wave[a-zA-Z0-9_\-]*|\.[a-zA-Z0-9_\-]+transition[a-zA-Z0-9_\-]*)', css)
print("Divider/transition classes:", set(matches))
