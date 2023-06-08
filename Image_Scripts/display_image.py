import os
import sys
import pygame

def display_image(image_path):
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    pygame.display.flip()

# Specify the folder path where the images are located
folder_path = "../image_example"

# Initialize Pygame
pygame.init()

# Set the screen size based on the first image's dimensions
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png"))]
if len(image_files) == 0:
    print("No image files found in the folder.")
    sys.exit()

first_image_path = os.path.join(folder_path, image_files[0])
first_image = pygame.image.load(first_image_path)
screen_width = first_image.get_width()
screen_height = first_image.get_height()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Viewer")

# Set the initial index to 0
current_index = 0

# Display the first image
image_path = os.path.join(folder_path, image_files[current_index])
display_image(image_path)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Increment the index to switch to the next image
                current_index = (current_index + 1) % len(image_files)
            elif event.key == pygame.K_LEFT:
                # Decrement the index to switch to the previous image
                current_index = (current_index - 1) % len(image_files)

            # Display the new image
            image_path = os.path.join(folder_path, image_files[current_index])
            display_image(image_path)

pygame.quit()
