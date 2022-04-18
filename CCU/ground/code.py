import digitalio
import board
import time
import radio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

print("Hello")

packet_count = 0

while True:
    led.value = not led.value
    radio_message = radio.try_read()
    if radio_message is not None:
        message = print("Radio Message: {:d} {:s}".format(packet_count, str(radio_message, 'ascii')))
        packet_count = packet_count + 1
    time.sleep(0.5)
