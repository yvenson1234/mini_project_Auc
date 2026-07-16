from dataclasses import dataclass
from src.entities.book import Book
from src.use_cases.interfaces.book_repository import BookRepository

@dataclass
class ReturnBookInput:
    book_id: str

@dataclass
class ReturnBookOutput:
    book: Book | None
    success: bool
    message: str

class ReturnBookUseCase:
    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def execute(self, input_data: ReturnBookInput) -> ReturnBookOutput:
        book = self.repository.find_by_id(input_data.book_id)
        if book is None:
            return ReturnBookOutput(book=None, success=False, message="Book not found")

        try:
            book.return_book()
            updated_book = self.repository.update(book)
            return ReturnBookOutput(book=updated_book, success=True, message="Book returned successfully")
        except ValueError as exc:
            return ReturnBookOutput(book=book, success=False, message=str(exc))