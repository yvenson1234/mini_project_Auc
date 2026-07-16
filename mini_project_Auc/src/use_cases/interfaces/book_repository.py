from abc import ABC, abstractmethod
from typing import List, Optional
from src.entities.book import Book

class BookRepository(ABC):

    @abstractmethod
    def save(self, book: Book) -> Book:
        pass    

    @abstractmethod
    def update(self, book: Book) -> Book:
        pass    

    @abstractmethod
    def find_by_id(self, book_id: str) -> Optional[Book]:
        pass    

    @abstractmethod
    def list_all(self) -> List[Book]:
        pass    

    @abstractmethod
    def search_by_title(self, title: str) -> List[Book]:
        pass