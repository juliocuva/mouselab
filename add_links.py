import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Card 1 (bemap.pro)
content = re.sub(
    r'(<!-- Card 1 -->\s*)<div class="group cursor-pointer',
    r'\1<a href="https://www.bemap.pro/" target="_blank" rel="noopener noreferrer" class="group cursor-pointer block',
    content, count=1
)
# The first closing div before Card 3 is for Card 1
content = re.sub(
    r'(</p>\s*)</div>(\s*<!-- Card 3 -->)',
    r'\1</a>\2',
    content, count=1
)


# Replace Card 3 (AxisONE Coffee)
content = re.sub(
    r'(<!-- Card 3 -->\s*)<div class="group cursor-pointer',
    r'\1<a href="https://axisonecoffee.com/" target="_blank" rel="noopener noreferrer" class="group cursor-pointer block',
    content, count=1
)
# The closing div before Right Column is for Card 3
content = re.sub(
    r'(</p>\s*)</div>(\s*</div>\s*<!-- Columna Derecha -->)',
    r'\1</a>\2',
    content, count=1
)


# Replace Card 2 (Becoffee.pro)
content = re.sub(
    r'(<!-- Card 2 -->\s*)<div class="group cursor-pointer',
    r'\1<a href="https://becoffee.pro/" target="_blank" rel="noopener noreferrer" class="group cursor-pointer block',
    content, count=1
)
# The closing div before Card 4 is for Card 2
content = re.sub(
    r'(</p>\s*)</div>(\s*<!-- Card 4 -->)',
    r'\1</a>\2',
    content, count=1
)

# Card 4 doesn't have a link provided (Custom Web Dev). We'll leave it as a div for now or give it a # link.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated cards to be clickable links.")
