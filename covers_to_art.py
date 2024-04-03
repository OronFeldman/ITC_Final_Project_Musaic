from colors import *
from images import *

image_target =
threshold = 70

current_directory = os.getcwd()
resize_images(load_images_in_directory("colors_covers"), "resized_images", 102, 102)

covers = load_images_in_directory('resized_images')
image = Image.open(image_target)
colors = image.getcolors()
images_by_color = get_images_by_colors(covers, colors, threshold)
images = get_images_by_pixel(images_by_color, image, colors)
combined_image = combine_images(images, image)
combined_image.save(current_directory + "/output_" + image_target)
