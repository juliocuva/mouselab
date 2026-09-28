import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

contact_block_old = r"""<div class="mt-8 space-y-3 text-\[#304269\] text-base">
                            <p><span class="font-bold">Sede Principal:</span> <span class="font-light">Pereira, Risaralda</span></p>
                            <p><span class="font-bold text-\[#F26101\]"><i class="fab fa-whatsapp mr-2"></i>WhatsApp:</span> <a href="https://wa.me/573013970002" target="_blank" class="font-light hover:text-\[#F26101\] transition-colors">\+57 301 397 0002</a></p>
                            <p><a href="https://www.linkedin.com/in/julio-cesar-uva-ram%C3%ADrez/" target="_blank" class="font-light hover:text-\[#F26101\] transition-colors"><i class="fab fa-linkedin mr-2 text-\[#0077B5\] text-lg"></i>Julio César Uva Ramírez</a></p>
                            <p><span class="font-bold">Agencia:</span> <a href="mailto:mouselabco@gmail.com" class="font-light hover:text-\[#F26101\] transition-colors">mouselabco@gmail.com</a></p>
                            <p><span class="font-bold">Directo:</span> <a href="mailto:juliocuva@gmail.com" class="font-light hover:text-\[#F26101\] transition-colors">juliocuva@gmail.com</a></p>
                        </div>"""

contact_block_new = r"""<div class="mt-8 space-y-3 text-[#304269] text-base">
                            <p><a href="https://www.linkedin.com/in/julio-cesar-uva-ram%C3%ADrez/" target="_blank" class="font-light hover:text-[#F26101] transition-colors"><i class="fab fa-linkedin mr-2 text-[#0077B5] text-lg"></i>Julio César Uva Ramírez</a></p>
                            <p><span class="font-bold">Sede Principal:</span> <span class="font-light">Pereira, Risaralda</span></p>
                            <p><span class="font-bold text-[#F26101]"><i class="fab fa-whatsapp mr-2"></i>WhatsApp:</span> <a href="https://wa.me/573013970002" target="_blank" class="font-light hover:text-[#F26101] transition-colors">+57 301 397 0002</a></p>
                            <p><span class="font-bold">Agencia:</span> <a href="mailto:mouselabco@gmail.com" class="font-light hover:text-[#F26101] transition-colors">mouselabco@gmail.com</a></p>
                            <p><span class="font-bold">Directo:</span> <a href="mailto:juliocuva@gmail.com" class="font-light hover:text-[#F26101] transition-colors">juliocuva@gmail.com</a></p>
                        </div>"""

content = re.sub(contact_block_old, contact_block_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Moved LinkedIn to the top.")
