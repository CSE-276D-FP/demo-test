import os
import cv2

class CameraCapture:
    def find(self):
        index = 0
        arr = []
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            else:
                arr.append(index)
            cap.release()
            index += 1
        print(arr)

    def start_camera_preview(self):
        camera = cv2.VideoCapture(0)  # Use index 0 for the first USB camera
        if not camera.isOpened():
            print("Failed to open the camera")
            return

        # Set camera resolution (optional)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        # Create the preview window
        cv2.namedWindow("Camera Preview", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Camera Preview", 800, 600)

        while True:
            # Capture a frame
            ret, frame = camera.read()
            if not ret:
                print("Failed to capture a frame")
                break

            # Show the frame in the preview window
            cv2.imshow("Camera Preview", frame)

            # Check for key press to capture photo
            key = cv2.waitKey(1)
            if key == ord("s"):  # Press 's' to capture photo
                self.capture_photo(camera, frame)
                break
            elif key == 27:  # Press 'Esc' to exit without saving
                break

        # Close the preview window
        cv2.destroyAllWindows()

    def capture_photo(self, camera, frame):
        # Create the folder if it doesn't exist
        folder_name = "../image_example"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Generate a unique filename
        index = len(os.listdir(folder_name)) + 1
        filename = os.path.join(folder_name, f"photo{index}.jpg")

        # Save the captured frame to a file
        cv2.imwrite(filename, frame)

        # Release the camera
        camera.release()

        print("Photo saved as", filename)

# Create an instance of the CameraCapture class
capture = CameraCapture()

# Call the start_camera_preview method to start the camera preview
# capture.start_camera_preview()

# Call the find method to find camera indexes
capture.find()