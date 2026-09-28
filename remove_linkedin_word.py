import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_linkedin = r"""<p><span class="font-bold text-\[#0077B5\]"><i class="fab fa-linkedin mr-2"></i>LinkedIn:</span> <a href="https://www.linkedin.com/in/julio-cesar-uva-ram%C3%ADrez/" target="_blank" class="font-light hover:text-\[#F26101\] transition-colors">Julio César Uva Ramírez</a></p>"""
new_linkedin = r"""<p><a href="https://www.linkedin.com/in/julio-cesar-uva-ram%C3%ADrez/" target="_blank" class="font-light hover:text-[#F26101] transition-colors"><i class="fab fa-linkedin mr-2 text-[#0077B5] text-lg"></i>Julio César Uva Ramírez</a></p>"""

content = re.sub(old_linkedin, new_linkedin, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed LinkedIn word.")
