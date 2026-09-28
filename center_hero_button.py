import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

cta_old = r"""<a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-\[#25D366\] text-white text-base font-bold px-12 py-5 rounded-full hover:bg-\[#128C7E\] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                        <i class="fab fa-whatsapp text-xl mr-2 align-middle"></i> Ponte en contacto
                    </a>"""

cta_new = r"""<div class="w-full text-center mt-2">
                        <a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-[#25D366] text-white text-base font-bold px-12 py-5 rounded-full hover:bg-[#128C7E] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                            <i class="fab fa-whatsapp text-xl mr-2 align-middle"></i> Ponte en contacto
                        </a>
                    </div>"""

# Replace only the first occurrence (which is the hero button, not the bottom form button)
content = content.replace(
    '<a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-[#25D366] text-white text-base font-bold px-12 py-5 rounded-full hover:bg-[#128C7E] transition-colors duration-500 shadow-xl hover:shadow-2xl">\n                        <i class="fab fa-whatsapp text-xl mr-2 align-middle"></i> Ponte en contacto\n                    </a>',
    '<div class="w-full text-center mt-2">\n                        <a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-[#25D366] text-white text-base font-bold px-12 py-5 rounded-full hover:bg-[#128C7E] transition-colors duration-500 shadow-xl hover:shadow-2xl">\n                            <i class="fab fa-whatsapp text-xl mr-2 align-middle"></i> Ponte en contacto\n                        </a>\n                    </div>',
    1
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Centered Hero button.")
