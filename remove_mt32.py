import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove md:mt-32 from the cards in the divisiones section
new_content = content.replace('md:mt-32', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed md:mt-32 to align cards at the top.")
