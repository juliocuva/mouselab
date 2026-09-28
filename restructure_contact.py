import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the contact section and replace its content to restructure it.
# The contact section starts at `<section id="contacto"` and ends before `<!-- 6. Footer -->`

start = content.find('<!-- 5. Minimal Contact Form -->')
end = content.find('<!-- 6. Footer -->')

contact_section_old = content[start:end]

contact_section_new = r"""<!-- 5. Minimal Contact Form -->
    <section id="contacto" class="py-16 md:py-0 min-h-screen flex items-center bg-white">
        <div class="max-w-[90%] mx-auto w-full">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 md:gap-20 items-center">
                
                <!-- Left: Text and Contact Info -->
                <div data-aos="fade-right">
                    <span class="text-[9px] uppercase tracking-[0.3em] font-bold text-gray-400 block mb-4">Contacto</span>
                    <h2 class="text-4xl md:text-5xl md:text-6xl font-light tracking-tight text-[#304269]">¡Iniciemos un <br><span class="font-black tracking-tighter">proyecto!</span></h2>
                    <p class="text-gray-500 font-light text-base md:text-lg mt-6 max-w-md">Hablemos sobre tu próximo ecosistema digital. Si tienes un problema de negocio, nosotros diseñamos la arquitectura.</p>
                    
                    <div class="mt-8 md:mt-12 space-y-3 text-[#304269] text-base">
                        <p><a href="https://www.linkedin.com/in/julio-cesar-uva-ram%C3%ADrez/" target="_blank" class="font-light hover:text-[#F26101] transition-colors"><i class="fab fa-linkedin mr-2 text-[#0077B5] text-lg"></i>Julio César Uva Ramírez</a></p>
                        <p><span class="font-bold">Sede Principal:</span> <span class="font-light">Pereira, Risaralda</span></p>
                        <p><span class="font-bold text-[#F26101]"><i class="fab fa-whatsapp mr-2"></i>WhatsApp:</span> <a href="https://wa.me/573013970002" target="_blank" class="font-light hover:text-[#F26101] transition-colors">+57 301 397 0002</a></p>
                        <p><span class="font-bold">Agencia:</span> <a href="mailto:mouselabco@gmail.com" class="font-light hover:text-[#F26101] transition-colors">mouselabco@gmail.com</a></p>
                        <p><span class="font-bold">Directo:</span> <a href="mailto:juliocuva@gmail.com" class="font-light hover:text-[#F26101] transition-colors">juliocuva@gmail.com</a></p>
                    </div>
                </div>
                
                <!-- Right: Formulario -->
                <div data-aos="fade-left" data-aos-delay="200">
                    <form action="#" method="POST" class="space-y-6 md:space-y-8 bg-[#D9E8F5] p-8 md:p-12 rounded-[2.5rem] shadow-[0_10px_40px_-15px_rgba(0,0,0,0.03)] border border-gray-100">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
                            <div class="flex flex-col">
                                <label for="empresa" class="text-sm font-medium text-[#304269] mb-2 pl-2">Empresa o startup</label>
                                <input type="text" id="empresa" class="w-full bg-white rounded-xl px-5 py-3 md:py-4 text-base text-[#304269] focus:outline-none focus:ring-2 focus:ring-[#F26101] transition-all shadow-sm" placeholder="Ej. MouseLab" required>
                            </div>
                            <div class="flex flex-col">
                                <label for="email" class="text-sm font-medium text-[#304269] mb-2 pl-2">Correo corporativo</label>
                                <input type="email" id="email" class="w-full bg-white rounded-xl px-5 py-3 md:py-4 text-base text-[#304269] focus:outline-none focus:ring-2 focus:ring-[#F26101] transition-all shadow-sm" placeholder="ejemplo@empresa.com" required>
                            </div>
                        </div>

                        <div class="flex flex-col mt-4">
                            <label for="tipo" class="text-sm font-medium text-[#304269] mb-2 pl-2">Área de requerimiento</label>
                            <div class="relative">
                                <select id="tipo" class="w-full bg-white rounded-xl px-5 py-3 md:py-4 text-base text-[#304269] focus:outline-none focus:ring-2 focus:ring-[#F26101] transition-all appearance-none cursor-pointer shadow-sm">
                                    <option value="" disabled selected>Selecciona una opción...</option>
                                    <option value="saas">Desarrollo Plataforma SaaS</option>
                                    <option value="ai">Integración de Inteligencia Artificial</option>
                                    <option value="cloud">Arquitectura Cloud & Microservicios</option>
                                    <option value="consultoria">Consultoría Tecnológica</option>
                                </select>
                                <i class="fas fa-chevron-down absolute right-6 top-4 md:top-5 text-sm text-gray-400 pointer-events-none"></i>
                            </div>
                        </div>
                        <div class="pt-6 md:pt-8 text-center">
                            <a href="https://wa.me/573013970002" target="_blank" class="inline-block w-full bg-[#25D366] text-white text-sm md:text-base font-bold px-8 py-4 md:py-5 rounded-full hover:bg-[#128C7E] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                                <i class="fab fa-whatsapp text-xl mr-2 align-middle"></i> Ponte en contacto
                            </a>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    </section>

    """

content = content.replace(contact_section_old, contact_section_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restructured Contact Section.")
