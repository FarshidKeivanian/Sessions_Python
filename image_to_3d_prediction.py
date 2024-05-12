#pip install opencv-python
#pip install tensorflow
#pip install --upgrade tensorflow

import os
import cv2
import numpy as np
import tensorflow as tf
from tkinter import Tk, filedialog

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Set up the tkinter environment and hide the root window
root = Tk()
root.withdraw()

# Open file dialog to select an image
file_path = filedialog.askopenfilename()

# Read the image if a file was selected
if file_path:
    image = cv2.imread(file_path)
else:
    print("No file selected.")
    exit()  # Exit if no image is selected

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(None, None, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    # Add more layers as needed
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(3)  # Output with three dimensions
])

# Training configurations
model.compile(optimizer='adam', loss='mse')

# Assuming train_images and train_labels are the training data
# model.fit(train_images, train_labels, epochs=10)

# Predict the 3D image
predicted_3d = model.predict(gray_image.reshape(1, *gray_image.shape, 1))
# Code for displaying the 3D image (depends on your specific application)
