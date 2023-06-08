import pyaudio
import soundfile as sf
import time
import os
import numpy as np

def record_audio(output_file, max_duration):
    # Set audio parameters
    format = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    frames_per_buffer = 1024

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open audio stream
    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=frames_per_buffer)

    print("Recording started...")

    # Start recording
    frames = []
    start_time = time.time()
    while time.time() - start_time < max_duration:
        data = stream.read(frames_per_buffer)
        frames.append(data)

    print("Recording stopped.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate PyAudio
    audio.terminate()

    # Create the folder if it doesn't exist
    folder_path = os.path.dirname(output_file)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Convert frames to a NumPy array
    audio_data = np.frombuffer(b"".join(frames), dtype=np.int16)

    # Save the recorded audio as an MP3 file
    sf.write(output_file, audio_data, sample_rate)



# Specify the folder path and maximum recording duration in seconds
folder_path = "C:/Users/calvi/OneDrive/Documents/CSE 276/demo-test/sound_example"
output_file = os.path.join(folder_path, "audio.mp3")
max_duration = 5  # Maximum recording duration in seconds

# Call the recording function
record_audio(output_file, max_duration)
