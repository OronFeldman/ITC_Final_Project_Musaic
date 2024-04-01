import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt


def adjust_brightness(image_df, factor_array):
    adjusted_images = np.empty((0, image_df.shape[1] - 2), dtype=float)
    album_names = []
    targets_list = []
    for ind1, factor in enumerate(factor_array):
        for ind2 in range(len(image_df['album_name'])):
            album_names.append(image_df.loc[ind2, 'album_name'])
            targets_list.append(image_df.loc[ind2, 'target'])
            image = np.array(image_df.iloc[ind2, 2:].astype(float))
            adjusted_image = image * factor
            adjusted_image = np.clip(adjusted_image, 0, 255)
            adjusted_images = np.concatenate((adjusted_images, adjusted_image.reshape(1, image_df.shape[1] - 2)), axis=0)
    image_detail_df = pd.DataFrame({'album_name': album_names, 'target': targets_list})
    adjusted_df = pd.DataFrame(adjusted_images, columns=image_df.columns[2:])
    adjusted_images_df = pd.concat([image_detail_df, adjusted_df], axis=1)
    return adjusted_images_df


def change_perspective(image_df, angle_array):
    adjusted_images = np.empty((0, image_df.shape[1] - 2), dtype=float)
    album_names = []
    targets_list = []
    for ind1, angle in enumerate(angle_array):
        for ind2 in range(len(image_df['target'])):
            album_names.append(image_df.loc[ind2, 'album_name'])
            targets_list.append(image_df.loc[ind2, 'target'])
            image = np.array(image_df.iloc[ind2, 2:].astype(float)).reshape((31, 31))
            M = cv2.getRotationMatrix2D((31 / 2, 31 / 2), angle, 1)
            adjusted_image = cv2.warpAffine(image, M, (31, 31)).reshape(-1)
            adjusted_images = np.concatenate((adjusted_images, adjusted_image.reshape(1, image_df.shape[1] - 2)), axis=0)
    image_detail_df = pd.DataFrame({'album_name': album_names, 'target': targets_list})
    adjusted_df = pd.DataFrame(adjusted_images, columns=image_df.columns[2:])
    adjusted_images_df = pd.concat([image_detail_df, adjusted_df], axis=1)
    return adjusted_images_df


def image_plot(df):
    for ind in range(df.shape[0]):
        album_name = df.loc[ind, 'album_name']
        image = df.iloc[ind, 2:].values.astype(float).reshape((31, 31))
        fig = plt.figure()
        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.title(f'Image: {ind + 1} (Album name: {album_name})')
        plt.show()


def main():
    factor_array = np.arange(0.6, 1.6, 0.2)
    angle_array = np.arange(0, 6, 1.25)
    image_df = pd.read_csv('images.csv')
    adjusted_images_df = adjust_brightness(image_df, factor_array)
    adjusted_images_df = change_perspective(adjusted_images_df, angle_array)
    image_plot(adjusted_images_df)
    adjusted_images_df = adjusted_images_df.sample(frac=1, random_state=42)
    adjusted_images_df.to_csv('adjusted_images.csv', index=False)


if __name__ == '__main__':
    main()
