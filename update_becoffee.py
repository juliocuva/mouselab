import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Becoffee paragraph
content = content.replace(
    'El ecosistema digital diseñado para conectar productores, tostadores y amantes del café a nivel global.',
    'Vende tu café de forma ágil y directa por WhatsApp.'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Becoffee text.")
