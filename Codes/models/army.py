from .base_user import BaseUser
from .emergency_contact import FirstEmergencyContact,SecondEmergencyContact


class Army(BaseUser):
    def __init__(self,first_name=None,middle_name=None, surname=None, email=None, telephone_number=None,address_location=None, citizenship_number=None,father_name=None,mother_name=None,religion=None,district=None,village=None,dob_ad=None,dob_bd=None,army_id=None,first_emergency_contact=None,second_emergency_contact=None):
        super().__init__(first_name,middle_name, surname, email, telephone_number,address_location, citizenship_number,father_name,mother_name,religion,district,village,dob_ad,dob_bd)
        self.army_id = army_id
        self.first_emergency_contact = first_emergency_contact if first_emergency_contact else FirstEmergencyContact()
        self.second_emergency_contact = second_emergency_contact if second_emergency_contact else SecondEmergencyContact()


