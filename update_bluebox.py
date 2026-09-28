import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Blue Box in El Lab
blue_box_old = r"""<span class="text-xs font-bold uppercase tracking-widest text-\[#F26101\] mb-4 block">Garantía</span>
                            <h4 class="text-3xl md:text-4xl font-black tracking-tighter mb-4 text-\[#304269\]">Calidad Certificada 3M™</h4>
                            <p class="text-base text-gray-500 font-light leading-relaxed">Ejecución bajo los más estrictos estándares técnicos, utilizando materiales originales para resultados perdurables.</p>
                        </div>
                        <div>
                            <span class="text-xs font-bold uppercase tracking-widest text-\[#F26101\] mb-4 block">Alcance</span>
                            <h4 class="text-3xl md:text-4xl font-black tracking-tighter mb-4 text-\[#304269\]">Hubs Operativos</h4>
                            <p class="text-base text-gray-500 font-light leading-relaxed">Centros estratégicos en Medellín y Cali que optimizan tiempos de respuesta y garantizan cobertura nacional.</p>"""

blue_box_new = r"""<span class="text-xs font-bold uppercase tracking-widest text-[#F26101] mb-4 block">Infraestructura Cloud</span>
                            <h4 class="text-3xl md:text-4xl font-black tracking-tighter mb-4 text-[#304269]">Arquitectura Escalable</h4>
                            <p class="text-base text-[#304269] font-light leading-relaxed">Diseñamos bases de datos y microservicios preparados para soportar alto tráfico y crecer junto a tu modelo de negocio sin fricciones tecnológicas.</p>
                        </div>
                        <div>
                            <span class="text-xs font-bold uppercase tracking-widest text-[#F26101] mb-4 block">Metodología</span>
                            <h4 class="text-3xl md:text-4xl font-black tracking-tighter mb-4 text-[#304269]">Desarrollo Ágil & IA</h4>
                            <p class="text-base text-[#304269] font-light leading-relaxed">Aceleramos el tiempo de comercialización implementando automatización e Inteligencia Artificial en cada ciclo del desarrollo.</p>"""

content = re.sub(blue_box_old, blue_box_new, content)

# 2. Update Footer "Garantía" / Certificaciones
footer_cert_old = r"""                  <!-- Certificaciones -->
                  <div class="md:col-span-3">
                      <h5 class="text-\[#F26101\] text-xs font-black uppercase tracking-\[0.2em\] mb-6">Garantía</h5>
                      <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                          <h6 class="text-white font-black tracking-tight mb-2">Partner Certificado 3M™</h6>
                          <p class="text-xs text-gray-400 font-light">
                              Garantía MCS™ sobre materiales y procesos de manufactura.
                          </p>
                      </div>
                  </div>"""

footer_cert_new = r"""                  <!-- Tech Stack -->
                  <div class="md:col-span-3">
                      <h5 class="text-[#F26101] text-xs font-black uppercase tracking-[0.2em] mb-6">Partners & Stack</h5>
                      <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                          <h6 class="text-white font-black tracking-tight mb-2">Despliegue Cloud</h6>
                          <p class="text-xs text-gray-400 font-light">
                              Infraestructura de alto rendimiento alojada en AWS y Vercel.
                          </p>
                      </div>
                  </div>"""
                  
content = re.sub(footer_cert_old, footer_cert_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated blue box and footer.")
