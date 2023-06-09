import pygame
from moviepy.editor import *
import os

directory = "../video_example"  # Directory path containing the mp4 files

pygame.display.set_caption('Yee')

# Get a list of all mp4 files in the directory
mp4_files = [file for file in os.listdir(directory) if file.endswith(".mp4")]

# Loop through each mp4 file
for video_name in mp4_files:
    video_path = os.path.join(directory, video_name)
    clip = VideoFileClip(video_path.replace("\\", "/"))
    clip.preview()

pygame.quit()