import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Scale down Bahia
content = content.replace(
    '<img src="img/logo_bahia.png" alt="Bahía Guacamayas" class="h-16 object-contain brightness-0">',
    '<img src="img/logo_bahia.png" alt="Bahía Guacamayas" class="h-12 object-contain brightness-0">'
)

# Scale down Sagrado Corazón
content = content.replace(
    '<img src="img/logo_sc.png" alt="Sagrado Corazón" class="h-20 object-contain brightness-0">',
    '<img src="img/logo_sc.png" alt="Sagrado Corazón" class="h-14 object-contain brightness-0">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Scaled down logos.")
