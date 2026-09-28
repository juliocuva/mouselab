import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero to include the floating image on the right
hero_pattern = re.compile(r'(<div class="relative z-10 max-w-\[90%\] mx-auto w-full">)\s*(<!-- Text Content Card -->\s*<div class="bg-\[#F9F9F8\]/95.*?(?:</div>\s*){2})', re.DOTALL)

def hero_replacement(m):
    return """<div class="relative z-10 max-w-[90%] mx-auto w-full grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
            <!-- Text Content Card -->
            <div class="lg:col-span-5 lg:col-start-1">
                <div class="bg-[#F9F9F8]/95 backdrop-blur-xl p-10 md:p-16 rounded-[2.5rem] shadow-[0_20px_60px_-15px_rgba(0,0,0,0.3)] w-full" data-aos="fade-right" data-aos-duration="1200">
                    <div class="flex items-center gap-4 mb-8">
                        <div class="h-px w-12 bg-yellow-500"></div>
                        <span class="text-[9px] uppercase tracking-[0.3em] font-bold text-gray-400">Estrategia & Construcción de Marca</span>
                    </div>
                    <h1 class="text-6xl md:text-8xl font-light text-[#111] leading-[0.9] tracking-tighter mb-8">
                        Ingeniería<br>
                        <span class="font-black">Visual</span> <span class="font-light italic">&</span><br>
                        <span class="font-black">Retail<span class="text-yellow-500">.</span></span>
                    </h1>
                    <p class="text-lg text-gray-500 font-light leading-relaxed mb-12">
                        Traducimos la identidad corporativa en entornos físicos de alto impacto. 50 años liderando la adecuación comercial a escala nacional.
                    </p>
                    <a href="#estudio" class="group flex items-center gap-6 w-fit">
                        <span class="text-[10px] font-bold uppercase tracking-widest text-[#111] group-hover:text-yellow-500 transition-colors">Explorar el trabajo</span>
                        <div class="w-12 h-px bg-[#111] group-hover:w-24 group-hover:bg-yellow-500 transition-all duration-500"></div>
                    </a>
                </div>
            </div>
            
            <!-- Restored Floating Image -->
            <div class="lg:col-span-7 hidden lg:flex justify-end" data-aos="fade-left" data-aos-duration="1500" data-aos-delay="300">
                <div class="relative w-full max-w-lg">
                    <img src="img/premium_float.jpg" alt="Detalle Banco Popular" class="rounded-[2.5rem] shadow-2xl w-full object-cover aspect-[4/3] border-4 border-white/20">
                </div>
            </div>"""

new_content = hero_pattern.sub(hero_replacement, content, count=1)

# 2. Change Solidez image
new_content = new_content.replace('src="img/premium_float.jpg" alt="Detalle operativo"', 'src="img/premium_solidez.jpg" alt="Detalle operativo"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Hero to grid + restored float, and updated Solidez image.")
