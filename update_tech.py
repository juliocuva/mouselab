import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Marquee (Marcas que respaldan -> Tech Partners)
marquee_old = r"""<!-- 1.5. Trusted By (Clients Marquee/Grid) -->
    <section class="py-16 bg-white border-y border-gray-100">
        <div class="max-w-\[90%\] mx-auto">
            <p class="text-\[10px\] uppercase tracking-\[0.3em\] text-gray-400 text-center mb-10 font-bold">Marcas que respaldan nuestra ingeniería visual</p>
            <div class="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-60 grayscale hover:grayscale-0 transition-all duration-500">
                <!-- Client 1 -->
                <h4 class="text-2xl font-black tracking-tighter text-\[#304269\]">Banco de Bogotá</h4>
                <!-- Client 2 -->
                <h4 class="text-3xl font-black text-red-600 tracking-widest">OXXO</h4>
                <!-- Client 3 -->
                <h4 class="text-2xl font-black text-green-600 tracking-tighter flex items-center gap-1"><i class="fas fa-leaf text-lg"></i> Banco Popular</h4>
                <!-- Client 4 -->
                <h4 class="text-2xl font-black text-orange-500 tracking-tighter">ara</h4>
            </div>
        </div>
    </section>"""

marquee_new = r"""<!-- 1.5. Trusted By (Tech Stack Marquee) -->
    <section class="py-16 bg-white border-y border-gray-100">
        <div class="max-w-[90%] mx-auto">
            <p class="text-[10px] uppercase tracking-[0.3em] text-gray-400 text-center mb-10 font-bold">Tecnologías que respaldan nuestro desarrollo</p>
            <div class="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-60 hover:opacity-100 transition-all duration-500">
                <h4 class="text-2xl font-black tracking-tighter text-gray-800">Next.js</h4>
                <h4 class="text-2xl font-black tracking-tighter text-blue-500"><i class="fab fa-react"></i> React</h4>
                <h4 class="text-2xl font-black tracking-tighter text-yellow-500"><i class="fab fa-python"></i> Python</h4>
                <h4 class="text-2xl font-black tracking-tighter text-green-600">OpenAI</h4>
                <h4 class="text-2xl font-black tracking-tighter text-orange-500"><i class="fab fa-aws"></i> AWS</h4>
                <h4 class="text-2xl font-black tracking-tighter text-black">Vercel</h4>
            </div>
        </div>
    </section>"""
content = re.sub(marquee_old, marquee_new, content)

# 2. Update Infrastructure List
list_old = r"""<h2 class="text-sm md:text-base font-bold uppercase tracking-\[0.3em\] text-\[#F26101\] mb-20 text-center">Infraestructura Interna</h2>
            
            <div class="max-w-5xl mx-auto divide-y divide-white/10">
                <div class="py-12 group cursor-pointer flex flex-col md:flex-row justify-between items-start md:items-center" data-aos="fade-up">
                    <h3 class="text-3xl md:text-5xl font-light tracking-tight text-white group-hover:text-\[#F26101\] transition-colors duration-500">01. <span class="font-black tracking-tighter">Metalmecánica</span> Aplicada</h3>
                    <p class="text-base md:text-lg text-gray-400 font-light max-w-sm mt-6 md:mt-0 text-left md:text-right opacity-0 group-hover:opacity-100 transition-opacity duration-500 leading-relaxed">Corte estructural, soldadura y ensamblaje para mobiliario y avisos elevados.</p>
                </div>
                <div class="py-12 group cursor-pointer flex flex-col md:flex-row justify-between items-start md:items-center" data-aos="fade-up">
                    <h3 class="text-3xl md:text-5xl font-light tracking-tight text-white group-hover:text-\[#F26101\] transition-colors duration-500">02. Cama Plana UV <span class="font-black tracking-tighter">& CNC</span></h3>
                    <p class="text-base md:text-lg text-gray-400 font-light max-w-sm mt-6 md:mt-0 text-left md:text-right opacity-0 group-hover:opacity-100 transition-opacity duration-500 leading-relaxed">Precisión milimétrica sobre maderas, acrílicos, alucobond y sustratos rígidos.</p>
                </div>
                <div class="py-12 group cursor-pointer flex flex-col md:flex-row justify-between items-start md:items-center" data-aos="fade-up">
                    <h3 class="text-3xl md:text-5xl font-light tracking-tight text-white group-hover:text-\[#F26101\] transition-colors duration-500">03. Artes Gráficas <span class="font-black tracking-tighter">Offset</span></h3>
                    <p class="text-base md:text-lg text-gray-400 font-light max-w-sm mt-6 md:mt-0 text-left md:text-right opacity-0 group-hover:opacity-100 transition-opacity duration-500 leading-relaxed">Impresión masiva y gran formato con fidelidad de color corporativa absoluta.</p>
                </div>
                <div class="py-12 group cursor-pointer flex flex-col md:flex-row justify-between items-start md:items-center" data-aos="fade-up">
                    <h3 class="text-3xl md:text-5xl font-light tracking-tight text-white group-hover:text-\[#F26101\] transition-colors duration-500">04. Instalación <span class="font-black tracking-tighter">Certificada</span></h3>
                    <p class="text-base md:text-lg text-gray-400 font-light max-w-sm mt-6 md:mt-0 text-left md:text-right opacity-0 group-hover:opacity-100 transition-opacity duration-500 leading-relaxed">Personal técnico certificado en alturas para despliegues seguros a nivel nacional.</p>
                </div>
            </div>"""

list_new = r"""<h2 class="text-sm md:text-base font-bold uppercase tracking-[0.3em] text-[#F26101] mb-20 text-center">Core Tech Stack & Capacidades</h2>
            
            <div class="max-w-5xl mx-auto divide-y divide-white/10">
                <div class="py-12 group cursor-pointer flex flex-col md:flex-row justify-between items-start md:items-center" data-aos="fade-up">
                    <h3 class="text-3xl md:text-5xl font-light tracking-tight text-white group-hover:text-[#F26101] transition-colors duration-500">01. <span class="font-black tracking-tighter">Frontend</span> UI/UX</h3>
                    <p class="text-base md:text-lg text-gray-400 font-light max-w-sm mt-6 md:mt-0 text-left md:text-right opacity-0 group-hover:opacity-100 transition-opacity duration-500 leading-relaxed">React, Next.js y Tailwind. Desarrollo de interfaces ultrarrápidas orientadas a la conversión B2B.</p>
                </div>
                <div class="py-12 group cursor-pointer flex flex-col md:flex-row justify-between items-start md:items-center" data-aos="fade-up">
                    <h3 class="text-3xl md:text-5xl font-light tracking-tight text-white group-hover:text-[#F26101] transition-colors duration-500">02. Backend <span class="font-black tracking-tighter">& Cloud</span></h3>
                    <p class="text-base md:text-lg text-gray-400 font-light max-w-sm mt-6 md:mt-0 text-left md:text-right opacity-0 group-hover:opacity-100 transition-opacity duration-500 leading-relaxed">Node.js, Python, AWS. Arquitectura de microservicios y despliegues escalables en la nube.</p>
                </div>
                <div class="py-12 group cursor-pointer flex flex-col md:flex-row justify-between items-start md:items-center" data-aos="fade-up">
                    <h3 class="text-3xl md:text-5xl font-light tracking-tight text-white group-hover:text-[#F26101] transition-colors duration-500">03. Inteligencia <span class="font-black tracking-tighter">Artificial</span></h3>
                    <p class="text-base md:text-lg text-gray-400 font-light max-w-sm mt-6 md:mt-0 text-left md:text-right opacity-0 group-hover:opacity-100 transition-opacity duration-500 leading-relaxed">OpenAI, LLMs. Integración de agentes autónomos y automatización inteligente de flujos corporativos.</p>
                </div>
                <div class="py-12 group cursor-pointer flex flex-col md:flex-row justify-between items-start md:items-center" data-aos="fade-up">
                    <h3 class="text-3xl md:text-5xl font-light tracking-tight text-white group-hover:text-[#F26101] transition-colors duration-500">04. Data <span class="font-black tracking-tighter">& Analytics</span></h3>
                    <p class="text-base md:text-lg text-gray-400 font-light max-w-sm mt-6 md:mt-0 text-left md:text-right opacity-0 group-hover:opacity-100 transition-opacity duration-500 leading-relaxed">PostgreSQL, Redis. Procesamiento en tiempo real, trazabilidad de datos y dashboards B2B.</p>
                </div>
            </div>"""
content = re.sub(list_old, list_new, content)

# 3. Update Contact Form Title & Subtitle
form_old = r"""<h2 class="text-4xl md:text-5xl md:text-6xl font-light tracking-tight text-\[#304269\]">Iniciar <br><span class="font-black tracking-tighter">Proyecto</span><span class="text-\[#F26101\]">.</span></h2>
                        <p class="text-gray-500 font-light text-base md:text-lg mt-6">Contáctenos para licitaciones corporativas y evaluación de ingeniería visual.</p>"""
form_new = r"""<h2 class="text-4xl md:text-5xl md:text-6xl font-light tracking-tight text-[#304269]">Iniciar <br><span class="font-black tracking-tighter">Proyecto</span><span class="text-[#F26101]">.</span></h2>
                        <p class="text-gray-500 font-light text-base md:text-lg mt-6">Hablemos sobre tu próximo ecosistema digital. Si tienes un problema de negocio, nosotros diseñamos la arquitectura.</p>"""
content = re.sub(form_old, form_new, content)

# Update Razón Social to Empresa/Startup
content = content.replace('Razón Social</label>', 'Empresa o Startup</label>')


# 4. Update Footer Hubs to WhatsApp Contact
footer_hubs_old = r"""<!-- Hubs Operativos -->
                <div class="md:col-span-3">
                    <h5 class="text-\[#F26101\] text-xs font-black uppercase tracking-\[0.2em\] mb-6">Hubs Operativos</h5>
                    <ul class="space-y-4 text-gray-400 font-light text-sm">
                        <li><span class="text-white font-medium">Sede Principal:</span> Pereira, Risaralda</li>
                        <li><span class="text-white font-medium">Planta Medellín:</span> Cobertura Antioquia</li>
                        <li><span class="text-white font-medium">Planta Cali:</span> Cobertura Pacífico</li>
                    </ul>
                </div>"""
footer_hubs_new = r"""<!-- Contacto Directo -->
                <div class="md:col-span-3">
                    <h5 class="text-[#F26101] text-xs font-black uppercase tracking-[0.2em] mb-6">Contacto Directo</h5>
                    <ul class="space-y-4 text-gray-400 font-light text-sm">
                        <li><span class="text-white font-medium">Sede Principal:</span> Pereira, Risaralda</li>
                        <li>
                            <a href="https://wa.me/573013970002" target="_blank" rel="noopener noreferrer" class="hover:text-white transition-colors flex items-center gap-2">
                                <i class="fab fa-whatsapp text-[#F26101]"></i> <span class="text-white font-medium">WhatsApp:</span> +57 301 397 0002
                            </a>
                        </li>
                        <li><span class="text-white font-medium">Email:</span> hello@mouselab.dev</li>
                    </ul>
                </div>"""
content = re.sub(footer_hubs_old, footer_hubs_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated all sections.")
