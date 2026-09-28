import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<img src="img/logo_sc.png" alt="Sagrado Corazón" class="h-20 object-contain brightness-0">',
    '<img src="img/logo_sc.png" alt="Sagrado Corazón" class="h-20 object-contain brightness-0">\n                <img src="img/becoffee-logo.svg" alt="Becoffee" class="h-12 object-contain brightness-0">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added becoffee logo.")
