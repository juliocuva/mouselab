import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<img src="img/premium_hero.jpg" alt="Arquitectura Corporativa" class="w-full h-full object-cover">',
    '<img src="img/mouselab_hero.jpg" alt="Software Engineering & AI Solutions" class="w-full h-full object-cover">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated hero image.")
