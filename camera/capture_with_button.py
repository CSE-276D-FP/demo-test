import cv2
import tkinter as tk
from PIL import ImageTk, Image
import threading
import sys
import os

class CameraPreview:
    def __init__(self, window):
        self.window = window
        self.window.title("Camera Preview")

        # Create a label to display the camera feed
        self.label = tk.Label(self.window)
        self.label.pack()

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=10)

        # Create a button to capture the photo
        self.capture_button = tk.Button(self.button_frame, text="Capture", command=self.capture_image)
        self.capture_button.pack(side=tk.LEFT, padx=5)

        # Create a button to exit the program
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.exit_program)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        # Access the USB camera
        self.cap = cv2.VideoCapture(0)

        # Check if the camera is opened successfully
        if not self.cap.isOpened():
            raise Exception("Unable to access the camera")

        # Start a thread to continuously update the camera preview
        self.thread = threading.Thread(target=self.update_preview)
        self.thread.daemon = True
        self.thread.start()

    def update_preview(self):
        while True:
            # Capture a frame from the camera
            ret, frame = self.cap.read()

            # If the frame is captured successfully, update the preview
            if ret:
                # Convert the frame from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Resize the frame to fit the label
                frame = cv2.resize(frame, (640, 480))

                # Convert the frame to PIL ImageTk format
                image = Image.fromarray(frame)
                image = ImageTk.PhotoImage(image)

                # Update the label with the new image
                self.label.configure(image=image)
                self.label.image = image

    def capture_image(self):
        # Capture a frame from the camera
        ret, frame = self.cap.read()

        # Create the folder if it doesn't exist
        folder_name = "../image_example"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Generate a unique filename
        index = len(os.listdir(folder_name)) + 1
        filename = os.path.join(folder_name, f"photo{index}.jpg")
        
        # If the frame is captured successfully, save it to an image file
        if ret:
            cv2.imwrite(filename, frame)
            print("Image captured successfully!")

    def exit_program(self):
        # Release the camera and close the program
        self.cap.release()
        self.window.destroy()
        sys.exit()
    
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

def main():
    # Create a tkinter window
    window = tk.Tk()

    # Create the camera preview
    camera_preview = CameraPreview(window)

    # Run the tkinter event loop
    window.mainloop()

    # Close the camera and destroy the window when the event loop is finished
    camera_preview.cap.release()
    window.destroy()

# Call the main function to start the application
main()
