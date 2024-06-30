import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Load and preprocess images
def load_and_preprocess_image(file_path):
    image = cv2.imread(file_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (100, 100))
    return resized_image

# Create a simple model
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(100, 100)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# GUI for image uploading and result display
root = Tk()
root.title("Image Upload, Training and Testing")

selected_images = []
model = None

def upload_images():
    file_paths = filedialog.askopenfilenames(title="Select images", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    for file_path in file_paths:
        img = load_and_preprocess_image(file_path)
        selected_images.append(img)
    result_text.set(f"{len(file_paths)} images uploaded.")

def on_train():
    global model
    if selected_images:
        images = np.array(selected_images)
        train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)
        labels = np.ones(len(train_images))  # Assuming all images are positive cases
        test_labels = np.ones(len(test_images))

        model = create_model()
        model.fit(train_images, labels, epochs=10)
        results = model.evaluate(test_images, test_labels)
        result_text.set(f"Model trained.\nAccuracy on Test Data: {results[1]*100:.2f}%")
        test_btn.config(state=NORMAL)

def upload_test_image():
    file_path = filedialog.askopenfilename(title="Select test image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    if file_path:
        test_image = load_and_preprocess_image(file_path)
        test_image = np.expand_dims(test_image, axis=0) / 255.0  # Normalize the image
        prediction = model.predict(test_image)
        if prediction[0] > 0.5:
            result_text.set("Prediction: Farshid")
        else:
            result_text.set("Prediction: Not Farshid")

# Result display
result_text = StringVar()
result_label = Label(root, textvariable=result_text, height=4)
result_label.pack()

# Upload button
upload_btn = Button(root, text="Upload Images", command=upload_images)
upload_btn.pack()

# Train button
train_btn = Button(root, text="Train Model", command=on_train)
train_btn.pack()

# Test button
test_btn = Button(root, text="Test Model", command=upload_test_image, state=DISABLED)
test_btn.pack()

root.mainloop()
