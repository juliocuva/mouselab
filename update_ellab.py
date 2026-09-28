import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change Title "Ingeniería que Factura" to "Ingeniería que Soluciona"
content = content.replace(
    'Ingeniería que <br><span class="font-black tracking-tighter">Factura</span>',
    'Ingeniería que <br><span class="font-black tracking-tighter">Soluciona</span>'
)

# 2. Change Supporting Image
content = content.replace(
    '<img src="img/premium_solidez.jpg" alt="Detalle operativo" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105">',
    '<img src="img/mouselab_flow.jpg" alt="Data flow dashboard" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105">'
)

# 3. Change Blue Box characteristics
blue_box_old = r"""                <!-- Right Column: Info Box -->
                <div class="lg:col-span-7" data-aos="fade-left">
                    <div class="bg-[#D9E8F5] p-12 lg:p-20 rounded-[3rem] h-full flex flex-col justify-center shadow-[0_20px_60px_-15px_rgba(0,0,0,0.05)]">
                        
                        <div class="space-y-16">
                            <div>
                                <span class="text-[#F26101] text-[10px] font-black uppercase tracking-[0.3em] mb-4 block">GARANTÍA</span>
                                <h4 class="text-3xl md:text-4xl font-black text-[#304269] tracking-tight mb-4">Calidad Certificada 3M™</h4>
                                <p class="text-gray-500 font-light leading-relaxed">Ejecución bajo los más estrictos estándares técnicos, utilizando materiales originales para resultados perdurables.</p>
                            </div>
                            
                            <div class="w-full h-px bg-gray-200"></div>
                            
                            <div>
                                <span class="text-[#F26101] text-[10px] font-black uppercase tracking-[0.3em] mb-4 block">ALCANCE</span>
                                <h4 class="text-3xl md:text-4xl font-black text-[#304269] tracking-tight mb-4">Hubs Operativos</h4>
                                <p class="text-gray-500 font-light leading-relaxed">Centros estratégicos en Medellín y Cali que optimizan tiempos de respuesta y garantizan cobertura nacional.</p>
                            </div>
                        </div>
                    </div>
                </div>"""

blue_box_new = r"""                <!-- Right Column: Info Box -->
                <div class="lg:col-span-7" data-aos="fade-left">
                    <div class="bg-[#D9E8F5] p-12 lg:p-20 rounded-[3rem] h-full flex flex-col justify-center shadow-[0_20px_60px_-15px_rgba(0,0,0,0.05)]">
                        
                        <div class="space-y-16">
                            <div>
                                <span class="text-[#F26101] text-[10px] font-black uppercase tracking-[0.3em] mb-4 block">INFRAESTRUCTURA CLOUD</span>
                                <h4 class="text-3xl md:text-4xl font-black text-[#304269] tracking-tight mb-4">Arquitectura Escalable</h4>
                                <p class="text-[#304269] font-light leading-relaxed opacity-80">Diseñamos bases de datos y microservicios preparados para soportar alto tráfico y crecer junto a tu modelo de negocio sin fricciones tecnológicas.</p>
                            </div>
                            
                            <div class="w-full h-px bg-[#304269] opacity-10"></div>
                            
                            <div>
                                <span class="text-[#F26101] text-[10px] font-black uppercase tracking-[0.3em] mb-4 block">METODOLOGÍA</span>
                                <h4 class="text-3xl md:text-4xl font-black text-[#304269] tracking-tight mb-4">Desarrollo Ágil & IA</h4>
                                <p class="text-[#304269] font-light leading-relaxed opacity-80">Aceleramos el tiempo de comercialización (Time-to-Market) implementando automatización e Inteligencia Artificial en cada ciclo del desarrollo.</p>
                            </div>
                        </div>
                    </div>
                </div>"""

content = content.replace(blue_box_old, blue_box_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated El Lab section.")
