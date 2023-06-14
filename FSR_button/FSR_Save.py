# Save Button class and functions
from gpiozero import Button
import time
import os

from pydub import AudioSegment
from FSR_Abs import FSR_Abs_Button

class FSR_Save_Button(FSR_Abs_Button):
    def add_refresh_fcn(self, refresh_fcn):
        """Attach refresh_audio function from mainAudioControl.py so that the
            newly saved file is added to the files to be played back

        Args:
            refresh_fcn (function): refresh audio file function from main script
        """
        self.refresh_fcn = refresh_fcn

    def default_mode(self):
        """Save button does nothing in default mode, needs to be initialized to
            a non-None function to avoid gpiozero error
        """
        self.button.when_pressed = lambda : print("Save press")
    
    def save_rec(self):
        """Converts the .wav temp recording into an .mp3 recording and deletes
            the .wav temp file

        Raises:
            RuntimeError: when this function is called without post_rec_mode
        """
        print("Saving recording")
        os.system("cvlc --play-and-exit ../tts/post_recording_save.mp3")

        if self.filename is None:
            raise RuntimeError("Make sure you call post_rec_mode")
        
        # Save .wav file to .mp3
        wav_audio = AudioSegment.from_wav(self.filename + ".wav")
        wav_audio.export("../sound_example/" + self.filename + ".mp3", format="mp3")
        if self.recButton is None:
            raise RuntimeError("Make sure to add rec button")
        
        self.recButton.set_all_default()    # return everything to idle default state
        self.refresh_fcn()
        
        time.sleep(1)                       # allow time for the .mp3 conversion to finish
        os.remove(self.filename + ".wav")   # remove .wav tempfile


    def post_rec_mode(self, filename):
        """Intiializes recording filename to be played when the save
            button is pressed during post-record mode

        Args:
            filename (string): filename of the .wav recording
        """
        self.filename = filename
        self.button.when_pressed = self.save_rec
