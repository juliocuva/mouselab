import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace AxisONE tag
content = content.replace(
    '<span class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-6 block group-hover:text-[#F26101] transition-colors">Coffee Tech</span>',
    '<span class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-6 block group-hover:text-[#F26101] transition-colors">Traceability & EUDR</span>'
)

# Replace AxisONE paragraph
content = content.replace(
    'Plataforma tecnológica avanzada para la gestión, trazabilidad y optimización de la industria cafetera.',
    'Turn volume coffee into verified, transparent, and EUDR-compliant digital packages for international buyers.'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated AxisONE text.")
