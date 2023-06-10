from gpiozero import Button
import time
import pygame


class FSR_Abs_Button:
    def __init__(self, pin):
        self.button = Button(pin, pull_up=False)
        self.toggle = False
        self.recButton = None
    
    def cancel_rec(self):
        print("cancel rec")
        if self.recButton is None:
            raise RuntimeError("Make sure you add the Rec Button")
        self.recButton.set_all_default()

    def cancel_rec_mode(self):
        self.button.when_pressed = self.cancel_rec
   
    def add_rec_btn(self, recButton):
        self.recButton = recButton

