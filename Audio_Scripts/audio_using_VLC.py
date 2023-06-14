import vlc
import keyboard

'''
This is one option to play mp3 file.
This program will use VLC media player to play audio from a specific file
It also has user input to pause and play media
NOTE: This file was used for testing and is not used in the final code
'''

def play_pause(p):
    if p.is_playing():
        p.pause()
    else:
        p.play()

# Create a VLC media player instance
audio_file = "C:/Users/calvi/OneDrive/Documents/CSE 276/demo-test/sound_example/sample2.mp3"
p = vlc.MediaPlayer(audio_file)

# Register the 'a' key for playing or pausing the media
keyboard.add_hotkey('a', play_pause, args=(p,))

# Start the event listener
keyboard.wait('esc')
