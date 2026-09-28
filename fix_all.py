import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix divisiones (remove lg:pt-48)
content = content.replace('class="flex flex-col gap-12 md:gap-16 lg:pt-48"', 'class="flex flex-col gap-12 md:gap-16"')

# 2. Add map
pattern = re.compile(r'(<section id="contacto" class="py-32 bg-white">.*?<div class="max-w-4xl mx-auto px-6">.*?)(<form.*?</form>)(.*?)(</section>)', re.DOTALL)
match = pattern.search(content)

if match:
    form_html = match.group(2)
    
    new_section = f"""<section id="contacto" class="py-32 bg-white">
        <div class="max-w-[90%] mx-auto">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 md:gap-24 items-start">
                
                <!-- Left: Formulario -->
                <div data-aos="fade-right">
                    <div class="mb-12">
                        <span class="text-[9px] uppercase tracking-[0.3em] font-bold text-gray-400 block mb-4">Contacto</span>
                        <h2 class="text-4xl md:text-5xl md:text-6xl font-light tracking-tight text-[#111]">Iniciar <br><span class="font-black tracking-tighter">Proyecto</span><span class="text-yellow-500">.</span></h2>
                        <p class="text-gray-500 font-light text-base md:text-lg mt-6">Contáctenos para licitaciones corporativas y evaluación de ingeniería visual.</p>
                    </div>
                    
                    {form_html}
                </div>

                <!-- Right: Mapa -->
                <div class="w-full h-full min-h-[500px] md:min-h-[700px] rounded-[3rem] overflow-hidden shadow-[0_20px_60px_-15px_rgba(0,0,0,0.1)] relative" data-aos="fade-left">
                    <iframe 
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1m3!1d127255.11053457193!2d-74.1950453303666!3d4.648283717208168!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e3f9bfd2da6cb29%3A0x239d635520a33914!2sBogot%C3%A1%2C%20Colombia!5e0!3m2!1sen!2sus!4v1716300000000!5m2!1sen!2sus" 
                        width="100%" 
                        height="100%" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade"
                        class="absolute inset-0 grayscale hover:grayscale-0 transition-all duration-1000">
                    </iframe>
                </div>
            </div>
        </div>
    </section>"""
    
    new_content = pattern.sub(new_section, content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated Contact and Divisiones sections.")
else:
    print("Could not match.")
