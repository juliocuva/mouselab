import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'class="sticky top-0 w-full z-[999]',
    'class="fixed top-0 left-0 w-full z-[999]'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Changed sticky to fixed.")
