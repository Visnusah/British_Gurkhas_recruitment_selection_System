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

background = "#2D8A69"
framebg = "black"
framefg = "white"

root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False, False)

style_container = ttk.Style()
style_container.theme_use("default")
style_container.configure('elder.TFrame', background="white", foreground="black")

style = ttk.Style()
style.theme_use("default")
style.configure('elder.TButton',
                background='#316B94',
                foreground='white',
                font=('arial', 15),
                padding=[50,10,50,10])
style.map('elder.TButton', background=[('active', '#FFCB3B')])




# create a main frame
mainFrame = ctk.CTkFrame(root, width=555, height=431, corner_radius=30, bg_color="transparent")
mainFrame.grid(row=0, column=1, padx=350, pady=150)

# create a label for login
login_label = Label(mainFrame, text="Login", font=("Trebuchet MS", 50, "bold"), bg="#DBDBDB", fg=background)
login_label.place(x=200, y=18)




# Entry fields for username and password
username = ctk.CTkEntry(mainFrame, width=487, height=56, corner_radius=10, font=("Arial ", 20), fg_color=background, text_color="white", placeholder_text="Username", placeholder_text_color="white")
username.place(x=40, y=130)


password = ctk.CTkEntry(mainFrame, width=487,height=56, corner_radius=10, font=("Arial", 20), show="*", fg_color=background, text_color="white", placeholder_text="Password", placeholder_text_color="white")
password.place(x=40, y=210)


# create a button for login
login_btm = ctk.CTkButton(mainFrame, text="Login", width=120, height=40, corner_radius=20, font=("Trebuchet MS", 20), command=lambda: print("Login"), fg_color="#314C3B")
login_btm.place(x=200, y=290)

# create a forget password button and register button
label1 = ctk.CTkLabel(mainFrame, text="Foget Password?", font=("Trebuchet MS", 15, "bold"), text_color=background, cursor="hand2")
label1.place(x=40, y=360)
# fonts -> arial, Helvetica, Times New Roman, Verdana, Comic Sans MS, Courier New, Georgia, Tahoma, Trebuchet MS, Arial Black, Impact, Lucida Console, Palatino Linotype, Book Antiqua, Garamond, Calibri, Candara, Arial Narrow, Arial Rounded MT Bold, Century Gothic, Franklin Gothic Medium, Lucida Sans Unicode, Trebuchet MS, Arial Unicode MS, Tahoma, Geneva, Verdana, Courier New, Lucida Console, Monaco, Lucida Sans Typewriter, Avant Garde, Arial Black, Impact, Charcoal, sans-serif
label2 = ctk.CTkLabel(mainFrame, text="Don’t have Account ?",  font=("Trebuchet MS", 15, "bold"), text_color=background, cursor="hand2")
label2.place(x=350, y=360)

# create a image object with reference NOTE:
imageOne = ImageTk.PhotoImage(Image.open("Assets/logo.png")) # open the image
labenOne = Label(root, image = imageOne, bg=background) # attach the image to a label
labenOne.image = imageOne # keep a reference to the image object to prevent garbage collection by python
labenOne.place(x= 20, y=0) # place the label in the window

# label for logo title



root.mainloop()