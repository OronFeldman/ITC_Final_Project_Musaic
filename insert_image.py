import cv2


def insert_image_func(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (299, 299))
    img = img / 255
    img_to_inference = img.reshape((1,) + img.shape)
    return img_to_inference
