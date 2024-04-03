from PIL import Image
import os


def resize_images(images, output_directory, target_width, target_height):
    """
    receives a list of PIL images and create a new folder with resized images
    """
    for i, image in enumerate(images):
        resized_image = image.resize((target_width, target_height), Image.BICUBIC)
        output_filename = f"{str(i)}_resized.jpg"
        output_path = os.path.join(output_directory, output_filename)
        resized_image.save(output_path)
