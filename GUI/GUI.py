from tkinter import *
import os
import sys
sys.path.append("../camera")
# from capture import CameraCapture
# from contAudioButton import cont_Audio_Button

class StartScreen:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master 
        
        self.audioButton = Button(self.master, text="Audio", command=self.load_audio, height=7, width=15)
        self.audioButton.grid(row=1, column=1)

        self.videoButton = Button(self.master, text="Video", command=self.load_video, height=7, width=15)
        self.videoButton.grid(row=1, column=40)
        
        self.photoButton = Button(self.master, text="Photo", command=self.load_photo, height=7, width=15)
        self.photoButton.grid(row=2, column=10)
        
        self.recButton = Button(self.master, text="Recording", command=self.load_rec, height=7, width=15)
        self.recButton.grid(row=3, column=1)
        
        self.clockButton = Button(self.master, text="Clock", command=self.load_clock, height=7, width=15)
        self.clockButton.grid(row=3, column=40)

    def load_audio(self):
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()

        # use `root` with another class
        self.another = Audio(self.master)
        
    def load_video(self):
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()

        # use `root` with another class
        self.another = Video(self.master)
        
    def load_photo(self):
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()

        # use `root` with another class
        self.another = Photo(self.master)
        
    def load_rec(self):
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()

        # use `root` with another class
        self.another = Rec(self.master)
        
    def load_clock(self):
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()

        # use `root` with another class
        self.another = Clock(self.master)

class Video:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Playing Timelapse...")
        self.label.grid(row=1, column=1)
        
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
class Audio:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Playing Audio...")
        self.label.grid(row=1, column=1)
        
        # self.playButton = Button(self.master, text="Play", command=pygame.mixer.music.play(), height=7, width=15)
        # self.playButton.grid(row=3, column=40)
        
        # self.pauseButton = Button(self.master, text="Pause", command=pygame.mixer.music.pause(), height=7, width=15)
        # self.pauseButton.grid(row=3, column=40)
        
        # self.skipButton = Button(self.master, text="Skip", command=play_next_audio(current_audio_index), height=7, width=15)
        # self.skipButton.grid(row=3, column=40)
        
        # os.system('python ../Audio_Scripts/contAudioButton2.py')
        
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
class Photo:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Displaying Photo...")
        self.label.grid(row=1, column=1)
        
        os.system('python ../Image_Scripts/display_image.py')

        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)

class Rec:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Choose Microphone or Camera")
        self.label.grid(row=1, column=1)
        
        self.micButton = Button(self.master, text="Microphone", command=self.load_mic, height=7, width=15)
        self.micButton.grid(row=3, column=1)
        
        self.camButton = Button(self.master, text="Camera", command=self.load_cam, height=7, width=15)
        self.camButton.grid(row=4, column=1)
        
        # os.system('python ../Audio_Scripts/mic_recording.py')
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        self.camButton.destroy()
        self.micButton.destroy()
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
    def load_mic(self):
        self.label.destroy()
        self.camButton.destroy()
        self.micButton.destroy()
        self.menuButton.destroy()

        # use `root` with another class
        self.another = Mic(self.master)
        
    def load_cam(self):
        self.label.destroy()
        self.camButton.destroy()
        self.micButton.destroy()
        self.menuButton.destroy()

        # use `root` with another class
        self.another = Cam(self.master)
        
class Mic:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Do you want to start recording?")
        self.label.grid(row=1, column=1)
        
        self.yesButton = Button(self.master, text="Yes", command=self.record, height=7, width=15)
        self.yesButton.grid(row=3, column=1)
        
        self.noButton = Button(self.master, text="No", command=self.record, height=7, width=15)
        self.noButton.grid(row=6, column=1)
        
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.yesButton.destroy()
        self.noButton.destroy()
        self.label.destroy()
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
    def record(self):
        os.system('python ../Audio_Scripts/mic_recording.py')

class Cam:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Photo Time!")
        self.label.grid(row=1, column=1)
        
        os.system('python ../camera/capture_with_button.py')
        
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.menuButton.destroy()
        self.label.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
class Clock:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Starting clock...")
        self.label.grid(row=1, column=1)
        
        # os.system('python ../Alarm/Alarm_Reminder.py')
        
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)

root = Tk()
root.geometry('1020x600')
run = StartScreen(root)
root.mainloop()