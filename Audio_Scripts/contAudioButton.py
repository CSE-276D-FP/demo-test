import os
import sys
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import filedialog

from signal import pause
sys.path.append("../FSR_button")
from FSR_PlayPause import FSR_PlayPause_Button

root = Tk()
root.withdraw()

#folder_path = filedialog.askdirectory(title="Select Audio Folder")
folder_path = "../sound_example"
if not folder_path:
    sys.exit(0)

audio_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.mp3')])

pygame.init()

pygame.mixer.init()
clock = pygame.time.Clock()

current_audio_index = 0
paused = False

# Button initialization
playButton = FSR_PlayPause_Button(17)
playButton.default_mode()
skipButton = FSR_PlayPause_Button(27)
skipButton.default_mode()
recButton = FSR_PlayPause_Button(19)
recButton.default_mode()
saveButton = FSR_PlayPause_Button(26)
saveButton.default_mode()

def play_next_audio():
    global current_audio_index
    if current_audio_index < len(audio_files):
        audio_file = audio_files[current_audio_index]
        audio_path = os.path.join(folder_path, audio_file)
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        current_audio_index = (current_audio_index + 1) % len(audio_files)  # Wrap around to the beginning
    else:
        pygame.mixer.music.stop()

play_next_audio()

display = pygame.display.set_mode((300, 300))
# Set the music end event
music_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(music_end)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            # print("Keyboard event occured")
            # if event.key == K_SPACE:
            #     if paused:
            #         pygame.mixer.music.unpause()
            #         paused = False
            #     else:
            #         pygame.mixer.music.pause()
            #         paused = True

            if event.key == K_RIGHT: # skip
                pygame.mixer.music.stop()
                current_audio_index = (current_audio_index + 1) % len(audio_files)
                play_next_audio()
        elif event.type == music_end:
            play_next_audio()

    clock.tick(30)  # Adjust the playback speed as needed

pause()
pygame.quit()
root.destroy()
