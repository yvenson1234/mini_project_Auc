from dataclasses import dataclass
from src.entities.reservation import Reservation
from src.use_cases.interfaces.book_repository import BookRepository
from src.use_cases.interfaces.reservation_repository import ReservationRepository

@dataclass
class CancelReservationInput:
    reservation_id: str

@dataclass
class CancelReservationOutput:
    reservation: Reservation | None
    success: bool
    message: str

class CancelReservationUseCase:
    def __init__(self, reservation_repository: ReservationRepository, book_repository: BookRepository) -> None:
        self.reservation_repository = reservation_repository
        self.book_repository = book_repository

    def execute(self, input_data: CancelReservationInput) -> CancelReservationOutput:
        reservation = self.reservation_repository.find_by_id(input_data.reservation_id)
        if reservation is None:
            return CancelReservationOutput(reservation=None, success=False, message="Reservation not found")

        book = self.book_repository.find_by_id(reservation.book_id)
        if book is None:
            return CancelReservationOutput(reservation=None, success=False, message="Associated book not found")

        try:
            reservation.cancel_reservation()
            book.return_book()

            self.book_repository.update(book)
            updated_reservation = self.reservation_repository.update(reservation)

            return CancelReservationOutput(reservation=updated_reservation, success=True, message="Reservation canceled successfully")
        except ValueError as exc:
            return CancelReservationOutput(reservation=reservation, success=False, message=str(exc))