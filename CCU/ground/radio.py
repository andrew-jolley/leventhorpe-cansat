# Version 1 - 27th Feb 2023

# Importing libraries
import digitalio
import board
import busio
import adafruit_rfm9x

# Setting up the radio with SPI pins
spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)

# Starting the radio the radio
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.2)
print("RFM9x radio ready")

def send(message):
    rfm9x.send(message)

def try_read():
    return rfm9x.receive(timeout=1.0)

def rssi():
    return rfm9x.rssi
