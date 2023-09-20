import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load the saved model
model_path = r'C:\Users\Lakshya Singh\Desktop\Hackathon - Hack Battle\Training Data\imageclassifier.keras'
model = tf.keras.models.load_model(model_path)

# Evaluate the model on the test set
test_dir = r"C:\Users\Lakshya Singh\Desktop\Hackathon - Hack Battle\Training Data"

test_datagen = ImageDataGenerator(rescale=1.0 / 255)
batch_size = 8
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(256, 256),
    batch_size=batch_size,
    class_mode='categorical'  # Change to 'binary' for binary classification
)

# Evaluate the model on the test data
eval_result = model.evaluate(test_generator, verbose=1)

print("\nTest Loss:", eval_result[0])
print("Test Accuracy:", eval_result[1])

# ~76% accuracy on training data
# ~72% accuracy on testing data
