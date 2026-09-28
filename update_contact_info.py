import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

contact_info = r"""Hablemos sobre tu próximo ecosistema digital. Si tienes un problema de negocio, nosotros diseñamos la arquitectura.</p>
                        
                        <div class="mt-8 space-y-3 text-[#304269] text-base">
                            <p><span class="font-bold">Sede Principal:</span> <span class="font-light">Pereira, Risaralda</span></p>
                            <p><span class="font-bold text-[#F26101]"><i class="fab fa-whatsapp mr-2"></i>WhatsApp:</span> <a href="https://wa.me/573013970002" target="_blank" class="font-light hover:text-[#F26101] transition-colors">+57 301 397 0002</a></p>
                            <p><span class="font-bold">Agencia:</span> <a href="mailto:mouselabco@gmail.com" class="font-light hover:text-[#F26101] transition-colors">mouselabco@gmail.com</a></p>
                            <p><span class="font-bold">Directo:</span> <a href="mailto:juliocuva@gmail.com" class="font-light hover:text-[#F26101] transition-colors">juliocuva@gmail.com</a></p>
                        </div>"""

content = content.replace(
    'Hablemos sobre tu próximo ecosistema digital. Si tienes un problema de negocio, nosotros diseñamos la arquitectura.<br><br><span class="font-bold text-[#F26101]">WhatsApp Directo: <a href="https://wa.me/573013970002" target="_blank">+57 301 397 0002</a></span></p>',
    contact_info
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated contact info block above form.")
