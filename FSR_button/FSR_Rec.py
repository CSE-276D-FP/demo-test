from gpiozero import Button
import time
import pygame
import os


class FSR_Rec_Button:
    def __init__(self, pin):
        self.button = Button(pin, pull_up=False)
        self.toggle = False

    def trigger_rec_mode1(self):
        print("Record")
        pygame.mixer.music.stop()
        os.system("cvlc --play-and-exit ../tts/pre_recording_prompt.mp3")
        # raise("Not implemented yet")

    def default_mode(self, rec_mode):
        self.button.when_pressed = rec_mode
    
    def end_rec(self):
        self.button.when_pressed = None
        if(self.button.is_pressed):
            return True
        return False
    
    def replay_rec(self):
        raise("Not implemented yet")
        return
    
    def rec_mode(self):
        self.button.when_pressed = self.replay_rec
