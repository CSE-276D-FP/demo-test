#!/usr/bin/env python
# coding: utf-8

# In[1]:


from iconify import Icon
import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QIcon
from IPython.display import display
import time
import tkinter as tk
import datetime
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
from PySide2 import QtCore, QtGui, QtWidgets, QtSvg, QtXml


# In[4]:


def open_alarm():
    # Implement the alarm function later
    pass

def open_stopwatch():
    pass

def open_timer():
    pass
# the main window
window = tk.Tk()
window.title("Alarm Clock")


# buttons for alarm, stopwatch, and timer with icons
alarm_button = tk.Button(window, text="Alarm", compound=tk.LEFT, command=open_alarm)
alarm_button.pack(side=tk.LEFT, padx=20, pady=20)

stopwatch_button = tk.Button(window,  text="Stopwatch", compound=tk.LEFT, command=open_stopwatch)
stopwatch_button.pack(side=tk.LEFT, padx=20, pady=20)

timer_button = tk.Button(window, text="Timer", compound=tk.LEFT, command=open_timer)
timer_button.pack(side=tk.LEFT, padx=20, pady=20)

#  the main event loop
window.mainloop()


# In[ ]:





# In[ ]:




