from gpiozero import Button
import time
import pygame
import os

import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment

def record_audio(output_wav, output_mp3, max_duration):
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

def save_audio(output_wav):
    # Convert WAV to MP3
    wav_audio = AudioSegment.from_wav(output_wav)
    wav_audio.export(output_mp3, format="mp3")
    os.remove(output_wav)

# stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
def delete_audio(output_wav):
    try:
        os.remove(output_wav + ".wav")
    except OSError:
        pass

def gen_filename():
    return "local_recording" + str(int(time.time()))

class FSR_Rec_Button:
    def __init__(self, pin, otherButtons):
        self.button = Button(pin, pull_up=False)
        self.toggle = False
        self.otherButtons = otherButtons
        self.recentRecording = None

        for b in otherButtons:
            b.add_rec_btn(self)

    def default_mode(self):
        self.button.when_pressed = self.trigger_rec_mode 
    
    def trigger_rec_mode(self):
        print("Record")
        pygame.mixer.music.pause()
        os.system("cvlc --play-and-exit ../tts/pre_recording_prompt.mp3")

        self.button.when_pressed = self.start_recording

        for b in self.otherButtons:
            b.cancel_rec_mode(self)

    def set_all_default(self):
        for b in self.otherButtons:
            b.default_mode()
        self.default_mode()
    
    def start_recording(self):
        print("Start recording")
        
        folder_path = os.getcwd()
        self.recentRecording = gen_filename()
        output_wav = os.path.join(folder_path, self.recentRecording + ".wav")
        output_mp3 = os.path.join(folder_path, self.recentRecording + ".mp3")
        max_duration = 5

        record_audio(output_wav, output_mp3, max_duration)

        
        self.button.when_pressed = self.end_recording
        

    def end_recording(self):
        print("Stop recording - list options for different save/delete/record")
        sd.stop()
        

        self.button.when_pressed = self.replay_rec_mode

        '''
        for b in self.otherButtons:
            b.post_rec_mode(self, self.recentRecording)
        '''

    def replay_rec_mode(self):
        print("Re-recording")
        delete_audio(self.recentRecording)
        self.trigger_rec_mode()
        # self.set_all_default()

    def replay_rec(self):
        raise("Not implemented yet")
        return
    
    def rec_mode(self):
        self.button.when_pressed = self.replay_rec


