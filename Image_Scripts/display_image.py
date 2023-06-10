import os
import sys
import pygame
import time

def display_image(image_path):
    image = pygame.image.load(image_path)
    image_width, image_height = image.get_size()
    aspect_ratio = min(screen_width / image_width, screen_height / image_height)
    scaled_width = int(image_width * aspect_ratio * 0.9)  # Reduce size by 10%
    scaled_height = int(image_height * aspect_ratio * 0.9)  # Reduce size by 10%
    scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))
    x = (screen_width - scaled_width) // 2
    y = (screen_height - scaled_height) // 2
    screen.fill((0, 0, 0))
    screen.blit(scaled_image, (x, y))

def play_pause_slideshow():
    global is_playing
    is_playing = not is_playing
    
def quit_slideshow():
    pygame.quit()
    sys.exit()


# Specify the folder path where the images are located
folder_path = '../image_example'

# Initialize Pygame
pygame.init()

# Set the screen size to 1020x600
screen_width = 1020
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("")

# Get a list of image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png"))]
if len(image_files) == 0:
    print("No image files found in the folder.")
    sys.exit()

# Set the initial index to 0
current_index = 0

# Set the time interval between image switches (in seconds)
interval = 1

# Set the initial time for the timer
timer_start = time.time()

# Initialize play/pause flag
is_playing = True

# Font settings
font = pygame.font.Font(None, 24)

# Button settings
button_width = 120
button_height = 40
button_color = (150, 150, 150)
button_text_color = (255, 255, 255)
button_font = pygame.font.Font(None, 24)

# Calculate the total width for both buttons
total_button_width = button_width * 2 + 10  # Add spacing between buttons

# Quit button
quit_text = "Quit"
quit_text_render = button_font.render(quit_text, True, button_text_color)
quit_text_rect = quit_text_render.get_rect(center=(screen_width // 2 + total_button_width // 2 - button_width // 2, screen_height - button_height - 10))
quit_button_rect = pygame.Rect(0, 0, button_width, button_height)
quit_button_rect.center = quit_text_rect.center

# Main loop
running = True
while running:
    # Play/Pause button
    play_pause_text = "Pause" if is_playing else "Play"
    play_pause_text_render = button_font.render(play_pause_text, True, button_text_color)
    play_pause_text_rect = play_pause_text_render.get_rect(center=(screen_width // 2 - total_button_width // 2 + button_width // 2, screen_height - button_height - 10))
    play_pause_button_rect = pygame.Rect(0, 0, button_width, button_height)
    play_pause_button_rect.center = play_pause_text_rect.center

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_pause_button_rect.collidepoint(event.pos):
                play_pause_slideshow()
            elif quit_button_rect.collidepoint(event.pos):
                quit_slideshow()
                
    if is_playing:
        # Check if the time interval has passed
        elapsed_time = time.time() - timer_start
        if elapsed_time >= interval:
            # Increment the index to switch to the next image
            current_index = (current_index + 1) % len(image_files)

            # Reset the timer
            timer_start = time.time()

    # Display the image
    image_path = os.path.join(folder_path, image_files[current_index])
    display_image(image_path)
    
    # Display the title
    title_text = "Image Slideshow"
    title_render = font.render(title_text, True, (255, 255, 255))
    title_rect = title_render.get_rect(center=(screen_width // 2, 20))
    screen.blit(title_render, title_rect)

    # Draw the button
    pygame.draw.rect(screen, button_color, play_pause_button_rect)
    screen.blit(play_pause_text_render, play_pause_text_rect)
    
    pygame.draw.rect(screen, button_color, quit_button_rect)
    screen.blit(quit_text_render, quit_text_rect)

    pygame.display.flip()

pygame.quit()
