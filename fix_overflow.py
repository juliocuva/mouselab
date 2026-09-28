import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a wrapper div right after the header
content = content.replace(
    '</header>',
    '</header>\n    <main class="w-full overflow-hidden">'
)

# Close the wrapper div right before scripts
content = content.replace(
    '<!-- Scripts for Animations -->',
    '</main>\n\n    <!-- Scripts for Animations -->'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added overflow hidden wrapper.")
