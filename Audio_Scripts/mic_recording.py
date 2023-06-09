import sounddevice as sd
import soundfile as sf
import os
import numpy as np
from pydub import AudioSegment
import keyboard


def record_audio(output_wav, output_mp3, max_duration):
    # Set audio parameters
    sample_rate = 44100
    duration = max_duration

    # Record audio
    print("Recording Started")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    print("Recording stopped")

    # Create the folder if it doesn't exist
    folder_path = os.path.dirname(output_wav)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the recorded audio as a WAV file
    sf.write(output_wav, audio_data, sample_rate)

    # Convert WAV to MP3
    wav_audio = AudioSegment.from_wav(output_wav)
    wav_audio.export(output_mp3, format="mp3")

def delete_recording():
    # Delete the WAV file
    os.remove(output_mp3)

# Specify the folder path and maximum recording duration in seconds
folder_path = os.getcwd()
output_wav = os.path.join(folder_path, "audio.wav")
output_mp3 = os.path.join(folder_path, "audio.mp3")
max_duration = 5  # Maximum recording duration in seconds

# Call the recording function
record_audio(output_wav, output_mp3, max_duration)

# Play the recorded audio
sd.play(sf.read(output_wav)[0], samplerate=44100)
sd.wait()

os.remove(output_wav)

# Wait for the user to input 's' or any other key
print("Press 's' to keep the recording or any other key to delete it.")
keyboard_input = keyboard.read_key()

'''
# Check if the user pressed 's' or any other key
if keyboard_input.lower() == 's':
    print("Keeping the recording.")
else:
    print("Deleting the recording.")
    delete_recording()
'''
