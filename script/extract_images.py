import re
import base64
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "traveltarget")
INPUT_FILE = os.path.join(BASE_DIR, "index.html")
OUTPUT_FILE = os.path.join(BASE_DIR, "index_clean.html")
PIC_DIR = os.path.join(BASE_DIR, "pic")

os.makedirs(PIC_DIR, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read()

counter = 0
ext_map = {
    "image/jpeg": "jpg",
    "image/png": "png",
    "image/gif": "gif",
    "image/webp": "webp",
    "image/svg+xml": "svg",
}

def replace_base64(match):
    global counter
    mime = match.group(1)
    b64data = match.group(2)
    ext = ext_map.get(mime, "bin")
    counter += 1
    filename = f"img_{counter:03d}.{ext}"
    filepath = os.path.join(PIC_DIR, filename)
    with open(filepath, "wb") as img_f:
        img_f.write(base64.b64decode(b64data))
    print(f"  [{counter}] {filepath} ({mime})")
    return f"'pic/{filename}'"

pattern = r"'data:(image/[^;]+);base64,([A-Za-z0-9+/=\s]+)'"

new_content = re.sub(pattern, replace_base64, content)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"\nDone: {counter} images -> {PIC_DIR}/")
print(f"Output: {OUTPUT_FILE}")
