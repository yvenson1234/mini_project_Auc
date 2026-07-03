from dataclasses import dataclass, field
from enum import Enum

class Faculty(Enum) :
    CS = "CS"
    BA = "BA"
    CE = "CE"

@dataclass
class Student:
    id : int
    firstName : str
    lastName : str
    email : str
    faculty : Faculty


    def __post_init__(self):
        if not self.firstName.strip():
            raise ValueError("Student first name cannot be empty !!")
        if not self.email.strip():
            raise ValueError("Student email cannot be empty!!")
        if not self.lastName.strip():
            raise ValueError("Student last name cannot be empty!!")
            raise ValueError("Customer address connot be empty!!")
        self.name=self.name.strip()
        self.email=self.email.strip()
        self.phone=self.phone.strip()
        self.address=self.address.strip()