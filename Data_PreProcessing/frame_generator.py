import cv2
import os

def video_to_frames(video_path, output_folder, num_frames=80):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read and save frames
    success, frame = video_capture.read()
    count = 0

    while success and count < num_frames:
        count += 1

        # Save frame as PNG
        frame_path = os.path.join(output_folder, f"{count}.png")
        cv2.imwrite(frame_path, frame)

        # Read next frame
        success, frame = video_capture.read()

    # Release video capture object
    video_capture.release()

# Replace 'your_video.mp4' with the path to your video file
video_path = 'inpaint_out.mp4'

# Replace 'output_frames' with the desired output folder name
output_folder = 'customf_inpainted'

# Convert video to the first 80 frames
video_to_frames(video_path, output_folder, num_frames=80)
