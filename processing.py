import tensorflow as tf
import keras 
from keras.models import load_model
from keras.preprocessing.image import img_to_array
#import cv2
import numpy as np

def call_model():
    global model
    model = load_model('Final Model/model.h5')
    print("***Loading Model Now ...***")

    return model

def preprocess(image,target):
    print("***Processing Inputs...***")
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image,axis=0)

    return image
    