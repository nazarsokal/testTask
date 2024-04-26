import configparser

# class ConfigManager:
#     def __init__(self) -> None:
#         self.config = configparser.ConfigParser()
#         self.config.read('config/config.ini')
    
config = configparser.ConfigParser()
config.read('config/config.ini')

bot_config = config['BOT']

TOKEN = bot_config['TOKEN']
ID = bot_config['ID']
USERNAME = bot_config['USERNAME']