from gpiozero import Button

class FSR_Button:
    def __init__(self, pin, on_fcn, off_fcn):
        self.on_fcn = on_fcn
        self.off_fcn = off_fcn

        self.button = Button(pin, pull_up=False)

    def activate(self):
        if self.button.is_pressed:
            self.on_fcn()
        else:
            self.off_fcn()


def print_ON():
    print("Button is pressed")

def print_OFF():
    print("Button is NOT pressed")

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
