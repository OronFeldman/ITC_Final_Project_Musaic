from colors import *
from images import *
import gradio as gr

image_target = ""
threshold = 70


def covers_to_art(folder, target_image, threshold=70):
    threshold = int(threshold)
    resize_images(load_images_in_directory(folder), "resized_images", 50, 50)
    covers = load_images_in_directory('resized_images')
    image = Image.open(target_image)
    colors = image.getcolors()
    images_by_color = get_images_by_colors(covers, colors, threshold)
    images = get_images_by_pixel(images_by_color, image, colors)
    combined_image = combine_images(images, image)
    return combined_image


demo = gr.Interface(fn=covers_to_art, inputs=["text", "text", "text"], outputs="image", title="Musaic art creator",
                    description="Upload a vinyl/cd picture to detect the album and print some info about it.")
demo.launch()
