#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
from PySide2 import QtCore, QtGui, QtWidgets, QtSvg, QtXml
import tkinter as Tkinter
import datetime
import time


# In[10]:


counter = datetime.timedelta()
running = False

def counter_label(label):
    def count():
        if running:
            global counter

            # To manage the initial delay.
            if counter == datetime.timedelta():
                display = "Starting..."
            else:
                display = str(counter)

            label['text'] = display
            counter += datetime.timedelta(seconds=1)
            label.after(1000, count)  # Call count function again after 1 second

    # Triggering the start of the counter.
    count()

# start function of the stopwatch
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

# Stop function of the stopwatch
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False

# Reset function of the stopwatch
def Reset(label):
    global counter
    counter = datetime.timedelta()

    # If reset is pressed after pressing stop.
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Use stopwatch!'
    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'

root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=100)
label = Tkinter.Label(root, text="Use stopwatch!", fg="black", font="ROMAN 20 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
root.mainloop()


# In[ ]:




