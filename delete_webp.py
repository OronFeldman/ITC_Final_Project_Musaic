import os

# Set the directory path and file extension you want to delete
DIRECTORY_PATH = 'C:/Users/solom/OneDrive/Desktop/Data Science ITC/Data Science OCT-23/Final Project/pythonProject/scraped_images_test'
EXTENSION_TO_DELETE = '.webp'

def delete_files_with_extension(directory, extension):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                os.remove(os.path.join(subdir, file))
                print(f"Deleted {file} from {subdir}")

# Call the function with your directory path and file extension
delete_files_with_extension(DIRECTORY_PATH, EXTENSION_TO_DELETE)
