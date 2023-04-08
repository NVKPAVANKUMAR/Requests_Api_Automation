import configparser
import os
from pathlib import Path

path = Path(__file__)
ROOT_DIR = path.parent.parent.absolute()
config_path = os.path.join(ROOT_DIR, "configurations/config.ini")
# config_path = '..\\configurations\\config.ini'
print(config_path)
config = configparser.RawConfigParser()
config.read(config_path)
base_uri: str = config.get('common info', 'BASE_URI')


class ReadConfig:

    @staticmethod
    def getBaseURI():
        base_uri: str = config.get('common info', 'BASE_URI')
        return base_uri
