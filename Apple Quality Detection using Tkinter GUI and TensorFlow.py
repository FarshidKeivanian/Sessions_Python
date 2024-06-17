# pip install --upgrade pip
# pip install requests pillow
# pip install tensorflow opencv-python numpy scikit-learn matplotlib
# pip install tk

import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class AppleQualityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apple Quality Detection")
        
        self.low_quality_files = []
        self.high_quality_files = []
        self.images = []
        self.labels = []
        
        self.model = None
        
        self.create_widgets()
    
    def create_widgets(self):
        self.upload_low_quality_btn = tk.Button(self.root, text="Upload Low Quality Apples", command=self.upload_low_quality)
        self.upload_low_quality_btn.pack(pady=10)
        
        self.low_quality_listbox = tk.Listbox(self.root)
        self.low_quality_listbox.pack(pady=10)
        
        self.upload_high_quality_btn = tk.Button(self.root, text="Upload High Quality Apples", command=self.upload_high_quality)
        self.upload_high_quality_btn.pack(pady=10)
        
        self.high_quality_listbox = tk.Listbox(self.root)
        self.high_quality_listbox.pack(pady=10)
        
        self.train_btn = tk.Button(self.root, text="Train Model", command=self.train_model)
        self.train_btn.pack(pady=10)
        
        self.status_label = tk.Label(self.root, text="Status: Waiting for input")
        self.status_label.pack(pady=10)
        
        self.upload_test_image_btn = tk.Button(self.root, text="Upload Test Image", command=self.upload_test_image, state=tk.DISABLED)
        self.upload_test_image_btn.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
    
    def upload_low_quality(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.low_quality_files = list(file_paths)
            self.update_listbox(self.low_quality_listbox, self.low_quality_files)
            messagebox.showinfo("Info", "Low quality apple images uploaded successfully")
            self.status_label.config(text="Status: Low quality images uploaded")
    
    def upload_high_quality(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.high_quality_files = list(file_paths)
            self.update_listbox(self.high_quality_listbox, self.high_quality_files)
            messagebox.showinfo("Info", "High quality apple images uploaded successfully")
            self.status_label.config(text="Status: High quality images uploaded")
    
    def update_listbox(self, listbox, files):
        listbox.delete(0, tk.END)
        for file in files:
            listbox.insert(tk.END, os.path.basename(file))
    
    def load_images(self, file_paths, label):
        print(f"Loading images for label {label}...")
        for file_path in file_paths:
            if os.path.exists(file_path):
                try:
                    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        img = cv2.resize(img, (128, 128))
                        self.images.append(img)
                        self.labels.append(label)
                        print(f"Loaded image: {file_path}")
                    else:
                        print(f"Failed to load image: {file_path}")
                except Exception as e:
                    print(f"Error loading image {file_path}: {e}")
            else:
                print(f"File does not exist: {file_path}")
    
    def train_model(self):
        if not self.low_quality_files or not self.high_quality_files:
            messagebox.showwarning("Warning", "Please upload images before training")
            return
        
        self.images = []
        self.labels = []
        self.load_images(self.low_quality_files, label=1)
        self.load_images(self.high_quality_files, label=0)
        
        if len(self.images) == 0 or len(self.labels) == 0:
            messagebox.showwarning("Warning", "No images were loaded. Please check the file paths and try again.")
            return
        
        print(f"Loaded {len(self.images)} images with labels: {len(self.labels)}")
        
        self.status_label.config(text="Status: Training model...")
        self.root.update_idletasks()
        
        images = np.array(self.images).reshape(-1, 128, 128, 1)
        labels = np.array(self.labels)
        
        print(f"Images shape: {images.shape}, Labels shape: {labels.shape}")
        
        train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)
        
        self.model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        
        history = self.model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))
        
        loss, accuracy = self.model.evaluate(test_images, test_labels)
        print(f"Test Accuracy: {accuracy * 100:.2f}%")
        
        self.status_label.config(text="Status: Training completed", bg='green')
        self.train_btn.config(bg='green')
        self.upload_test_image_btn.config(state=tk.NORMAL)
        
        plt.plot(history.history['accuracy'], label='Accuracy')
        plt.plot(history.history['val_accuracy'], label='Val Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.ylim([0, 1])
        plt.legend(loc='lower right')
        plt.show()
    
    def upload_test_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            result = self.predict_quality(file_path)
            self.result_label.config(text=f"The quality of the apple is: {result}")
    
    def predict_quality(self, file_path):
        try:
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                return "Image not found"
            img = cv2.resize(img, (128, 128))
            img = img.reshape(1, 128, 128, 1)
            prediction = self.model.predict(img)
            print(f"Prediction raw value: {prediction}")
            return "High Quality" if prediction < 0.5 else "Low Quality"
        except Exception as e:
            return f"Error predicting image quality: {e}"

if __name__ == "__main__":
    root = tk.Tk()
    app = AppleQualityApp(root)
    root.mainloop()
