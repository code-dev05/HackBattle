import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

# Load the trained model
model_path = r'imageclassifier.h5'
model = tf.keras.models.load_model(model_path)

for i in range(1,100):
    img = cv2.imread(r"Bodyshot\ ({}).png".format(i))

    # Resize and preprocess the image
    resize = tf.image.resize(img, (256, 256))
    input_data = np.expand_dims(resize / 255, 0)  # Preprocess the image and expand dimensions for batch

    # Make predictions
    predictions = model.predict(input_data)

    # Get the class with the highest probability
    predicted_class = np.argmax(predictions)

    print(f"Predicted class: {predicted_class}")
