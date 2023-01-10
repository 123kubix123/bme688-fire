import time
import board
import busio
import adafruit_bme680
import json

class BME68X:
    def __init__(self, SCL=board.GP1, SDA=board.GP0):
        # Initialize I2C
        # busio.I2C(SCL, SDA)
        self.i2c = busio.I2C(board.GP1, board.GP0)

        # Create BME68X object
        self.bme68x = adafruit_bme680.Adafruit_BME680_I2C(self.i2c)

        # change this to match the location's pressure (hPa) at sea level
        # bme68x.sea_level_pressure = 1013.25
        self.bme68x.sea_level_pressure = 1013

        # You will usually have to add an offset to account for the temperature of
        # the sensor. This is usually around 5 degrees but varies by use. Use a
        # separate temperature sensor to calibrate this one.
        self.temperature_offset = -2
        self.data = {}
        
    def read_data(self):
        self.data = {
            'temperature': self.bme68x.temperature + self.temperature_offset,
            'gas_resistance': self.bme68x.gas,
            'humidity': self.bme68x.relative_humidity,
            'pressure': self.bme68x.pressure,
            #'altitude': self.bme68x.altitude,
            'air_quality': 0
            }
        
        return self.data