import cv2
import time

def capture_photo():
    camera = cv2.VideoCapture(0)  # Use index 0 for the first USB camera
    if not camera.isOpened():
        print("Failed to open the camera")
        return

    # Set camera resolution (optional)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Define the time-lapse duration and interval between photos
    duration = 10  # Time-lapse duration in seconds
    interval = 1   # Interval between photos in seconds

    # Calculate the number of photos to capture
    num_photos = int(duration / interval)

    # Create a directory to store the time-lapse photos
    directory = "timelapse"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(num_photos):
        # Capture a frame
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture a frame")
            break

        # Save the captured frame with a unique filename
        filename = os.path.join(directory, f"photo_{i+1}.jpg")
        cv2.imwrite(filename, frame)

        # Wait for the specified interval
        time.sleep(interval)

    # Release the camera
    camera.release()

    print("Time-lapse captured and saved in the", directory, "directory")

# Call the capture_photo function to create a time-lapse
capture_photo()
