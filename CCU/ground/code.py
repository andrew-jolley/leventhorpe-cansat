# Version 1 - 27th Feb 2023

# Importing libraries
import digitalio
import board
import time
import radio

# Flash the LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

print("Hello")

# Setting variables
packet_count = 0

# Recieve and display messages
while True:
    led.value = not led.value
    radio_message = radio.try_read()
    if radio_message is not None:
        message = print("{:s}".format(str(radio_message, 'ascii')))
        packet_count = packet_count + 1
    time.sleep(0.5)
