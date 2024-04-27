import mysql.connector
import config
import configparser
class DatabaseServiceClass:
    
    def __intint__(self):
        pass
        # dbConfig = config.config['DB']
        # self.dataBase = mysql.connector.connect(
        #     host = dbConfig['HOST'],
        #     user = dbConfig['USER'],
        #     password = dbConfig['PASSWORD'],
        #     database = dbConfig['DATABASE']
        # )
        # self.dbCursor = self.dataBase.cursor

    async def writeUser(self, userId, userNickName, userFirstName, userLastName):
        dbConfig = config.config['DB']
        dataBase = mysql.connector.connect(
            host = dbConfig['HOST'],
            user = dbConfig['USER'],
            port = dbConfig['PORT'],
            password = dbConfig['PASSWORD'],
            database = dbConfig['NAME']
        )
        dbCursor = dataBase.cursor()

        if not dataBase.is_connected():
            print("Error connecting to database")
        else:
            try:
                if not dataBase.is_connected():
                    print("Error connecting to database")
                else:
                

                    sqlSelect = "SELECT * FROM users_list WHERE userID = %s"
                    sqlVal = (str(userId), )
                    dbCursor.execute(sqlSelect, sqlVal)
                    selectResult = dbCursor.fetchall()
                    print(len(selectResult))

                    if len(selectResult) == 0:
                        sqlInsert = "INSERT INTO users_list (userID, userNickName, userFirstName, userLastName) VALUES (%s, %s, %s, %s)"
                        val = (userId, userNickName, userFirstName, userLastName)
                        dbCursor.execute(sqlInsert, val)
                        dataBase.commit()
            except mysql.connector.Error as err:
                print("Error:", err)
            dbCursor.close()
            dataBase.close()


        
