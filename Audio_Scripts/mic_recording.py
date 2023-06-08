import sounddevice as sd
import soundfile as sf
import os
import numpy as np

def record_audio(output_file, max_duration):
    # Set audio parameters
    sample_rate = 44100
    duration = max_duration

    # Record audio
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    # Create the folder if it doesn't exist
    folder_path = os.path.dirname(output_file)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the recorded audio as an MP3 file
    sf.write(output_file, audio_data, sample_rate)

# Specify the folder path and maximum recording duration in seconds
folder_path = os.getcwd()
output_file = os.path.join(folder_path, "audio.wav")
max_duration = 5  # Maximum recording duration in seconds

# Call the recording function
record_audio(output_file, max_duration)

# Play the recorded audio
sd.play(sf.read(output_file)[0], samplerate=44100)
sd.wait()
