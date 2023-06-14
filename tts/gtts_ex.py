# File to generate audio prompts (Google Text-to-Speech)
# Source: https://geeksforgeeks.org/convert-text-speech-python

from gtts import gTTS
import os

# key: name of audio file
# value: text that is used for text-to-speech
text_input = {
    'pre_recording_prompt.mp3'  : '''To begin recording, press the recording button and press it again to stop.
                                    To cancel, press any other button'''
    ,
    'cancel_recording.mp3'      : '''Exiting recording mode.'''
    ,
    'recording_started.mp3'     : '''Recording started'''
    ,
    'recording_stopped.mp3'     : '''Recording stopped'''
    ,
    'recording_timeout.mp3'     : '''Max recording length exceeded.'''
    ,
    'post_recording_prompt.mp3' : '''To play back your recording, press the play button. 
                                    To save your recording, press the save button. 
                                    To discard your recording, press the skip button.
                                    To record again, first make sure to save if desired, then press the recording button.'''
    ,
    'post_recording_save.mp3'   : '''Saving and exiting recording mode.'''
    ,
    'post_recording_no_save.mp3': '''Exiting recording mode without saving.'''
}

language = 'en'     # English language for text-to-speech

# Generates a text-to-speech message from each item in text_input
for filename in text_input:
    print("Create object")
    myobj = gTTS(text=text_input[filename], lang=language, slow=False)
    print("Saving file " + filename)
    myobj.save("temp_" + filename)
    
    # Reduce volume of the audio message
    # https://www.maketecheasier.com/normalize-music-files-with-ffmpeg/
    os.system('ffmpeg -i {infile} -filter:a "volume=0.5" {outfile}'
                .format(infile="temp_" + filename, outfile=filename))
    os.remove("temp_" + filename)
