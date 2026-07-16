from src.use_cases.reserve_book import ReserveBookOutput
from src.use_cases.cancel_reservation import CancelReservationOutput

class ReservationPresenter:
    def format_reservation(self, output: ReserveBookOutput) -> str:
        if not output.success:
            return f"RESERVATION FAILED: {output.message}"
        res = output.reservation
        return f"RESERVATION CONFIRMED!\n   Reservation ID: {res.id}\n   Book ID: {res.book_id}\n   User ID: {res.user_id}"

    def format_cancel(self, output: CancelReservationOutput) -> str:
        if not output.success:
            return f"CANCELLATION FAILED: {output.message}"
        res = output.reservation
        return f"CANCELLATION COMPLETED!\n   Reservation {res.id} is now canceled."