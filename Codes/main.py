# main.py

import tkinter as tk
from tkinter import messagebox
from testfile1 import open_phase2_part1_window
# from phase2_part1 import open_phase2_part1_window
from db.database import connect_database,execute_query
from db.type import DATABASE_TYPE


def auto_established_db_connection():
    host = "localhost"
    username= "root"
    password="root"
    db_name  = "BGRSS"
    db_mysql =  connect_database(DATABASE_TYPE.MYSQL,host,username,password,db_name)
    db_sqllite =  connect_database(DATABASE_TYPE.SQLITE,db_name=db_name)
    if(db_mysql):
        print("Database Successfully Connected")
    else:
        print("Failed to Connect Database")

auto_established_db_connection()

def main():
    root = tk.Tk()
    root.title("Main Window")

    # Open the login window when the main window starts
    open_phase2_part1_window(root)

    root.mainloop()

if __name__ == "__main__":
    main()
