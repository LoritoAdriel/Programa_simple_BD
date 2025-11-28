import mysql.connector 
from mysql.connector import Error

class Database:
    def __init__(self, host='localhost', user='root', password='root', database='Cine'):
        self.config = dict(host=host, user=user, password=password, database=database)

    def get_connection(self):
        try:
            conn = mysql.connector.connect(**self.config)
            return conn
        except Error as e:
            print('Error de conexión:', e)
            return None
