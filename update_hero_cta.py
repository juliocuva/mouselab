import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

cta_old = r"""<a href="#estudio" class="group flex items-center gap-6 w-fit">
                        <span class="text-\[10px\] font-bold uppercase tracking-widest text-\[#304269\] group-hover:text-\[#F26101\] transition-colors">Explorar el trabajo</span>
                        <div class="w-12 h-px bg-\[#111\] group-hover:w-24 group-hover:bg-\[#F26101\] transition-all duration-500"></div>
                    </a>"""

cta_new = r"""<a href="https://wa.me/573013970002" target="_blank" class="group flex items-center gap-3 w-fit bg-[#25D366] hover:bg-[#128C7E] text-white px-8 py-4 rounded-full transition-all duration-500 shadow-lg hover:shadow-2xl">
                        <i class="fab fa-whatsapp text-xl"></i>
                        <span class="text-xs font-bold uppercase tracking-widest">Iniciar Proyecto</span>
                    </a>"""

content = re.sub(cta_old, cta_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Hero CTA to WhatsApp.")
