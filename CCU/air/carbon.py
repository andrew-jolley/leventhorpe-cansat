# SPDX-FileCopyrightText: 2020 by Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import busio
import adafruit_scd30

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(scl=board.GP13, sda=board.GP12)


scd = adafruit_scd30.SCD30(i2c)
# scd.temperature_offset = 10
#print("Temperature offset:", scd.temperature_offset)

# scd.measurement_interval = 4
#print("Measurement interval:", scd.measurement_interval)

# scd.self_calibration_enabled = True
#print("Self-calibration enabled:", scd.self_calibration_enabled)

# scd.ambient_pressure = 1100
#print("Ambient Pressure:", scd.ambient_pressure)

# scd.altitude = 100
#print("Altitude:", scd.altitude, "meters above sea level")

# scd.forced_recalibration_reference = 409
#print("Forced recalibration reference:", scd.forced_recalibration_reference)
#print("")

def value():
    return scd.CO2

def temp():
    return scd.temperature

def pressure():
    return scd.ambient_pressure

def humidity():
    return scd.relative_humidity

def altitude():
    return scd.altitude

#while True:
    #data = scd.data_available
    #if data:
        #print("Data Available!")
        #print("CO2:", scd.CO2, "PPM")
        #print("Temperature:", scd.temperature, "degrees C")
        #print("Humidity::", scd.relative_humidity, "%%rH")
        #print("")
        #print("Waiting for new data...")
        #print("")

    time.sleep(0.5)
