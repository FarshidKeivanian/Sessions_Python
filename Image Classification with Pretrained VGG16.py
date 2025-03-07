import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np
import cv2

# Load pre-trained VGG16 model
model = VGG16(weights="imagenet")

# Load an image for classification
image_path = "Dog.jpg"  # Replace with an actual image path
image = cv2.imread(image_path)
image = cv2.resize(image, (224, 224))
image = np.expand_dims(image, axis=0)
image = preprocess_input(image)

# Predict the image class
predictions = model.predict(image)
label = decode_predictions(predictions, top=3)[0]

# Print the top-3 predictions
for (class_id, label, score) in label:
    print(f"{label}: {score:.2f}")
