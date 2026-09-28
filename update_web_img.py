import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Custom Web is Card 4
web_pattern = re.compile(
    r'(<!-- Card 4 -->.*?<img src=")(.*?)(" alt=")(.*?)(" class="w-full h-full object-cover)', 
    re.DOTALL
)

def replace_web_img(match):
    return f'{match.group(1)}img/bahia.png{match.group(3)}Custom Web Dev{match.group(5)}'

content = web_pattern.sub(replace_web_img, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Custom Web image.")
