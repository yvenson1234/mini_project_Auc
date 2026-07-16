from dataclasses import dataclass
from typing import List
from src.entities.book import Book
from src.use_cases.interfaces.book_repository import BookRepository

@dataclass
class ListBooksOutput:
    books: List[Book]
    success: bool
    message: str

class ListBooksUseCase:
    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def execute(self) -> ListBooksOutput:
        books = self.repository.list_all()
        return ListBooksOutput(books=books, success=True, message="Books retrieved successfully")