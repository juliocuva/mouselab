import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to extract the 4 cards
# They are inside <div class="lg:col-span-8"> ... <div class="grid ..."> (Cards) </div> </div>
cards_pattern = re.compile(r'(<!-- Card 1 -->.*?)(<!-- Card 2 -->.*?)(<!-- Card 3 -->.*?)(<!-- Card 4 -->.*?</div>)\s*</div>\s*</div>\s*</div>\s*</section>', re.DOTALL)
match = cards_pattern.search(content)

if match:
    card1 = match.group(1)
    card2 = match.group(2)
    card3 = match.group(3)
    card4 = match.group(4)
    
    # We replace the entire section
    section_pattern = re.compile(r'<section id="divisiones" class="py-32 bg-\[#F9F9F8\]">.*?</section>', re.DOTALL)
    
    new_section = f"""<section id="divisiones" class="py-32 bg-[#F9F9F8]">
        <div class="max-w-[90%] mx-auto">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16 lg:pl-16 xl:pl-24 items-start">
                
                <!-- Columna Izquierda -->
                <div class="flex flex-col gap-12 md:gap-16">
                    <div data-aos="fade-right" class="mb-4">
                        <h2 class="text-5xl md:text-6xl font-black tracking-tighter text-[#111] mb-6">Divisiones<span class="yellow-dot"></span></h2>
                        <p class="text-lg text-gray-500 font-light leading-relaxed max-w-sm">Desarrollamos entornos que comunican y venden, integrando diseño, manufactura y montaje a gran escala.</p>
                    </div>
                    {card1}
                    {card3}
                </div>

                <!-- Columna Derecha -->
                <div class="flex flex-col gap-12 md:gap-16 lg:pt-48">
                    {card2}
                    {card4}
                </div>
            </div>
        </div>
    </section>"""
    
    new_content = section_pattern.sub(new_section, content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated Divisiones to 2-column masonry layout.")
else:
    print("Could not match cards.")
