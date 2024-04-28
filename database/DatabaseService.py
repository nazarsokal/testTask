import mysql.connector
import config
import configparser
 
class DatabaseServiceClass:
    
    def __init__(self):
        dbConfig = config.config['DB']
        self.dataBase = mysql.connector.connect(
            host = dbConfig['HOST'],
            user = dbConfig['USER'],
            port = dbConfig['PORT'],
            password = dbConfig['PASSWORD'],
            database = dbConfig['NAME']
        )
        self.dbCursor = self.dataBase.cursor()

        try:
            if not self.dataBase.is_connected():
                print("Error connecting to database")
            else:
                ...
        except mysql.connector.Error as err:
            print("Error:", err)
        #self.close()


    def writeUser(self, userId, userNickName, userFirstName, userLastName):
        sqlSelect = "SELECT * FROM users_list WHERE userID = %s"
        sqlVal = (str(userId), )
        self.dbCursor.execute(sqlSelect, sqlVal)
        selectResult = self.dbCursor.fetchall()
        if len(selectResult) == 0:
            sqlInsert = "INSERT INTO users_list (userID, userNickName, userFirstName, userLastName) VALUES (%s, %s, %s, %s)"
            val = (userId, userNickName, userFirstName, userLastName)
            self.dbCursor.execute(sqlInsert, val)
            self.dataBase.commit()
            self.close()

    def writeUserAnnouncement(self, userID: int,
                              messageID: int,
                              userAnnounecementTitle: str,
                              userAnnounecement: str,
                              photoID: str | None):
        sqlInsert = "INSERT INTO request_table (userID, messageID, userAnnounecementTitle ,userRequest, photoID) VALUES (%s, %s, %s, %s, %s)"
        sqlInsertValue = (userID, messageID, userAnnounecementTitle, userAnnounecement, photoID)
        self.dbCursor.execute(sqlInsert, sqlInsertValue)
        self.dataBase.commit()
        self.close()
        
    def close(self):
        self.dbCursor.close()
        self.dataBase.close()
        
    #назар лох
        