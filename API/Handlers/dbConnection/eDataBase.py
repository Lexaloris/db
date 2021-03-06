from API.connection import db1
import MySQLdb

def clear(request):
    try:
        connection = db1.connection
        with connection:
            cursor = connection.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            cursor.execute("TRUNCATE TABLE Followers")
            cursor.execute("TRUNCATE TABLE Forums")
            cursor.execute("TRUNCATE TABLE Posts")
            cursor.execute("TRUNCATE TABLE Subscriptions")
            cursor.execute("TRUNCATE TABLE Threads")
            cursor.execute("TRUNCATE TABLE Users")
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    except MySQLdb.Error:
        raise MySQLdb.Error("Cant drop DataBase")
