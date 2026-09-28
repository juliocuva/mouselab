import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Header Logo (black on yellow)
header_text = r'<div class="text-2xl font-black tracking-tighter text-\[#111\]">mouse<span class="font-light">lab</span><span class="text-yellow-500">\.dev</span></div>'
header_img = r'<img src="img/mouselab.png" alt="MouseLab.dev" class="h-8 object-contain filter brightness-0 opacity-90">'
content = re.sub(header_text, header_img, content)

# Footer Logo (white on dark grey)
footer_text = r'<div class="text-3xl font-black tracking-tighter text-white mb-8">mouse<span class="font-light">lab</span><span class="text-yellow-500">\.dev</span></div>'
footer_img = r'<img src="img/mouselab.png" alt="MouseLab.dev" class="h-10 mb-8 object-contain filter brightness-0 invert opacity-90">'
content = re.sub(footer_text, footer_img, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated logos to image with correct filters.")
