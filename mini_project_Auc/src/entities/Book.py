from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import uuid

def _now() -> datetime:
    return datetime.now(timezone.utc)

class Category(Enum):
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

class BookStatus(Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"

@dataclass
class Book:
    title: str
    author: str
    category: Category
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: BookStatus = field(default=BookStatus.AVAILABLE)
    created_at: datetime = field(default_factory=_now)
    updated_at: datetime = field(default_factory=_now)

    def __post_init__(self) -> None:
        if not self.title or not self.title.strip():
            raise ValueError("Book title cannot be empty")
        if not self.author or not self.author.strip():
            raise ValueError("Book author cannot be empty")
        self.title = self.title.strip()
        self.author = self.author.strip()
    
    def is_available(self) -> bool:
        return self.status == BookStatus.AVAILABLE

    def reserve(self) -> None:
        if not self.is_available():
            raise ValueError(f"Cannot reserve a book that is '{self.status.value}'.")
        self.status = BookStatus.RESERVED
        self.updated_at = _now()

    def return_book(self) -> None:
        if self.status != BookStatus.RESERVED:   
            raise ValueError(f"Cannot return a book that is '{self.status.value}'.")
        self.status = BookStatus.AVAILABLE
        self.updated_at = _now()