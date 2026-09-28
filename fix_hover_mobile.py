import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace opacity-0 with opacity-100 md:opacity-0 in the stack section
content = content.replace(
    'opacity-0 group-hover:opacity-100 transition-opacity',
    'opacity-100 md:opacity-0 group-hover:opacity-100 transition-opacity'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated opacity for mobile.")
