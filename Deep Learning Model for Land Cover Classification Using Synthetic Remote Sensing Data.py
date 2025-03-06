import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.utils import to_categorical

# Load the dataset from the updated URL
url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/Updated_Synthetic_Remote_Sensing_Dataset.csv"
data = pd.read_csv(url)

# Display the first few rows of the dataset to understand its structure (optional)
print(data.head())

# Assuming the dataset has columns: 'Red', 'Green', 'Blue', 'NIR', 'SWIR', and 'Land_Cover'
# Replace with the actual column names if they differ
features = ['Red', 'Green', 'Blue', 'NIR', 'SWIR']
label_column = 'Land_Cover'  # Corrected column name

# Separate features and labels
X = data[features].values
y = data[label_column].values

# Prepare the data
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)  # Encode labels as integers
y_categorical = to_categorical(y_encoded)  # One-hot encoding

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build a deep learning model
model = Sequential([
    Dense(64, input_dim=len(features), activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(len(label_encoder.classes_), activation='softmax')  # Output layer for multi-class classification
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=20, batch_size=16, validation_split=0.2, verbose=1)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy:.2f}")

# Save the model summary for documentation
model.summary()
