import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Form Padding on Mobile (p-12 to p-6)
content = content.replace(
    '<form action="#" method="POST" class="space-y-8 bg-[#D9E8F5] p-12 md:p-20 rounded-[3rem]',
    '<form action="#" method="POST" class="space-y-8 bg-[#D9E8F5] p-6 md:p-20 rounded-[3rem]'
)

# 2. Add Mobile Menu
# We will inject a hamburger button next to the nav, and a mobile menu div right after the header closing tag.
# We also need a tiny JS script to toggle it.

nav_old = r"""<div class="max-w-\[90%\] mx-auto flex justify-between items-center">
            <div class="flex-shrink-0 flex items-center">
                <img src="img/mouselab.png" alt="MouseLab.dev" class="h-8 object-contain filter brightness-0 invert opacity-90">
            </div>
            <nav class="hidden md:flex space-x-12 items-center">"""

nav_new = r"""<div class="max-w-[90%] mx-auto flex justify-between items-center">
            <div class="flex-shrink-0 flex items-center">
                <img src="img/mouselab.png" alt="MouseLab.dev" class="h-8 object-contain filter brightness-0 invert opacity-90">
            </div>
            
            <!-- Desktop Nav -->
            <nav class="hidden md:flex space-x-12 items-center">"""

content = re.sub(nav_old, nav_new, content)

# Now inject the hamburger button and mobile menu
header_end = r"""</header>"""
mobile_menu = r"""    <!-- Mobile Menu Button (Only visible on small screens) -->
            <button id="mobile-menu-btn" class="md:hidden text-white focus:outline-none">
                <i class="fas fa-bars text-2xl"></i>
            </button>
        </div>
        
        <!-- Mobile Dropdown -->
        <div id="mobile-menu" class="hidden md:hidden absolute top-full left-0 w-full bg-[#304269] shadow-lg border-t border-white/10 flex flex-col p-6 space-y-6">
            <a href="#estudio" class="text-sm uppercase tracking-[0.15em] font-medium text-white hover:text-[#F26101]">El Lab</a>
            <a href="#divisiones" class="text-sm uppercase tracking-[0.15em] font-medium text-white hover:text-[#F26101]">Plataformas</a>
            <a href="#infraestructura" class="text-sm uppercase tracking-[0.15em] font-medium text-white hover:text-[#F26101]">Stack Tecnológico</a>
            <a href="#contacto" class="text-sm uppercase tracking-[0.15em] font-bold border border-[#F26101] text-[#F26101] px-6 py-3 rounded-full text-center hover:bg-[#F26101] hover:text-white transition-colors duration-500">Contacto</a>
        </div>
    </header>"""

content = content.replace(r"""</nav>
        </div>
    </header>""", r"""</nav>""" + mobile_menu)

# Add the JS logic at the bottom
script_old = r"""// Header sizing logic
        window.addEventListener('scroll', () => {"""
script_new = r"""// Mobile Menu Toggle
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');
        btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
        });
        
        // Header sizing logic
        window.addEventListener('scroll', () => {"""

content = content.replace(script_old, script_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied responsive fixes.")
