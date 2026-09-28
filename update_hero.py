import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_hero = """    <!-- 1. Hero Section (Card over Background) -->
    <section class="relative min-h-screen flex items-center pt-24 pb-12 overflow-hidden">
        <!-- Background Image -->
        <div class="absolute inset-0 z-0">
            <img src="img/premium_hero.jpg" alt="Arquitectura Corporativa" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-black/10"></div> <!-- Subtle overlay -->
        </div>

        <div class="relative z-10 max-w-[90%] mx-auto w-full">
            <!-- Text Content Card -->
            <div class="bg-[#F9F9F8]/95 backdrop-blur-xl p-10 md:p-16 rounded-[2.5rem] shadow-[0_20px_60px_-15px_rgba(0,0,0,0.3)] max-w-2xl lg:ml-8" data-aos="fade-right" data-aos-duration="1200">
                <div class="flex items-center gap-4 mb-8">
                    <div class="h-px w-12 bg-yellow-500"></div>
                    <span class="text-[9px] uppercase tracking-[0.3em] font-bold text-gray-400">Estrategia & Construcción de Marca</span>
                </div>
                <h1 class="text-6xl md:text-8xl font-light text-[#111] leading-[0.9] tracking-tighter mb-8">
                    Ingeniería<br>
                    <span class="font-black">Visual</span> <span class="font-light italic">&</span><br>
                    <span class="font-black">Retail<span class="text-yellow-500">.</span></span>
                </h1>
                <p class="text-lg text-gray-500 font-light leading-relaxed max-w-sm mb-12">
                    Traducimos la identidad corporativa en entornos físicos de alto impacto. 50 años liderando la adecuación comercial a escala nacional.
                </p>
                <a href="#estudio" class="group flex items-center gap-6 w-fit">
                    <span class="text-[10px] font-bold uppercase tracking-widest text-[#111] group-hover:text-yellow-500 transition-colors">Explorar el trabajo</span>
                    <div class="w-12 h-px bg-[#111] group-hover:w-24 group-hover:bg-yellow-500 transition-all duration-500"></div>
                </a>
            </div>
        </div>
    </section>"""

# Find the hero section. It starts with <!-- 1. Hero Section --> and ends before <!-- 1.5. Trusted By --> or <!-- 2. The Studio
pattern = re.compile(r'\s*<!-- 1\. Hero Section .*?-->.*?<section.*?</section>', re.DOTALL)
content = pattern.sub('\n' + new_hero, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero section updated to Card layout.")
