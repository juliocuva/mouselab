import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the floating image block from the Hero
pattern = re.compile(r'\s*<!-- Restored Floating Image -->.*?</div>\s*</div>', re.DOTALL)
new_content = pattern.sub('', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed floating image from Hero.")
