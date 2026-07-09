
from interfaces.book_repository import BookRepository





class ReturnBookUseCase:

    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, book_id):

        book = self.book_repository.get_by_id(book_id)

        if book is None:
            raise ValueError("Book not found.")

        book.return_book()

        self.book_repository.update(book)

        return book