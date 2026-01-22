import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="DB_USER",
        password="DB_PASS",
        database="DB_NAME"
    )
