# Record Button class and functions
from gpiozero import Button
import time
import pygame
import os

import sounddevice as sd
import soundfile as sf
from rec_unlimited import start_recording

def record_audio(output_wav, max_duration):
    """Alternative library to record audio, only supports recording for full
        duration of the max_duration. Currently unused.

    Args:
        output_wav (string): filename of output .wav
        max_duration (int): max length of recording in seconds
    """
    # Set audio parameters
    sample_rate = 44100
    duration = max_duration

    # Record audio
    print("Recording Started")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    print("Recording timed out")

    # Create the folder if it doesn't exist
    folder_path = os.path.dirname(output_wav)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the recorded audio as a WAV file
    sf.write(output_wav, audio_data, sample_rate)
    time.sleep(2)
    print(".wav file written")


def delete_audio(output_wav):
    """Remove specified .wav file if it exists
    Source: stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist

    Args:
        output_wav (string): name of output .wav file
    """
    try:
        os.remove(output_wav + ".wav")
    except OSError:
        pass

def gen_filename():
    """Create descending filename IDs for newer files to make them appear
        at the top of the playlist

    Returns:
        string: generated filename {ID}local_recording
    """
    return str(100000000000 - int(time.time())) + "local_recording"

class FSR_Rec_Button:
    def __init__(self, pin, otherButtons):
        """Constructor for the record button

        Args:
            pin (int): GPIO pin
            otherButtons (list): list of other buttons (Play/Pause, Skip, Save)
        """
        self.button = Button(pin, pull_up=False)
        self.otherButtons = otherButtons
        self.recentRecording = None         # filename of the most recent recording

        for b in otherButtons:
            b.add_rec_btn(self)             # attach the Record button reference

    def default_mode(self):
        """Begin recording mode when the record button is pressed in idle default state
        """
        self.button.when_pressed = self.trigger_rec_mode 
    
    def trigger_rec_mode(self):
        """Prompt the user with instructions on how to use recording mode and
            initialize button press events to start recording (record button) or
            return to idle default state (other button)
        """
        print("Record")
        pygame.mixer.music.pause()      # pause currently playing audio
        os.system("cvlc --play-and-exit ../tts/pre_recording_prompt.mp3") # play audio prompt

        self.button.when_pressed = self.start_recording

        # change other buttons to cancel recording mode upon press
        for b in self.otherButtons:
            b.cancel_rec_mode()

    def set_all_default(self):
        """Set all buttons to idle default state functions
        """
        for b in self.otherButtons:
            b.default_mode()
        self.default_mode()
    
    def start_recording(self):
        """Start recording, saves recording into .wav temp file
        """
        print("Start recording file", self.recentRecording)
        os.system("cvlc --play-and-exit ../tts/recording_started.mp3")
        
        # intialize variables for recording
        folder_path = os.getcwd()
        self.recentRecording = gen_filename()
        output_wav = os.path.join(folder_path, self.recentRecording + ".wav")
        max_duration = 10
        self.is_timed_out = False

        # alternative method to record audio
        # record_audio(output_wav, max_duration)

        # set up next record button press to trigger end of recording
        # unfortunately does not work because the gpiozero button listener stops
        # running when the recording is in progress, cannot async interrupt it
        self.button.when_pressed = self.end_recording

        # start recording
        self.is_timed_out = start_recording(output_wav, max_duration)

        if self.is_timed_out:
            # play timeout message and end recording without requiring another
            # button press
            os.system("cvlc --play-and-exit ../tts/recording_timeout.mp3")
            self.end_recording()

    def end_recording(self):
        """End recording and intiialize new button functionality for post-record

        Raises:
            KeyboardInterrupt: stops the recording if ongoing
        """
        print("Stop recording - list options for different save/delete/record")
        if not self.is_timed_out:
            raise KeyboardInterrupt
        os.system("cvlc --play-and-exit ../tts/recording_stopped.mp3")
        os.system("cvlc --play-and-exit ../tts/post_recording_prompt.mp3")

        # sd.stop()
        
        # set the next record button press to trigger re-recording
        self.button.when_pressed = self.replay_rec_mode

        # set next button presses to post-recording function
        for b in self.otherButtons:
            b.post_rec_mode(self.recentRecording)
        
    def replay_rec_mode(self):
        """After recording, deletes temp .wav file and redirects to pre-record stage
        """
        print("Re-recording")
        delete_audio(self.recentRecording)
        self.trigger_rec_mode()
        # self.set_all_default()



