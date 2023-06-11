import shutil
import os
import subprocess

# Change usb source name
usb_source = "/media/hahui/NEW VOLUME"
# Destination path
mp3_destination = "./sound_example"

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
    destination_file = os.path.join(mp3_destination, file)
    shutil.copy2(source_file, destination_file)

exit()
