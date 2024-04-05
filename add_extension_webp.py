import os

def add_extension_to_files(directory, extension):
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Get the full path of the file
            filepath = os.path.join(root, filename)
            # Check if the file has an extension already
            if '.' not in filename:
                # Rename the file with the new extension
                os.rename(filepath, filepath + extension)

# Example usage:
directory_path = 'C:/Users/solom/OneDrive/Desktop/Data Science ITC/Data Science OCT-23/Final Project/pythonProject/scraped_images_test'
file_extension = '.webp'  # Change this to the desired extension

add_extension_to_files(directory_path, file_extension)