import tensorflow as tf
import requests
from io import BytesIO
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Ask the user for their student ID
student_id = input("Please enter your student ID: ")

def classify_image(url):
    # Download the image from the URL
    response = requests.get(url)
    img = tf.keras.preprocessing.image.load_img(BytesIO(response.content), target_size=(224, 224))
    
    # Preprocess the image
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = tf.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    # Predict using the model
    preds = model.predict(x)
    
    # Decode predictions to understand the result better
    decoded_preds = decode_predictions(preds, top=3)[0]  # Top 3 predictions
    
    # Use the last digit of the student ID to determine the threshold
    threshold = int(str(student_id)[-1]) / 100
    confidence = max(pred[2] for pred in decoded_preds)
    print("Threshold:", threshold)
    print("Predictions:", decoded_preds)
    
    if confidence > threshold:
        print("Confident prediction:", decoded_preds[0][1], "with confidence:", confidence)
    else:
        print("Uncertain prediction")

# URL of the image to classify
image_url = "https://github.com/FarshidKeivanian/Sessions_Python/raw/main/Orange.jpg"
classify_image(image_url)
