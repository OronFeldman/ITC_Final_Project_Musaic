from colors import *
from images import *

current_directory = os.getcwd()
resize_images(load_images_in_directory("colors_covers"), "resized_images", 51, 51)

covers = load_images_in_directory('resized_images')
image = Image.open("chien.png")
colors = image.getcolors()
images_by_color = get_images_by_colors(covers, colors, 70)
print(images_by_color)
images = get_images_by_pixel(images_by_color, image, colors)
combine_images(images, image, current_directory + "/output.png")
