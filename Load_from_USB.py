import shutil
import os
import subprocess

def is_USB_plugged_in():
    result = subprocess.run(['lsblk', '-o', 'name,label,type,mountpoint'], capture_output=True, text=True)
    output = result.stdout

    lines = output.split('\n')
    usb_drives = []

    for line in output.split('\n'):
        if line.startswith('/media'):
            usb_drives.append(line)

    return usb_drives


# Get the USB drive with media files
media_usb_drives = is_USB_plugged_in()
print(media_usb_drives)
if len(media_usb_drives) > 0:
    # Assume the first media USB drive found is the desired source
    usb_source = media_usb_drives[0]
    print(usb_source)
else:
    print("No media USB drive found.")
    exit()

# usb_source = "/media/hahui/NEW VOLUME"
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
