from gpiozero import Button
import time
import pygame
from FSR_Abs import FSR_Abs_Button


class FSR_PlayPause_Button(FSR_Abs_Button):
    def set_play(self):
        # print("play reset")
        self.toggle = False

    def play_pause(self):
        print("Play/Pause")
        self.toggle = not self.toggle
        # print(self.toggle)
        if (self.toggle):
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        time.sleep(0.2)

    def default_mode(self):
        self.button.when_pressed = self.play_pause
   
    def cancel_rec_mode(self, recButton):
        self.toggle = True
        super().cancel_rec_mode(recButton)

    def replay_rec(self):
        raise("Not implemented yet")
        return
    
    def rec_mode(self):
        self.button.when_pressed = self.replay_rec
