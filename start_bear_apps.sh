#!/bin/sh

###
# This is a shell script to run the necessary files for button control
# and GUI for the bear. This will be made a desktop icon so that it can be launched
# through the touchscreen without the need for a mouse and keyboard
###

# # Load Media Files from USB to Pi
# cd 
# cd demo-test
# python Load_from_USB.py

#Go to Audio Scripts directory and run mainAudioControl for physical buttons 
cd 
cd demo-test/Audio_Scripts
python mainAudioControl.py

#Go to GUI directory and execute GUI script
cd
cd demo-test/GUI
python GUI.py


