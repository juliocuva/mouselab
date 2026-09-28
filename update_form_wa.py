import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix form select options
old_select = r"""<select id="tipo" class="w-full bg-transparent border-b-2 border-gray-200 py-4 text-base text-gray-600 focus:outline-none focus:border-\[#F26101\] transition-colors appearance-none cursor-pointer">
                        <option value="" disabled selected>.*?rea de requerimiento...</option>
                        <option value="adecuacion">Adecuación Arquitectónica \(Bancos / Oficinas\)</option>
                        <option value="retail">Despliegue Retail / Fachadas</option>
                        <option value="senalizacion">Señalética y Avisos Elevados</option>
                    </select>"""

new_select = r"""<select id="tipo" class="w-full bg-transparent border-b-2 border-gray-200 py-4 text-base text-gray-600 focus:outline-none focus:border-[#F26101] transition-colors appearance-none cursor-pointer">
                        <option value="" disabled selected>Área de requerimiento...</option>
                        <option value="saas">Desarrollo Plataforma SaaS</option>
                        <option value="ai">Integración de Inteligencia Artificial</option>
                        <option value="cloud">Arquitectura Cloud & Microservicios</option>
                        <option value="consultoria">Consultoría Tecnológica</option>
                    </select>"""
content = re.sub(old_select, new_select, content)

# Change Submit Button to WhatsApp Button directly
old_button = r"""<button type="submit" class="bg-\[#111\] text-white text-xs font-bold uppercase tracking-\[0.2em\] px-16 py-6 rounded-full hover:bg-\[#F26101\] hover:text-\[#304269\] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                        Enviar Solicitud
                    </button>"""

new_button = r"""<a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-[#25D366] text-white text-xs font-bold uppercase tracking-[0.2em] px-12 py-6 rounded-full hover:bg-[#128C7E] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                        <i class="fab fa-whatsapp text-lg mr-2 align-middle"></i> Escríbenos a WhatsApp
                    </a>"""
content = re.sub(old_button, new_button, content)

# Replace the text above the form to also include the direct number
content = content.replace(
    'Hablemos sobre tu próximo ecosistema digital. Si tienes un problema de negocio, nosotros diseñamos la arquitectura.</p>',
    'Hablemos sobre tu próximo ecosistema digital. Si tienes un problema de negocio, nosotros diseñamos la arquitectura.<br><br><span class="font-bold text-[#F26101]">WhatsApp Directo: <a href="https://wa.me/573013970002" target="_blank">+57 301 397 0002</a></span></p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Form options and WhatsApp button.")
