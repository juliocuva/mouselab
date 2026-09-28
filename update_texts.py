import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. HERO SECTION ---
content = content.replace('Estrategia & Construcción de Marca', 'Arquitectura de Soluciones & IA')
content = content.replace(
    'Ingeniería<br>\n                        <span class="font-black">Visual</span> <span class="font-light italic">&</span><br>\n                        <span class="font-black">Retail',
    'Software<br>\n                        <span class="font-black">Engineering</span> <span class="font-light italic">&</span><br>\n                        <span class="font-black">AI Solutions'
)
content = content.replace(
    'Traducimos la identidad corporativa en entornos físicos de alto impacto. 50 años liderando la adecuación comercial a escala nacional.',
    'Creamos productos digitales de alto impacto impulsados por Inteligencia Artificial. Expertos en arquitectura de soluciones tecnológicas escalables.'
)

# --- 2. EXPERIENCIA (Arquitectura de Soluciones) ---
content = content.replace('La solidez de la <br><span class="font-black tracking-tighter">experiencia</span>', 'Arquitectura de <br><span class="font-black tracking-tighter">Soluciones</span>')
content = content.replace(
    'Nuestra trayectoria no se mide solo en cinco décadas de historia, sino en la capacidad probada de materializar desafíos arquitectónicos bajo estándares de precisión milimétrica.',
    'No solo escribimos código, construimos los cimientos de tu negocio. Integramos Inteligencia Artificial y arquitecturas robustas para garantizar que cada producto sea escalable, rápido y esté listo para facturar desde el día uno.'
)

# --- 3. PRODUCTOS (Cards) ---
# Título sección
content = content.replace('Divisiones<span class="yellow-dot">', 'Productos<span class="yellow-dot">')
content = content.replace(
    'Desarrollamos entornos que comunican y venden, integrando diseño, manufactura y montaje a gran escala.',
    'Plataformas propietarias y soluciones SaaS desarrolladas desde cero con IA, pensadas para dominar sus respectivos nichos.'
)

# Card 1: bemap.pro
content = content.replace('Sector Financiero', 'SaaS & Analytics')
content = content.replace('Adecuación <br><span class="font-black tracking-tighter">Bancaria</span>', 'bemap<span class="font-black tracking-tighter">.pro</span>')
content = content.replace(
    'Mobiliario operativo, módulos de autoservicio, revestimientos arquitectónicos y señalética normativa de alta seguridad.',
    'Nuestra plataforma estrella en facturación. Solución integral potenciada por IA para maximizar el rendimiento y la eficiencia.'
)

# Card 3: AxisONE (está debajo de bemap en el código, en la col izquierda)
content = content.replace('Supermercados', 'Coffee Tech')
content = content.replace('Grandes <br><span class="font-black tracking-tighter">Superficies</span>', 'AxisONE <br><span class="font-black tracking-tighter">Coffee</span>')
content = content.replace(
    'Mega-estructuras, branding exterior de gran escala y revestimientos arquitectónicos para supermercados.',
    'Plataforma tecnológica avanzada para la gestión, trazabilidad y optimización de la industria cafetera.'
)

# Card 2: Becoffee
content = content.replace('Consumo Masivo', 'E-Commerce & B2B')
content = content.replace('Retail & <br><span class="font-black tracking-tighter">Franquicias</span>', 'Becoffee<span class="font-black tracking-tighter">.pro</span>')
content = content.replace(
    'Fachadas comerciales, avisos termoformados y decoración integral de tiendas de conveniencia.',
    'El ecosistema digital diseñado para conectar productores, tostadores y amantes del café a nivel global.'
)

# Card 4: Web / Custom
content = content.replace('Comunicación Visual', 'Software Factory')
content = content.replace('Señalización <br><span class="font-black tracking-tighter">Interior</span>', 'Custom <br><span class="font-black tracking-tighter">Web Dev</span>')
content = content.replace(
    'Sistemas de orientación comercial, material POP, ambientación de pasillos y marcación de categorías.',
    'Desarrollo de sitios web corporativos y plataformas a la medida con arquitecturas modernas (Next.js, React, Tailwind).'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated texts to MouseLab profile.")
