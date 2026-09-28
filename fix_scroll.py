import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Disable scroll listener
content = content.replace(
    """window.addEventListener('scroll', () => {
            const nav = document.getElementById('navbar');
            if (window.scrollY > 50) {
                nav.classList.remove('py-4');
                nav.classList.add('py-2');
            } else {
                nav.classList.add('py-4');
                nav.classList.remove('py-2');
            }
        });""",
    ""
)

# And if they meant "take the menu out of the fixed position so it scrolls away naturally":
# Let's remove 'fixed' from header and change it to 'absolute' so it stays at the very top but scrolls away.
# Actually "saca el menu del scroll" means "take it out of the scroll", which usually means "stop making it sticky/fixed when scrolling".
# If I make it absolute, it just stays at the top.
# Wait, if they just meant the shrinking animation, I already removed it above.
# Let's remove `fixed` and make it `absolute` just in case. Or `relative`? If I make it `absolute`, `pt-24` on hero still works perfectly.
content = content.replace(
    '<header class="fixed w-full z-[999] transition-all duration-500 py-4 bg-[#304269] text-white shadow-sm" id="navbar">',
    '<header class="absolute top-0 w-full z-[999] transition-all duration-500 py-4 bg-[#304269] text-white" id="navbar">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated scroll behavior.")
