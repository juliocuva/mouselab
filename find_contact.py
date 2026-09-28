import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('id="contacto"')
print(content[start-200:start+800])
