# pip install --upgrade pip
# pip install requests pillow
# pip install tensorflow opencv-python numpy scikit-learn matplotlib

import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from PIL import Image

# Paths to apple images on GitHub
low_quality_images = [
    "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/l.apple1.png",
    "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/l.apple2.png",
    "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/l.apple3.jpg"
]

high_quality_images = [
    "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/h.apple1.jpg",
    "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/h.apple2.jpg",
    "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/h.apple3.jpg"
]

images = []
labels = []

# Function to read images from URLs
def read_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    else:
        print(f"Failed to load image from URL: {url}")
        return None

# Load low quality images
for url in low_quality_images:
    img = read_image_from_url(url)
    if img is not None:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (128, 128))
        images.append(img)
        labels.append(1)

# Load high quality images
for url in high_quality_images:
    img = read_image_from_url(url)
    if img is not None:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (128, 128))
        images.append(img)
        labels.append(0)

if len(images) == 0:
    raise ValueError("No images found. Please check the image URLs and ensure they are accessible.")

images = np.array(images).reshape(-1, 128, 128, 1)
labels = np.array(labels)

train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

loss, accuracy = model.evaluate(test_images, test_labels)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Display results
plt.plot(history.history['accuracy'], label='Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

# Predict apple quality
def predict_quality(image_path):
    img = read_image_from_url(image_path)
    if img is None:
        return "Image not found"
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (128, 128))
    img = img.reshape(1, 128, 128, 1)
    prediction = model.predict(img)
    return "Good" if prediction < 0.5 else "Bad"

example_image_url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/h.apple1.jpg"
result = predict_quality(example_image_url)
print(f"The quality of the apple is: {result}")
