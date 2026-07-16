from src.use_cases.add_book import AddBookUseCase, AddBookInput
from src.use_cases.list_books import ListBooksUseCase
from src.use_cases.reserve_book import ReserveBookUseCase, ReserveBookInput
from src.use_cases.cancel_reservation import CancelReservationUseCase, CancelReservationInput
from src.entities.book import Category

from src.adapters.presenters.book_presenter import BookPresenter
from src.adapters.presenters.reservation_presenter import ReservationPresenter

class LibraryController:
    def __init__(
        self,
        add_book_uc: AddBookUseCase,
        list_books_uc: ListBooksUseCase,
        reserve_book_uc: ReserveBookUseCase,
        cancel_res_uc: CancelReservationUseCase,
        book_presenter: BookPresenter,
        res_presenter: ReservationPresenter
    ) -> None:
        self.add_book_uc = add_book_uc
        self.list_books_uc = list_books_uc
        self.reserve_book_uc = reserve_book_uc
        self.cancel_res_uc = cancel_res_uc
        self.book_presenter = book_presenter
        self.res_presenter = res_presenter

    def add_new_book(self, title: str, author: str, category: Category) -> str:
        input_data = AddBookInput(title=title, author=author, category=category)
        output_data = self.add_book_uc.execute(input_data)
        return self.book_presenter.format_add_book(output_data)

    def show_all_books(self) -> str:
        output_data = self.list_books_uc.execute()
        return self.book_presenter.format_list_books(output_data)

    def reserve_book(self, book_id: str, user_id: int) -> str:
        input_data = ReserveBookInput(book_id=book_id, user_id=user_id)
        output_data = self.reserve_book_uc.execute(input_data)
        return self.res_presenter.format_reservation(output_data)

    def cancel_reservation(self, reservation_id: str) -> str:
        input_data = CancelReservationInput(reservation_id=reservation_id)
        output_data = self.cancel_res_uc.execute(input_data)
        return self.res_presenter.format_cancel(output_data)