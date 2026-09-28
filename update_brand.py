import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and Meta
content = content.replace('Gráficas Olímpica |', 'mouselab.dev |')
content = content.replace('content="Gráficas Olímpica', 'content="mouselab.dev')

# 2. Update Header Logo
header_logo_pattern = re.compile(r'<img src="img/logo-graficas\.png" alt="Gráficas Olímpica" class="h-8">')
header_text_logo = r'<div class="text-2xl font-black tracking-tighter text-[#111]">mouse<span class="font-light">lab</span><span class="text-yellow-500">.dev</span></div>'
content = header_logo_pattern.sub(header_text_logo, content)

# 3. Update Footer Logo
footer_logo_pattern = re.compile(r'<img src="img/logo-graficas\.png" alt="Gráficas Olímpica" class="h-10 mb-8 filter brightness-0 invert opacity-90">')
footer_text_logo = r'<div class="text-3xl font-black tracking-tighter text-white mb-8">mouse<span class="font-light">lab</span><span class="text-yellow-500">.dev</span></div>'
content = footer_logo_pattern.sub(footer_text_logo, content)

# 4. Update Copyright (and year)
content = content.replace('2024 Gráficas Olímpica', '2026 mouselab.dev')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated brand name to mouselab.dev everywhere.")
