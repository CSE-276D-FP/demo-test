# Play/Pause Button class and functions
from gpiozero import Button
import time
import pygame
import os
from FSR_Abs import FSR_Abs_Button


class FSR_PlayPause_Button(FSR_Abs_Button):
    def set_play(self):
        """Called when the music is playing from outside the play button press
            e.g. when skip button triggers skip + playing of music
        """
        # print("play reset")
        self.toggle = False

    def play_pause(self):
        """Playing and pausing of music, with slight delay to avoid accidental trigger
        """
        print("Play/Pause")
        self.toggle = not self.toggle   # flips between Play and Pause function
        # print(self.toggle)
        if (self.toggle):
            pygame.mixer.music.pause()  # pauses audio loop
        else:
            pygame.mixer.music.unpause()    # plays audio loop
        time.sleep(0.2)

    def default_mode(self):
        """Sets idle default mode to play/pause music when play/pause button is pressed
        """
        self.button.when_pressed = self.play_pause
   
    def cancel_rec_mode(self):
        """Reset the toggle state and set all buttons back to idle default mode
        """
        self.toggle = True          # resets toggle because canceling should return to a paused audio state
        super().cancel_rec_mode()   # set all buttons back to default mode

    def replay_rec(self):
        """Replays the .wav temp recording during post-record mode

        Raises:
            RuntimeError: when this function is called without post_rec_mode
        """
        print("Replaying recording")
        if self.filename is None:
            raise RuntimeError("Make sure you call post_rec_mode")
        os.system("cvlc --play-and-exit " + self.filename + ".wav")

    def post_rec_mode(self, filename):
        """Intiializes recording filename to be played when the play/pause
            button is pressed during post-record mode

        Args:
            filename (string): filename of the .wav recording
        """
        self.filename = filename
        self.button.when_pressed = self.replay_rec
