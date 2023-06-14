# Main script for audio control sequence (low-tech version)
import os
import sys
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import filedialog

from signal import pause
sys.path.append("../FSR_button")
from FSR_PlayPause import FSR_PlayPause_Button
from FSR_Skip import FSR_Skip_Button
from FSR_Rec import FSR_Rec_Button
from FSR_Save import FSR_Save_Button

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

def refresh_audio():
    """Refresh list of audio files (e.g. to include newly saved files in dir)
    """
    global audio_files, current_audio_index, skipButton, playButton
    # sorts all .mp3 files in source dir
    audio_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.mp3')])
    # resets the index to play the first song (should be the most recently saved
    # recording unless another manually loaded file has a numeric prefix)
    current_audio_index = 0 
    skipButton.update_audio(current_audio_index)    # sync skip button's audio index

    play_next_audio(current_audio_index)  # set up audio to play but leave it paused
    playButton.play_pause()

def play_next_audio(current_audio_index):
    """Plays the next audio file in the list

    Args:
        current_audio_index (int): audio index of currently playing audio file
    """
    global audio_files, folder_path
    if current_audio_index < len(audio_files):
        # loads and plays audio file in the list at index current_audio_index
        audio_file = audio_files[current_audio_index]
        audio_path = os.path.join(folder_path, audio_file)
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        playButton.set_play()               # update Play button to play state
    else:
        pygame.mixer.music.stop()

# Button initialization
playButton = FSR_PlayPause_Button(17)
playButton.default_mode()

skipButton = FSR_Skip_Button(27, play_next_audio, current_audio_index, len(audio_files))
skipButton.default_mode()

saveButton = FSR_Save_Button(26)
saveButton.default_mode()
saveButton.add_refresh_fcn(refresh_audio)

recButton = FSR_Rec_Button(19, [playButton, skipButton, saveButton])
recButton.default_mode()

# Set first song to be played but keep it paused at start
play_next_audio(current_audio_index)
playButton.play_pause()


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
        elif event.type == music_end:
            # synchronize the skip button's audio index and current_audio_index
            current_audio_index = (skipButton.get_audio_index() + 1) % len(audio_files)  # Wrap around to the beginning
            skipButton.update_audio(current_audio_index)
            play_next_audio(current_audio_index)    # play beginning song

    clock.tick(30)  # Adjust the playback speed as needed

pause()
pygame.quit()
root.destroy()

