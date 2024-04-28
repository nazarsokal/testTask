from telebot.types import User
import sqlite3
 
class DatabaseServiceClass:
    def __init__(self):

        self.dataBase = sqlite3.connect('database\\database.db')
        self.dbCursor = self.dataBase.cursor()

        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS users_list (userID VARCHAR(255), userNickName VARCHAR(255), userFirstName VARCHAR(255), userLastName VARCHAR(255))")
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS announcement_table (userID VARCHAR(255), messageID VARCHAR(255), userAnnouncementTitle VARCHAR(255), userAnnouncementBody TEXT, photoID VARCHAR(255), isClosed TINYINT(1) DEFAULT '0')")

    def writeUser(self, user : User):
        sqlSelect = "SELECT * FROM users_list WHERE userID = ?"
        sqlVal = (str(user.id), )
        self.dbCursor.execute(sqlSelect, sqlVal)
        selectResult = self.dbCursor.fetchall()
        if len(selectResult):
            return
        
        sqlInsert = "INSERT INTO users_list (userID, userNickName, userFirstName, userLastName) VALUES (?, ?, ?, ?)"
        val = (user.id, user.username, user.first_name, user.last_name)
        self.dbCursor.execute(sqlInsert, val)
        self.dataBase.commit()

    def writeUserAnnouncement(self, userID: int,
                              messageID: int,
                              userAnnounecementTitle: str,
                              userAnnounecementBody: str,
                              photoID: str | None):
        sqlInsert = "INSERT INTO announcement_table (userID, messageID, userAnnouncementTitle ,userAnnouncementBody, photoID, isClosed) VALUES (?, ?, ?, ?, ?, ?)"
        sqlInsertValue = (userID, messageID, userAnnounecementTitle, userAnnounecementBody, photoID, False)
        self.dbCursor.execute(sqlInsert, sqlInsertValue)
        self.dataBase.commit()
    
    def get_user_requests(self, userID) -> list[dict]:
        sqlSelectAnnouncement = "SELECT userID, messageID, userAnnouncementTitle ,userAnnouncementBody, photoID, isClosed FROM announcement_table WHERE userID = ?"
        sqlVal = (userID, )
        self.dbCursor.execute(sqlSelectAnnouncement, sqlVal)
        selectAnnResult = self.dbCursor.fetchall()
        result = [{
            "userID":dt[0],
            "messageID":dt[1],
            "title": dt[2],
            "body":dt[3],
            "photo":dt[4],
            "isClosed":dt[5],
        } for dt in selectAnnResult]
        return result

    def close(self):
        self.dbCursor.close()
        self.dataBase.close()
                