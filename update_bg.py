import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<section id="infraestructura" class="py-32 bg-[#111] text-white">',
    '<section id="infraestructura" class="py-32 bg-[#304269] text-white">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated background.")
