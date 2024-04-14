import argparse
import json
from inference import inference_func
from insert_image import insert_image_func

with open('musaic_conf.json', 'r') as file:
    config = json.load(file)

HELP_METHODS = config.get("help_methods")
HELP_ARGS = config.get("help_args")
CLASSES_DICT = config.get("classes_dict")
NAMES_DICT = config.get("names_dict")

with open('README.md', 'r') as file:
    APP_DESCRIPTION = file.read()


def main():
    parser = argparse.ArgumentParser(description=APP_DESCRIPTION)
    parser.add_argument("method", help=HELP_METHODS,
                        choices=['inference', 'mosaic'])
    parser.add_argument("args", nargs='*', help=HELP_ARGS)
    args = parser.parse_args()

    if args.method == 'inference':
        try:
            img = insert_image_func(*args.args)
            inference_func(img, CLASSES_DICT, NAMES_DICT)
        except TypeError as e:
            print(f'Error calling {args.method}: {e}\n Image path or array are required.')
    else:
        print(f'Method {args.method} not found.')
