import sqlite3
from sqlite3.dbapi2 import Cursor
#establish a connection to SQL database if database doesnt exist a new one will be created at that port
conn = sqlite3.connect("Movies.sqlite")
#database must be according to the data design in our fall we have Movies with 2 Attribiute ID and Movie_Name
#cursor Objext to excute SQL statments on the SQL database
cursor = conn.cursor()
#SQL query needs to be excuted using this 
sql_query = """ CREATE TABLE Movie (
    id integer PRIMARY KEY , 
    Movie_Name text NOT NULL
    )"""


cursor.execute(sql_query)