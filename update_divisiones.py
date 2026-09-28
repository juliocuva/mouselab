import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the top part of Divisiones
top_pattern = re.compile(r'(\s*<!-- 3\. Divisions \(Minimalist Cards\) -->\s*<section id="divisiones" class="py-32 bg-\[#F9F9F8\]">\s*<div class="max-w-\[90%\] mx-auto">)\s*<div class="mb-24 flex flex-col md:flex-row items-end gap-16 lg:pl-16 xl:pl-24">\s*<h2 class="text-4xl md:text-6xl font-black tracking-tighter text-\[#111\] min-w-max">Divisiones<span class="yellow-dot"></span></h2>\s*<p class="text-base md:text-lg text-gray-500 font-light max-w-lg mb-2">Desarrollamos entornos que comunican y venden, integrando diseño, manufactura y montaje a gran escala.</p>\s*</div>\s*<!-- Wrapper para reducir las tarjetas al 80% -->\s*<div class="w-full lg:w-\[80%\] mx-auto">\s*<div class="grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-16">', re.DOTALL)

top_replacement = r"""\1
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 lg:pl-16 xl:pl-24 items-start">
                
                <!-- Columna Izquierda: Título y Párrafo -->
                <div class="lg:col-span-4 sticky top-32" data-aos="fade-right">
                    <h2 class="text-5xl md:text-6xl font-black tracking-tighter text-[#111] mb-6">Divisiones<span class="yellow-dot"></span></h2>
                    <p class="text-lg text-gray-500 font-light leading-relaxed max-w-sm">Desarrollamos entornos que comunican y venden, integrando diseño, manufactura y montaje a gran escala.</p>
                </div>

                <!-- Columna Derecha: Tarjetas (Grid 2x2) -->
                <div class="lg:col-span-8">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12">"""

new_content = top_pattern.sub(top_replacement, content)

# Remove the closing wrapper div we added earlier
bottom_pattern = re.compile(r'</div> <!-- Cierre del wrapper del 80% -->\s*</div>\s*</section>')
bottom_replacement = r"""    </div>
                </div>
            </div>
        </div>
    </section>"""
    
new_content = bottom_pattern.sub(bottom_replacement, new_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Divisiones to side-by-side layout.")
