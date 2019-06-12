from flask import Flask, request
application = Flask(__name__)

import shortuuid
import os
from imageio import imread
from manager.manager import ImageManager

import matplotlib.pyplot as plt

manager = ImageManager()

@application.route('/register', methods=['POST'])
def register():
    f = request.files['image']
    img = imread(f.read())
    return manager.register(img)

@application.route('/predict', methods=['POST'])
def predict():
    f = request.files['image']
    img = imread(f.read())
    return manager.predict(img)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
