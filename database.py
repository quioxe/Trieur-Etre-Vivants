import sqlite3
from sqlite3 import Error
try:
    conn = sqlite3.connect("sqlite.db")
except Error as e:
    print(e)
    conn = None
    
def get_cursor():
    cursor = None
    try:
        cursor = conn.cursor()
    except Error as e:
        print(e)
    return cursor
    
def create_table(sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

    




