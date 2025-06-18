import os

import pyheif
from PIL import Image

input_folder = "/home/stefano/Scrivania/heic_input"
output_folder = "/home/stefano/Scrivania/jpeg_output"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".heic"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.rsplit(".", 1)[0] + ".jpg")

        print(f"Converting: {filename}")
        heif_file = pyheif.read(input_path)
        image = Image.frombytes(
            heif_file.mode, heif_file.size, heif_file.data,
            "raw", heif_file.mode
        )
        image.save(output_path, "JPEG", quality=95)

print("✅ Conversione completata.")


# https://heic.digital/