import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Becoffee is Card 2
becoffee_pattern = re.compile(
    r'(<!-- Card 2 -->.*?<img src=")(.*?)(" alt=")(.*?)(" class="w-full h-full object-cover)', 
    re.DOTALL
)

def replace_becoffee_img(match):
    return f'{match.group(1)}img/becoffee.png{match.group(3)}Becoffee Dashboard{match.group(5)}'

content = becoffee_pattern.sub(replace_becoffee_img, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Becoffee image.")
