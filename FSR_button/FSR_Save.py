from gpiozero import Button
import time
import pygame

from FSR_Abs import FSR_Abs_Button

class FSR_Save_Button(FSR_Abs_Button):
    def default_mode(self):
        self.button.when_pressed = None 
    
    def save_rec(self):
        raise("Not implemented yet")
        return
    
    def rec_mode(self):
        self.button.when_pressed = self.save_rec
