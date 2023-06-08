from gpiozero import Button

class FSR_Button:
    def __init__(self, pin):
        self.button = Button(pin, pull_up=False)
        self.toggle = False

    def activate(self, on_fcn, off_fcn):
        if self.button.is_pressed:
            self.toggle = not self.toggle

        if self.toggle:
            on_fcn()
        else:
            off_fcn()


def print_ON():
    print("Button is on Play mode")

def print_OFF():
    print("Button is Pause mode")

if __name__ == "__main__":
    button = FSR_Button(17, print_ON, print_OFF)
    while True:
        button.activate()

"""
button = Button(17, pull_up=False)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is NOT pressed")
"""
