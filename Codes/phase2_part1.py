import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
from models.army import Army
from models.helper import get_splitted_name


def open_phase2_part1(phase2_part1_window,on_next_click=None,on_back_click=None,pass_data_fun=None):

    # phase2_part1_window colors and fonts
    background = "#2D8A69" 
    framefg = "white" 
    frame_clr= "#DBDBDB"


    font1 = ("Arial", 20) # for the entry fields, buttons
    logout_font = ("Trebuchet MS", 15, "bold") # for the forget password and register label
    next_btn_font = ("Trebuchet MS", 17, "bold") # for the forget password and register label
    phase_font = ("Trebuchet MS", 30, "bold") # for the login label
    part1_font = ("Trebuchet MS", 20, "bold") # for the login label
    heading_font = ("Trebuchet MS", 17, "bold") # for the login label

    phase2_part1_window.config(bg=background)
    # phase2_part1_window.resizable(False, False)

    # Label for Application Form
    application_form = Label(phase2_part1_window, text="Phase 2", font=phase_font, bg=background, fg=framefg)
    application_form.place(x= 550, y=20)

    #LogOut Button
    def logout():
        phase2_part1_window.destroy()
        import login
        login.phase2_part1_window.mainloop()
        
    logout_button = ctk.CTkButton(phase2_part1_window,
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
    logo_icon = Label(phase2_part1_window, image = imageOne, bg=background) # attach the image to a label
    logo_icon.image = imageOne # keep a reference to the image object to prevent garbage collection by python
    logo_icon.place(x= 20, y=0) # place the label in the window    


    # create a main frame
    form_Frame = ctk.CTkFrame(phase2_part1_window, width=1157, height=520, corner_radius=30, bg_color="transparent")
    form_Frame.grid(row=0, column=1, padx=61, pady=140)


    part1_lbl = Label(form_Frame, text="Part 1".upper(), font=part1_font,bg=frame_clr)
    part1_lbl.place(x=20, y=5)


    heading_lbl = Label(form_Frame, text="Applicant's Details - Must be Completed by the Applicant:".upper(), font=heading_font,bg=frame_clr)
    heading_lbl.place(x=235, y=50)

    # Entry Fields for Application Form
    # First Column

    full_name = ctk.CTkEntry(form_Frame, width=1000, height=56, corner_radius=10,font=font1, placeholder_text="Name of Applicant (In Full)".upper(), border_color=frame_clr)
    full_name.place(x=80, y=110)

    address = ctk.CTkEntry(form_Frame, width=650, height=56, corner_radius=10,font=font1, placeholder_text="Address of Applicant".upper(),  border_color=frame_clr)
    address.place(x=80, y=195)

    email = ctk.CTkEntry(form_Frame, width=650, height=56, corner_radius=10,font=font1, placeholder_text="Email Address".upper(), border_color=frame_clr)
    email.place(x=80, y=280)

    citizenship = ctk.CTkEntry(form_Frame, width=1000, height=56, corner_radius=10,font=font1, placeholder_text="NEPALESE CITIZENSHIP CERTIFICATE NO OF APPLICANT".upper(), border_color=frame_clr)
    citizenship.place(x=80, y=365)

    # Second Column

    date_of_birth = ctk.CTkEntry(form_Frame, width=300, height=56, corner_radius=10,font=font1, placeholder_text="Date of Birth (AD)".upper(), border_color=frame_clr)
    date_of_birth.place(x=780, y=195)

    telephone_number = ctk.CTkEntry(form_Frame, width=300, height=56, corner_radius=10,font=font1, placeholder_text="Telephone Number".upper(), border_color=frame_clr)
    telephone_number.place(x=780, y=280)



    def get_army_data():
        fname, mname,lname = get_splitted_name(full_name.get())
        army = Army(
            first_name=fname,
            middle_name=mname,
            surname=lname,
            address_location=address.get(),
            email=email.get(),
            dob_ad=date_of_birth.get(),
            citizenship_number=citizenship.get(),
            telephone_number=telephone_number.get(),
        )
        return army

    def next_click():
        army = get_army_data()
        pass_data_fun(army)
        on_next_click()



    def back_click():  
        # Implement Back feature to navigate-Up 
        on_back_click()


    back_btn = ctk.CTkButton(phase2_part1_window, text="Back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#2D8A69", bg_color=frame_clr,command=back_click)
    back_btn.place(x=480, y=590)
    
    next_btn = ctk.CTkButton(phase2_part1_window, text="Next", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#2D8A69", bg_color=frame_clr,command=next_click)
    next_btn.place(x=680, y=590)
      