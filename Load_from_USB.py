'''
This script will load mp3 and image files from a USB to a local desired directory
This is intended to be used at lauch of our app so that wanted files will be added
This is intended for our low end prototype as a way to load files without the need for another computer to set files
This script works and will be used in run_bear_gui.sh
'''

import shutil
import os
import subprocess

# NOTE: Change usb source name depending on system and USB name
usb_source = "/media/hahui/*"

# Destination path for mp3 files
mp3_destination = "./sound_example"

#Destination path for img files
img_destination = "./image_example"

# All files from USB
all_files = os.listdir(usb_source)

# Filter MP3 files
mp3_files = [file for file in all_files if file.endswith('.mp3')]

# Filter image files
image_files = [f for f in all_files if f.endswith((".jpg", ".jpeg", ".png"))]

# Copy MP3 files to the destination folder
for file in mp3_files:
    source_file = os.path.join(usb_source, file)
    destination_file = os.path.join(mp3_destination, file)
    shutil.copy2(source_file, destination_file)

# Copy image files to the destination folder
for file in image_files:
    source_file = os.path.join(usb_source, file)
    destination_file = os.path.join(img_destination, file)
    shutil.copy2(source_file, destination_file)

exit()
