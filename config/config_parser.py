import configparser

class ConfigGetter:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config/config.ini')

    def get(self, section, key):
        return self.config[section][key]