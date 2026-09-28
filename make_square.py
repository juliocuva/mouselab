import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change brand-dot from round to square
content = content.replace(
    'border-radius: 50%;',
    'border-radius: 0;' # Making it perfectly square
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated brand-dot to square.")
