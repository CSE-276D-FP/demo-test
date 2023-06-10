from gpiozero import Button
import time
import pygame
import os

from pydub import AudioSegment
from FSR_Abs import FSR_Abs_Button

class FSR_Save_Button(FSR_Abs_Button):
    def add_refresh_fcn(self, refresh_fcn):
        self.refresh_fcn = refresh_fcn

    def default_mode(self):
        self.button.when_pressed = lambda : print("Save press")
    
    def save_rec(self):
        print("Saving recording")

        if self.filename is None:
            raise RuntimeError("Make sure you call post_rec_mode")
        # Save .wav file to .mp3
        wav_audio = AudioSegment.from_wav(self.filename + ".wav")
        wav_audio.export("../sound_example/" + self.filename + ".mp3", format="mp3")
        if self.recButton is None:
            raise RuntimeError("Make sure to add rec button")
        self.recButton.set_all_default()

        self.refresh_fcn()
        
        time.sleep(1)
        os.remove(self.filename + ".wav")


    def post_rec_mode(self, filename):
        self.filename = filename
        self.button.when_pressed = self.save_rec
