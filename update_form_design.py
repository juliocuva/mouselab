import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the inner form
form_old = r"""                  <div class="grid grid-cols-1 md:grid-cols-2 gap-16">
                      <div class="relative">
                          <input type="text" id="empresa" class="w-full bg-transparent border-b-2 border-gray-200 py-4 text-base text-\[#304269\] focus:outline-none focus:border-\[#F26101\] transition-colors peer placeholder-transparent" placeholder="Empresa" required>
                          <label for="empresa" class="absolute left-0 -top-4 text-xs font-bold uppercase tracking-widest text-gray-400 transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-4 peer-focus:-top-4 peer-focus:text-xs peer-focus:text-\[#F26101\]">Empresa o Startup</label>
                      </div>
                      <div class="relative">
                          <input type="email" id="email" class="w-full bg-transparent border-b-2 border-gray-200 py-4 text-base text-\[#304269\] focus:outline-none focus:border-\[#F26101\] transition-colors peer placeholder-transparent" placeholder="Email" required>
                          <label for="email" class="absolute left-0 -top-4 text-xs font-bold uppercase tracking-widest text-gray-400 transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-4 peer-focus:-top-4 peer-focus:text-xs peer-focus:text-\[#F26101\]">Correo Corporativo</label>
                      </div>
                  </div>
  
                  <div class="relative mt-8">
                      <select id="tipo" class="w-full bg-transparent border-b-2 border-gray-200 py-4 text-base text-gray-600 focus:outline-none focus:border-\[#F26101\] transition-colors appearance-none cursor-pointer">
                          <option value="" disabled selected>Área de requerimiento...</option>
                          <option value="saas">Desarrollo Plataforma SaaS</option>
                          <option value="ai">Integración de Inteligencia Artificial</option>
                          <option value="cloud">Arquitectura Cloud & Microservicios</option>
                          <option value="consultoria">Consultoría Tecnológica</option>
                      </select>
                      <i class="fas fa-chevron-down absolute right-0 top-6 text-xs text-gray-400 pointer-events-none"></i>
                  </div>
                  <div class="pt-12 text-center">
                      <a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-\[#25D366\] text-white text-xs font-bold uppercase tracking-\[0.2em\] px-12 py-6 rounded-full hover:bg-\[#128C7E\] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                        <i class="fab fa-whatsapp text-lg mr-2 align-middle"></i> Escríbenos a WhatsApp
                    </a>
                  </div>"""

form_new = r"""                  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                      <div class="flex flex-col">
                          <label for="empresa" class="text-sm font-medium text-[#304269] mb-2 pl-2">Empresa o startup</label>
                          <input type="text" id="empresa" class="w-full bg-white rounded-xl px-6 py-4 text-base text-[#304269] focus:outline-none focus:ring-2 focus:ring-[#F26101] transition-all shadow-sm" placeholder="Ej. MouseLab" required>
                      </div>
                      <div class="flex flex-col">
                          <label for="email" class="text-sm font-medium text-[#304269] mb-2 pl-2">Correo corporativo</label>
                          <input type="email" id="email" class="w-full bg-white rounded-xl px-6 py-4 text-base text-[#304269] focus:outline-none focus:ring-2 focus:ring-[#F26101] transition-all shadow-sm" placeholder="ejemplo@empresa.com" required>
                      </div>
                  </div>
  
                  <div class="flex flex-col mt-8">
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
                  <div class="pt-12 text-center">
                      <a href="https://wa.me/573013970002" target="_blank" class="inline-block bg-[#25D366] text-white text-base font-bold px-12 py-5 rounded-full hover:bg-[#128C7E] transition-colors duration-500 shadow-xl hover:shadow-2xl">
                        <i class="fab fa-whatsapp text-xl mr-2 align-middle"></i> Ponte en contacto
                    </a>
                  </div>"""

content = re.sub(form_old, form_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated form design.")
