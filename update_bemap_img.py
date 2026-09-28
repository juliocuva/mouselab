import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# bemap is Card 1
bemap_pattern = re.compile(
    r'(<!-- Card 1 -->.*?<img src=")(.*?)(" alt=")(.*?)(" class="w-full h-full object-cover)', 
    re.DOTALL
)

def replace_bemap_img(match):
    return f'{match.group(1)}img/bemap.png{match.group(3)}bemap.pro{match.group(5)}'

content = bemap_pattern.sub(replace_bemap_img, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated bemap image.")
