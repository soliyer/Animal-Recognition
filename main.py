# main.py

from model_loader import load_trained_model
from image_processor import load_and_prepare_image
from predictor import make_prediction

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


def get_prediction(image_path):
    model = load_trained_model('animal_recognition_model.h5')
    processed_image = load_and_prepare_image(image_path)
    predicted_index = make_prediction(model, processed_image)
    return class_names[predicted_index]
