from utils.twillio import TwillioBuilder
from utils.thermometer import Thermometer

client = TwillioBuilder(account_sid='ACfb0c56c2ba89c89d62e6e41f2d1dff3f', auth_token='4de437c048d1053f5bbbc66a54c61593')

temp = Thermometer.get_reading()

client.send_message(f'The current temperature is: {temp}')
