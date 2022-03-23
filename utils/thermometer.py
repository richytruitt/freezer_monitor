import datetime
import os
import random
from utils.twillio import TwillioBuilder
from config.config_parser import ConfigGetter

class Thermometer:

    @classmethod
    def get_reading(self):
        client = TwillioBuilder(account_sid=os.getenv('TWILIO_ACCT_SID'), auth_token=os.getenv('TWILIO_AUTH_TOKEN'))
        config = ConfigGetter()

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
            temp = random.randint(0,2)

        current_time = datetime.datetime.now().strftime('%R')

        list_of_times = config.get('scheduler', 'execution_times')
        if current_time in list_of_times or temp > 3:
            if temp > 3:
                client.send_message(f'ALERT! Freezer temp is above allowed threshold')
            else:
                client.send_message(f'The current temperature is: {temp}')

        else:
            print(f'Current temp is fine, and is not a designated time to send a text')