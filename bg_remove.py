from PIL import Image
from rembg import remove
import os

input_path = input("Image path: ")
output_dir = input("Save to folder (leave blank for same folder): ").strip()

# Get file extension and base name
base = os.path.splitext(os.path.basename(input_path))[0]
ext = os.path.splitext(input_path)[1].lower()

# Set output directory
if output_dir:
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{base}_nobg{ext}")
else:
    output_path = os.path.join(os.path.dirname(input_path), f"{base}_nobg{ext}")

img = Image.open(input_path)
result = remove(img)

# Convert to RGB if saving as JPEG
if ext in ['.jpg', '.jpeg']:
    result = result.convert('RGB')

result.save(output_path)
print(f"Saved: {output_path}")

