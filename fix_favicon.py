import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = content.replace(
    '<title>mouselab.dev | Retail & Corporate Architecture</title>',
    '<title>MouseLab.dev | Ingeniería de Software & IA</title>\n    <link rel="icon" type="image/png" href="img/mouselab.png">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated title and favicon.")
