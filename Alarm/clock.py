import os
import tkinter as tk
from tkinter import font

def open_alarm():
    # Implement the alarm function later
    pass

def open_stopwatch():
    os.system('python stopwatch.py')

def open_timer():
    os.system('python timer.py')

# the main window
window = tk.Tk()
window.title("Alarm Clock")

# Load the icon images
alarm_icon = Image.open("noun-alarm.png")
stopwatch_icon = Image.open("noun-stopwatch-1.png")
timer_icon = Image.open("/noun-timer.png")

# Resize the icons if necessary
icon_width, icon_height = 20, 20  # Adjust the size of the icons as needed
alarm_icon = alarm_icon.resize((icon_width, icon_height))
stopwatch_icon = stopwatch_icon.resize((icon_width, icon_height))
timer_icon = timer_icon.resize((icon_width, icon_height))

# Convert the icons to Tkinter-compatible image objects
alarm_image = ImageTk.PhotoImage(alarm_icon)
stopwatch_image = ImageTk.PhotoImage(stopwatch_icon)
timer_image = ImageTk.PhotoImage(timer_icon)


# buttons for alarm, stopwatch, and timer with icons
custom_font = font.Font(size=45)
alarm_button = tk.Button(window, text="Alarm", image=alarm_image, command=open_alarm, font=custom_font)
alarm_button.place(x=105, y=150)

stopwatch_button = tk.Button(window, text="Stopwatch",image=stopwatch_image, command=open_stopwatch, font=custom_font)
stopwatch_button.place(x=580, y=150)

timer_button = tk.Button(window, text="Timer", image=timer_image,command=open_timer, font=custom_font)
timer_button.place(x=330, y=330)

alarm_button = tk.Button(window, text="Alarm", image=alarm_image, command=open_alarm, font=custom_font)
alarm_button.place(x=105, y=150)

stopwatch_button = tk.Button(window, text="Stopwatch", image=stopwatch_image, command=open_stopwatch, font=custom_font)
stopwatch_button.place(x=580, y=150)

# the main event loop
window.geometry('1024x530')
window.mainloop()
