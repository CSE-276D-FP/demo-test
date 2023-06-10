from gpiozero import Button
import time
import pygame
import os


class FSR_Abs_Button:
    def __init__(self, pin):
        self.button = Button(pin, pull_up=False)
        self.toggle = False
        self.recButton = None
    
    def cancel_rec(self):
        print("cancel rec")
        os.system("cvlc --play-and-exit ../tts/cancel_recording.mp3")
        
        if self.recButton is None:
            raise RuntimeError("Make sure you add the Rec Button")
        self.recButton.set_all_default()

    def cancel_rec_mode(self):
        self.button.when_pressed = self.cancel_rec
   
    def add_rec_btn(self, recButton):
        self.recButton = recButton

