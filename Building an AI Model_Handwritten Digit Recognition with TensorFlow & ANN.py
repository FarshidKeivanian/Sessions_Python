import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load MNIST dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to range [0,1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the ANN model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Flatten the 28x28 images
    keras.layers.Dense(128, activation='relu'),  # Fully connected layer
    keras.layers.Dense(10, activation='softmax') # Output layer (10 classes)
])

# Compile and train the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

# Visualize a prediction
import numpy as np
plt.imshow(x_test[0], cmap='gray')
plt.title(f"Predicted Label: {np.argmax(model.predict(x_test[:1]))}")
plt.show()
