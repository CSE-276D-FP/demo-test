from tkinter import *
from tkinter import font
import os
# import sys
# sys.path.append("../camera")
# from capture import CameraCapture
# from contAudioButton import cont_Audio_Button

class StartScreen:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master 
        custom_font = font.Font(size=40)
        self.label = Label(self.master, text="Menu", font=custom_font)
        self.label.place(x=450, y=20)
        
        custom_font = font.Font(size=55)
        self.audioButton = Button(self.master, text="Audio", command=self.load_audio, height=2, width=5, font=custom_font)
        self.audioButton.place(x=70, y=100)

        self.videoButton = Button(self.master, text="Video", command=self.load_video, height=2, width=5, font=custom_font)
        self.videoButton.place(x=390, y=100)
        
        self.photoButton = Button(self.master, text="Photo", command=self.load_photo, height=2, width=5, font=custom_font)
        self.photoButton.place(x=710, y=100)
        
        self.clockButton = Button(self.master, text="Clock", command=self.load_clock, height=2, width=5, font=custom_font)
        self.clockButton.place(x=710, y=320)
        
        self.recButton = Button(self.master, text="Record", command=self.load_rec, height=2, width=5, font=custom_font)
        self.recButton.place(x=390, y=320)
        
        inst_custom_font = font.Font(size=37)
        self.instButton = Button(self.master, text="How To\n Use", command=self.load_inst, height=3, width=7, font=inst_custom_font)
        self.instButton.place(x=70, y=320)

    def load_audio(self):
        self.label.destroy()
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()
        self.instButton.destroy()

        # use `root` with another class
        self.another = Audio(self.master)
        
    def load_video(self):
        # self.audioButton.destroy()
        # self.videoButton.destroy()
        # self.photoButton.destroy()
        # self.recButton.destroy()
        # self.clockButton.destroy()
        # self.instButton.destroy()
        os.system('python ../Video_Scripts/play_video.py')
        
    def load_photo(self):
        os.system('python ../Image_Scripts/display_image.py')
        
    def load_rec(self):
        self.label.destroy()
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()
        self.instButton.destroy()

        # use `root` with another class
        self.another = Rec(self.master)
        
    def load_clock(self):
        self.label.destroy()
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()
        self.instButton.destroy()

        # use `root` with another class
        self.another = Clock(self.master)
        
    def load_inst(self):
        self.label.destroy()
        self.audioButton.destroy()
        self.videoButton.destroy()
        self.photoButton.destroy()
        self.recButton.destroy()
        self.clockButton.destroy()
        self.instButton.destroy()

        # use `root` with another class
        self.another = Instruction(self.master)


class Video:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Playing Timelapse...")
        self.label.grid(row=1, column=1)
        
        self.menuButton = Button(self.master, text="Menu", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
class Audio:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Play/Pause/Skip Audio Messages on Bear")
        self.label.grid(row=1, column=1)
        
        # self.playButton = Button(self.master, text="Play", command=pygame.mixer.music.play(), height=7, width=15)
        # self.playButton.grid(row=3, column=40)
        
        # self.pauseButton = Button(self.master, text="Pause", command=pygame.mixer.music.pause(), height=7, width=15)
        # self.pauseButton.grid(row=3, column=40)
        
        # self.skipButton = Button(self.master, text="Skip", command=play_next_audio(current_audio_index), height=7, width=15)
        # self.skipButton.grid(row=3, column=40)
        
        # os.system('python ../Audio_Scripts/contAudioButton2.py')
        
        self.menuButton = Button(self.master, text="Menu", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
# class Photo:
#     def __init__(self, master):

#         # keep `root` in `self.master`
#         self.master = master

#         self.label = Label(self.master, text="")
#         self.label.grid(row=1, column=1)
        
#         os.system('python ../Image_Scripts/display_image.py')

#         self.menuButton = Button(self.master, text="Back", command=self.load_menu, height=2, width=8)
#         self.menuButton.grid(row=4, column=4)
        
#     def load_menu(self):
#         self.label.destroy()
#         self.menuButton.destroy()
        
#         # use `root` with another class
#         self.another = StartScreen(self.master)

class Rec:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master
        
        custom_font = font.Font(size=30)
        self.label = Label(self.master, text="Choose Microphone or Camera", font=custom_font)
        self.label.place(x=200, y=20)
        
        custom_font = font.Font(size=45)
        self.micButton = Button(self.master, text="Microphone", command=self.load_mic, height=2, width=9, font=custom_font)
        self.micButton.place(x=105, y=150)
        
        self.camButton = Button(self.master, text="Camera", command=self.load_cam, height=2, width=9, font=custom_font)
        self.camButton.place(x=580, y=150)
        
        # os.system('python ../Audio_Scripts/mic_recording.py')
        self.menuButton = Button(self.master, text="Menu", command=self.load_menu, height=2, width=9, font=custom_font)
        self.menuButton.place(x=330, y=330)
        
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
        
        custom_font = font.Font(size=40)
        self.label = Label(self.master, text="Do you want to start recording?", font=custom_font)
        self.label.place(x=250, y=20)
        
        custom_font = font.Font(size=60)
        self.yesButton = Button(self.master, text="Yes", command=self.record, height=2, width=8, font=custom_font)
        self.yesButton.place(x=125, y=200)
        
        self.menuButton = Button(self.master, text="Menu", command=self.load_menu, height=2, width=8, font=custom_font)
        self.menuButton.place(x=600, y=200)
        
        
    def load_menu(self):
        self.yesButton.destroy()
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

        custom_font = font.Font(size=25)
        self.label = Label(self.master, text="Do you want to take a photo or a timelapse Video?", font=custom_font)
        self.label.place(x=110, y=20)
        
        custom_font = font.Font(size=45)
        self.photoButton = Button(self.master, text="Photo", command=self.load_photo, height=2, width=9, font=custom_font)
        self.photoButton.place(x=105, y=150)
        
        self.tlButton = Button(self.master, text="Timelapse\n Video", command=self.load_tl, height=2, width=9, font=custom_font)
        self.tlButton.place(x=580, y=150)
        
        self.menuButton = Button(self.master, text="Menu", command=self.load_menu, height=2, width=9, font=custom_font)
        self.menuButton.place(x=330, y=330)
        
        
    def load_menu(self):
        self.photoButton.destroy()
        self.tlButton.destroy()
        self.menuButton.destroy()
        self.label.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
    def load_photo(self):
        os.system('python ../camera/capture_optimized.py')
        
    def load_tl(self):
        os.system('python ../camera/timelapse_with_buttons.py')
        
class Clock:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        self.label = Label(self.master, text="Starting clock...")
        self.label.grid(row=1, column=1)
        
        # os.system('python ../Alarm/Alarm_Reminder.py')
        
        self.menuButton = Button(self.master, text="Menu", command=self.load_menu, height=2, width=8)
        self.menuButton.grid(row=4, column=4)
        
    def load_menu(self):
        self.label.destroy()
        self.menuButton.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)
        
class Instruction:
    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master
        
        self.canvas = Canvas(root)
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Add some content to the scrollable frame
        # for i in range(50):
        #     label = Label(self.scrollable_frame, text="Label {}".format(i))
        #     label.grid(row=i, column=0, sticky="w")
        
        custom_font = font.Font(size=25)
        label = Label(self.scrollable_frame, text="Welcome to the Instructions Page!", font = custom_font)
        # label = Label(self.scrollable_frame, text="Welcome to the Instructions Page!")
        label.grid(row=0, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="Audio: Click on Audio button to hear your saved audio messages. Listen to your personalized messages")
        label.grid(row=1, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="Video: Click on the ‘Video’ button to play your saved timelapse videos. Relive your fun, favorite, and proud moments.")
        label.grid(row=2, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="Photo: Click on the ‘Photo’ button to see your saved photos. The photos will run on a loop and timelapse through your photos.")
        label.grid(row=3, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="         Click ‘Pause’ to stop on a photo. Click ‘Play’ to resume the slideshow. Click ‘Exit’ to return to menu")
        label.grid(row=4, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="Record: Click on Record to either access the ‘Microphone’ or ‘Camera’")
        label.grid(row=5, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="     -Microphone: click on ‘Microphone’ to record an audio message")
        label.grid(row=6, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="         -Click on ‘Yes’ to to open the recording window. Click on ‘Record’ to begin recording. Click on “Exit” to close the window")
        label.grid(row=7, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="     -Camera: click on ‘Camera’ to take a photo or a timelapse video")
        label.grid(row=8, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="         -Click on ‘Photo’ to open camera preview window. Click on ‘Capture’ to take a photo")
        label.grid(row=9, column=0, sticky="w")
        
        label = Label(self.scrollable_frame, text="         -Click on ‘Timelapse Video’ to open camera preview window. Click on ‘Start Capture’ to take a timelapse video")
        label.grid(row=10, column=0, sticky="w")
            
        # Add a button to the scrollable frame
        button = Button(self.scrollable_frame, text="Menu", command=self.load_menu)
        button.grid(row=20, column=0, pady=10)

        # Place the canvas and scrollbar in the root window
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Configure grid weights to allow expansion
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        root.mainloop()
    
        
    def load_menu(self):
        self.canvas.destroy()
        
        # use `root` with another class
        self.another = StartScreen(self.master)


root = Tk()
root.geometry('1024x530')
root.configure(bg='grey')
run = StartScreen(root)
root.mainloop()