import mysql.connector
import config
import configparser
class DatabaseService:
    
    # check if connection is setteled
    async def establishConnection():
        dataBase = mysql.connector.connect(
            host = config['DB'],
            user = config['DB'],
            password = config['DB']
        )

        if dataBase.is_connected():
            print("Good")