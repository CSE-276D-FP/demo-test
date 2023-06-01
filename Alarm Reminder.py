#!/usr/bin/env python
# coding: utf-8

# In[6]:


from IPython.display import display
import time
import tkinter as tk
import datetime
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image


# In[7]:


import os

current_path = os.getcwd()
print("Current working directory:", current_path)


# In[8]:


import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print("Desktop path:", desktop_path)


# In[10]:


def open_alarm():
    # Implement the alarm function later
    pass

def open_stopwatch():
    # Implement the stopwatch function later
    pass

def open_timer():
    # Implement the timer function later
    pass

# the main window
window = tk.Tk()
window.title("Alarm Clock")


# buttons for alarm, stopwatch, and timer with icons
alarm_button = tk.Button(window, text="Alarm", compound=tk.LEFT, command=open_alarm)
alarm_button.pack(side=tk.LEFT, padx=10, pady=10)

stopwatch_button = tk.Button(window,  text="Stopwatch", compound=tk.LEFT, command=open_stopwatch)
stopwatch_button.pack(side=tk.LEFT, padx=10, pady=10)

timer_button = tk.Button(window, text="Timer", compound=tk.LEFT, command=open_timer)
timer_button.pack(side=tk.LEFT, padx=10, pady=10)

#  the main event loop
window.mainloop()







# In[ ]:




