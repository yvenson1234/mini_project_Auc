from dataclasses import dataclass
from src.entities.book import Book, Category
from src.use_cases.interfaces.book_repository import BookRepository

@dataclass
class AddBookInput:
    title: str
    author: str
    category: Category

@dataclass
class AddBookOutput:
    book: Book | None
    success: bool
    message: str

class AddBookUseCase:
    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def execute(self, input_data: AddBookInput) -> AddBookOutput:
        try:
            new_book = Book(
                title=input_data.title,
                author=input_data.author,
                category=input_data.category
            )
            saved_book = self.repository.save(new_book)
            return AddBookOutput(book=saved_book, success=True, message="Book added successfully")
        except ValueError as exc:
            return AddBookOutput(book=None, success=False, message=str(exc))