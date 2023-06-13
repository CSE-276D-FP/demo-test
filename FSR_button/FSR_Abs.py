# Abstract Button class and functions (extended by Play/Pause, Skip, and Save Buttons)
from gpiozero import Button
import time
import os


class FSR_Abs_Button:
    def __init__(self, pin):
        """Constructor for generic button

        Args:
            pin (int): GPIO pin number
        """
        self.button = Button(pin, pull_up=False)
        self.toggle = False                         # used by Play/Pause
        self.recButton = None                       # ref to record button
    
    def add_rec_btn(self, recButton):
        """Initialize reference to record button (cannot be done in constructor
            since the record button requires a list of other buttons)
        """
        self.recButton = recButton

    def cancel_rec(self):
        """When pressed in pre-record mode, cancels the recording by returning
            all buttons to idle default state.

        Raises:
            RuntimeError: when record button is not attached correctly
        """
        print("cancel rec")
        os.system("cvlc --play-and-exit ../tts/cancel_recording.mp3")
        
        if self.recButton is None:
            raise RuntimeError("Make sure you add the Rec Button")
        self.recButton.set_all_default()

    def cancel_rec_mode(self):
        """Sets button to cancel recording when pressed
        """
        self.button.when_pressed = self.cancel_rec
   

