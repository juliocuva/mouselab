import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

cta_old = r"""<a href="https://wa.me/573013970002" target="_blank" class="group flex items-center justify-center gap-3 w-fit border-2 border-\[#25D366\] text-\[#25D366\] bg-transparent hover:bg-\[#25D366\] hover:text-white px-8 py-4 rounded-full transition-all duration-500 shadow-lg hover:shadow-2xl">
                        <i class="fab fa-whatsapp text-xl"></i>
                        <span class="text-xs font-bold uppercase tracking-widest">Iniciar Proyecto</span>
                    </a>"""

cta_new = r"""<a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-[#25D366] text-white text-base font-bold px-12 py-5 rounded-full hover:bg-[#128C7E] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                        <i class="fab fa-whatsapp text-xl mr-2 align-middle"></i> Ponte en contacto
                    </a>"""

content = re.sub(cta_old, cta_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Hero CTA to exact contact button.")
