import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Define the data directories
train_dir = 'Training Data'

# Create an ImageDataGenerator for data augmentation and preprocessing
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Define the batch size
batch_size = 8

# Create the train generator
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(256, 256),
    batch_size=batch_size,
    class_mode='categorical'  # Change to 'binary' for binary classification
)

# Build the model
model = Sequential([
    Conv2D(16, (3, 3), activation='relu', input_shape=(256, 256, 3)),
    MaxPooling2D(2, 2),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')  # Change to 1 for binary classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # Change to 'binary_crossentropy' for binary classification
              metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=20,
    verbose=1
)

# Plot training history (accuracy and loss)
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training Accuracy')
plt.legend(loc='lower right')

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()

# # Evaluate the model on the test set
# test_dir = 'Testing Data'
#
# test_datagen = ImageDataGenerator(rescale=1.0 / 255)
#
# test_generator = test_datagen.flow_from_directory(
#     test_dir,
#     target_size=(256, 256),
#     batch_size=batch_size,
#     class_mode='categorical'  # Change to 'binary' for binary classification
# )

# # Evaluate the model on the test data
# eval_result = model.evaluate(test_generator, verbose=1)
#
# print("\nTest Loss:", eval_result[0])
# print("Test Accuracy:", eval_result[1])
#

# Save the model
model.save('imageclassifier.keras')
