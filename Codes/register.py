from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import sqlite3 as db

root = Tk()
root.maxsize(1280, 832)
root.minsize(1280, 832)

root.geometry("1250x700+210+100")
root.title("British Gurkhas recruitment process")


# root colors and fonts
background = "#2D8A69" 
framefg = "white" 
frame_clr= "#DBDBDB"

root.config(bg=background)
root.resizable(False, False)

font1 = ("Arial", 20) # for the entry fields, buttons
font2 = ("Trebuchet MS", 15, "bold") # for the forget password and register label
font3 =("Trebuchet MS", 50, "bold") # for the login label

# connect to the database
conn = db.connect("database.db")
cursor = conn.cursor()



#functions
def logout():
    root.destroy()
    import login
    login.root.mainloop()

# create a main frame
main_Frame = ctk.CTkFrame(root, width=724, height=587, corner_radius=30)
main_Frame.grid(row=0, column=1, padx=278, pady=122)


Sign_up_label = Label(main_Frame,
                      text="Sign Up",
                      font=font3,
                      bg=frame_clr,
                      fg=background)
Sign_up_label.place(x=279, y=10)

# create a label for the username, password, email, dob, number, and repassword
name_entry = ctk.CTkEntry(main_Frame,
                          width=291,
                          height=56,
                          font=font1,
                          placeholder_text="Name")
name_entry.place(x=40, y=134)

email_entry = ctk.CTkEntry(main_Frame,
                           width=291,
                           height=56,
                           font=font1,
                           placeholder_text="Email")
email_entry.place(x=392, y=134)

dob_entry = ctk.CTkEntry(main_Frame,
                         width=291,
                         height=56,
                         font=font1,
                         placeholder_text="Date of Birth")
dob_entry.place(x=40, y=217)

password_entry = ctk.CTkEntry(main_Frame,
                              width=291,
                              height=56,
                              font=font1,
                              show="*",
                              placeholder_text="Password")
password_entry.place(x=392, y=217)

number_entry = ctk.CTkEntry(main_Frame,
                            width=291,
                            height=56,
                            font=font1,
                            placeholder_text="Phone Number")
number_entry.place(x=40, y=300)

repassword_entry = ctk.CTkEntry(main_Frame,
                                width=291,height=56,
                                font=font1,
                                show="*",
                                placeholder_text="Re-enter Password")
repassword_entry.place(x=392, y=300)


# Sign up btn
singin_btn = ctk.CTkButton(main_Frame,
                           text="Sign Up",
                           width=134,
                           height=59,
                           font=font1,
                           command=lambda: messagebox.showinfo("Sign Up", "Sign Up Successful!"),
                           fg_color="#314C3B",
                           hover_color=background)

singin_btn.place(x=292, y=387)

already_have_account = ctk.CTkButton(main_Frame,
                                     text="Already have an account?",
                                     font=font2,
                                     text_color="black",
                                     fg_color=frame_clr,
                                     hover_color=frame_clr,
                                     command=logout)

already_have_account.place(x=258, y=486)


root.mainloop()