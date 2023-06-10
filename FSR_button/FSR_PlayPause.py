from gpiozero import Button
import time
import pygame
import os
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
   
    def cancel_rec_mode(self):
        self.toggle = True
        super().cancel_rec_mode()

    def replay_rec(self):
        print("Replaying recording")
        if self.filename is None:
            raise RuntimeError("Make sure you call post_rec_mode")
        os.system("cvlc --play-and-exit " + self.filename + ".wav")

    def post_rec_mode(self, filename):
        self.filename = filename
        self.button.when_pressed = self.replay_rec
