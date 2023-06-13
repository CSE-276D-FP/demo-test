# Skip Button class and functions
from gpiozero import Button
import time
import pygame
import os
from FSR_Abs import FSR_Abs_Button
from FSR_Rec import delete_audio

class FSR_Skip_Button(FSR_Abs_Button):
    def __init__(self, pin, play_fcn, audio_index, max_audio):
        """Constructor for skip button

        Args:
            pin (int): GPIO pin number
            play_fcn (function): play_next_audio function from main script
            audio_index (int): current audio file index that is played
            max_audio (int): number of audio files
        """
        self.button = Button(pin, pull_up=False)
        self.play = play_fcn
        self.index = audio_index    # might be better as global/static var access
        self.max_audio = max_audio  # might be better as global/static var access

    def update_audio(self, audio_index):
        """ Sets a audio index
        """
        self.index = audio_index

    def get_audio_index(self):
        """
        Returns:
            int: current audio index
        """
        return self.index

    def skip(self):
        """Skips to the next songs and starts playing it
        """
        print("Skipping")
        pygame.mixer.music.stop()                       # stops current audio
        self.index = (self.index + 1) % self.max_audio  # increments audio file index
        self.play(self.index)                           # plays next audio file

    def default_mode(self):
        """Skips song when button is pressed in idle default mode
        """
        self.button.when_pressed = self.skip
    
    def no_save_rec(self):
        """Deletes the .wav temp file and resets all buttons to default idle state

        Raises:
            RuntimeError: when this function is called without post_rec_mode
            RuntimeError: when this function is called without initializing record button
        """
        print("Exiting record mode")
        os.system("cvlc --play-and-exit ../tts/post_recording_no_save.mp3")

        if self.filename is None:
            raise RuntimeError("Make sure you call post_rec_mode")
        delete_audio(self.filename + ".wav")    # delete temp file
        
        if self.recButton is None:
            raise RuntimeError("Make sure to add rec button")
        self.recButton.set_all_default()        # reset all buttons to idle default state

    def post_rec_mode(self, filename):
        """Intiializes recording filename to be played when the skip
            button is pressed during post-record mode

        Args:
            filename (string): filename of the .wav recording
        """
        self.filename = filename
        self.button.when_pressed = self.no_save_rec
