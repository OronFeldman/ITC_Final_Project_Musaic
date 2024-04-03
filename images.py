from PIL import Image
import os


def load_images_in_directory(directory_path):
    """
    returns a list of PIL images from a directory
    """
    all_files = os.listdir(directory_path)

    # Filter for image files (you can customize the list of valid extensions)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [file for file in all_files if any(file.lower().endswith(ext) for ext in image_extensions)]

    # Load each image using Pillow and return a list of Image objects
    images = [Image.open(os.path.join(directory_path, file)) for file in image_files]
    return images


def resize_images(images, output_directory, target_width, target_height):
    """
    receives a list of PIL images and create a new folder with resized images
    """
    for i, image in enumerate(images):
        resized_image = image.resize((target_width, target_height), Image.BICUBIC)
        output_filename = f"{str(i)}_resized.jpg"
        output_path = os.path.join(output_directory, output_filename)
        resized_image.save(output_path)


