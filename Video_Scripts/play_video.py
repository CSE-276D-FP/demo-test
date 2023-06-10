# import pygame
# from moviepy.editor import *
# import os

# directory = "../video_example"  # Directory path containing the mp4 files

# pygame.display.set_caption('Yee')

# # Get a list of all mp4 files in the directory
# mp4_files = [file for file in os.listdir(directory) if file.endswith(".mp4")]

# # Loop through each mp4 file
# for video_name in mp4_files:
#     video_path = os.path.join(directory, video_name)
#     clip = VideoFileClip(video_path.replace("\\", "/"))
#     clip.preview()

# pygame.quit()

# import pygame
# from moviepy.editor import *
# import os
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up the display
# screen = pygame.display.set_mode((400, 400))
# pygame.display.set_caption('Yee')

# # Get the directory path containing the mp4 files
# directory = "../video_example"

# # Get a list of all mp4 files in the directory
# mp4_files = [file for file in os.listdir(directory) if file.endswith(".mp4")]

# # Loop through each mp4 file
# for video_name in mp4_files:
#     video_path = os.path.join(directory, video_name)
#     clip = VideoFileClip(video_path.replace("\\", "/"))
#     clip.preview()

#     # Create the exit button
#     button_font = pygame.font.Font(None, 36)
#     button_text = button_font.render("Exit", True, (255, 255, 255))
#     button_rect = button_text.get_rect(center=(200, 350))

#     # Display the button on the screen
#     screen.blit(button_text, button_rect)

#     # Update the display
#     pygame.display.flip()

#     # Event handling loop
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if button_rect.collidepoint(event.pos):
#                     pygame.quit()
#                     sys.exit()


import pygame
from moviepy.editor import *
import os
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Timelapse Videos')

# Get the directory path containing the mp4 files
directory = "../video_example"

# Get a list of all mp4 files in the directory
mp4_files = [file for file in os.listdir(directory) if file.endswith(".mp4")]

# Loop through each mp4 file
for video_name in mp4_files:
    video_path = os.path.join(directory, video_name)
    clip = VideoFileClip(video_path.replace("\\", "/"))
    final = clip.fx(vfx.resize, width=2000, height=525)
    # clip.preview()
    final.preview()

    # Update the display
    pygame.display.flip()
 
# Create the exit button
button_font = pygame.font.Font(None, 45)
button_text = button_font.render("Exit", True, (0,0,0))

button_width = button_text.get_width() + 20
button_height = button_text.get_height() + 10
button_x = 600
button_y = 600

button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
button_color = (220,220, 220)

# Display the button background
pygame.draw.rect(screen, button_color, button_rect)

# Display the button text
screen.blit(button_text, button_rect.move(10, 5))
       
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            pygame.quit()
            # sys.exit()

# pygame.quit()