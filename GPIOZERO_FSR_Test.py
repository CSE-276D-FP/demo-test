from gpiozero import MCP3008
from time import sleep

fsr_pin = 0  # GPIO pin number where the FSR is connected (e.g., GPIO 17)
fsr = MCP3008(channel=fsr_pin)

while True:
    fsr_value = fsr.value
    print(f"FSR Value: {fsr_value}")
    sleep(0.1)  # Delay between readings