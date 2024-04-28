import configparser
    
config = configparser.ConfigParser()
config.read('config/config.ini')

TOKEN = config['BOT']['TOKEN']

ANNOUNCEMENT_CHANNEL_ID = config['CHATS']['ANNOUNCEMENT_CHANNEL_ID']
ANNOUNCEMENT_CHANNEL_LINK = config['CHATS']['ANNOUNCEMENT_CHANNEL_LINK']
SUPPORT_GROUP_LINK = config['CHATS']['SUPPORT_GROUP_LINK']