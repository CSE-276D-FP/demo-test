# Source: geeksforgeeks.org/convert-text-speech-python

from gtts import gTTS
import os

text_input = {
    'pre_recording_prompt'  : '''To begin recording, press the recording button and press it again to stop.
                                    To cancel, press any other button'''
    ,
    'cancel_recording'      : '''Exiting recording mode.'''
    ,
    'recording_started'     : '''Recording started'''
    ,
    'recording_stopped'     : '''Recording stopped'''
    ,
    'post_recording_prompt' : '''If you want to play back your recording, press the play button. 
            If you want to save your recording, press the save button. 
            If you do not want to save your recording, press the skip button.
            If you want to record again, first make sure you save if desired, then press the recording button.'''
    ,
    'post_recording_save'   : '''Saving, then exiting recording mode.'''
    ,
    'post_recording_no_save': '''Exiting recording mode without saving.'''
}

language = 'en'

for filename in text_input:
    print("Create object")
    myobj = gTTS(text=text_input[filename], lang=language, slow=False)
    print("Saving file" + filename + ".mp3")
    myobj.save(filename + ".mp3")
    
# print("Playing file")
# os.system("mpg321 welcome.mp3")
