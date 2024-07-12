from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3 as db
from user import User

root = Tk()
root.title("British Gurkhas recruitment process")
root.maxsize(1280, 770)
root.minsize(1280, 770)

# root colors and fonts
background = "#2D8A69" 
framefg = "white" 
frame_clr= "#DBDBDB"


font1 = ("Arial", 20) # for the entry fields, buttons
logout_font = ("Trebuchet MS", 15, "bold") # for the forget password and register label
next_btn_font = ("Trebuchet MS", 17, "bold") # for the forget password and register label
phase_font = ("Trebuchet MS", 30, "bold") # for the login label
part2_font = ("Trebuchet MS", 20, "bold") # for the login label
subheading_font = ("Trebuchet MS", 17, "bold") # for the login label
heading_font = ("Trebuchet MS", 17, "bold") # for the login label

root.geometry("1250x700+210+100") # width x height + x_offset + y_offset
root.config(bg=background)
root.resizable(False, False)

# Label for Application Form
application_form = Label(root, text="Phase 2", font=phase_font, bg=background, fg=framefg)
application_form.place(x= 550, y=20)

#LogOut Button
def logout():
    root.destroy()
    import login
    login.root.mainloop()
    
logout_button = ctk.CTkButton(root,
                       text="Log Out".upper(),
                       width=138,
                       height=58,
                       corner_radius=10,
                       font=logout_font,
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
form_Frame = ctk.CTkFrame(root, width=1157, height=590, corner_radius=30, bg_color="transparent")
form_Frame.grid(row=0, column=1, padx=61, pady=120)


part2_lbl = Label(form_Frame, text="Part 2".upper(), font=part2_font,bg=frame_clr)
part2_lbl.place(x=20, y=5)


heading_lbl = Label(form_Frame, text="EMERGENCY CONTACT DETAIL - MUST BE COMPLETED BY THE APPLICANT:".upper(), font=heading_font,bg=frame_clr)
heading_lbl.place(x=235, y=20)

# Entry Fields for Application Form
# First Column

part2_lbl = Label(form_Frame, text="First Contact:".upper(), font=subheading_font,bg=frame_clr)
part2_lbl.place(x=80, y=75)

detail_full_name = ctk.CTkEntry(form_Frame, width=1000, height=56, font=font1,corner_radius=10, placeholder_text="Detail Full Name".upper(), border_color=frame_clr)
detail_full_name.place(x=80, y=110)

address = ctk.CTkEntry(form_Frame, width=720, height=56, font=font1, corner_radius=10,placeholder_text="Address".upper(),  border_color=frame_clr)
address.place(x=80, y=175)

email = ctk.CTkEntry(form_Frame, width=550, height=56, font=font1, corner_radius=10,placeholder_text="Mobile Number".upper(), border_color=frame_clr)
email.place(x=80, y=240)


part3_lbl = Label(form_Frame, text="Second Contact:".upper(), font=subheading_font,bg=frame_clr)
part3_lbl.place(x=80, y=300)

detail_full_name = ctk.CTkEntry(form_Frame, width=1000, height=56, font=font1, corner_radius=10,placeholder_text="Detail Full Name".upper(), border_color=frame_clr)
detail_full_name.place(x=80, y=335)

address = ctk.CTkEntry(form_Frame, width=720, height=56, font=font1,corner_radius=10, placeholder_text="Address".upper(),  border_color=frame_clr)
address.place(x=80, y=400)

email = ctk.CTkEntry(form_Frame, width=550, height=56, font=font1, corner_radius=10,placeholder_text="Mobile Number".upper(), border_color=frame_clr)
email.place(x=80, y=465)

# Second Column

date_of_birth = ctk.CTkEntry(form_Frame, width=260, height=56, font=font1, corner_radius=10,placeholder_text="Date of Birth (AD)".upper(), border_color=frame_clr)
date_of_birth.place(x=820, y=175)

telephone_number = ctk.CTkEntry(form_Frame, width=430, height=56, font=font1, corner_radius=10,placeholder_text="Telephone Number".upper(), border_color=frame_clr)
telephone_number.place(x=650, y=240)


date_of_birth = ctk.CTkEntry(form_Frame, width=260, height=56, font=font1, corner_radius=10,placeholder_text="Date of Birth (AD)".upper(), border_color=frame_clr)
date_of_birth.place(x=820, y=400)

telephone_number = ctk.CTkEntry(form_Frame, width=430, height=56, font=font1, corner_radius=10,placeholder_text="Telephone Number".upper(), border_color=frame_clr)
telephone_number.place(x=650, y=465)


def get_user_data():
    user = User(
        full_name=detail_full_name.get(),
        passport_no=passport_no.get(),
        nnp_no=address.get(),
        father_name=email.get(),
        mother_name=mother_name.get(),
        see_year=see_year.get(),
        main_thar=main_thar.get(),
        attempt=date_of_birth.get(),
        religion=telephone_number.get(),
    )
    return user

def on_next_click():
    user = get_user_data()
    print(user.__dict__)
    return user


next_btn = ctk.CTkButton(root, text="Next", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#2D8A69", bg_color=frame_clr,command=on_next_click)
next_btn.place(x=573, y=655)






root.mainloop()