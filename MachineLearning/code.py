import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf


import tensorflow.contrib.keras as keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

data_dir = "./ocr_training_data"

print(len(data_dir))