import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<img src="img/logo_bahia.png" alt="Bahía Guacamayas" class="h-10 object-contain brightness-0">',
    '<img src="img/logo_bahia.png" alt="Bahía Guacamayas" class="h-16 object-contain brightness-0">'
)

content = content.replace(
    '<img src="img/logo_donmoiso.webp" alt="Don Moiso" class="h-12 object-contain brightness-0">',
    '<img src="img/logo_donmoiso.webp" alt="Don Moiso" class="h-20 object-contain brightness-0">'
)

content = content.replace(
    '<img src="img/logo_axisone.png" alt="AxisONE Coffee" class="h-10 object-contain brightness-0">',
    '<img src="img/logo_axisone.png" alt="AxisONE Coffee" class="h-16 object-contain brightness-0">'
)

content = content.replace(
    '<img src="img/logo_sc.png" alt="Sagrado Corazón" class="h-12 object-contain brightness-0">',
    '<img src="img/logo_sc.png" alt="Sagrado Corazón" class="h-20 object-contain brightness-0">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated logo sizes.")
