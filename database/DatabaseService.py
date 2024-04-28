from telebot.types import User
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


    def writeUser(self, user : User):
        sqlSelect = "SELECT * FROM users_list WHERE userID = %s"
        sqlVal = (str(user.id), )
        self.dbCursor.execute(sqlSelect, sqlVal)
        selectResult = self.dbCursor.fetchall()
        if len(selectResult) == 0:
            sqlInsert = "INSERT INTO users_list (userID, userNickName, userFirstName, userLastName) VALUES (%s, %s, %s, %s)"
            val = (user.id, user.username, user.first_name, user.last_name)
            self.dbCursor.execute(sqlInsert, val)
            self.dataBase.commit()
            self.close()

    def writeUserAnnouncement(self, userID, messageID, userAnnounecementTitle ,userAnnounecementBody, photoID):
        sqlInsert = "INSERT INTO announcement_table (userID, messageID, userAnnouncementTitle ,userAnnouncementBody, photoID) VALUES (%s, %s, %s, %s, %s)"
        sqlInsertValue = (userID, messageID, userAnnounecementTitle, userAnnounecementBody, photoID)
        self.dbCursor.execute(sqlInsert, sqlInsertValue)
        self.dataBase.commit()
        self.close()
    
    def get_user_requests(self, userID):
        sqlSelectAnnouncement = "SELECT * FROM announcement_table (userID, messageID, userAnnounecementTitle ,userAnnounecementBody, photoID) WHERE userID = %s"
        sqlVal = (userID)
        self.dbCursor.execute(sqlSelectAnnouncement, sqlVal)
        selectAnnResult = self.dbCursor.fetchall()
        self.close()
        return selectAnnResult

    def close(self):
        self.dbCursor.close()
        self.dataBase.close()
        
    #назар лох
        