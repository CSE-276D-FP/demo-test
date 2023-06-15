import os
import tkinter as tk
from tkinter import font
from PIL import ImageTk

def open_alarm():
   os.system('alarm_reminder.py')

def open_stopwatch():
    os.system('python stopwatch.py')

def open_timer():
    os.system('python timer.py')

# the main window
window = tk.Tk()
window.title("Alarm Clock")


# buttons for alarm, stopwatch, and timer with icons
custom_font = font.Font(size=45)
alarm_button = tk.Button(window, text="Alarm", command=open_alarm, font=custom_font)
alarm_button.place(x=105, y=150)

stopwatch_button = tk.Button(window, text="Stopwatch", command=open_stopwatch, font=custom_font)
stopwatch_button.place(x=580, y=150)

timer_button = tk.Button(window, text="Timer", command=open_timer, font=custom_font)
timer_button.place(x=330, y=330)

alarm_button = tk.Button(window, text="Alarm", command=open_alarm, font=custom_font)
alarm_button.place(x=105, y=150)

stopwatch_button = tk.Button(window, text="Stopwatch", command=open_stopwatch, font=custom_font)
stopwatch_button.place(x=580, y=150)

# the main event loop
window.geometry('1024x530')
window.mainloop()
