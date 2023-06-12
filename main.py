from PIL import Image
import os

def convert_to_webp(input_path, output_folder):
    image_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_folder, f"{image_name}.webp")
    
    image = Image.open(input_path)
    image.save(output_path, "WebP")

def convert_folder_images_to_webp(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        if os.path.isfile(input_path):
            convert_to_webp(input_path, output_folder)

# Example usage
input_folder = "before"
output_folder = "after"

convert_folder_images_to_webp(input_folder, output_folder)
