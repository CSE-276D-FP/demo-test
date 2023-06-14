'''
 This program is used for the final prototype
 This program is will be called from the main GUI.py script
 It handles recording audio, saving it to the directory sound_example, and playback
    - It will create a temp WAV file and be converted to an mp3
    - Has user inputs to save, delete, record
 The GUI for Recording is created in here using pygame
'''

import sounddevice as sd
import soundfile as sf
import os
import numpy as np
from pydub import AudioSegment
import keyboard
import sys
import pygame


def record_audio(output_wav, output_mp3, max_duration):
    # Set audio parameters. Used examples from Geeks for Geeks
    sample_rate = 44100
    duration = max_duration

    # Record audio
    print("Recording Started")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    print("Recording stopped")

    # Create the folder if it doesn't exist
    folder_path = os.path.dirname(output_wav)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the recorded audio as a WAV file
    sf.write(output_wav, audio_data, sample_rate)

    # Convert WAV to MP3
    wav_audio = AudioSegment.from_wav(output_wav)
    wav_audio.export(output_mp3, format="mp3")

def playback(output_wav):
    # Play the recorded audio
    sd.play(sf.read(output_wav)[0], samplerate=44100)
    sd.wait()

    # Delete the created WAV file because we are not using it anymore
    os.remove(output_wav)


def delete_recording():
    # Delete the mp3 file. All media files will be deleted at this point
    os.remove(output_mp3)


def quit_window():
    # Close window and exit program
    pygame.quit()
    sys.exit()

# Create a function to check if a button is clicked
def is_button_clicked(button_rect):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        return pygame.mouse.get_pressed()[0]
    return False


# Specify the folder path and maximum recording duration in seconds
folder_path = '../sound_example'
output_wav = os.path.join(folder_path, "audio.wav")

# Generate a unique filename
index = len(os.listdir(folder_path)) + 1
output_mp3 = os.path.join(folder_path, f"audio{index}.mp3")
#output_mp3 = os.path.join(folder_path, "audio.mp3")
max_duration = 5  # Maximum recording duration in seconds

# # Call the recording function
# record_audio(output_wav, output_mp3, max_duration)
# playback(output_wav)


#### Buttons to record, save, quit
# Initialize Pygame
pygame.init()

# Set the screen size to 1020x600
screen_width = 1024
screen_height = 530
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mic Recording")

# Font settings
font = pygame.font.Font(None, 24)

# Button settings
button_width = 300
button_height = 100
button_color = (150, 150, 150)
button_text_color = (255, 255, 255)
button_font = pygame.font.Font(None, 85)

# Calculate the total width for both buttons
total_button_width = button_width * 2 + 10  # Add spacing between buttons

# Quit button
quit_text = "Exit"
quit_text_render = button_font.render(quit_text, True, button_text_color)
quit_text_rect = quit_text_render.get_rect(center=(700, 250))
quit_button_rect = pygame.Rect(0, 0, button_width, button_height)
quit_button_rect.center = quit_text_rect.center


is_recording = False
running = True
while running:
     # Record button
    recording_text = "Recorded" if is_recording else "Record"
    recording_text_render = button_font.render(recording_text, True, button_text_color)
    recording_text_rect = recording_text_render.get_rect(center=(320, 250))
    recording_button_rect = pygame.Rect(0, 0, button_width, button_height)
    recording_button_rect.center = recording_text_rect.center

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if recording_button_rect.collidepoint(event.pos):
                is_recording= not is_recording
                recording_text ="Recording"
            elif quit_button_rect.collidepoint(event.pos):
                quit_window()

    screen.fill((200, 200, 200))

    # # Draw the buttons
    # pygame.draw.rect(screen, (0, 255, 0), recording_button_rect)
    # pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)

    # Check for button clicks
    if is_button_clicked(recording_button_rect):
        recording_text ="Recording"
        pygame.draw.rect(screen, button_color, recording_button_rect)
        screen.blit(recording_text_render, recording_text_rect)
        record_audio(output_wav, output_mp3, max_duration)
        playback(output_wav)

    if is_button_clicked(quit_button_rect):
        delete_recording()
        quit_window()

    # Draw the button
    pygame.draw.rect(screen, button_color, recording_button_rect)
    screen.blit(recording_text_render, recording_text_rect)

    pygame.draw.rect(screen, button_color, quit_button_rect)
    screen.blit(quit_text_render, quit_text_rect)
    
    pygame.display.flip()

pygame.quit()
sys.exit()



####
