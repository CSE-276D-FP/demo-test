from tkinter import *
import os


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
        
        self.clockButton = Button(self.master, text="Clock", command=self.load_rec, height=7, width=15)
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

class Video:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Playing Video...")
        self.label.grid(row=1, column=1)
        
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
class Audio:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Playing Audio...")
        self.label.grid(row=1, column=1)
        # os.system('python ../Audio_Scripts/continuousAudio.py')
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
class Photo:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Displaying Photo...")
        self.label.grid(row=1, column=1)
        
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)

class Rec:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Start Recording...")
        self.label.grid(row=1, column=1)
        # os.system('python ../Audio_Scripts/mic_recording.py')
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)

root = Tk()
root.geometry('600x400')
run = StartScreen(root)
root.mainloop()