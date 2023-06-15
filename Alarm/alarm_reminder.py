

from tkinter import Tk, Label, Button, OptionMenu, StringVar, Text


def edit_alarms3():
    edit_window = Tk()

    # Edit Alarms Page - Components
    Label(edit_window, text="Edit Alarms", font=("Helvetica 20 bold"), fg="black").pack(pady=10)

    # Alarm details display
    alarm_details_label = Label(edit_window, text=alarm_details, font=("Helvetica 12"))
    alarm_details_label.pack()

    # Alarm hour selection
    hour = StringVar(edit_window)
    hours = [str(i).zfill(2) for i in range(1, 13)]
    hour.set(hours[0])
    hour_label = Label(edit_window, text="Hour:", font=("Helvetica 15"))
    hour_label.pack()
    hour_option_menu = OptionMenu(edit_window, hour, *hours)
    hour_option_menu.pack()

    # Alarm minute selection
    minute = StringVar(edit_window)
    minutes = [str(i).zfill(2) for i in range(60)]
    minute.set(minutes[0])
    minute_label = Label(edit_window, text="Minute:", font=("Helvetica 15"))
    minute_label.pack()
    minute_option_menu = OptionMenu(edit_window, minute, *minutes)
    minute_option_menu.pack()

    # Label selection
    label = StringVar(edit_window)
    label_options = ['Sleep', 'Wake up', 'Exercise']
    label.set(label_options[0])
    label_label = Label(edit_window, text="Label:", font=("Helvetica 15"))
    label_label.pack()
    label_option_menu = OptionMenu(edit_window, label, *label_options)
    label_option_menu.pack()

    # Save button
    def save_alarm_details():
        global alarm_details
        alarm_hour = hour.get()
        alarm_minute = minute.get()
        alarm_label_text = label.get()
        alarm_details = f"Alarm setting: {alarm_hour}:{alarm_minute}  {alarm_label_text}"
        alarm_details_label.config(text=alarm_details)
        alarm_label.config(text=alarm_details)  
        edit_window.destroy()

    save_button = Button(edit_window, text="Save", font=("Helvetica 15"), command=save_alarm_details)
    save_button.pack(pady=20)

    edit_window.mainloop()



# In[2]:


def open_set_alarm2():
    root = Tk()

    # Set Alarm Page - Components
    Label(root, text="Set Alarm", font=("Helvetica 20 bold"), fg="black").pack(pady=10)

    # Hour selection
    hour = StringVar(root)
    hours = [str(i).zfill(2) for i in range(1, 13)]
    hour.set(hours[0])
    hour_label = Label(root, text="Hour:", font=("Helvetica 15"))
    hour_label.pack()
    hour_option_menu = OptionMenu(root, hour, *hours)
    hour_option_menu.pack()

    # Minute selection
    minute = StringVar(root)
    minutes = [str(i).zfill(2) for i in range(60)]
    minute.set(minutes[0])
    minute_label = Label(root, text="Minute:", font=("Helvetica 15"))
    minute_label.pack()
    minute_option_menu = OptionMenu(root, minute, *minutes)
    minute_option_menu.pack()

    # AM/PM selection
    period = StringVar(root)
    periods = ['AM', 'PM']
    period.set(periods[0])
    period_label = Label(root, text="Period:", font=("Helvetica 15"))
    period_label.pack()
    period_option_menu = OptionMenu(root, period, *periods)
    period_option_menu.pack()

    # Repeat selection
    repeat = StringVar(root)
    repeat_options = ['Once', 'Daily', 'Weekly']
    repeat.set(repeat_options[0])
    repeat_label = Label(root, text="Repeat:", font=("Helvetica 15"))
    repeat_label.pack()
    repeat_option_menu = OptionMenu(root, repeat, *repeat_options)
    repeat_option_menu.pack()


    labels=StringVar(root)
    label_options = ['Sleep', 'Wake up', 'Exercise']
    labels.set(label_options[0])
    _label = Label(root, text="Label:", font=("Helvetica 15"))
    _label.pack()
    _option_menu = OptionMenu(root, labels, *label_options)
    _option_menu.pack()

    # Sound selection
    sound = StringVar(root)
    sound_options = ['Sound 1', 'Sound 2', 'Sound 3']
    sound.set(sound_options[0])
    sound_label = Label(root, text="Sound:", font=("Helvetica 15"))
    sound_label.pack()
    sound_option_menu = OptionMenu(root, sound, *sound_options)
    sound_option_menu.pack()

    # Snooze selection
    snooze = StringVar(root)
    snooze_options = ['Off', '5 minutes', '10 minutes', '15 minutes']
    snooze.set(snooze_options[0])
    snooze_label = Label(root, text="Snooze:", font=("Helvetica 15"))
    snooze_label.pack()
    snooze_option_menu = OptionMenu(root, snooze, *snooze_options)
    snooze_option_menu.pack()

    # Set Alarm button
    def set_alarm2(alarm_label, alarm_name):
        global alarm_details

        alarm_hour = hour.get()
        alarm_minute = minute.get()
        alarm_period = period.get()
        alarm_repeat = repeat.get()
        alarm_label_text = labels.get()
        alarm_sound = sound.get()
        alarm_snooze = snooze.get()

        alarm_details = f"Alarm {alarm_name} setting:\nTime: {alarm_hour}:{alarm_minute}  {alarm_label_text} "
        alarm_label.config(text=alarm_details)
        root.destroy()

    save_button = Button(root, text="Save Alarm", font=("Helvetica 15"))
    save_button.configure(command=lambda: set_alarm2(alarm_label, "1"))
    save_button.pack(pady=20)

    root.mainloop()



root = Tk()

# Main Page - Components
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="black").pack(pady=10)
alarm_label = Label(root, text="", font=("Helvetica 12"))
alarm_label.pack()
Button(root, text="+ Set New Alarm", font=("Helvetica 20"), command=open_set_alarm2).pack(side="top", anchor="ne")
Button(root, text="Edit Alarms", font=("Helvetica 20"), command=edit_alarms3).pack(side="top", anchor="nw")


root.mainloop()


