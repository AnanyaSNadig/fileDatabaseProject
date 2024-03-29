import mysql.connector, os
from datetime import datetime, timedelta

class Database:
    def __init__(self,database, host, user, password, port):
        #port = int(port) if port else 3306
        self.connection = mysql.connector.connect(
            database = database,
            host = host,
            user = user,
            password = password,
            port = port
        )
        self.cursor = self.connection.cursor()

    def get(self, timeFrame):
        query = "SELECT * FROM files WHERE replacedTime >= %s"
        timeFrameDiff = datetime.now() - timedelta(minutes = timeFrame)
        self.cursor.execute(query, ([timeFrameDiff]))
        return self.cursor.fetchall()
    
    # def add(self, filePath, searchString, replaceString, replacedTime):
    #     insert_query = "INSERT INTO files (filePath, searchString, replaceString, replacedTime) VALUES (%s, %s, %s, %s)"
        
    #     #TODO move time logic to Files.update method

    #     self.cursor.execute(insert_query, (filePath, searchString, replaceString, replacedTime))

    #     self.connection.commit()

    
    def add(self, filePath, searchString, replaceString, replacedTime):
        insert_query = "INSERT INTO files (filePath, searchString, replaceString, replacedTime) VALUES (%s, %s, %s, %s)"

        try:
            self.cursor.execute(insert_query, (filePath, searchString, replaceString, replacedTime))
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.connection.rollback() 
            return False 
        else:
            return True  


    def delete(self):
        pass

    def update(self):
        pass

    def close(self):
        self.cursor.close()
        self.connection.close()
