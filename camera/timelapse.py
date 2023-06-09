import cv2
import time
import os

def capture_photo():
    camera = cv2.VideoCapture(0)  # Use index 0 for the first USB camera
    if not camera.isOpened():
        print("Failed to open the camera")
        return

    # Set camera resolution (optional)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Define the time-lapse duration and interval between photos
    duration = 5  # Time-lapse duration in seconds
    interval = 1   # Interval between photos in seconds

    # Calculate the number of photos to capture
    num_photos = int(duration / interval)

    # Create a directory to store the time-lapse photos
    folder_name = "../video_example"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    # Generate a unique filename
    index = len(os.listdir(folder_name)) + 1
    video_name = os.path.join(folder_name, f"timelapse_video{index}.mp4")

    # Create a video writer
    fps = 1 / interval  # Frames per second (1 frame per interval)
    frame_size = (1280, 720)  # Frame size (should match camera resolution)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for video compression
    video_writer = cv2.VideoWriter(video_name, fourcc, fps, frame_size)

    for i in range(num_photos):
        # Capture a frame
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture a frame")
            break

        # # Save the captured frame with a unique filename
        # filename = os.path.join(directory, f"photo_{i+1}.jpg")
        # cv2.imwrite(filename, frame)

        # Add the frame to the video
        video_writer.write(frame)

        # Wait for the specified interval
        time.sleep(interval)

    # Release the camera
    camera.release()

    # Release the video writer
    video_writer.release()

    print("Time-lapse captured and saved as", video_name)

# Call the capture_photo function to create a time-lapse video
capture_photo()