class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "YourPassword",
            "db": "YourDatabase"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getTemperatuurWater(self):
        query = "SELECT TemperatuurWater FROM tbl_Meting"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getTemperatuurOmgeving(self):
        query = "SELECT TemperatuurOmgeving   FROM tbl_Meting"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getLuchvochtigheid(self):
        query = "SELECT Luchtvochtigheid FROM tbl_Meting"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getTijd(self):
        query = "SELECT Tijd FROM tbl_Meting"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def setDataToDatabase(self, TemperatuurOmgevingValue, TemperatuurWaterValue, LuchtvochtigheidValue):
        cursor = self.__connection.cursor()
        query = "INSERT INTO meting (TemperatuurOmgeving, TemperatuurWater, Luchtvochtigheid) VALUES(TemperatuurOmgevingValue, TemperatuurWaterValue, LuchtvochtigheidValue)"
        #combineren van de query en parameter
        command = query.format()
        cursor.execute(command)
        self.__connection.commit()
        cursor.close()
