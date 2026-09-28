import os
from PIL import Image

img_dir = "img"

# Images to compress and convert to WebP
to_compress = [
    "bahia.png",
    "becoffee.png",
    "bemap.png",
    "mouselab_hero.jpg",
    "mouselab_flowchart.jpg",
    "dashboard1.png",
]

# Dead files to delete (not referenced in index.html)
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

dead_files = [
    "premium_float.jpg",
    "mouselab_flow.jpg",
    "premium_interior.jpg",
    "premium_retail.jpg",
    "premium_super.jpg",
    "premium_hero.jpg",
    "premium_solidez.jpg",
    "premium_banca.jpg",
    "logo-graficas.png",
    "WhatsApp Image 2026-08-30 at 9.42.32 AM.jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.35 AM (2).jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.33 AM (1).jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.34 AM (4).jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.34 AM (2).jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.35 AM.jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.34 AM.jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.33 AM.jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.32 AM (2).jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.34 AM (3).jpeg",
    "WhatsApp Image 2026-08-30 at 9.43.12 AM.jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.36 AM.jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.35 AM (1).jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.31 AM.jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.32 AM (1).jpeg",
    "WhatsApp Image 2026-08-30 at 9.42.34 AM (1).jpeg",
]

print("=== STEP 1: Compressing images to WebP ===")
for filename in to_compress:
    src = os.path.join(img_dir, filename)
    if not os.path.exists(src):
        print(f"  SKIP (not found): {filename}")
        continue
    
    base = os.path.splitext(filename)[0]
    dst = os.path.join(img_dir, base + ".webp")
    
    orig_size = os.path.getsize(src) / 1024
    
    img = Image.open(src).convert("RGB")
    # Resize if wider than 1920px
    if img.width > 1920:
        ratio = 1920 / img.width
        img = img.resize((1920, int(img.height * ratio)), Image.LANCZOS)
    
    img.save(dst, "WEBP", quality=82, method=6)
    new_size = os.path.getsize(dst) / 1024
    
    print(f"  {filename:<35} {orig_size:>8.1f} KB -> {new_size:>7.1f} KB  ({round((1-new_size/orig_size)*100)}% saved)")

print("\n=== STEP 2: Deleting dead files ===")
for filename in dead_files:
    path = os.path.join(img_dir, filename)
    if os.path.exists(path):
        size = os.path.getsize(path) / 1024
        os.remove(path)
        print(f"  DELETED: {filename} ({size:.1f} KB)")
    else:
        print(f"  SKIP (not found): {filename}")

print("\nDone!")
