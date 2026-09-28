import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_form = """                    <form action="#" method="POST" class="space-y-8 bg-[#D9E8F5] p-12 md:p-20 rounded-[3rem] shadow-[0_10px_40px_-15px_rgba(0,0,0,0.03)] border border-gray-100" data-aos="fade-up" data-aos-delay="200">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="flex flex-col">
                        <label for="empresa" class="text-sm font-medium text-[#304269] mb-2 pl-2">Empresa o startup</label>
                        <input type="text" id="empresa" class="w-full bg-white rounded-xl px-6 py-4 text-base text-[#304269] focus:outline-none focus:ring-2 focus:ring-[#F26101] transition-all shadow-sm" placeholder="Ej. MouseLab" required>
                    </div>
                    <div class="flex flex-col">
                        <label for="email" class="text-sm font-medium text-[#304269] mb-2 pl-2">Correo corporativo</label>
                        <input type="email" id="email" class="w-full bg-white rounded-xl px-6 py-4 text-base text-[#304269] focus:outline-none focus:ring-2 focus:ring-[#F26101] transition-all shadow-sm" placeholder="ejemplo@empresa.com" required>
                    </div>
                </div>

                <div class="flex flex-col mt-4">
                    <label for="tipo" class="text-sm font-medium text-[#304269] mb-2 pl-2">Área de requerimiento</label>
                    <div class="relative">
                        <select id="tipo" class="w-full bg-white rounded-xl px-6 py-4 text-base text-[#304269] focus:outline-none focus:ring-2 focus:ring-[#F26101] transition-all appearance-none cursor-pointer shadow-sm">
                            <option value="" disabled selected>Selecciona una opción...</option>
                            <option value="saas">Desarrollo Plataforma SaaS</option>
                            <option value="ai">Integración de Inteligencia Artificial</option>
                            <option value="cloud">Arquitectura Cloud & Microservicios</option>
                            <option value="consultoria">Consultoría Tecnológica</option>
                        </select>
                        <i class="fas fa-chevron-down absolute right-6 top-5 text-sm text-gray-400 pointer-events-none"></i>
                    </div>
                </div>
                <div class="pt-8 text-center">
                    <a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-[#25D366] text-white text-base font-bold px-12 py-5 rounded-full hover:bg-[#128C7E] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                        <i class="fab fa-whatsapp text-xl mr-2 align-middle"></i> Ponte en contacto
                    </a>
                </div>
            </form>"""

# We will use regex to find <form action="#" method="POST" ... </form>
pattern = re.compile(r'<form action="#" method="POST".*?</form>', re.DOTALL)
content = pattern.sub(new_form, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Form replaced.")
