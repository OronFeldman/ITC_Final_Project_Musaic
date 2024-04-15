from tensorflow.keras.models import load_model
import numpy as np


def inference_func(img, classes_dict, names_dict):
    model = load_model(r'C:\Users\oronf\Documents\PythonProjects\FinalProjectDS\testing\InceptionResNetV2_model')
    predictions = model.predict(img)
    predicted_label = classes_dict[str(np.argmax(predictions, axis=1)[0])]
    album_name = names_dict[str(predicted_label)]
    print(f'The predicted label is: {predicted_label}')
    print(f'The album name is: {album_name}')
