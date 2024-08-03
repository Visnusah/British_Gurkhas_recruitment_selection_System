import sqlite3
import mysql.connector
from tkinter import messagebox

from db.type import DATABASE_TYPE

# Global variables for database connection
connection = None
cursor = None

def connect_database(which_db, host=None, user=None, password=None, db_name=None):
    global connection, cursor
    try:
        if which_db == DATABASE_TYPE.SQLITE:
            connection = sqlite3.connect(db_name)
        elif which_db == DATABASE_TYPE.MYSQL:
            connection = mysql.connector.connect(
                host=host, 
                user=user, 
                password=password, 
                database=db_name
            )
        else:
            print("Database Unavailable")
            return False
        cursor = connection.cursor()
        return True
    except (sqlite3.Error, mysql.connector.Error) as error:
        messagebox.showerror("Error", f"Error: {error}")
        return False

def disconnect_database():
    global connection, cursor
    try:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    except (sqlite3.Error, mysql.connector.Error) as err:
        messagebox.showerror("Error", f"Error: {err}")

def execute_query(query):
    global cursor, connection
    try:
        if cursor:
            cursor.execute(query)
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
            else:
                connection.commit()
                return cursor.lastrowid
        else:
            messagebox.showerror("Error", "No database connection established")
            return None
    except (sqlite3.Error, mysql.connector.Error) as error:
        messagebox.showerror("Error", f"Error: {error}")
        return None
