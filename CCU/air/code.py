# importing other information
import digitalio
import board
import time
#import bmp280
import radio
import carbon

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True

packet_count = 0

while True:
    led.value = not led.value
    print("Radio message sent")

    new_carbon = carbon.value()
    new_temp = carbon.temp()
    new_humidity = carbon.humidity()
    new_altitude = carbon.altitude()


    #cansat_temperature = bmp280.read_temperature()
    #room_temp = bmp280.read_temperature()
    #print(cansat_temperature)

    #cansat_pressure = bmp280.read_pressure()
    #room_pressure = bmp280.read_pressure()
    #print(cansat_pressure)

    #Q =  44330 * (1 - (1/1043.4) ** (1/5.255))

    #print("CO2: {:.2f} PPM, Pressure: {:.2f} mbar, Temperature: {:.2f} degrees C, Temperature: {:.2f} degrees C, Humidity: {:.1f} %%rH, Altitude: {:.0f}M.".format(new_carbon, carbon.temp, new_temp, carbon.temp, new_humidity, Q))

    #print("Temperature: {:.3f}^C Pressure: QNH {:.2f}".format(cansat_temperature, cansat_pressure))

    #radio.send("[LevCanSat] Temperature: {:.2f} Pressure {:.0f} mbar".format(room_temp, room_pressure))

    radio.send("[LevCanSat] CO2: {:.2f} PPM, Pressure: {:.2f} mbar, Temperature: {:.2f} degrees C, Temperature: {:.2f} degrees C, Humidity: {:.1f} %%rH, Altitude: {:.0f}M.".format(new_carbon, carbon.temp, new_temp, carbon.temp, new_humidity, Q))
    
    led.direction = digitalio.Direction.OUTPUT
    time.sleep(1)

