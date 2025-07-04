import os
from PIL import Image
input_folder = "input_images"
output_folder = "output_images"
resize_width = 800
resize_height = 600
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"Input folder '{input_folder}' created. Please add some images and re-run the script.")
    exit()
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img_resized = img.resize((resize_width, resize_height))
            
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.png")
            img_resized.save(output_path)

            print(f"Processed: {filename} → {output_path}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")


