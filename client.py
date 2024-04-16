import requests
import json


IND = 0


def ask_inference(img, classes_dict, names_dict, url, album_df):
    files = {
        'image': ('image.bin', img.tobytes(), 'application/octet-stream'),
        'classes_dict': ('classes_dict.json', json.dumps(classes_dict), 'application/json'),
        'names_dict': ('names_dict.json', json.dumps(names_dict), 'application/json')
    }

    inferenced_album = requests.post(url, files=files).text
    artist_name = album_df.loc[album_df['name'] == inferenced_album, 'artist_name'].values[IND]
    release_date = album_df.loc[album_df['name'] == inferenced_album, 'release_date'].values[IND]
    total_tracks = album_df.loc[album_df['name'] == inferenced_album, 'total_tracks'].values[IND]
    album_type = album_df.loc[album_df['name'] == inferenced_album, 'album_type'].values[IND]
    artist_genres = album_df.loc[album_df['name'] == inferenced_album, 'artist_genres'].values[IND]
    print(f'The album name is: {inferenced_album}\nArtist name: {artist_name}\nRelease date: {release_date}')
    print(f'Number of tracks: {total_tracks}\nAlbum type: {album_type}\nArtist genre: {artist_genres}')
