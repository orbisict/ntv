import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print("Sections found:", sections)

# Check images used
images = re.findall(r'<img[^>]*src=["\']([^"\']+)["\']', text)
print(f"Total img tags: {len(images)}")
print("Unique images:", set(images))

# Look at overall structure size
print("Total HTML length:", len(text))
