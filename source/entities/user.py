from dataclasses import dataclass, field
from enum import Enum



@dataclass
class user:
    id : int
    firstName : str
    lastName : str
    email : str
    


    def __post_init__(self):
        if not self.firstName.strip():
            raise ValueError("User first name cannot be empty !!")
        if not self.email.strip():
            raise ValueError("User email cannot be empty!!")
        if not self.lastName.strip():
            raise ValueError("User last name cannot be empty!!")
            raise ValueError("userr address connot be empty!!")
        self.name=self.name.strip()
        self.email=self.email.strip()
        