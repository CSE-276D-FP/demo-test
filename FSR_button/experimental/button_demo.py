# Example taken from gpiozero library documentation

from gpiozero import Button

button = Button(19, pull_up=False)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is NOT pressed")
