import cv2
import os

# Load the video
video_path = "test.mp4"
cap = cv2.VideoCapture(video_path)

# Initialize variables for frame skipping
frame_num = 0
skip_frames = 60

# Directory to save images
output_directory = "Noshot2"
os.makedirs(output_directory, exist_ok=True)

while cap.isOpened():
    ret, frame = cap.read()

    # Break the loop if there are no more frames
    if not ret:
        break

    # Save the frame as an image every 60 frames
    if frame_num % skip_frames == 0:
        image_path = os.path.join(output_directory, f'frame_{frame_num}.jpg')
        cv2.imwrite(image_path, frame)
    print(frame_num)
    frame_num += 1

# Release video capture object
cap.release()
cv2.destroyAllWindows()
