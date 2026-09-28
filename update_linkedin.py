import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Footer Social Links
footer_social_old = r"""<div class="flex gap-6 text-gray-500 text-sm">
                    <a href="#" class="hover:text-white transition-colors"><i class="fab fa-linkedin"></i></a>
                    <a href="#" class="hover:text-white transition-colors"><i class="fab fa-instagram"></i></a>
                </div>"""

footer_social_new = r"""<div class="flex gap-6 text-gray-500 text-sm">
                    <a href="https://www.linkedin.com/in/julio-cesar-uva-ram%C3%ADrez/" target="_blank" rel="noopener noreferrer" class="hover:text-white transition-colors"><i class="fab fa-linkedin text-xl"></i></a>
                </div>"""

content = content.replace(footer_social_old, footer_social_new)


# 2. Update Contact Block above form
contact_block_old = r"""<p><span class="font-bold text-\[#F26101\]"><i class="fab fa-whatsapp mr-2"></i>WhatsApp:</span> <a href="https://wa.me/573013970002" target="_blank" class="font-light hover:text-\[#F26101\] transition-colors">\+57 301 397 0002</a></p>"""

contact_block_new = r"""<p><span class="font-bold text-[#F26101]"><i class="fab fa-whatsapp mr-2"></i>WhatsApp:</span> <a href="https://wa.me/573013970002" target="_blank" class="font-light hover:text-[#F26101] transition-colors">+57 301 397 0002</a></p>
                            <p><span class="font-bold text-[#0077B5]"><i class="fab fa-linkedin mr-2"></i>LinkedIn:</span> <a href="https://www.linkedin.com/in/julio-cesar-uva-ram%C3%ADrez/" target="_blank" class="font-light hover:text-[#F26101] transition-colors">Julio César Uva Ramírez</a></p>"""

content = re.sub(contact_block_old, contact_block_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated LinkedIn and removed Instagram.")
