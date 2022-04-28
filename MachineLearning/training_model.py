import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

dir = "ocr_training_data/"
for folder in os.listdir(dir):
    if folder != ".DS_Store":
        dir += (folder + "/")
        for images in os.listdir(dir):
            print(folder,images)
    dir = "ocr_training_data/"
