from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
from threading import Thread
import sqlite3 as db
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize database and create user table if it doesn't exist
def initialize_database():
    try:
        conn = db.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS user(
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    name_1 TEXT,
                    dob_1 TEXT,
                    phone_1 TEXT
                )
            """
        )
        conn.commit()
    except db.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()

# Thread for opening register frame because it takes time to load
def threading():
    main_Frame.destroy()
    t1 = Thread(target=open_register)
    t1.start()

# Thread for opening login frame because it takes time to load
def threading2():
    main_Frame.destroy()
    t2 = Thread(target=create_login_frame)
    t2.start()

# Main window
root = Tk()
root.title("British Gurkhas recruitment process")

background = "#2D8A69"
framefg = "white"
frame_clr = "#DBDBDB"

font1 = ("Roboto", 20)
font2 = ("Roboto", 16, "bold")
font3 = ("Poppins", 50, "bold")
font4 = ("Roboto", 40, "bold")

root.config(bg=background)
root.geometry("1000x1000")

# Show message box when closing the window
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)  # Call on_closing function when closing the window

# Register Frame
# Register Frame with Form Validation
def open_register():
    global main_Frame, name_entry, email_entry, dob_entry, password_entry, number_entry, repassword_entry, show_password_var
    main_Frame.destroy()

    main_Frame = ctk.CTkFrame(root, width=724, height=587, corner_radius=30)
    main_Frame.place(relx=0.5, rely=0.5, anchor="center")

    Sign_up_label = Label(main_Frame, text="Sign Up", font=font4, bg=frame_clr, fg=background)
    Sign_up_label.place(x=260, y=10)

    name_entry = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, placeholder_text="Name")
    name_entry.place(x=40, y=134)

    email_entry = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, placeholder_text="Email")
    email_entry.place(x=392, y=134)

    dob_entry = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, placeholder_text="Date of Birth (YYYY-MM-DD)")
    dob_entry.place(x=40, y=217)

    show_password_var = IntVar()
    password_entry = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, show="*", placeholder_text="Password")
    password_entry.place(x=392, y=217)

    number_entry = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, placeholder_text="Phone Number")
    number_entry.place(x=40, y=300)

    repassword_entry = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, show="*", placeholder_text="Re-enter Password")
    repassword_entry.place(x=392, y=300)

    show_password_cb = Checkbutton(main_Frame, variable=show_password_var,bg="#343638", command=toggle_pw_show)
    show_password_cb.place(x=640, y=233)

    singin_btn = ctk.CTkButton(main_Frame, text="Sign Up", width=134, height=59, font=font1, command=validate_registration_form, fg_color="#314C3B", hover_color=background)
    singin_btn.place(x=292, y=387)

    already_have_account = ctk.CTkButton(main_Frame, text="Already have an account?", font=font2, text_color="black", fg_color=frame_clr, hover_color=frame_clr, command=threading2)
    already_have_account.place(x=258, y=486)

def toggle_pw_show():
    if show_password_var.get():
        password_entry.configure(show="")
        repassword_entry.configure(show="")
    else:
        password_entry.configure(show="*")
        repassword_entry.configure(show="*")

def validate_registration_form():
    name = name_entry.get()
    email = email_entry.get()
    dob = dob_entry.get()
    password = password_entry.get()
    repassword = repassword_entry.get()
    phone = number_entry.get()

    if not name or not email or not dob or not password or not repassword or not phone:
        messagebox.showerror("Registration Failed", "All fields are required!")
        return

    if not validate_email(email):
        messagebox.showerror("Registration Failed", "Invalid email format!")
        return

    if not validate_dob(dob):
        messagebox.showerror("Registration Failed", "Invalid date of birth format! Use YYYY-MM-DD.")
        return

    if password != repassword:
        messagebox.showerror("Registration Failed", "Passwords do not match!")
        return

    if not validate_phone(phone):
        messagebox.showerror("Registration Failed", "Invalid phone number!")
        return

    save_registration()  # Save the data to the database after successful validation


def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def validate_dob(dob):
    dob_regex = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(dob_regex, dob) is not None

def validate_phone(phone):
    return phone.isdigit() and len(phone) in (10, 13)



def save_registration():
    try:
        conn = db.connect("database.db")
        cursor = conn.cursor()

        # Get the email entered by the user
        email = email_entry.get()
        # receiver_email = email_entry.get()

        # Check if the email (username) already exists
        cursor.execute("SELECT * FROM user WHERE username = ?", (email,))
        if cursor.fetchone():
            messagebox.showerror("Registration Error", "Email already exists. Please use a different email.")
            return

        # Retrieve values from entry widgets
        name = name_entry.get()
        password = password_entry.get()
        dob = dob_entry.get()
        phone = number_entry.get()

        # Insert the new user into the database
        cursor.execute(
            "INSERT INTO user (username, password, name_1, dob_1, phone_1) VALUES (?, ?, ?, ?, ?)",
            (email, password, name, dob, phone),
        )
        conn.commit()

        # Send email to the registered user
        send_registration_email(email, name, password, phone, dob)

        messagebox.showinfo("Registration", "Registration Successful!")
    except db.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()

    # Clear all entry fields after successful registration
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    dob_entry.delete(0, END)
    password_entry.delete(0, END)
    number_entry.delete(0, END)
    repassword_entry.delete(0, END)

def send_registration_email(email, name, password, phone, dob):
    try:
        server = smtplib.SMTP_SSL("mail.sharmaanand.com.np", 465)  
        server.login("info@sharmaanand.com.np", "admin@444$")
        message = MIMEText(f"Dear {name},\n\nThank you for registering with us!\n\nHere are your registration details:\n\nName: {name}\nEmail: {email}\nPhone Number: {phone}\nDate of Birth: {dob}\nPassword: {password}\n\nBest regards,\nAnand Sharma", "plain")
        message["Subject"] = "Registration Confirmation"
        message["From"] = "info@sharmaanand.com.np"
        message["To"] = email

        server.sendmail(message["From"], message["To"], message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


# Phase 1
def open_phase1():
    global main_Frame

    # Create a main frame
    main_frame = ctk.CTkFrame(root, width=1157, height=600, corner_radius=30, bg_color="transparent")
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Phase 1 label
    phase1_label = Label(main_frame, text="Phase 1", font=font4, bg=frame_clr, fg=background)
    phase1_label.place(relx=0.5, rely=0.05, anchor="center")

    # Entry Fields for Application Form
    # First Column
    first_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="First / middle Names", border_color=frame_clr)
    first_name.place(x=80, y=80)

    passport_no = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Passport Number", border_color=frame_clr)
    passport_no.place(x=80, y=140)

    nnp_no = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="NNP Number", border_color=frame_clr)
    nnp_no.place(x=80, y=200)

    father_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Father's Name", border_color=frame_clr)
    father_name.place(x=80, y=260)

    mother_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Mother's Name", border_color=frame_clr)
    mother_name.place(x=80, y=320)

    see_year = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="SEE Year", border_color=frame_clr)
    see_year.place(x=80, y=380)

    # Second Column
    surname = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Surname", border_color=frame_clr)
    surname.place(x=587, y=80)

    dob = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Date of Birth", border_color=frame_clr)
    dob.place(x=587, y=140)

    citizenship = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Citizenship Number", border_color=frame_clr)
    citizenship.place(x=587, y=200)

    gfname = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Grandfather's Name", border_color=frame_clr)
    gfname.place(x=587, y=260)

    address = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Address", border_color=frame_clr)
    address.place(x=587, y=320)

    phone = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Phone Number", border_color=frame_clr)
    phone.place(x=587, y=380)

    # Log out button
    logout_btn = ctk.CTkButton(main_frame, text="Log Out", width=100, height=40, font=font2, command=logout, fg_color="#314C3B", hover_color=background)
    logout_btn.place(relx=0.95, rely=0.05, anchor="ne")

def logout():
    global main_Frame
    main_Frame.destroy()
    create_login_frame() 
   



# Save Login Information
def save_login():
    global username, password
    uname = username.get()
    pwd = password.get()

    if not uname or not pwd:
        messagebox.showerror("Login Failed", "Username and Password cannot be empty!")
        return

    try:
        conn = db.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (uname, pwd))
        row = cursor.fetchone()
        if row:
            messagebox.showinfo("Login Success", "Login Successful!")
            open_phase1()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password!")
    except db.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()

def create_login_frame():
    global main_Frame, username, password

    main_Frame = ctk.CTkFrame(root, width=724, height=587, corner_radius=30)
    main_Frame.place(relx=0.5, rely=0.5, anchor="center")

    login_label = Label(main_Frame, text="Log In", font=font3, bg=frame_clr, fg=background)
    login_label.place(relx=0.5, rely=0.1, anchor="center")

    username = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, placeholder_text="Username", fg_color=background, text_color=framefg, placeholder_text_color=framefg)
    username.place(relx=0.5, rely=0.3, anchor="center")

    password = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, show="*", placeholder_text="Password", fg_color=background, text_color=framefg, placeholder_text_color=framefg)
    password.place(relx=0.5, rely=0.45, anchor="center")

    login_btn = ctk.CTkButton(main_Frame, text="Log In", width=134, height=59, font=font1, command=save_login, fg_color="#314C3B", hover_color=background)
    login_btn.place(relx=0.5, rely=0.6, anchor="center")

    register_btn = ctk.CTkButton(main_Frame, text="Create an account?", font=font2, text_color="black", fg_color=frame_clr, hover_color=frame_clr, command=threading)
    register_btn.place(relx=0.5, rely=0.75, anchor="center")

    try:
        imageOne = ImageTk.PhotoImage(Image.open("Assets/logo.png").resize((150, 115)))
        logo_icon = Label(root, image=imageOne, bg=background)
        logo_icon.image = imageOne
        logo_icon.place(x=20, y=0)
        
        imageThree = ImageTk.PhotoImage(Image.open("Assets/user.png").resize((31, 31)))
        User_icon = Label(main_Frame, image=imageThree, bg=background)
        User_icon.image = imageThree
        User_icon.place(x=460, y=155)
        
        imageTwo = ImageTk.PhotoImage(Image.open("Assets/password.png").resize((31, 31)))
        password_icon = Label(main_Frame, image=imageTwo, bg=background)
        password_icon.image = imageTwo
        password_icon.place(x=460, y=250)
    except Exception as e:
        messagebox.showerror("Image Error", str(e))

# Initialize database and open Login Frame on Startup
initialize_database()
create_login_frame()

root.mainloop()
