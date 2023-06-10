from gpiozero import Button
import time
import pygame
from FSR_Abs import FSR_Abs_Button

class FSR_Skip_Button(FSR_Abs_Button):
    def __init__(self, pin, play_fcn, audio_index, max_audio):
        self.button = Button(pin, pull_up=False)
        self.play = play_fcn
        self.index = audio_index
        self.max_audio = max_audio

    def update_audio(self, audio_index):
        self.index = audio_index

    def get_audio_index(self):
        return self.index

    def skip(self):
        print("Skipping")
        pygame.mixer.music.stop()
        self.index = (self.index + 1) % self.max_audio
        self.play(self.index)

    def default_mode(self):
        self.button.when_pressed = self.skip
    
    def no_save_rec(self):
        raise("Not implemented yet")
        return
    
    def rec_mode(self):
        self.button.when_pressed = self.no_play_rec
