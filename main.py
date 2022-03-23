from utils.twillio import TwillioBuilder
from utils.thermometer import Thermometer
import os

client = TwillioBuilder(account_sid=os.getenv('TWILIO_ACCT_SID'), auth_token=os.getenv('TWILIO_AUTH_TOKEN'))

temp = Thermometer.get_reading()

client.send_message(f'The current temperature is: {temp}')
