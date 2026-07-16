from typing import List, Optional
from src.entities.book import Book
from src.use_cases.interfaces.book_repository import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self) -> None:
        self._books: dict[str, Book] = {}

    def save(self, book: Book) -> Book:
        self._books[book.id] = book
        return book

    def update(self, book: Book) -> Book:
        if book.id in self._books:
            self._books[book.id] = book
        return book

    def find_by_id(self, book_id: str) -> Optional[Book]:
        return self._books.get(book_id)

    def list_all(self) -> List[Book]:
        return list(self._books.values())

    def search_by_title(self, title: str) -> List[Book]:
        return [
            book for book in self._books.values()
            if title.lower() in book.title.lower()
        ]