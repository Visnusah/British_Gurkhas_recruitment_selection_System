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
from backend import initialize_db, save_admin
from tkinter import ttk  # Add this at the beginning of your file if not already included


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
    main_Frame.destroy()
 
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
font3 = ("Trebuchet MS", 40, "bold")

font1 = ("Arial", 20) # for the entry fields, buttons
logout_font = ("Trebuchet MS", 15, "bold") # for the forget password and register label
next_btn_font = ("Trebuchet MS", 17, "bold") # for the forget password and register label
phase_font = ("Trebuchet MS", 30, "bold") # for the login label
part1_font = ("Trebuchet MS", 20, "bold") # for the login label
part2_font = ("Trebuchet MS", 20, "bold") # for the login label
heading_font = ("Trebuchet MS", 17, "bold") # for the login label
subheading_font = ("Trebuchet MS", 17, "bold") # for the login label

root.config(bg=background)
root.resizable(False, False)
root.geometry("1250x700+210+100")

# show message box when closing the window
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        
root.protocol("WM_DELETE_WINDOW", on_closing) # call on_closing function when closing the window

# Register Frame
def open_register():
    global main_Frame, name_entry, email_entry, dob_entry, password_entry, number_entry, repassword_entry, show_password_var
    main_Frame.destroy()
    
    main_Frame = ctk.CTkFrame(root, width=724, height=587, corner_radius=30)
    main_Frame.grid(row=0, column=0, padx=278, pady=122)

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
    
    show_password_var = IntVar()
    password_entry = ctk.CTkEntry(main_Frame, width=291, height=56, font=font1, show="*", placeholder_text="Password")
    password_entry.place(x=392, y=217)
    
    show_password_cb = Checkbutton(main_Frame, variable=show_password_var,bg="#F9F9FB", command=toggle_pw_show)
    show_password_cb.place(x=640, y=233)

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
                               command=validate_registration_form,
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
        message = MIMEText(f"Dear {name},\n\nThank you for registering with us!\n\nHere are your registration details:\n\nName: {name}\nEmail:{email}\nPhone Number: {phone}\nDate of Birth: {dob}\nPassword: {password}\n\nBest regards,\nAnand Sharma", "plain")
        message["Subject"] = "Registration Confirmation"
        message["From"] = "info@sharmaanand.com.np"
        message["To"] = email

        server.sendmail(message["From"], message["To"], message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def logout():
    logout_btn.destroy()
    main_frame.destroy()
    t3 = Thread(target=create_login_frame)
    t3.start()

    
def open_phase2_part1():
    main_frame.destroy()
    t4 = Thread(target=phase2_part1)
    t4.start()
    main_Frame.destroy()
    admin_btn.destroy()
    
def open_phase2_part2():
    main_frame.destroy()
    t5 = Thread(target=phase2_part2)
    t5.start()
    main_Frame.destroy()
    admin_btn.destroy()
    
def medical_test():
    main_frame.destroy()
    t6 = Thread(target=phase3)
    t6.start()
    main_Frame.destroy()
    admin_btn.destroy()
    
def back_to_phase3():
    main_frame.destroy()
    t6 = Thread(target=phase3)
    t6.start()
    main_Frame.destroy()
    admin_btn.destroy()

def back_to_phase1():
    main_frame.destroy()
    t6 = Thread(target=open_phase1)
    t6.start()
    main_Frame.destroy()
    admin_btn.destroy()
    
def back_to_phase2_part1():
    main_frame.destroy()
    t6 = Thread(target=phase2_part1)
    t6.start()
    main_Frame.destroy()

def back_to_phase2_part2():
    main_frame.destroy()
    t6 = Thread(target=phase2_part2)
    t6.start()
    main_Frame.destroy()


# Phase 1    
def open_phase1():
    global main_frame, root, logout_btn, part1_lbl
    cursor_icon1.destroy() # destroy the cursor icon
    admin_btn.destroy() # destroy the admin button
    main_Frame.destroy() # destroy the main frame 
    
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=1157, height=650, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=61, pady=150)
    
    part1 = Label(main_frame, text="Phase 1".upper(), font=phase_font, bg=frame_clr, fg='black')
    part1.place(x=565, y=20)
    
    # Entry Fields for Application Form
    # First Column
    first_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="First / middle Names", border_color=frame_clr)
    first_name.place(x=80, y=80)
    
    passport_no = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Passport Number", border_color=frame_clr)
    passport_no.place(x=80, y=165)
    
    nnp_no = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="NNP Number",  border_color=frame_clr)
    nnp_no.place(x=80, y=250)
    
    father_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Father's Name", border_color=frame_clr)
    father_name.place(x=80, y=335)
    
    mother_name = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="Mother's Name", border_color=frame_clr)
    mother_name.place(x=80, y=420)
    
    see_year = ctk.CTkEntry(main_frame, width=486, height=56, font=font1, placeholder_text="SEE Year", border_color=frame_clr)
    see_year.place(x=80, y=505)
    
    # Second Column
    
    surname = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Surname", border_color=frame_clr)
    surname.place(x=640, y=80)
    
    main_thar = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Main Thar", border_color=frame_clr)
    main_thar.place(x=640, y=165)
    
    attepmpt = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Attempt", border_color=frame_clr)
    attepmpt.place(x=640, y=250)
    
    religion = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Religion", border_color=frame_clr)
    religion.place(x=640, y=335)
    
    district = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="District", border_color=frame_clr)
    district.place(x=640, y=420)
    
    village = ctk.CTkEntry(main_frame, width=197, height=56, font=font1, placeholder_text="Village", border_color=frame_clr)
    village.place(x=640, y=505)
    
    # Third Column
    dob_ad = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Date of Birth(AD)", border_color=frame_clr)
    dob_ad.place(x=900, y=80)
    
    dob_bd = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Date of Birth(BD)", border_color=frame_clr)
    dob_bd.place(x=900, y=165)
    
    contact_no = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Contact Number", border_color=frame_clr)
    contact_no.place(x=900, y=250)
    
    kin_contact = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Kin's Contact Number", border_color=frame_clr)
    kin_contact.place(x=900, y=335)
    
    see_gpa = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="SEE GPA", border_color=frame_clr)
    see_gpa.place(x=900, y=420)
    
    blood_grp = ctk.CTkEntry(main_frame, width=208, height=56, font=font1, placeholder_text="Blood Group", border_color=frame_clr)
    blood_grp.place(x=900, y=505)
    
    # Log out button)
    logout_btn = ctk.CTkButton(root, text="Log Out", width=100, height=40, font=font2, command=logout, fg_color="#314C3B", hover_color=background)
    logout_btn.place(x=1150, y=10)
    
    next_btn = ctk.CTkButton(main_frame, text="Next", width=120, height=40, corner_radius=10, font=font2, fg_color="#314C3B", bg_color=frame_clr,command=open_phase2_part1)
    next_btn.place(x=550, y=585)
    
# Phase 2 part one
def phase2_part1():
    global main_frame
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=1157, height=520, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=61, pady=140)

    part1_lbl = Label(main_frame, text="Part 1".upper(), font=part1_font,bg=frame_clr)
    part1_lbl.place(x=20, y=5)

    heading_lbl = Label(main_frame, text="Applicant's Details - Must be Completed by the Applicant:".upper(), font=heading_font,bg=frame_clr)
    heading_lbl.place(x=235, y=50)

    # Entry Fields for Application Form
    # First Column
    full_name = ctk.CTkEntry(main_frame, width=1000, height=56, corner_radius=10,font=font1, placeholder_text="Name of Applicant (In Full)".upper(), border_color=frame_clr)
    full_name.place(x=80, y=110)

    address = ctk.CTkEntry(main_frame, width=650, height=56, corner_radius=10,font=font1, placeholder_text="Address of Applicant".upper(),  border_color=frame_clr)
    address.place(x=80, y=195)
    
    email = ctk.CTkEntry(main_frame, width=650, height=56, corner_radius=10,font=font1, placeholder_text="Email Address".upper(), border_color=frame_clr)
    email.place(x=80, y=280)

    citizenship = ctk.CTkEntry(main_frame, width=1000, height=56, corner_radius=10,font=font1, placeholder_text="NEPALESE CITIZENSHIP CERTIFICATE NO OF APPLICANT".upper(), border_color=frame_clr)
    citizenship.place(x=80, y=365)

    # Second Column
    date_of_birth = ctk.CTkEntry(main_frame, width=300, height=56, corner_radius=10,font=font1, placeholder_text="Date of Birth (AD)".upper(), border_color=frame_clr)
    date_of_birth.place(x=780, y=195)

    telephone_number = ctk.CTkEntry(main_frame, width=300, height=56, corner_radius=10,font=font1, placeholder_text="Telephone Number".upper(), border_color=frame_clr)
    telephone_number.place(x=780, y=280)

    next_btn = ctk.CTkButton(main_frame, text="Next", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=open_phase2_part2)
    next_btn.place(x=980, y=455)
    
    back_btn = ctk.CTkButton(main_frame, text="back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=back_to_phase1)
    back_btn.place(x=30,y=445)

def phase2_part2():
    global main_frame
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=1157, height=590, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=61, pady=120)

    part2_lbl = Label(main_frame, text="Part 2".upper(), font=font1,bg=frame_clr)
    part2_lbl.place(x=20, y=5)

    heading_lbl = Label(main_frame, text="EMERGENCY CONTACT DETAIL - MUST BE COMPLETED BY THE APPLICANT:".upper(), font=heading_font,bg=frame_clr)
    heading_lbl.place(x=235, y=20)

    # Entry Fields for Application Form
    # First Column
    part2_lbl = Label(main_frame, text="First Contact:".upper(), font=part2_font,bg=frame_clr)
    part2_lbl.place(x=80, y=75)

    fec_full_name = ctk.CTkEntry(main_frame, width=1000, height=56, font=font1,corner_radius=10, placeholder_text="Detail Full Name".upper(), border_color=frame_clr)
    fec_full_name.place(x=80, y=110)

    fec_address = ctk.CTkEntry(main_frame, width=720, height=56, font=font1, corner_radius=10,placeholder_text="Address".upper(),  border_color=frame_clr)
    fec_address.place(x=80, y=175)

    fec_mobile_number = ctk.CTkEntry(main_frame, width=550, height=56, font=font1, corner_radius=10,placeholder_text="Mobile Number".upper(), border_color=frame_clr)
    fec_mobile_number.place(x=80, y=240)

    part3_lbl = Label(main_frame, text="Second Contact:".upper(), font=subheading_font,bg=frame_clr)
    part3_lbl.place(x=80, y=300)

    sec_full_name = ctk.CTkEntry(main_frame, width=1000, height=56, font=font1, corner_radius=10,placeholder_text="Detail Full Name".upper(), border_color=frame_clr)
    sec_full_name.place(x=80, y=335)

    sec_address = ctk.CTkEntry(main_frame, width=720, height=56, font=font1,corner_radius=10, placeholder_text="Address".upper(),  border_color=frame_clr)
    sec_address.place(x=80, y=400)

    sec_mobile_number = ctk.CTkEntry(main_frame, width=550, height=56, font=font1, corner_radius=10,placeholder_text="Mobile Number".upper(), border_color=frame_clr)
    sec_mobile_number.place(x=80, y=465)

    # Second Column
    fec_date_of_birth = ctk.CTkEntry(main_frame, width=260, height=56, font=font1, corner_radius=10,placeholder_text="Date of Birth (AD)".upper(), border_color=frame_clr)
    fec_date_of_birth.place(x=820, y=175)

    fec_telephone_number = ctk.CTkEntry(main_frame, width=430, height=56, font=font1, corner_radius=10,placeholder_text="Telephone Number".upper(), border_color=frame_clr)
    fec_telephone_number.place(x=650, y=240)

    sec_date_of_birth = ctk.CTkEntry(main_frame, width=260, height=56, font=font1, corner_radius=10,placeholder_text="Date of Birth (AD)".upper(), border_color=frame_clr)
    sec_date_of_birth.place(x=820, y=400)

    sec_telephone_number = ctk.CTkEntry(main_frame, width=430, height=56, font=font1, corner_radius=10,placeholder_text="Telephone Number".upper(), border_color=frame_clr)
    sec_telephone_number.place(x=650, y=465)

    next_btn = ctk.CTkButton(main_frame, text="Next", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=medical_test)
    next_btn.place(x=980, y=535)
    
    back_btn = ctk.CTkButton(main_frame, text="back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=back_to_phase2_part1)
    back_btn.place(x=30,y=535)
    
def show_medical_date():
    main_frame.destroy()
    t7 = Thread(target=medi_date_lbl).start()
    main_Frame.destroy()
    admin_btn.destroy()

def show_physical_date():
    main_frame.destroy()
    t7 = Thread(target=Phy_ass_lbl).start()
    main_Frame.destroy()
    admin_btn.destroy()

def show_education_date():
    main_frame.destroy()
    t7 = Thread(target=edu_ass_lbl).start()
    main_Frame.destroy()
    admin_btn.destroy()
    
def show_int_date():
    main_frame.destroy()
    t7 = Thread(target=int_ass_lbl).start()
    main_Frame.destroy()
    admin_btn.destroy()
    
def open_admin():
    main_Frame.destroy()
    admin_btn.destroy()
    t8 = Thread(target=create_login_admin).start()
    
def open_user():
    main_Frame.destroy()
    user_btn.destroy()
    t9 = Thread(target=create_login_frame).start()
    
def dashboard():
    main_frame.destroy()
    t10 = Thread(target=admin_dashboard).start()
    
def phase3():
    global main_frame, medical_btn, Physical_ass_btn, educational_ass_btn, intervie_btn
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=941, height=575, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=170, pady=146)
    
    part3_lbl = Label(main_frame, text="Phase 3", font=phase_font, bg=frame_clr, fg='#6B7273')
    part3_lbl.place(x= 400, y= 20)
    
    medical_btn = ctk.CTkButton(main_frame, 
                                text="Medical",
                                width=691,
                                height=71,
                                corner_radius=10,
                                font=part1_font,
                                fg_color="#2D8A69",
                                text_color="white",
                                command=show_medical_date)
    medical_btn.place(x= 140, y= 97)
    Physical_ass_btn = ctk.CTkButton(main_frame, 
                                text="Physical Assessments",
                                width=691,
                                height=71,
                                corner_radius=10,
                                font=part1_font,
                                fg_color="#2D8A69",
                                text_color="white",
                                command=show_physical_date)
    Physical_ass_btn.place(x= 140, y= 199)
    educational_ass_btn = ctk.CTkButton(main_frame, 
                                text="Educational Assessments",
                                width=691,
                                height=71,
                                corner_radius=10,
                                font=part1_font,
                                fg_color="#2D8A69",
                                text_color="white",
                                command=show_education_date)
    educational_ass_btn.place(x= 140, y= 310)
    intervie_btn = ctk.CTkButton(main_frame, 
                                text="Interview",
                                width=691,
                                height=71,
                                corner_radius=10,
                                font=part1_font,
                                fg_color="#2D8A69",
                                text_color="white",
                                command=show_int_date)
    intervie_btn.place(x= 140, y= 403)
    
    back_btn = ctk.CTkButton(main_frame, text="back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=back_to_phase2_part2)
    back_btn.place(x=30,y=510)

    finish_btn = ctk.CTkButton(main_frame, text="Finish", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=logout)
    finish_btn.place(x=700,y=510)
      
def medi_date_lbl():
    global main_frame
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=941, height=282, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=170, pady=146)
    
    part3_lbl = Label(main_frame, text="Phase 3", font=phase_font, bg=frame_clr, fg='#6B7273')
    part3_lbl.place(x= 400, y= 20)
    
    medical_date_lbl = Label(main_frame, text="Medical Date: ", font=part1_font, bg=frame_clr, fg='black', width=20, height=2)
    medical_date_lbl.place(x= 190, y= 100)
    
    display_date_lbl = Label(main_frame, text="Year-Month-Day", font=part1_font, bg='white', fg='black', width=20, height=2)
    display_date_lbl.place(x= 380, y= 100)
    
    back_btn = ctk.CTkButton(main_frame, text="back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=back_to_phase3)
    back_btn.place(x=30,y=220)

def Phy_ass_lbl():
    global main_frame
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=941, height=282, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=170, pady=146)
    
    part3_lbl = Label(main_frame, text="Phase 3", font=phase_font, bg=frame_clr, fg='#6B7273')
    part3_lbl.place(x= 400, y= 20)
    
    Physical_ass_lbl_lbl = Label(main_frame, text="Physical Assessments", font=part1_font, bg=frame_clr, fg='black', width=20, height=2)
    Physical_ass_lbl_lbl.place(x= 150, y= 100)
    
    display_date_lbl = Label(main_frame, text="Year-Month-Day", font=part1_font, bg='white', fg='black', width=20, height=2)
    display_date_lbl.place(x= 390, y= 100)
    
    back_btn = ctk.CTkButton(main_frame, text="back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=back_to_phase3)
    back_btn.place(x=30,y=220)

def edu_ass_lbl():
    global main_frame
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=941, height=282, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=170, pady=146)
    
    part3_lbl = Label(main_frame, text="Phase 3", font=phase_font, bg=frame_clr, fg='#6B7273')
    part3_lbl.place(x= 400, y= 20)
    
    Physical_ass_lbl_lbl = Label(main_frame, text="Educational Assessments", font=part1_font, bg=frame_clr, fg='black', width=20, height=2)
    Physical_ass_lbl_lbl.place(x= 150, y= 100)
    
    display_date_lbl = Label(main_frame, text="Year-Month-Day", font=part1_font, bg='white', fg='black', width=20, height=2)
    display_date_lbl.place(x= 390, y= 100)

    back_btn = ctk.CTkButton(main_frame, text="back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=back_to_phase3)
    back_btn.place(x=30,y=220)

    
def int_ass_lbl():

    global main_frame
    # create a main frame
    main_frame = ctk.CTkFrame(root, width=941, height=282, corner_radius=30, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=170, pady=146)
    
    part3_lbl = Label(main_frame, text="Phase 3", font=phase_font, bg=frame_clr, fg='#6B7273')
    part3_lbl.place(x= 400, y= 20)
    
    Physical_ass_lbl_lbl = Label(main_frame, text="Interview", font=part1_font, bg=frame_clr, fg='black', width=20, height=2)
    Physical_ass_lbl_lbl.place(x= 150, y= 100)
    
    display_date_lbl = Label(main_frame, text="Year-Month-Day", font=part1_font, bg='white', fg='black', width=20, height=2)
    display_date_lbl.place(x= 390, y= 100)

    back_btn = ctk.CTkButton(main_frame, text="back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#314C3B", bg_color=frame_clr,command=back_to_phase3)
    back_btn.place(x=30,y=220)

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
# Login Frame
def create_login_frame():
    global main_Frame, username, password, admin_btn, cursor_icon1, admin_btn
    main_Frame = ctk.CTkFrame(master=root, width=555, height=431, corner_radius=30)
    main_Frame.grid(row=0, column=1, padx=350, pady=150)

    login_label = Label(main_Frame, text="Login", font=font3, bg=frame_clr, fg=background)
    login_label.place(x=230, y=18)

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

    admin_btn = ctk.CTkButton(root, text="Admin", font=font3, text_color='white', fg_color=background,
                            command=open_admin, hover_color=background)
    admin_btn.place(x=1050, y=20)
    try:
        image_cr = ImageTk.PhotoImage(Image.open("Assets/Cursor.png").resize((30, 30)))
        cursor_icon1 = Label(root, image=image_cr, bg=background)
        cursor_icon1.image = image_cr
        cursor_icon1.place(x=1170, y=70) 
    except Exception as e:
        messagebox.showerror("Image Error", str(e))
    
def create_login_admin():
    global main_Frame, username_admin, password_admin, user_btn
    cursor_icon1.destroy()
    
    main_Frame = ctk.CTkFrame(master=root, width=555, height=431, corner_radius=30)
    main_Frame.grid(row=0, column=0, padx=350, pady=150)

    login_label = Label(main_Frame, text="Login", font=font3, bg=frame_clr, fg='#020202')
    login_label.place(x=230, y=18)

    username_admin = ctk.CTkEntry(main_Frame, width=487, height=56, corner_radius=10, font=font1,
                            fg_color="#020202", text_color=framefg, placeholder_text="Username",
                            placeholder_text_color=framefg)
    username_admin.place(x=40, y=130)

    password_admin = ctk.CTkEntry(main_Frame, width=487, height=56, corner_radius=10, font=font1, show="*",
                            fg_color="#020202", text_color=framefg, placeholder_text="Password",
                            placeholder_text_color=framefg)
    password_admin.place(x=40, y=210)

    login_Btn = ctk.CTkButton(main_Frame, text="Login", width=120, height=40, corner_radius=10, font=font2,
                              command=lambda: save_admin(username_admin.get(), password_admin.get(), admin_dashboard), fg_color="#020202", hover_color="#3276FF", text_color="white")
    login_Btn.place(x=200, y=290)
    
    user_btn = ctk.CTkButton(root, text="User", font=font3, text_color='white', fg_color=background,
                              command=open_user, hover_color=background)
    user_btn.place(x=1050, y=20)

txt_lbl = ctk.CTkLabel(root, text="The British Army", font=("Arial", 20), fg_color=background, text_color="White")  
txt_lbl.place(x=8, y=93)
def logout_admin():
    main_frame.destroy()
    logout_btn_admin.destroy()
    t11 = Thread(target=create_login_frame)
    t11.start()

# def admin_dashboard():
#     global main_frame, admin_lbl, logout_btn_admin
#     main_Frame.destroy()
#     user_btn.destroy()
    
    
#     main_frame = ctk.CTkFrame(root, width=941, height=575, corner_radius=20, bg_color="transparent")
#     main_frame.grid(row=0, column=1, padx=120, pady=146)
    
#     admin_lbl = Label(master=root, text="Dashboard", font=("Trebuchet MS", 40, "bold"), bg=background, fg='white')
#     admin_lbl.place(x=526, y=76)
    
#     # button for Show Details, Updates Details, Delete Details and User Assessments Data
#     show_details_btn = ctk.CTkButton(master=main_frame, text="Show Details", width=20, height=2, font=font1, fg_color=background, corner_radius=5)
#     show_details_btn.grid(row=0, column=0, padx=60, pady=30)
    
#     update_details_btn = ctk.CTkButton(master=main_frame, text="Update Details", width=20, height=2, font=font1,fg_color=background,corner_radius=5)
#     update_details_btn.grid(row=0, column=1, padx=60, pady=30)
#     
#     delete_details_btn = ctk.CTkButton(master=main_frame, text="Delete Details", width=20, height=2, font=font1, fg_color=background, corner_radius=5)
#     delete_details_btn.grid(row=0, column=2, padx=60, pady=30)
    
#     user_assessments_data_btn = ctk.CTkButton(master=main_frame, text="User Assessments Data", width=20, height=2, font=font1, fg_color=background, corner_radius=5)
#     user_assessments_data_btn.grid(row=0, column=3, padx=60, pady=30)
    
#     # Log out button)
#     logout_btn_admin = ctk.CTkButton(root, text="Log Out", width=100, height=40, font=font2, command=logout_admin, fg_color="#314C3B", hover_color=background)
#     logout_btn_admin.place(x=1150, y=10)
# IMP:
def fetch_user_details(details_tree):
    try:
        conn = db.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username, name_1, dob_1, phone_1 FROM user")
        records = cursor.fetchall()
        print("Fetched records:", records)  # Debugging output to check what is fetched

        # Clear existing data in the tree
        details_tree.delete(*details_tree.get_children())  # Ensure all children are removed

        # Insert new data into the tree
        for record in records:
            print("Inserting record:", record)  # Debugging output to check what is being inserted
            details_tree.insert('', 'end', values=record)
    except db.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()

def delete_user(Username):
    if not Username:
        messagebox.showerror("Error", "Please enter an email address.")
        return

    # Verification step before deletion
    if not messagebox.askyesno("Verify", "Are you sure you want to delete this user?"):
        return

    try:
        conn = db.connect("database.db")
        cursor = conn.cursor()
        print(f"Attempting to delete user with Username: {Username}")  # Debugging output
        cursor.execute("DELETE FROM user WHERE Username = ?", (Username,))
        conn.commit()
        print(f"Rows affected: {cursor.rowcount}")  # Debugging output
        if cursor.rowcount == 0:
            messagebox.showinfo("Result", "No user found with that email.")
        else:
            messagebox.showinfo("Success", "User deleted successfully.")
            fetch_user_details(details_tree)  # Refresh the details display
    except db.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()
def admin_dashboard():
    global main_frame, admin_lbl, logout_btn_admin, details_tree, email_entry, update_frame, update_email_entry, update_name_entry, update_dob_entry, update_phone_entry
    # ... existing code ...
    main_Frame.destroy()
    user_btn.destroy()
    
    main_frame = ctk.CTkFrame(root, width=941, height=575, corner_radius=20, bg_color="transparent")
    main_frame.grid(row=0, column=1, padx=20, pady=130)
    
    dashboard_lbl = Label(main_frame, text="Dashboard", font=("Trebuchet MS", 20, "bold"), bg=frame_clr, fg='black')
    dashboard_lbl.place(x=400, y=20)
        
    show_details_btn = ctk.CTkButton(master=main_frame, text="Show Details", command=lambda: fetch_user_details(details_tree))
    show_details_btn.place(x=50, y=50)
    
    columns = ('username', 'name', 'dob', 'phone')
    details_tree = ttk.Treeview(main_frame, columns=columns, show='headings')
    for col in columns:
        details_tree.heading(col, text=col.capitalize())  # Ensure headings are set
    details_tree.place(x=50, y=100)

    email_entry = ctk.CTkEntry(main_frame, width=300, placeholder_text="Enter user email to delete", border_color=background)
    email_entry.place(x=55, y=330)
    
    delete_btn = ctk.CTkButton(main_frame, text="Delete User", command=lambda: delete_user(email_entry.get()), fg_color="#FF6347", hover_color="#FF4500")
    delete_btn.place(x=375, y=330)

    logout_btn_admin = ctk.CTkButton(root, text="Log Out", width=100, height=40, font=font2, command=logout_admin, fg_color="#314C3B", hover_color=background)
    logout_btn_admin.place(x=1150, y=10)

    # Frame for updates
    update_frame = ctk.CTkFrame(main_frame, width=500, height=300, corner_radius=10, bg_color=frame_clr)
    update_frame.place(x=50, y=370)

    # Entry widgets for updating user data
    update_email_entry = ctk.CTkEntry(update_frame, width=300, placeholder_text="Enter email to update", border_color=background)
    update_email_entry.grid(row=0, column=0, padx=10, pady=10)

    update_name_entry = ctk.CTkEntry(update_frame, width=300, placeholder_text="New Name", border_color=background)
    update_name_entry.grid(row=1, column=0, padx=10, pady=10)

    update_dob_entry = ctk.CTkEntry(update_frame, width=300, placeholder_text="New DOB", border_color=background)
    update_dob_entry.grid(row=2, column=0, padx=10, pady=10)

    update_phone_entry = ctk.CTkEntry(update_frame, width=300, placeholder_text="New Phone", border_color=background)
    update_phone_entry.grid(row=3, column=0, padx=10, pady=10)

    # Button to fetch data into entry widgets
    fetch_data_btn = ctk.CTkButton(update_frame, text="Fetch Data", command=lambda: fetch_data_for_update(update_email_entry.get()))
    fetch_data_btn.grid(row=0, column=1, padx=10, pady=10)

    # Button to update data
    update_data_btn = ctk.CTkButton(update_frame, text="Update Data", command=lambda: update_user_data(update_email_entry.get(), update_name_entry.get(), update_dob_entry.get(), update_phone_entry.get()))
    update_data_btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

def fetch_data_for_update(email):
    if not email:
        messagebox.showerror("Error", "Please enter an email address.")
        return
    try:
        conn = db.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name_1, dob_1, phone_1 FROM user WHERE username = ?", (email,))
        user_data = cursor.fetchone()
        if user_data:
            update_name_entry.delete(0, END)
            update_name_entry.insert(0, user_data[0])
            update_dob_entry.delete(0, END)
            update_dob_entry.insert(0, user_data[1])
            update_phone_entry.delete(0, END)
            update_phone_entry.insert(0, user_data[2])
        else:
            messagebox.showinfo("Result", "No user found with that email.")
    except db.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()

def update_user_data(email, name, dob, phone):
    if not (email and name and dob and phone):
        messagebox.showerror("Error", "All fields must be filled out.")
        return
    try:
        conn = db.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET name_1 = ?, dob_1 = ?, phone_1 = ? WHERE username = ?", (name, dob, phone, email))
        conn.commit()
        if cursor.rowcount == 0:
            messagebox.showinfo("Result", "No user found with that email.")
        else:
            messagebox.showinfo("Success", "User updated successfully.")
            fetch_user_details(details_tree)  # Refresh the details display
    except db.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        conn.close()
        
try:
    imageOne = ImageTk.PhotoImage(Image.open("Assets/British.png").resize((80, 80)))
    logo_icon = Label(root, image=imageOne, bg=background)
    logo_icon.image = imageOne
    logo_icon.place(x=30, y=8)
except Exception as e:
    messagebox.showerror("Image Error", str(e))
    

initialize_database()
initialize_db()  # Initialize the database and create the admin table
create_login_frame() # create login frame

root.mainloop()
