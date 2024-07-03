from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3 as db

root = Tk()
root.title("British Gurkhas recruitment process")
root.maxsize(1280, 832)
root.minsize(1280, 832)

# root colors and fonts
background = "#2D8A69" 
framefg = "white" 
frame_clr= "#DBDBDB"


font1 = ("Arial", 20) # for the entry fields, buttons
font2 = ("Trebuchet MS", 15, "bold") # for the forget password and register label
font3 =("Trebuchet MS", 50, "bold") # for the login label

root.geometry("1250x700+210+100") # width x height + x_offset + y_offset
root.config(bg=background)
root.resizable(False, False)

# Label for Application Form
application_form = Label(root, text="Phase 1", font=font3, bg=background, fg=framefg)
application_form.place(x= 550, y=20)

#LogOut Button
def logout():
    root.destroy()
    import login
    login.root.mainloop()
    
logout_button = ctk.CTkButton(root,
                       text="Log Out",
                       width=138,
                       height=58,
                       corner_radius=10,
                       font=font2,
                       fg_color="white",
                       text_color="black",
                       command=logout)

logout_button.place(x= 1100, y=20)

# icon 
# create a image object with reference NOTE: for the logo
imageOne = ImageTk.PhotoImage(Image.open("Assets/logo.png").resize((150,115))) # open the image
logo_icon = Label(root, image = imageOne, bg=background) # attach the image to a label
logo_icon.image = imageOne # keep a reference to the image object to prevent garbage collection by python
logo_icon.place(x= 20, y=0) # place the label in the window    


# create a main frame
form_Frame = ctk.CTkFrame(root, width=1157, height=600, corner_radius=30, bg_color="transparent")
form_Frame.grid(row=0, column=1, padx=61, pady=189)

# Entry Fields for Application Form
# First Column
first_name = ctk.CTkEntry(form_Frame, width=486, height=56, font=font1, placeholder_text="First / middle Names", border_color=frame_clr)
first_name.place(x=80, y=25)

passport_no = ctk.CTkEntry(form_Frame, width=486, height=56, font=font1, placeholder_text="Passport Number", border_color=frame_clr)
passport_no.place(x=80, y=110)

nnp_no = ctk.CTkEntry(form_Frame, width=486, height=56, font=font1, placeholder_text="NNP Number",  border_color=frame_clr)
nnp_no.place(x=80, y=195)

father_name = ctk.CTkEntry(form_Frame, width=486, height=56, font=font1, placeholder_text="Father's Name", border_color=frame_clr)
father_name.place(x=80, y=280)

mother_name = ctk.CTkEntry(form_Frame, width=486, height=56, font=font1, placeholder_text="Mother's Name", border_color=frame_clr)
mother_name.place(x=80, y=365)

see_year = ctk.CTkEntry(form_Frame, width=486, height=56, font=font1, placeholder_text="SEE Year", border_color=frame_clr)
see_year.place(x=80, y=450)

# Second Column

surname = ctk.CTkEntry(form_Frame, width=197, height=56, font=font1, placeholder_text="Surname", border_color=frame_clr)
surname.place(x=640, y=25)

main_thar = ctk.CTkEntry(form_Frame, width=197, height=56, font=font1, placeholder_text="Main Thar", border_color=frame_clr)
main_thar.place(x=640, y=110)

attepmpt = ctk.CTkEntry(form_Frame, width=197, height=56, font=font1, placeholder_text="Attempt", border_color=frame_clr)
attepmpt.place(x=640, y=195)

religion = ctk.CTkEntry(form_Frame, width=197, height=56, font=font1, placeholder_text="Religion", border_color=frame_clr)
religion.place(x=640, y=280)

district = ctk.CTkEntry(form_Frame, width=197, height=56, font=font1, placeholder_text="District", border_color=frame_clr)
district.place(x=640, y=365)

village = ctk.CTkEntry(form_Frame, width=197, height=56, font=font1, placeholder_text="Village", border_color=frame_clr)
village.place(x=640, y=450)

# Third Column
dob_ad = ctk.CTkEntry(form_Frame, width=208, height=56, font=font1, placeholder_text="Date of Birth(AD)", border_color=frame_clr)
dob_ad.place(x=900, y=25)

dob_bd = ctk.CTkEntry(form_Frame, width=208, height=56, font=font1, placeholder_text="Date of Birth(BD)", border_color=frame_clr)
dob_bd.place(x=900, y=110)

contact_no = ctk.CTkEntry(form_Frame, width=208, height=56, font=font1, placeholder_text="Contact Number", border_color=frame_clr)
contact_no.place(x=900, y=195)

kin_contact = ctk.CTkEntry(form_Frame, width=208, height=56, font=font1, placeholder_text="Kin's Contact Number", border_color=frame_clr)
kin_contact.place(x=900, y=280)

see_gpa = ctk.CTkEntry(form_Frame, width=208, height=56, font=font1, placeholder_text="SEE GPA", border_color=frame_clr)
see_gpa.place(x=900, y=365)

blood_grp = ctk.CTkEntry(form_Frame, width=208, height=56, font=font1, placeholder_text="Blood Group", border_color=frame_clr)
blood_grp.place(x=900, y=450)

next_btn = ctk.CTkButton(root, text="Next", width=120, height=40, corner_radius=10, font=font2, fg_color="#314C3B", bg_color=frame_clr)
next_btn.place(x=573, y=725)





root.mainloop()