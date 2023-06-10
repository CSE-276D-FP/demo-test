import time
import tkinter as Tkinter
from tkinter import messagebox
from tkinter import font
import pygame

def play_sound():
    pygame.mixer.music.play()
    
def exit_program():
    timer_root.destroy()

timer_root = Tkinter.Tk()

# setting geometry of tk window
timer_root.geometry('1024x530')
timer_root.title("Timer")


# Define dictionaries for hour, minute, and second options
hour_options = {str(i).zfill(2): i for i in range(0, 24)}
minute_options = {str(i).zfill(2): i for i in range(0, 60)}
second_options = {str(i).zfill(2): i for i in range(0, 60)}

# Set the default values to "00"
hour = Tkinter.StringVar()
minute = Tkinter.StringVar()
second = Tkinter.StringVar()

hour.set("00")
minute.set("00")
second.set("00")


# Use Entry class to take input from the user
hourEntry = Tkinter.OptionMenu(timer_root, hour, *hour_options.keys())
hourEntry.config(width=3, font=("Arial", 50, ""))
hourEntry.place(x=300, y=100)

minuteEntry = Tkinter.OptionMenu(timer_root, minute, *minute_options.keys())
minuteEntry.config(width=3, font=("Arial", 50, ""))
minuteEntry.place(x=400, y=100)

secondEntry = Tkinter.OptionMenu(timer_root, second, *second_options.keys())
secondEntry.config(width=3, font=("Arial", 50, ""))
secondEntry.place(x=500, y=100)

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:

            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        timer_root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
            play_sound()

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

# button widget
custom_font = font.Font(size=45)
btn = Tkinter.Button(timer_root, text='Set Time Countdown', bd='5',command=submit, font=custom_font)
btn.place(x = 200,y = 250)

custom_font = font.Font(size=45)
btn = Tkinter.Button(timer_root, text='Exit', bd='5',command=exit_program, font=custom_font)
btn.place(x = 400, y = 380)

timer_root.mainloop()
