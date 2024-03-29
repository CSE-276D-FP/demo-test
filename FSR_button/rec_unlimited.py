#!/usr/bin/env python3
# File modified from: https://github.com/spatialaudio/python-sounddevice/blob/master/examples/rec_unlimited.py
# Handles the recording of audio used in audio control sequence. Generates a .wav
# file and has a maximum length limit.

"""Create a recording with arbitrary duration.

The soundfile module (https://python-soundfile.readthedocs.io/)
has to be installed!

"""
import argparse
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

import time


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args(remaining)

q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


def start_recording(max_duration, filename):
    """Generates a .wav recording when this function is run. Stops when the max
        duration is reached on the recording.

    Args:
        max_duration (int): max length of recording in seconds
        filename (string): name of the audio recording (without file extension)

    Raises:
        KeyboardInterrupt: when the recording should be stopped from timeout

    Returns:
        Boolean: True if recording stopped due to timeout
    """
    is_timed_out = False
    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info['default_samplerate'])
        if filename is None:
            args.filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
                                            suffix='.wav', dir='')
        elif args.filename is None:
            args.filename = filename
            

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                        channels=args.channels, subtype=args.subtype) as file:
            with sd.InputStream(samplerate=args.samplerate, device=args.device,
                                channels=args.channels, callback=callback):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)

                # Records until the max duration is reached
                start_time = time.time()
                while time.time() < start_time + max_duration:
                    file.write(q.get())
                is_timed_out = True
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        # Expected behavior to end the process is the Keyboard Interrupt
        # (Keyboard Interrupt can be Ctrl+C but it's thrown in the program logic)
        print('\nRecording finished: ' + repr(args.filename))

        # returns whether recording stopped due to timeout or manual stop
        return is_timed_out     
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))

if __name__ == "__main__":
    start_recording(10)         # test for recording with max duration 10
