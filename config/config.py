import configparser
    
config = configparser.ConfigParser()
config.read('config/config.ini')

TOKEN = config['BOT']['TOKEN']
ANNOUNCEMENT_CHANNEL_ID = config['BOT']['ANNOUNCEMENT_CHANNEL_ID']