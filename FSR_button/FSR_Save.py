from gpiozero import Button
import time
import pygame


class FSR_Save_Button:
    def __init__(self, pin):
        self.button = Button(pin, pull_up=False)
        self.toggle = False

    def default_mode(self):
        self.button.when_pressed = None 
    
    def cancel_rec(self):
        self.button.when_pressed = None
        if(self.button.is_pressed):
            return True
        return False
    
    def save_rec(self):
        raise("Not implemented yet")
        return
    
    def rec_mode(self):
        self.button.when_pressed = self.save_rec
