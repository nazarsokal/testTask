import mysql.connector
import config
import configparser
 
class DatabaseServiceClass:
    
    def __intint__(self):
        pass


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
                    if len(selectResult) == 0:
                        if userNickName == None:
                            userNickName = "-"
                        sqlInsert = "INSERT INTO users_list (userID, userNickName, userFirstName, userLastName) VALUES (%s, %s, %s, %s)"
                        val = (userId, userNickName, userFirstName, userLastName)
                        dbCursor.execute(sqlInsert, val)
                        dataBase.commit()
            except mysql.connector.Error as err:
                print("Error:", err)
            dbCursor.close()
            dataBase.close()


        
