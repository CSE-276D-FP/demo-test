import cv2
import time
import os
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
from threading import Thread

class CameraPreview:
    def __init__(self, window, camera):
        self.window = window
        self.camera = camera
        if not self.camera.isOpened():
            print("Failed to open the camera")
            return

        self.preview_label = tk.Label(window)
        self.preview_label.pack()

        self.update_preview()

    def update_preview(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            image = image.resize((640, 480), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            self.preview_label.configure(image=photo)
            self.preview_label.image = photo  # Keep a reference

        self.window.after(10, self.update_preview)

    def close(self):
        self.camera.release()

def capture_photo(camera):
    # Set camera resolution (optional)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Create a directory to store the time-lapse photos
    folder_name = "../image_example"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Generate a unique filename
    index = len(os.listdir(folder_name)) + 1
    filename = os.path.join(folder_name, f"photo{index}.jpeg")
    
    ret, frame = camera.read()
    cv2.imwrite(filename, frame)
    print("Image captured successfully!")

def start_capture(camera):
    capture_button.config(state=tk.DISABLED)  # Disable the capture button during capture
    exit_button.config(state=tk.DISABLED)  # Disable the exit button during capture

    # Start a new thread for capturing the time-lapse video
    capture_thread = Thread(target=capture_photo, args=(camera,))
    capture_thread.start()

    def enable_buttons():
        capture_button.config(state=tk.NORMAL)  # Re-enable the capture button after capture
        exit_button.config(state=tk.NORMAL)  # Re-enable the exit button after capture

    # Schedule the enable_buttons function to be called after the capture thread completes
    window.after(1000 * 5, enable_buttons)  # Wait for 5 seconds

def exit_program():
    window.destroy()

# Create a Tkinter window
window = tk.Tk()
window.title("Photo Capture")

# Create a camera instance
camera = cv2.VideoCapture(0)  # Use index 0 for the first USB camera

# Create a camera preview object
camera_preview = CameraPreview(window, camera)

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack(side=tk.BOTTOM, pady=10)

# Create a capture button
custom_font = font.Font(size=20)
capture_button = tk.Button(button_frame, text="Capture", command=lambda: start_capture(camera), font=custom_font, width = 5, height = 2)
capture_button.pack(side=tk.LEFT, padx=10)

# Create an exit button
exit_button = tk.Button(button_frame, text="Exit", command=exit_program, font=custom_font, width = 5, height = 2)
exit_button.pack(side=tk.LEFT, padx=10)

# Start the Tkinter event loop
window.mainloop()

# Close the camera preview when the window is closed
camera_preview.close()
