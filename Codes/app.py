from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import customtkinter as ctk

root = Tk()
root.title("British Gurkhas recruitment process")
root.maxsize(1280, 832)
root.minsize(1280, 832)

# fonts -> arial, Helvetica, Times New Roman, Verdana, Comic Sans MS, Courier New, Georgia, Tahoma, Trebuchet MS, Arial Black, Impact, Lucida Console, Palatino Linotype, Book Antiqua, Garamond, Calibri, Candara, Arial Narrow, Arial Rounded MT Bold, Century Gothic, Franklin Gothic Medium, Lucida Sans Unicode, Trebuchet MS, Arial Unicode MS, Tahoma, Geneva, Verdana, Courier New, Lucida Console, Monaco, Lucida Sans Typewriter, Avant Garde, Arial Black, Impact, Charcoal, sans-serif

# root colors and fonts
background = "#2D8A69" 
framefg = "white" 
frame_clr= "#DBDBDB"

font1 = ("Arial", 20, "bold") # for the entry fields, buttons
font2 = ("Trebuchet MS", 15, "bold") # for the forget password and register label
font3 =("Trebuchet MS", 50, "bold") # for the login label

root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False, False)


def open_register():
    print("Register")

# create a main frame
mainFrame = ctk.CTkFrame(root, width=555, height=431, corner_radius=30, bg_color="transparent")
mainFrame.grid(row=0, column=1, padx=350, pady=150)

# create a label for login
login_label = Label(mainFrame,
                    text="Login",
                    font=("Trebuchet MS", 50, "bold"),
                    bg=frame_clr,
                    fg=background)

login_label.place(x=200, y=18)


# Entry field for username
username = ctk.CTkEntry(mainFrame,
                        width=487,
                        height=56, 
                        corner_radius=10, 
                        font=font1,
                        fg_color=background,
                        text_color=framefg,
                        placeholder_text="Username",
                        placeholder_text_color=framefg)

username.place(x=40, y=130)

# entry field for password
password = ctk.CTkEntry(mainFrame,
                        width=487,
                        height=56,
                        corner_radius=10,font=("Arial", 20),
                        show="*",
                        fg_color=background,
                        text_color=framefg,
                        placeholder_text="Password",
                        placeholder_text_color="white")

password.place(x=40, y=210)


# create a button for login
login_btm = ctk.CTkButton(mainFrame,
                          text="Login",
                          width=120,height=40,
                          corner_radius=10,
                          font=font2,
                          command=lambda: print("Login"),
                          fg_color="#314C3B")

login_btm.place(x=200, y=290)


# create a forget password button and register button
forget_btm = ctk.CTkButton(mainFrame, text="Foget Password?",
                      font=font2, text_color=background,
                      fg_color=frame_clr,
                      command=lambda: print("Forget Password"),
                      hover_color=frame_clr,) #color match with the background for visibility of the text
forget_btm.place(x=40, y=360)

new_Account_btm = ctk.CTkButton(mainFrame, text="Don’t have Account ?",
                      font=font2, text_color=background,
                      fg_color=frame_clr,
                      command=open_register,
                      hover_color=frame_clr,) #color match with the background for visibility of the text
new_Account_btm.place(x=350, y=360)



# create a image object with reference NOTE: for the logo
imageOne = ImageTk.PhotoImage(Image.open("Assets/logo.png")) # open the image
logo_icon = Label(root, image = imageOne, bg=background) # attach the image to a label
logo_icon.image = imageOne # keep a reference to the image object to prevent garbage collection by python
logo_icon.place(x= 20, y=0) # place the label in the window

# create a image object with reference NOTE: for the user icon
imageThree = ImageTk.PhotoImage(Image.open("Assets/user.png").resize((31,31))) # open the image
User_icon = Label(mainFrame, image = imageThree, bg=background) # attach the image to a label
User_icon.image = imageThree # keep a reference to the image object to prevent garbage collection by python
User_icon.place(x= 470, y= 139) # place the label in the window

# create a image object with reference NOTE: for the password icon
imageTwo = ImageTk.PhotoImage(Image.open("Assets/password.png").resize((31,31))) # open the image
password_icon = Label(mainFrame, image = imageTwo, bg=background) # attach the image to a label
password_icon.image = imageTwo # keep a reference to the image object to prevent garbage collection by python
password_icon.place(x= 470, y=218, ) # place the label in the window

root.mainloop()