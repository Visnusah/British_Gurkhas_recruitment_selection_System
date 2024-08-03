from tkinter import *
import tkinter as tk
from tkinter import messagebox
from phase2_part1 import open_phase2_part1
from phase2_part2 import open_phase2_part2,received_data
from db.database import connect_database
from db.type import DATABASE_TYPE


def auto_established_db_connection():
    host = "localhost"
    username= "root"
    password="root"
    db_name  = "BGRSS"
    if(connect_database(DATABASE_TYPE.MYSQL,host,username,password,db_name)):
        print("Database Successfully Connected")
    else:
        print("Failed to Connect Database")

auto_established_db_connection()


def move_next():
    global counter

    if not counter > len(frames):
        for frame in frames:
            frame.pack_forget()
        
        counter += 1
        new_frame = frames[counter]
        new_frame.pack()


def move_back():
    global counter

    if not counter == 0:
        for frame in frames:
            frame.pack_forget()
        
        counter -= 1
        new_frame = frames[counter]
        new_frame.pack()


def data_transfer(value):
    if value is not None:
        received_data(value)


root = tk.Tk()
root.geometry("1250x700+210+100")
root.title("Main Window")

frame_clr= "#DBDBDB"
next_btn_font = ("Trebuchet MS", 17, "bold") # for the forget password and register label

dashboard_frame = tk.Frame(root)
dashboard_frame.pack(fill=tk.BOTH, expand=True)


part1_frame = tk.Frame(dashboard_frame)
part1_frame.pack(fill=tk.BOTH, expand=True)
open_phase2_part1(part1_frame,move_next,move_back, data_transfer)


part2_frame = tk.Frame(dashboard_frame)
part2_frame.pack(fill=tk.BOTH, expand=True)
open_phase2_part2(part2_frame,lambda:None, move_back)

frames = [part1_frame,part2_frame]
counter = 0

root.mainloop()