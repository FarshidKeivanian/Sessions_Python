import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout, BatchNormalization
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.utils import to_categorical

# Load the dataset
file_path = "Updated_Synthetic_Remote_Sensing_Dataset.csv"
data = pd.read_csv(file_path)

# Define feature columns and label column
features = ['Red', 'Green', 'Blue', 'NIR', 'SWIR']
label_column = 'Land_Cover'

# Separate features and labels
X = data[features].values
y = data[label_column].values

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)  # Convert categorical labels to integers
y_categorical = to_categorical(y_encoded)  # One-hot encoding

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Reshape data for CNN input (1D convolution, adding a single channel)
X_train_reshaped = X_train_scaled.reshape(-1, len(features), 1)
X_test_reshaped = X_test_scaled.reshape(-1, len(features), 1)

# Build CNN model
model = Sequential([
    Conv1D(64, kernel_size=2, activation='relu', input_shape=(len(features), 1)),
    BatchNormalization(),
    MaxPooling1D(pool_size=2),
    Dropout(0.3),
    
    Conv1D(32, kernel_size=2, activation='relu'),
    BatchNormalization(),
    MaxPooling1D(pool_size=2),
    Dropout(0.2),
    
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.3),
    
    Dense(len(label_encoder.classes_), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train_reshaped, y_train, epochs=50, batch_size=16, validation_split=0.2, verbose=1)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test_reshaped, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy:.2f}")

# Save the model summary for documentation
model.summary()
