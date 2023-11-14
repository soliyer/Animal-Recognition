# predictor.py

import numpy as np


def make_prediction(model, processed_image):
    prediction = model.predict(processed_image)
    return np.argmax(prediction[0])
