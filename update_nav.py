import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the nav menu
nav_old = r"""            <nav class="hidden md:flex space-x-12 items-center">
                <a href="#estudio" class="text-xs uppercase tracking-[0.15em] hover-line pb-1 font-medium">Estudio</a>
                <a href="#Productos" class="text-xs uppercase tracking-[0.15em] hover-line pb-1 font-medium">Productos</a>
                <a href="#infraestructura" class="text-xs uppercase tracking-[0.15em] hover-line pb-1 font-medium">Infraestructura</a>
                <a href="#contacto" class="text-xs uppercase tracking-[0.15em] font-bold border border-white px-6 py-2 hover:bg-white hover:text-[#304269] hover:text-[#F26101] transition-colors duration-500">Contacto</a>
            </nav>"""

nav_new = r"""            <nav class="hidden md:flex space-x-12 items-center">
                <a href="#estudio" class="text-xs uppercase tracking-[0.15em] hover-line pb-1 font-medium">El Lab</a>
                <a href="#divisiones" class="text-xs uppercase tracking-[0.15em] hover-line pb-1 font-medium">Plataformas</a>
                <a href="#infraestructura" class="text-xs uppercase tracking-[0.15em] hover-line pb-1 font-medium">Stack Tecnológico</a>
                <a href="#contacto" class="text-xs uppercase tracking-[0.15em] font-bold border border-white px-6 py-2 hover:bg-white hover:text-[#304269] transition-colors duration-500">Contacto</a>
            </nav>"""

content = content.replace(nav_old, nav_new)

# Also fix the section id for divisiones if it got renamed to #Productos
content = content.replace('id="Productos"', 'id="divisiones"')

# And fix the footer links!
footer_nav_old = r"""                    <ul class="space-y-4 text-gray-400 font-light text-sm flex flex-col">
                        <a href="#estudio" class="hover:text-white transition-colors w-fit">El Estudio</a>
                        <a href="#Productos" class="hover:text-white transition-colors w-fit">Productos</a>
                        <a href="#infraestructura" class="hover:text-white transition-colors w-fit">Infraestructura</a>
                    </ul>"""
footer_nav_new = r"""                    <ul class="space-y-4 text-gray-400 font-light text-sm flex flex-col">
                        <a href="#estudio" class="hover:text-white transition-colors w-fit">El Lab</a>
                        <a href="#divisiones" class="hover:text-white transition-colors w-fit">Plataformas</a>
                        <a href="#infraestructura" class="hover:text-white transition-colors w-fit">Stack Tecnológico</a>
                    </ul>"""

content = content.replace(footer_nav_old, footer_nav_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Nav")
