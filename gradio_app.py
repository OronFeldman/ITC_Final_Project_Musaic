import gradio as gr
from tabulate import tabulate
import csv
import os
from PIL import Image


def get_album_name_by_number(number):
    folder_path = "images"
    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        # Check if the filename matches the pattern "number_album_name.jpg"
        if filename.startswith(f"{number}_") and filename.endswith(".jpg"):
            # Extract album name from filename
            album_name = filename.split("_", 1)[1].split(".")[0]
            return album_name
    return None


def get_album_info(album_name):
    """
    Retrieve album information based on the provided album name.
    """

    csv_file = "albums_database.csv"
    album_info = {}
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['name'] == album_name:
                album_info['Album name'] = row['name']
                album_info['Artist name'] = row['artist_name']
                album_info['Artist genres'] = row['artist_genres']
                album_info['Release date'] = row['release_date']
                album_info['Total tracks'] = int(row['total_tracks'])
                album_info['Popularity'] = int(row['popularity'])
                break

    return album_info


def get_info_table(number):
    """
    Generate a tabulated representation of album information.
    """
    number = 88
    album_name = get_album_name_by_number(number)
    album_info = get_album_info(album_name)

    info_list = [
        ("Name", album_info.get("name", "")),
        ("Artist Name", album_info.get("artist_name", "")),
        ("Artist Genres", album_info.get("artist_genres", "")),
        ("Release Date", album_info.get("release_date", "")),
        ("Total Tracks", album_info.get("total_tracks", "")),
        ("Popularity", album_info.get("popularity", ""))
    ]
    table = tabulate(info_list, headers=["Attribute", "Value"], tablefmt="grid")
    return table


def get_dictionary_contents(album_image):
    # Assuming image_file is provided as input
    image_file = '88_"Awaken, My Love!".jpg'
    number = 88
    album_name = get_album_name_by_number(number)
    dictionary = get_album_info(album_name)
    contents_str = ""
    for key, value in dictionary.items():
        contents_str += f"{key}: {value}\n\n"

    image_pil = Image.open(image_file)
    return image_pil, contents_str


outputs = [
    gr.Image(label="Album Image"),
    gr.Textbox(label="Album Information")
]

demo = gr.Interface(fn=get_dictionary_contents, inputs="image", outputs=outputs, title="Album Detector",
                    description="Upload a vinyl/cd picture to detect the album and print some info about it.")
demo.launch()
