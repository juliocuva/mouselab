import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Header theme (Yellow -> Deep Blue #304269, text -> white)
content = content.replace('bg-[#FFFF00] text-black', 'bg-[#304269] text-white')
content = content.replace('hover:text-[#FFFF00]', 'hover:text-[#F26101]')
content = content.replace('border-black px-6 py-2 hover:bg-black', 'border-white px-6 py-2 hover:bg-white hover:text-[#304269]')
content = content.replace(
    '<img src="img/mouselab.png" alt="MouseLab.dev" class="h-8 object-contain filter brightness-0 opacity-90">',
    '<img src="img/mouselab.png" alt="MouseLab.dev" class="h-8 object-contain filter brightness-0 invert opacity-90">'
)

# 2. Accents (Yellow -> Orange #F26101)
content = content.replace('text-yellow-500', 'text-[#F26101]')
content = content.replace('bg-yellow-500', 'bg-[#F26101]')
content = content.replace('border-yellow-500', 'border-[#F26101]')
content = content.replace('text-[#FFFF00]', 'text-[#F26101]') # e.g. Footer headings

# 3. Headings & Dark Elements (Black/111 -> Deep Blue #304269)
content = content.replace('text-[#111]', 'text-[#304269]')
content = content.replace('text-black', 'text-[#304269]')

# 4. Backgrounds (F9F9F8 -> D9E8F5, Footer 1A1A1A -> 304269)
content = content.replace('bg-[#F9F9F8]', 'bg-[#D9E8F5]')
content = content.replace('bg-[#1A1A1A]', 'bg-[#304269]')
content = content.replace('bg-gray-50', 'bg-[#D9E8F5]')

# 5. Fix form input colors which might have been changed to #304269 but placeholders need contrast
# We will leave as is for now, tailwind classes will handle it.

# Update yellow-dot class to brand-dot
content = content.replace('yellow-dot', 'brand-dot')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update input.css
with open('input.css', 'r', encoding='utf-8') as f:
    css = f.read()
css = css.replace('.yellow-dot::after {', '.brand-dot::after {')
css = css.replace('background-color: #FFFF00;', 'background-color: #F26101;')
with open('input.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied Mouselab Color Palette.")
