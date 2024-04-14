from PIL import Image
import os
import random


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
    Receives a list of PIL images and creates a new folder with resized images.
    """
    # Create the output directory if it does not exist
    os.makedirs(output_directory, exist_ok=True)

    for i, image in enumerate(images):
        resized_image = image.resize((target_width, target_height), Image.BICUBIC)
        output_filename = f"{str(i)}_resized.jpg"
        output_path = os.path.join(output_directory, output_filename)
        resized_image.save(output_path)


def get_images_by_pixel(images_by_color, target_image, target_colors):
    """
    returns a lists of PIL images, each image represents a pixel of the target_image
    """
    width, height = target_image.size
    target_colors = [color[1][:-1] for color in target_colors]
    images_by_pixel = []
    for y in range(height):
        for x in range(width):
            # Get the RGB color of the current pixel
            pixel_color = target_image.getpixel((x, y))[:-1]
            index = target_colors.index(pixel_color)
            images_by_pixel.append(random.choice(images_by_color[index]))
    return images_by_pixel


def combine_images(images_by_pixel, target_image):
    """
    returns the final image obtained with images_by_pixel
    """
    size = target_image.size
    # Ensure the size is valid
    if len(images_by_pixel) != size[0] * size[1]:
        raise ValueError("Number of images does not match the specified size.")

    # Get the size of each individual image (assuming all have the same size)
    image_width, image_height = images_by_pixel[0].size

    # Create a new image with the specified dimensions
    combined_image = Image.new('RGB', (image_width * size[1], image_height * size[0]))

    # Paste each image onto the new image
    for i in range(size[0]):
        for j in range(size[1]):
            index = i * size[1] + j
            combined_image.paste(images_by_pixel[index], (j * image_width, i * image_height))
    return combined_image
