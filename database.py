import sqlite3
from sqlite3 import Error


class Database:

    def __init__(self) -> None:
        self.conn = None
        try:
            self.conn = sqlite3.connect("sqlite.db")
            return self
        except Error as e:
            print(e)
    

    def create_table(self, sql):
        try:
            c = self.conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)




