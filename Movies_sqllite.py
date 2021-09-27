from sqlite3.dbapi2 import Cursor
from flask import Flask , request , jsonify
import json
import sqlite3
app = Flask (__name__)

#function to connect to the database
def db_connection():
    conn = None 
    try:
        conn = sqlite3.connect('Movies.sqlite')
    except sqlite3.error as fehler:
        print(fehler)
    return conn
@app.route("/")

def index():
    return "Hello World."


@app.route("/movies", methods = ['GET', 'POST'])    
def movies():
    #grab the database Connection
    conn = db_connection()
    #grab the cursor Object
    cursor = conn.cursor()
    if request.method == 'GET':
        # This will grab all Movies in the database and save them in cursor variable
        cursor = conn.execute("SELECT * FROM Movie")
        allmovies = [
            dict(id=row[0], Movie_Name = row[1])
            for row in cursor.fetchall()
        ]
        if allmovies is not None:
            return jsonify(allmovies)
    # postin new movies to the database    
    if request.method == 'POST':
        new_movie = request.form['Movie_Name']
        sql = """ INSERT INTO Movie (Movie_Name)
            VALUES (? ) """
        #the , after new movies is to indicate that this is a string
        cursor = cursor.execute(sql, (new_movie,))
        conn.commit()
        return f"Movie with the id: {cursor.lastrowid} created seccessfully"