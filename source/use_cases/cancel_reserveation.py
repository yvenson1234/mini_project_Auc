from entities.Reservation import Reservation






class CancelReservationUseCase:

    def __init__(self, reservation_repository, book_repository):
        self.reservation_repository = reservation_repository
        self.book_repository = book_repository

    def execute(self, book_name: str):

        reservation = self.reservation_repository.get_by_book_name(book_name)

        if reservation is None:
            raise ValueError("Reservation not found.")

        reservation.cancel_reservation()

        self.book_repository.update(reservation.book)

        self.reservation_repository.update(reservation)

        return reservation