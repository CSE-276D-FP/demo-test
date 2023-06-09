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
        folder_name = "image_example"
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

# import os
# import cv2
# import pygame

# class CameraCapture:
#     def __init__(self):
#         self.camera = cv2.VideoCapture(0)  # Use index 0 for the first USB camera

#     def find(self):
#         index = 0
#         arr = []
#         while True:
#             cap = cv2.VideoCapture(index)
#             if not cap.read()[0]:
#                 break
#             else:
#                 arr.append(index)
#             cap.release()
#             index += 1
#         print(arr)

#     def start_camera_preview(self):
#         if not self.camera.isOpened():
#             print("Failed to open the camera")
#             return

#         # Set camera resolution (optional)
#         self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#         self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#         # Initialize Pygame
#         pygame.init()

#         # Create the Pygame window
#         window_width, window_height = 800, 600
#         window = pygame.display.set_mode((window_width, window_height))
#         pygame.display.set_caption("Camera Preview")

#         # Create the font for button text
#         font = pygame.font.SysFont(None, 30)

#         # Run the camera preview loop
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_s:  # Press 's' to capture photo
#                         ret, frame = self.camera.read()
#                         if not ret:
#                             print("Failed to capture a frame")
#                             break
#                         self.capture_photo(frame)

#             # Capture a frame
#             ret, frame = self.camera.read()
#             if not ret:
#                 print("Failed to capture a frame")
#                 break

#             # Convert the frame to RGB format for Pygame
#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             # Create a Pygame surface from the frame
#             frame_surface = pygame.surfarray.make_surface(rgb_frame)

#             # Scale the frame surface to fit the window size
#             frame_surface = pygame.transform.scale(frame_surface, (window_width, window_height))

#             # Clear the window
#             window.fill((0, 0, 0))

#             # Blit the frame surface onto the window
#             window.blit(frame_surface, (0, 0))

#             # Create the "Capture Photo" button
#             button_width, button_height = 150, 50
#             button_x = (window_width - button_width) // 2
#             button_y = window_height - button_height - 20
#             capture_button = pygame.draw.rect(window, (255, 0, 0), (button_x, button_y, button_width, button_height))

#             # Render the button text
#             button_text = font.render("Capture Photo", True, (255, 255, 255))
#             button_text_rect = button_text.get_rect(center=capture_button.center)
#             window.blit(button_text, button_text_rect)

#             # Update the display
#             pygame.display.flip()

#         # Release the camera and quit Pygame
#         self.camera.release()
#         pygame.quit()

#     def capture_photo(self, frame):
#         # Create the folder if it doesn't exist
#         folder_name = "image_example"
#         if not os.path.exists(folder_name):
#             os.makedirs(folder_name)
                                
#         # Generate a unique filename
#         index = len(os.listdir(folder_name)) + 1
#         filename = os.path.join(folder_name, f"photo{index}.jpg")

#         # Save the captured frame to a file
#         cv2.imwrite(filename, frame)

#         print("Photo saved as", filename)

# # Create an instance of the CameraCapture class
# capture = CameraCapture()

# # Call the run method to start the camera preview
# capture.start_camera_preview()