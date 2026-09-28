import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace root variable name and color
content = content.replace(
    '--brand-yellow: #FFFF00; /* Brighter, purer yellow matching the brand */',
    '--brand-orange: #F26101; /* Official MouseLab Orange */'
)

# Replace brand-dot background variable
content = content.replace(
    'background-color: var(--brand-yellow);',
    'background-color: var(--brand-orange);'
)

# Replace selection background color
content = content.replace(
    'selection:bg-[#FFFF00] selection:text-[#304269]',
    'selection:bg-[#F26101] selection:text-white'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dots and selection colors.")
