import os
from PIL import Image

def convert_webp_to_jpg(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith(".webp"):
                image = Image.open(filepath).convert("RGB")
                jpg_path = filepath[:-5] + ".jpg"
                image.save(jpg_path, "JPEG")
                print(f"Converted {filepath} to {jpg_path}")

# Replace 'your_directory_path' with the path to the directory containing your folders of webp images
convert_webp_to_jpg('C:/Users/solom/OneDrive/Desktop/Data Science ITC/Data Science OCT-23/Final Project/pythonProject/scraped_images_test')