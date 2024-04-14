import math
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from images import *
import random


def euclidean_distance(color1, color2):
    """
    returns the Euclidean distance between two colors
    """
    # Extract RGB components
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    # Calculate Euclidean distance
    distance = math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

    return distance


def get_dominant_color(image, k=1):
    """
    Return the most dominant color(s) of an image.
    """
    # Convert the image to a NumPy array
    image_array = np.array(image)
    # Flatten the array to 1D
    flattened_array = image_array.reshape((-1, 3))
    # Use k-means clustering to find dominant color
    kmeans = KMeans(n_clusters=k, n_init=10)  # Set n_init to suppress the warning
    kmeans.fit(flattened_array)
    # Get the RGB values of the dominant color(s)
    dominant_colors = kmeans.cluster_centers_.astype(int)

    dominant_color = tuple(dominant_colors[0]) if k == 1 else [tuple(color) for color in dominant_colors]
    return dominant_color


def show_color(color):
    # Create a small image with the specified color
    image_size = (100, 100, 3)  # Width, height, and 3 channels (RGB)
    color_image = np.full(image_size, color, dtype=np.uint8)
    # Display the image
    plt.imshow(color_image)
    plt.axis('off')  # Turn off axis labels
    plt.show()


def get_images_by_colors(images, colors, threshold):
    """
    returns a lists of lists of PIL images, every list represent a color associated to object colors
    """
    images_by_colors = [[] for _ in range(len(colors))]
    for image in images:
        color_index = -1
        min_dist = math.inf
        dominant_color = get_dominant_color(image)
        for i, color in enumerate(colors):
            color = color[1][:-1]
            curr_dist = euclidean_distance(dominant_color, color)
            if curr_dist < min_dist:
                min_dist = curr_dist
                color_index = i
        if min_dist < threshold:
            images_by_colors[color_index].append(image)
    return images_by_colors
