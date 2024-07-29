from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3 as db
from threading import *

# Thread for opening register frame because it takes time to load
def threading():
    main_Frame.destroy()
    t1 = Thread(target=open_register)
    t1.start()

    
# Thread for opening login frame because it takes time to load
def threading2():
    main_Frame.destroy()
    t2= Thread(target=create_login_frame)
    t2.start()

# main window
root = Tk()
root.title("British Gurkhas recruitment process")
root.maxsize(1280, 832)
root.minsize(1280, 832)

background = "#2D8A69"
framefg = "white"
frame_clr = "#DBDBDB"

font1 = ("Arial", 20)
font2 = ("Trebuchet MS", 15, "bold")
font3 = ("Trebuchet MS", 50, "bold")

root.config(bg=background)
root.resizable(False, False)
root.geometry("1250x700+210+100")

# show message box when closing the window
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        
root.protocol("WM_DELETE_WINDOW", on_closing) # call on_closing function when closing the window

    
# Login Frame
def create_login_frame():
    
    global main_Frame, username, password
    main_Frame = ctk.CTkFrame(master=root, width=555, height=431, corner_radius=30)
    main_Frame.grid(row=0, column=1, padx=350, pady=150)
    
    login_label = Label(main_Frame, text="Login", font=font3, bg=frame_clr, fg=background)
    login_label.place(x=200, y=18)
    
    username = ctk.CTkEntry(main_Frame, width=487, height=56, corner_radius=10, font=font1,
                            fg_color=background, text_color=framefg, placeholder_text="Username",
                            placeholder_text_color=framefg)
    username.place(x=40, y=130)
    
    password = ctk.CTkEntry(main_Frame, width=487, height=56, corner_radius=10, font=font1, show="*",
                            fg_color=background, text_color=framefg, placeholder_text="Password",
                            placeholder_text_color=framefg)
    password.place(x=40, y=210)
    
    login_Btn = ctk.CTkButton(main_Frame, text="Login", width=120, height=40, corner_radius=10, font=font2,
                              command=save_login, fg_color="#314C3B")
    login_Btn.place(x=200, y=290)
    
    forgot_Btn = ctk.CTkButton(main_Frame, text="Forgot Password?", font=font2, text_color=background,
                               fg_color=frame_clr, command=lambda: print("Forgot Password"),
                               hover_color=frame_clr)
    forgot_Btn.place(x=40, y=360)
    
    new_Account_Btn = ctk.CTkButton(main_Frame, text="Don't have Account?", font=font2, text_color=background,
                                    fg_color=frame_clr, command=threading, hover_color=frame_clr)
    new_Account_Btn.place(x=350, y=360)
    
    try:
        imageOne = ImageTk.PhotoImage(Image.open("Assets/logo.png").resize((150, 115)))
        logo_icon = Label(root, image=imageOne, bg=background)
        logo_icon.image = imageOne
        logo_icon.place(x=20, y=0)
        
        imageThree = ImageTk.PhotoImage(Image.open("Assets/user.png").resize((31, 31)))
        User_icon = Label(main_Frame, image=imageThree, bg=background)
        User_icon.image = imageThree
        User_icon.place(x=470, y=139)
        
        imageTwo = ImageTk.PhotoImage(Image.open("Assets/password.png").resize((31, 31)))
        password_icon = Label(main_Frame, image=imageTwo, bg=background)
        password_icon.image = imageTwo
        password_icon.place(x=470, y=218)
    except Exception as e:
        messagebox.showerror("Image Error", str(e))
        
# Register Frame
def open_register():
    global main_Frame
    main_Frame.destroy()
    
    main_Frame = ctk.CTkFrame(root, width=724, height=587, corner_radius=30)
    main_Frame.grid(row=0, column=1, padx=278, pady=122)

    Sign_up_label = Label(main_Frame,
                          text="Sign Up",
                          font=font3,
                          bg=frame_clr,
                          fg=background)
    Sign_up_label.place(x=279, y=10)
    
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
                                         command=threading2)

    already_have_account.place(x=258, y=486)


# Phase 1    
def open_phase1():
    global main_Frame
    
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=1157, height=600, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=61, pady=189)
    
    # Entry Fields for Application Form
    # First Column
    first_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="First / middle Names", border_color=frame_clr)
    first_name.place(x=80, y=25)
    
    passport_no = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Passport Number", border_color=frame_clr)
    passport_no.place(x=80, y=110)
    
    nnp_no = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="NNP Number",  border_color=frame_clr)
    nnp_no.place(x=80, y=195)
    
    father_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Father's Name", border_color=frame_clr)
    father_name.place(x=80, y=280)
    
    mother_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Mother's Name", border_color=frame_clr)
    mother_name.place(x=80, y=365)
    
    see_year = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="SEE Year", border_color=frame_clr)
    see_year.place(x=80, y=450)
    
    # Second Column
    
    surname = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Surname", border_color=frame_clr)
    surname.place(x=640, y=25)
    
    main_thar = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Main Thar", border_color=frame_clr)
    main_thar.place(x=640, y=110)
    
    attepmpt = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Attempt", border_color=frame_clr)
    attepmpt.place(x=640, y=195)
    
    religion = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Religion", border_color=frame_clr)
    religion.place(x=640, y=280)
    
    district = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="District", border_color=frame_clr)
    district.place(x=640, y=365)
    
    village = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Village", border_color=frame_clr)
    village.place(x=640, y=450)
    
    # Third Column
    dob_ad = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Date of Birth(AD)", border_color=frame_clr)
    dob_ad.place(x=900, y=25)
    
    dob_bd = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Date of Birth(BD)", border_color=frame_clr)
    dob_bd.place(x=900, y=110)
    
    contact_no = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Contact Number", border_color=frame_clr)
    contact_no.place(x=900, y=195)
    
    kin_contact = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Kin's Contact Number", border_color=frame_clr)
    kin_contact.place(x=900, y=280)
    
    see_gpa = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="SEE GPA", border_color=frame_clr)
    see_gpa.place(x=900, y=365)
    
    blood_grp = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Blood Group", border_color=frame_clr)
    blood_grp.place(x=900, y=450)
    
    next_btn = ctk.CTkButton(root, text="Next", width=120, height=40, corner_radius=10, font=font2, fg_color="#314C3B", bg_color=frame_clr)
    next_btn.place(x=573, y=725)
    
    
try:
    conn = db.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS user(
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """
    )
    conn.commit()
except db.Error as e:
    messagebox.showerror("Database Error", str(e))
finally:
    conn.close()

def save_login():
    try:
        global username, password
        conn = db.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user(username, password) VALUES(?, ?)",
            (username.get(), password.get())
        )
        conn.commit()
    except db.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()
    username.delete(0, END)
    password.delete(0, END)

create_login_frame() # create login frame
root.mainloop()