import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Marquee back to Client Logos
marquee_old = r"""<!-- 1.5. Trusted By (Tech Stack Marquee) -->
    <section class="py-16 bg-white border-y border-gray-100">
        <div class="max-w-\[90%\] mx-auto">
            <p class="text-\[10px\] uppercase tracking-\[0.3em\] text-gray-400 text-center mb-10 font-bold">Tecnologías que respaldan nuestro desarrollo</p>
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

marquee_new = r"""<!-- 1.5. Trusted By (Clients Marquee) -->
    <section class="py-16 bg-[#F9F9F8] border-y border-gray-100">
        <div class="max-w-[90%] mx-auto">
            <p class="text-[10px] uppercase tracking-[0.3em] text-[#304269] text-center mb-10 font-bold opacity-50">Marcas que respaldan nuestra ingeniería</p>
            <div class="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-70 grayscale hover:grayscale-0 transition-all duration-500">
                <img src="img/logo_bahia.png" alt="Bahía Guacamayas" class="h-10 object-contain brightness-0">
                <img src="img/logo_donmoiso.webp" alt="Don Moiso" class="h-12 object-contain brightness-0">
                <img src="img/logo_axisone.png" alt="AxisONE Coffee" class="h-10 object-contain brightness-0">
                <img src="img/logo_sc.png" alt="Sagrado Corazón" class="h-12 object-contain brightness-0">
            </div>
        </div>
    </section>"""

content = re.sub(marquee_old, marquee_new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated marquee with client logos.")
