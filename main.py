from utils.thermometer import Thermometer
import os
from datetime import datetime
import time
from config.config_parser import ConfigGetter
from apscheduler.schedulers.background import BackgroundScheduler

if __name__ == '__main__':
    config = ConfigGetter()
    list_of_times = config.get('scheduler', 'execution_times')

    print(f'List of times that the scheuler will send texts: {list_of_times}')
    scheduler = BackgroundScheduler()
    scheduler.add_job(Thermometer.get_reading, 'interval', minutes=1)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()

