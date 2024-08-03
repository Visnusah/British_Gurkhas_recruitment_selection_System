from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
from models.army import Army
from models.emergency_contact import FirstEmergencyContact,SecondEmergencyContact
from db.database import execute_query


previous_screen_data=None

def received_data(data):
    global previous_screen_data
    previous_screen_data=data

def open_phase2_part2(phase2_part2_window,on_finish_click, ob_back_click):
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


    phase2_part2_window.config(bg=background)

    # Label for Application Form
    application_form = Label(phase2_part2_window, text="Phase 2", font=phase_font, bg=background, fg=framefg)
    application_form.place(x= 550, y=20)

    #LogOut Button
    def logout():
        phase2_part2_window.destroy()
        import login
        login.phase2_part2_window.mainloop()
        
    logout_button = ctk.CTkButton(phase2_part2_window,
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
    logo_icon = Label(phase2_part2_window, image = imageOne, bg=background) # attach the image to a label
    logo_icon.image = imageOne # keep a reference to the image object to prevent garbage collection by python
    logo_icon.place(x= 20, y=0) # place the label in the window    


    # create a main frame
    form_Frame = ctk.CTkFrame(phase2_part2_window, width=1157, height=590, corner_radius=30, bg_color="transparent")
    form_Frame.grid(row=0, column=1, padx=61, pady=120)


    part2_lbl = Label(form_Frame, text="Part 2".upper(), font=part2_font,bg=frame_clr)
    part2_lbl.place(x=20, y=5)


    heading_lbl = Label(form_Frame, text="EMERGENCY CONTACT DETAIL - MUST BE COMPLETED BY THE APPLICANT:".upper(), font=heading_font,bg=frame_clr)
    heading_lbl.place(x=235, y=20)

    # Entry Fields for Application Form
    # First Column

    part2_lbl = Label(form_Frame, text="First Contact:".upper(), font=subheading_font,bg=frame_clr)
    part2_lbl.place(x=80, y=75)

    fec_full_name = ctk.CTkEntry(form_Frame, width=1000, height=56, font=font1,corner_radius=10, placeholder_text="Detail Full Name".upper(), border_color=frame_clr)
    fec_full_name.place(x=80, y=110)

    fec_address = ctk.CTkEntry(form_Frame, width=720, height=56, font=font1, corner_radius=10,placeholder_text="Address".upper(),  border_color=frame_clr)
    fec_address.place(x=80, y=175)

    fec_mobile_number = ctk.CTkEntry(form_Frame, width=550, height=56, font=font1, corner_radius=10,placeholder_text="Mobile Number".upper(), border_color=frame_clr)
    fec_mobile_number.place(x=80, y=240)


    part3_lbl = Label(form_Frame, text="Second Contact:".upper(), font=subheading_font,bg=frame_clr)
    part3_lbl.place(x=80, y=300)

    sec_full_name = ctk.CTkEntry(form_Frame, width=1000, height=56, font=font1, corner_radius=10,placeholder_text="Detail Full Name".upper(), border_color=frame_clr)
    sec_full_name.place(x=80, y=335)

    sec_address = ctk.CTkEntry(form_Frame, width=720, height=56, font=font1,corner_radius=10, placeholder_text="Address".upper(),  border_color=frame_clr)
    sec_address.place(x=80, y=400)

    sec_mobile_number = ctk.CTkEntry(form_Frame, width=550, height=56, font=font1, corner_radius=10,placeholder_text="Mobile Number".upper(), border_color=frame_clr)
    sec_mobile_number.place(x=80, y=465)

    # Second Column

    fec_date_of_birth = ctk.CTkEntry(form_Frame, width=260, height=56, font=font1, corner_radius=10,placeholder_text="Date of Birth (AD)".upper(), border_color=frame_clr)
    fec_date_of_birth.place(x=820, y=175)

    fec_telephone_number = ctk.CTkEntry(form_Frame, width=430, height=56, font=font1, corner_radius=10,placeholder_text="Telephone Number".upper(), border_color=frame_clr)
    fec_telephone_number.place(x=650, y=240)


    sec_date_of_birth = ctk.CTkEntry(form_Frame, width=260, height=56, font=font1, corner_radius=10,placeholder_text="Date of Birth (AD)".upper(), border_color=frame_clr)
    sec_date_of_birth.place(x=820, y=400)

    sec_telephone_number = ctk.CTkEntry(form_Frame, width=430, height=56, font=font1, corner_radius=10,placeholder_text="Telephone Number".upper(), border_color=frame_clr)
    sec_telephone_number.place(x=650, y=465)


    def get_army_data():
        first_emergency_contact = FirstEmergencyContact(full_name=fec_full_name.get(),address=fec_address.get(),mobile_number=fec_mobile_number.get(),dob_ad=fec_date_of_birth.get(),telephone_num=fec_telephone_number.get())
        second_emergency_contact = SecondEmergencyContact(full_name=sec_full_name.get(),address=sec_address.get(),mobile_number=sec_mobile_number.get(),dob_ad=sec_date_of_birth.get(),telephone_num=sec_telephone_number.get())
        army = Army(
            first_emergency_contact=first_emergency_contact,
            second_emergency_contact=second_emergency_contact
        )
        return army
    
    def save_data(part2_data,part1_data):
        fec_data = part2_data.first_emergency_contact
        sec_data = part2_data.second_emergency_contact
        army = part1_data
        fec_query = rf"INSERT into fec(fullname,address,mobile_number,telephone_number,dob_ad) VALUES ('{fec_data.full_name}','{fec_data.address}','{fec_data.mobile_number}','{fec_data.telephone_num}','{fec_data.dob_ad}')"
        sec_query = rf"INSERT into sec(fullname,address,mobile_number,telephone_number,dob_ad) VALUES ('{sec_data.full_name}','{sec_data.address}','{sec_data.mobile_number}','{sec_data.telephone_num}','{sec_data.dob_ad}')"
        
        inserted_fec_id = execute_query(fec_query)
        inserted_sec_id = execute_query(sec_query)

        if inserted_fec_id is not None and inserted_sec_id is not None:
            army_query = rf"""
            INSERT INTO army(first_name,middle_name,surname,email,address_location,telephone_number,citizenship_number,dob_ad,first_emergency_contact,second_emergency_contact) VALUES
('{army.first_name}','{army.middle_name}','{army.surname}','{army.email}','{army.address_location}','{army.telephone_number}','{army.citizenship_number}','{army.dob_ad}',{inserted_fec_id},{inserted_sec_id}) """
            print(army_query)
            result = execute_query(army_query)
            if result:
                messagebox.showinfo("Success", "Application Submitted Successfully")
        

    def next_click():
        part1_army_data = previous_screen_data
        part2_army_data = get_army_data()
        save_data(part2_army_data,part1_army_data)
        

    def back_click():
        ob_back_click()
        

    back_btn = ctk.CTkButton(phase2_part2_window, text="Back", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#2D8A69", bg_color=frame_clr,command=back_click)
    back_btn.place(x=480, y=655)
    
    next_btn = ctk.CTkButton(phase2_part2_window, text="Save", width=130, height=45, corner_radius=10, font=next_btn_font, fg_color="#2D8A69", bg_color=frame_clr,command=next_click)
    next_btn.place(x=680, y=655)