'''
NOTE: This file was used for testing and is not used in the final code
This code is using pygame to play mp3 audio sounds
'''

from pygame import mixer
  
# Starting the mixer
mixer.init()
  
# Loading the song from a specified directory
# audio_file = "C:/Users/calvi/OneDrive/Documents/CSE 276/demo-test/sound_example/sample2.mp3"
audio_file = "/Users/amandaquach/Downloads/CSE 276D/demo-test/sound_example/sample2.mp3"
mixer.music.load(audio_file)
  
# Setting the volume
mixer.music.set_volume(0.7)
  
# Start playing the song
mixer.music.play()
  
# User input for pause and play
while True:
      
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
  
        # Pausing the music
        mixer.music.pause()     
    elif query == 'r':
  
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
  
        # Stop the mixer
        mixer.music.stop()
        break