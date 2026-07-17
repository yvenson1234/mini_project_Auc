from entities.book import Book, Category
from entities.reservation import Reservation
from use_cases.add_book import AddBookUseCase
from use_cases.list_books import ListBooksUseCase
from use_cases.search_book import SearchBookUseCase
from use_cases.reserve_book import ReserveBookUseCase
from use_cases.cancel_reservation import CancelReservationUseCase
from use_cases.return_book import ReturnBookUseCase

class LibraryController:
    def __init__(self, book_repo, reservation_repo, presenter):
        self.presenter = presenter
        
        self.add_book_use_case = AddBookUseCase(book_repo)
        self.list_books_use_case = ListBooksUseCase(book_repo)
        self.search_book_use_case = SearchBookUseCase(book_repo)
        self.reserve_book_use_case = ReserveBookUseCase(book_repo, reservation_repo)
        self.cancel_reservation_use_case = CancelReservationUseCase(reservation_repo, book_repo)
        self.return_book_use_case = ReturnBookUseCase(book_repo)

    def add_book(self, book_id: int, title: str, author: str, category_name: str) -> str:
        try:
            category = Category[category_name.upper()]
            book = Book(id=book_id, title=title, author=author, category=category)
            saved_book = self.add_book_use_case.execute(book)
            return self.presenter.present_success(f"Book '{saved_book.title}' added successfully.")
        except KeyError:
            return self.presenter.present_error(f"Invalid Category: '{category_name}'.")
        except ValueError as e:
            return self.presenter.present_error(str(e))

    def list_all_books(self) -> str:
        books = self.list_books_use_case.execute()
        return self.presenter.present_book_list(books)

    def search_book(self, title: str) -> str:
        try:
            books = self.search_book_use_case.execute(title)
            return self.presenter.present_search_results(title, books)
        except ValueError as e:
            return self.presenter.present_error(str(e))

    def reserve_book(self, reservation_id: int, book_title: str, user_id: int) -> str:
        try:
            reservation = Reservation(
                reservation_id=reservation_id,
                book_name=book_title,
                user_id=user_id
            )
            res = self.reserve_book_use_case.execute(reservation)
            return self.presenter.present_success(
                f"Reservation #{res.reservation_id} created for '{res.book_name}' (User ID: {res.user_id})."
            )
        except ValueError as e:
            return self.presenter.present_error(str(e))

    def cancel_reservation(self, book_name: str) -> str:
        try:
            res = self.cancel_reservation_use_case.execute(book_name)
            return self.presenter.present_success(
                f"Reservation for '{res.book_name}' has been canceled. Book is now AVAILABLE."
            )
        except ValueError as e:
            return self.presenter.present_error(str(e))

    def return_book(self, book_id: int) -> str:
        try:
            book = self.return_book_use_case.execute(book_id)
            return self.presenter.present_success(f"Book ID {book.id} ('{book.title}') has been returned successfully.")
        except ValueError as e:
            return self.presenter.present_error(str(e))