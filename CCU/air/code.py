# SPDX-FileCopyrightText: 2020 by Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import digitalio
import busio
import adafruit_scd4x
import adafruit_tca9548a
import adafruit_bmp280
import adafruit_sgp30
import adafruit_rfm9x


i2c = busio.I2C(board.GP27, board.GP26)

tca = adafruit_tca9548a.TCA9548A(i2c)

scd4x = adafruit_scd4x.SCD4X(tca[0])
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(tca[1], address=0x76)
sgp30 = adafruit_sgp30.Adafruit_SGP30(tca[2])
spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)

# start the radio
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.2)
rfm9x.tx_power = 23

print("RFM9x radio ready")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

packet_count = 0


# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
print("Serial number:", [hex(i) for i in scd4x.serial_number])


print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.set_iaq_baseline(0x8973, 0x8AAE)
sgp30.set_iaq_relative_humidity(celsius=22.1, relative_humidity=44)

elapsed_sec = 0

scd4x.start_periodic_measurement()
print("Waiting for first measurement....")


firstPressure = 0
message = 1

while True:
    if firstPressure == 0:
        firstPressure +=1
        bmp280.sea_level_pressure = bmp280.pressure
    else:
        led.value = not led.value
        if scd4x.data_ready:
            time.sleep(1)
            co2 = scd4x.CO2
            humidity = scd4x.relative_humidity
            temperature = bmp280.temperature
            pressure = bmp280.pressure
            bmp280.sea_level_pressure = 1012.06
            voc = sgp30.TVOC
            altitude = bmp280.altitude

            print("CO2: %d ppm" % scd4x.CO2)
            print("Temperature: %0.1f *C" % scd4x.temperature)
            print("Humidity: %0.1f %%" % scd4x.relative_humidity)
            print()
            print('Temperature: {} degrees C'.format(bmp280.temperature))
            print('Pressure: {}hPa'.format(bmp280.pressure))
            print()
            print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
            time.sleep(1)
            print(sgp30.baseline_eCO2, sgp30.baseline_TVOC)

            print()
            print()

            print("[LevCanSat] Radio Message {0} | CO2: {1} PPM, Pressure: {2} mbar, Temperature: {3} degrees C, VOC: {4} PPB, Altitude: {5}M.".format(message, co2, pressure, temperature, voc, altitude))

            rfm9x.send("[LevCanSat] Radio Message {0} | CO2: {1} PPM, Pressure: {2} mbar, Temperature: {3} degrees C, VOC: {4} PPB, Altitude: {5}M.".format(message, co2, pressure, temperature, voc, altitude))
            message += 1

        time.sleep(1)
