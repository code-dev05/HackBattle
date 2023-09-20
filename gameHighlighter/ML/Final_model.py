import cv2
from moviepy.editor import *
import tensorflow as tf
import numpy as np
import os

def detect_headshot(frame, model):
    preprocessed_frame = preprocess_frame(frame)

    # Predict using the model
    prediction = model.predict(np.expand_dims(preprocessed_frame, axis=0))
    print(prediction[0][0], prediction[0][1], prediction[0][2])
    # Check the predicted class label
    if prediction[0][1] > 0.7:
        return True
    return False

def preprocess_frame(frame):
    # Resize the frame to 256x256 pixels and convert to RGB
    resized_frame = cv2.resize(frame, (256, 256))
    rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    # Normalize pixel values if needed
    # You may need to adapt this based on your model's preprocessing requirements
    preprocessed_frame = rgb_frame / 255.0
    return preprocessed_frame

def capture_object(model, vid_path):
    # Load the video
    video_path = vid_path
    cap = cv2.VideoCapture(video_path)
    # Initialize variables for frame skipping
    frame_num = 0

    # List to store frames with headshots
    headshot_frames = []
    headshot_timestamp = []

    # Run through every 60th frame
    while cap.isOpened():
        ret, frame = cap.read()

        # Break the loop if there are no more frames
        if not ret:
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Process the frame
        if detect_headshot(gray_frame, model):
            # Append the frame to the list if a headshot is detected
            headshot_frames.append(frame)
            headshot_timestamp.append(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
            print(frame)

        frame_num += 10  # Increment frame counter
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

    # Create new lists to store filtered frames and timestamps
    filtered_headshot_frames = []
    filtered_headshot_timestamp = []

    # Add the first frame and timestamp to the filtered lists
    if headshot_frames:
        filtered_headshot_frames.append(headshot_frames[0])
        filtered_headshot_timestamp.append(headshot_timestamp[0])

    # Iterate through the remaining frames and timestamps
    for i in range(1, len(headshot_timestamp)):
        if headshot_timestamp[i] - headshot_timestamp[i - 1] >= 3.5:
            # If the timestamps are more than 2.5 seconds apart, keep the frame and timestamp
            filtered_headshot_frames.append(headshot_frames[i])
            filtered_headshot_timestamp.append(headshot_timestamp[i])

    # Update the original lists with the filtered data
    # headshot_frames = filtered_headshot_frames
    # headshot_timestamp = filtered_headshot_timestamp

    # Release video capture object and return lists containing headshots
    cap.release()
    return filtered_headshot_frames, filtered_headshot_timestamp

def save_frames(headshot_frames):
    # Save the frames with headshots as image files
    output_directory = ""
    os.makedirs(output_directory, exist_ok=True)
    for idx, frame in enumerate(headshot_frames):
        image_path = os.path.join(output_directory, f"headshot_frame_{idx}.png")
        cv2.imwrite(image_path, frame)

def create_video(headshot_timestamp, video_path, headshot_frames):
    # Resize and trim the timestamps +-2 sec
    clips = []
    for idx, timestamp in enumerate(headshot_timestamp):
        video = VideoFileClip(video_path).subclip(timestamp-3, timestamp+1)

        # Resize the video clip
        resized_video = video.resize((1152, 720))
        clips.append(resized_video)

    # Concatenating Resized Video Clips
    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("highlight.mp4", codec="libx264", audio=False)  # Disable Audio Processing

    # Close Objects
    cv2.destroyAllWindows()
    print(len(headshot_frames))
    print(headshot_timestamp)


def main(vid_path):
    # Load the trained model
    model = tf.keras.models.load_model("Training Data/imageclassifier.keras")
    headshot_frames, headshot_timestamp = capture_object(model, vid_path)
    create_video(headshot_timestamp, vid_path, headshot_frames)
