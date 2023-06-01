import vlc
import keyboard

def play_pause(p):
    if p.is_playing():
        p.pause()
    else:
        p.play()

# Create a VLC media player instance
p = vlc.MediaPlayer("C:/Users/calvi/OneDrive/Documents/CSE 276/demo-test/sound_example/sample2.mp3")

# Register the 'a' key for playing or pausing the media
keyboard.add_hotkey('a', play_pause, args=(p,))

# Start the event listener
keyboard.wait('esc')
