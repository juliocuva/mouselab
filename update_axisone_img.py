import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# AxisONE card is Card 3
axisone_pattern = re.compile(
    r'(<!-- Card 3 -->.*?<img src=")(.*?)(" alt=")(.*?)(" class="w-full h-full object-cover)', 
    re.DOTALL
)

def replace_axisone_img(match):
    return f'{match.group(1)}img/dashboard1.png{match.group(3)}AxisONE Dashboard{match.group(5)}'

content = axisone_pattern.sub(replace_axisone_img, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated AxisONE image.")
