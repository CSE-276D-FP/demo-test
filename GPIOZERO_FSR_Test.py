'''
NOTE: This file was used for testing and is not used in the final code. It is used to test the FSR using gpiozero import
'''

from gpiozero import MCP3008
from time import sleep

fsr_pin = 17  # GPIO pin number where the FSR is connected (e.g., GPIO 17)
fsr = MCP3008(channel=fsr_pin)

while True:
    fsr_value = fsr.value
    print(f"FSR Value: {fsr_value}")
    sleep(0.1)  # Delay between readings
