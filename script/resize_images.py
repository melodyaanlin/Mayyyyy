from PIL import Image
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "traveltarget")
SRC_DIR = os.path.join(BASE_DIR, "pic", "source")
OUT_DIR = os.path.join(BASE_DIR, "pic", "thumbnail")
TARGET_W, TARGET_H = 800, 450
MAX_KB = 200
QUALITY_START = 85
QUALITY_MIN = 40
QUALITY_STEP = 5

os.makedirs(OUT_DIR, exist_ok=True)

for name in sorted(os.listdir(SRC_DIR)):
    if not name.lower().endswith((".jpg", ".jpeg")):
        continue
    src_path = os.path.join(SRC_DIR, name)
    out_path = os.path.join(OUT_DIR, name)

    img = Image.open(src_path)
    if img.mode == "RGBA":
        img = img.convert("RGB")
    img.thumbnail((TARGET_W, TARGET_H), Image.LANCZOS)

    quality = QUALITY_START
    img.save(out_path, "JPEG", quality=quality, optimize=True)

    while os.path.getsize(out_path) > MAX_KB * 1024 and quality > QUALITY_MIN:
        quality -= QUALITY_STEP
        img.save(out_path, "JPEG", quality=quality, optimize=True)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"  {name}: {img.size[0]}x{img.size[1]}, q={quality}, {size_kb:.0f}KB")

print(f"\nDone -> {OUT_DIR}/")
