# geeksforgeeks.org/convert-text-speech-python

from gtts import gTTS
import os

mytext = 'Press the record button to begin recording, and press it again to stop. Press any other button to cancel.'

language = 'en'

print("Create object")
myobj = gTTS(text=mytext, lang=language, slow=False)
print("Saving file")
myobj.save("pre_recording_prompt.mp3")
# print("Playing file")
# os.system("mpg321 welcome.mp3")
