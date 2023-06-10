from gpiozero import Button
import time
import pygame
import os

from pydub import AudioSegment
from FSR_Abs import FSR_Abs_Button

class FSR_Save_Button(FSR_Abs_Button):
    def default_mode(self):
        self.button.when_pressed = None 
    
    def save_rec(self, filename):
        print("Saving recording")

        # Save .wav file to .mp3
        wav_audio = AudioSegment.from_wav(filename + ".wav")
        wav_audio.export(filename + ".mp3", format="mp3")
        os.remove(filename + ".wav")

    def post_rec_mode(self, filename):
        self.button.when_pressed = self.save_rec(filename)
