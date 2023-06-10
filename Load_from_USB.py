import shutil
import os
import subprocess

# def is_USB_plugged_in():
#     result = subprocess.run(['mount'], capture_output=True, text=True)
#     output = result.stdout

#     media_devices = []

#     if output:
#         lines = output.split('\n')
#         for line in lines:
#             if '/media/' in line:
#                 device = line.split(' ')[0]
#                 media_devices.append(device)

#     return media_devices

# # Get the media devices
# media_devices = is_USB_plugged_in()

# if len(media_devices) > 0:
#     # Assume the first media device found is the desired source
#     usb_source = media_devices[0]
#     print(f"USB source: {usb_source}")
# else:
#     print("No media devices found.")
#     exit()

usb_source = "/dev/sda1"
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
