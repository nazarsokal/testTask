import configparser
import mysql.connector
# class ConfigManager:
#     def __init__(self) -> None:
#         self.config = configparser.ConfigParser()
#         self.config.read('config/config.ini')
    
config = configparser.ConfigParser()
config.read('config/config.ini')

TOKEN = config['BOT']['TOKEN']
ANNOUNCEMENT_CHANNEL_ID = config['FEEDBACK']['ANNOUNCEMENT_CHANNEL_ID']