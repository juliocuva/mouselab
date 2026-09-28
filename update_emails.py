import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<li><span class="text-white font-medium">Email:</span> hello@mouselab.dev</li>',
    '<li><span class="text-white font-medium">Agencia:</span> mouselabco@gmail.com</li>\n                        <li><span class="text-white font-medium">Directo:</span> juliocuva@gmail.com</li>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated emails.")
