import cv2

def capture_photo():
    camera = cv2.VideoCapture(0)  # Use index 0 for the first USB camera
    if not camera.isOpened():
        print("Failed to open the camera")
        return

    # Set camera resolution (optional)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Capture a frame
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture a frame")
        return

    # Save the captured frame to a file
    filename = "photo.jpg"
    cv2.imwrite(filename, frame)

    # Release the camera
    camera.release()

    print("Photo saved as", filename)

# Call the capture_photo function to take a photo
capture_photo()
