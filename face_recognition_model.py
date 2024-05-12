import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

# مسیر پوشه‌ای که تصاویر در آن قرار دارند
#image_folder = '/path/to/images'
image_folder = 'D:/imagess'

# خواندن تصاویر و تبدیل آن‌ها به خاکستری
def load_and_preprocess_images(image_folder):
    images = []
    for file_name in os.listdir(image_folder):
        file_path = os.path.join(image_folder, file_name)
        image = cv2.imread(file_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray_image, (100, 100))  # تغییر اندازه تصاویر
        images.append(resized_image)
    return np.array(images)

images = load_and_preprocess_images(image_folder)

# تقسیم داده‌ها به آموزشی و تست
train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)

# ساخت مدل
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(100, 100)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # فرض بر این است که تشخیص می‌دهیم آیا تصویر متعلق به فرشید است یا خیر
])

# کامپایل مدل
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# برچسب‌زنی تصاویر
labels = np.ones(len(train_images))  # چون همه تصاویر متعلق به یک شخص هستند

# آموزش مدل
model.fit(train_images, labels, epochs=10)

# ارزیابی مدل بر روی داده‌های تست
test_labels = np.ones(len(test_images))  # همه تصاویر تست هم متعلق به فرشید هستند
model.evaluate(test_images, test_labels)
