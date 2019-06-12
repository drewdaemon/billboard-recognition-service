import numpy as np
import cv2

from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import tensorflow as tf
import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

print(tf.__version__, keras.__version__)

class FeatureExtractor:

    def __init__(self):
        self.model = VGG16(weights='imagenet', include_top=False)

    def extract_features(self, img):
        img_data = cv2.resize(img, (224, 224))
        # drop alpha channel
        if img_data.shape[2] == 4:
            img_data = np.delete(img_data, 3, axis=2)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)
        features = self.model.predict(img_data, verbose=1)
        return features.ravel()
