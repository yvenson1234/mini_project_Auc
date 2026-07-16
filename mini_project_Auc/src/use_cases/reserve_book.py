from dataclasses import dataclass
from src.entities.reservation import Reservation
from src.use_cases.interfaces.book_repository import BookRepository
from src.use_cases.interfaces.reservation_repository import ReservationRepository

@dataclass
class ReserveBookInput:
    book_id: str
    user_id: int

@dataclass
class ReserveBookOutput:
    reservation: Reservation | None
    success: bool
    message: str

class ReserveBookUseCase:
    def __init__(self, book_repository: BookRepository, reservation_repository: ReservationRepository) -> None:
        self.book_repository = book_repository
        self.reservation_repository = reservation_repository

    def execute(self, input_data: ReserveBookInput) -> ReserveBookOutput:
        book = self.book_repository.find_by_id(input_data.book_id)
        if book is None:
            return ReserveBookOutput(reservation=None, success=False, message="Book not found")

        if not book.is_available():
            return ReserveBookOutput(reservation=None, success=False, message="Book is not available")

        active_count = self.reservation_repository.count_active_by_student_id(input_data.user_id)
        if active_count >= 3:
            return ReserveBookOutput(reservation=None, success=False, message="Student reached max limit of 3 active reservations")

        try:
            book.reserve()
            new_reservation = Reservation(book_id=input_data.book_id, user_id=input_data.user_id)
            
            self.book_repository.update(book)
            saved_reservation = self.reservation_repository.save(new_reservation)
            
            return ReserveBookOutput(reservation=saved_reservation, success=True, message="Book reserved successfully")
        except ValueError as exc:
            return ReserveBookOutput(reservation=None, success=False, message=str(exc))