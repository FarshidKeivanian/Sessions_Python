# pip install numpy matplotlib tensorflow scikit-learn opencv-python

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import os
import cv2

# Load and preprocess the dataset
def load_images(data_dirs):
    images = []
    labels = []
    for label, data_dir in data_dirs.items():
        for img_name in os.listdir(data_dir):
            img_path = os.path.join(data_dir, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (128, 128))
            images.append(img)
            labels.append(label)
    images = np.array(images)
    labels = np.array(labels)
    return images, labels

# Encode labels
def encode_labels(labels):
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    labels = le.fit_transform(labels)
    return labels, le

# Define paths for training and testing datasets
train_data_dirs = {
    'glioma': 'D:/brain_tumor/Training/glioma',
    'meningioma': 'D:/brain_tumor/Training/meningioma',
    'notumor': 'D:/brain_tumor/Training/notumor',
    'pituitary': 'D:/brain_tumor/Training/pituitary'
}

test_data_dirs = {
    'glioma': 'D:/brain_tumor/Testing/glioma',
    'meningioma': 'D:/brain_tumor/Testing/meningioma',
    'notumor': 'D:/brain_tumor/Testing/notumor',
    'pituitary': 'D:/brain_tumor/Testing/pituitary'
}

# Load training and testing datasets
train_images, train_labels = load_images(train_data_dirs)
test_images, test_labels = load_images(test_data_dirs)

# Encode labels
train_labels, label_encoder = encode_labels(train_labels)
test_labels = label_encoder.transform(test_labels)

# Normalize images
train_images = train_images / 255.0
train_images = np.expand_dims(train_images, axis=-1)
test_images = test_images / 255.0
test_images = np.expand_dims(test_images, axis=-1)

# Data augmentation
train_datagen = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
                                   width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
                                   horizontal_flip=True, fill_mode="nearest")
train_generator = train_datagen.flow(train_images, train_labels, batch_size=32)

# Build the CNN model with regularization
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    
    Conv2D(64, (3, 3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    
    Conv2D(128, (3, 3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(4, activation='softmax')  # 4 classes with softmax activation
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(train_generator, epochs=10, validation_data=(test_images, test_labels))

# Evaluate the model
loss, accuracy = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {accuracy}')

# Plot training & validation accuracy/loss values
def plot_history(history):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

plot_history(history)

# Prediction and visualization
def predict_and_visualize(model, images, labels, index):
    img = images[index]
    true_label = labels[index]
    prediction = model.predict(np.expand_dims(img, axis=0))
    predicted_class = np.argmax(prediction, axis=1)[0]
    class_names = label_encoder.inverse_transform([predicted_class])
    true_class_name = label_encoder.inverse_transform([true_label])
    plt.imshow(img.squeeze(), cmap='gray')
    plt.title(f'True: {true_class_name[0]}, Predicted: {class_names[0]}')
    plt.show()

# Predict and visualize a random image from the test set
import random
random_index = random.randint(0, len(test_images) - 1)
predict_and_visualize(model, test_images, test_labels, random_index)
