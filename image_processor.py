# image_processor.py

from PIL import Image
import numpy as np


def load_and_prepare_image(file_path, target_size=(32, 32)):
    img = Image.open(file_path)
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
