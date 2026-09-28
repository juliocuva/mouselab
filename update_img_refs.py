with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace old image references with WebP versions
replacements = {
    '"img/bahia.png"': '"img/bahia.webp"',
    '"img/becoffee.png"': '"img/becoffee.webp"',
    '"img/bemap.png"': '"img/bemap.webp"',
    '"img/mouselab_hero.jpg"': '"img/mouselab_hero.webp"',
    '"img/mouselab_flowchart.jpg"': '"img/mouselab_flowchart.webp"',
    '"img/dashboard1.png"': '"img/dashboard1.webp"',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated image references to WebP.")
