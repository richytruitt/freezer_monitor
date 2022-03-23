import os
import random

class Thermometer:

    @classmethod
    def get_reading(self):
        try:
            _os = os.uname().nodename

            if _os == 'raspberrypi':
                import adafruit_mcp9808
                import board
                import busio

            print(f'Running on {_os}')
            i2c = busio.I2C(board.SCL, board.SDA)
            mcp = adafruit_mcp9808.MCP9808(i2c)
            temp = ((mcp.temperature) * 9 / 5 + 32)

        except AttributeError:
            print('Running on a local machine, not setting board attributes. Generating random values for temperature')
            temp = random.randint(60,90)

        return temp