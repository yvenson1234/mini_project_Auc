from dataclasses import dataclass
from typing import List
from src.entities.book import Book
from src.use_cases.interfaces.book_repository import BookRepository

@dataclass
class SearchBookInput:
    title: str

@dataclass
class SearchBookOutput:
    books: List[Book]
    success: bool
    message: str

class SearchBookUseCase:
    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def execute(self, input_data: SearchBookInput) -> SearchBookOutput:
        clean_title = input_data.title.strip()
        if not clean_title:
            return SearchBookOutput(books=[], success=False, message="Search title cannot be empty")
        
        books = self.repository.search_by_title(clean_title)
        return SearchBookOutput(books=books, success=True, message=f"Found {len(books)} books")