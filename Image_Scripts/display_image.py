import os
import sys
import pygame
import time

def display_image(image_path):
    image = pygame.image.load(image_path)
    image_width, image_height = image.get_size()
    aspect_ratio = min(screen_width / image_width, screen_height / image_height)
    scaled_width = int(image_width * aspect_ratio)
    scaled_height = int(image_height * aspect_ratio)
    scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))
    x = (screen_width - scaled_width) // 2
    y = (screen_height - scaled_height) // 2
    screen.fill((0, 0, 0))
    screen.blit(scaled_image, (x, y))
    pygame.display.flip()

# Specify the folder path where the images are located
folder_path = '../image_example'

# Initialize Pygame
pygame.init()

# Set the screen size to 1020x600
screen_width = 1020
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Viewer")

# Get a list of image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png"))]
if len(image_files) == 0:
    print("No image files found in the folder.")
    sys.exit()

# Set the initial index to 0
current_index = 0

# Display the first image
image_path = os.path.join(folder_path, image_files[current_index])
display_image(image_path)

# Set the time interval between image switches (in seconds)
interval = 3

# Set the initial time for the timer
timer_start = time.time()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the time interval has passed
    elapsed_time = time.time() - timer_start
    if elapsed_time >= interval:
        # Increment the index to switch to the next image
        current_index = (current_index + 1) % len(image_files)

        # Display the new image
        image_path = os.path.join(folder_path, image_files[current_index])
        display_image(image_path)

        # Reset the timer
        timer_start = time.time()

pygame.quit()
