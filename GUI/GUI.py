from tkinter import *


class StartScreen:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master 
        
        self.audioButton = Button(self.master, text="Audio", command=self.load_audio, height=2, width=8)
        self.audioButton.grid(row=2, column=2)

        self.videoButton = Button(self.master, text="Video", command=self.load_video, height=2, width=8)
        self.videoButton.grid(row=4, column=4)

    def load_audio(self):
        self.audioButton.destroy()
        self.videoButton.destroy()

        # use `root` with another class
        self.another = Audio(self.master)
        
    def load_video(self):
        self.audioButton.destroy()
        self.videoButton.destroy()

        # use `root` with another class
        self.another = Video(self.master)


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
        
        self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)


root = Tk()
root.geometry('800x480')
run = StartScreen(root)
root.mainloop()