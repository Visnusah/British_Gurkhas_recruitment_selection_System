from models.helper import get_splitted_name


class EmergencyContact:
    def __init__(self, full_name=None,address=None,mobile_number=None,dob_ad=None,telephone_num=None):
        self.full_name = full_name
        self.address = address
        self.mobile_number = mobile_number
        self.telephone_num = telephone_num
        self.dob_ad = dob_ad


class FirstEmergencyContact(EmergencyContact):
    def __init__(self, full_name=None,address=None,mobile_number=None,dob_ad=None,telephone_num=None):
        super().__init__(full_name,address,mobile_number,dob_ad,telephone_num)


class SecondEmergencyContact(EmergencyContact):
    def __init__(self, full_name=None,address=None,mobile_number=None,dob_ad=None,telephone_num=None):
        super().__init__(full_name,address,mobile_number,dob_ad,telephone_num)

