import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change title
old_title = r'<h2 class="text-4xl md:text-5xl md:text-6xl font-light tracking-tight text-\[#304269\]">Iniciar <br><span class="font-black tracking-tighter">Proyecto</span><span class="text-\[#F26101\]">.</span></h2>'
new_title = r'<h2 class="text-4xl md:text-5xl md:text-6xl font-light tracking-tight text-[#304269]">¡Iniciemos un <br><span class="font-black tracking-tighter">proyecto!</span></h2>'
content = re.sub(old_title, new_title, content)

# 2. Adjust padding and gap
content = content.replace('id="contacto" class="py-32 bg-white"', 'id="contacto" class="py-16 md:py-20 min-h-screen flex items-center bg-white"')
content = content.replace('class="grid grid-cols-1 lg:grid-cols-2 gap-16 md:gap-24 items-start"', 'class="grid grid-cols-1 lg:grid-cols-2 gap-8 md:gap-16 items-stretch"')

# 3. Adjust map height to stretch with the flex container
# We replace `min-h-[500px] md:min-h-[700px]` with `h-full min-h-[300px]`
content = content.replace('w-full h-full min-h-[500px] md:min-h-[700px]', 'w-full h-full min-h-[300px] md:min-h-[400px] lg:absolute lg:inset-0')

# Actually, making it absolute will break the grid cell. 
# Better replace `min-h-[500px] md:min-h-[700px]` with `min-h-[300px] md:min-h-[100%]` or just remove the strict min-height and let it stretch.
content = content.replace('lg:absolute lg:inset-0', '') # remove if accidentally added
content = content.replace('w-full h-full min-h-[300px] md:min-h-[400px]', 'w-full h-full min-h-[350px] lg:min-h-0')

# Also, let's make the map container stretch
# We already changed items-start to items-stretch in the grid.
# The map container is `<div class="w-full h-full min-h-[350px] lg:min-h-0 rounded-[3rem] overflow-hidden shadow-[0_20px_60px_-15px_rgba(0,0,0,0.1)] relative" data-aos="fade-left">`

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modified Contact Section.")
