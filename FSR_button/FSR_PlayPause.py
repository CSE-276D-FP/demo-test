from gpiozero import Button
import time
import pygame


class FSR_PlayPause_Button:
    def __init__(self, pin):
        self.button = Button(pin, pull_up=False)
        self.toggle = False

    def play_pause(self):
        self.toggle = not self.toggle

        if (self.toggle):
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    def default_mode(self):
        self.button.when_pressed = self.play_pause
    
    def cancel_rec(self):
        self.button.when_pressed = None
        if(self.button.is_pressed):
            return True
        return False
    
    def replay_rec(self):
        raise("Not implemented yet")
        return
    
    def rec_mode(self):
        self.button.when_pressed = self.replay_rec
