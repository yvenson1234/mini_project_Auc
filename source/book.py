from dataclasses import dataclass, field
from enum import Enum


class Category(Enum) :
    EXACT_SCIENCE = "EXACT_SCIENCES"
    LIFE_SCIENCES = "LIFE_SCIENCES"
    HUMANITIES = "HUMANITIES"   
    SOCIAL_SCIENCES = "SOCIAL_SCIENCES"
    COMPUTER_SCIENCE = "COMPUTER_SCIENCE"
    ENGINEERING = "ENGINEERING"
    LANGUAGES_AND_LITERATURE = "LANGUAGES_AND_LITERATURE"
    ARTS_AND_DESIGN = "ARTS_AND_DESIGN"
    EDUCATION = "EDUCATION"
    BUSINESS_AND_MANAGEMENT = "BUSINESS_AND_MANAGEMENT"
    MEDICINE_AND_HEALTH = "MEDICINE_AND_HEALTH"
    ENVIRONMENTAL_SCIENCES = "ENVIRONMENTAL_SCIENCES"


@dataclass
class Book:
    id : int
    title : str
    author : str
    category : Category
    status :  str = field(default="AVAILABLE")

    def __post_init__(self):
        if  not self.title.strip():
            raise ValueError("Book title connot be empty !!")
        if not self.author.strip():
            raise ValueError("Book's author connot be empty!!")
        self.title=self.title.strip()
        self.author=self.author.strip()
    
    def is_avalaible(self) -> bool:
        return self.status == "AVAILABLE"

    def reserve(self):
        if self.is_avalaible():
            self.status = "RESERVED"
        else:
            raise ValueError(
                f"Cannot reserve a book who is {self.status}"
            )

    def borrow(self):
        if self.is_avalaible():
            self.status = "BORROWED"
        else:
            raise ValueError(
                f"Cannot borrow a book who is {self.status}"
            )

    def returnBook(self):
        self.status = "AVAILABLE"