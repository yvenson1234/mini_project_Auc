class CancelReservationUseCase:
    def __init__(self, reservation_repository, book_repository):
        self.reservation_repository = reservation_repository
        self.book_repository = book_repository

    def execute(self, book_name: str):
        reservation = self.reservation_repository.get_by_book_name(book_name)

        if reservation is None:
            raise ValueError("Reservation not found.")

        
        reservation.cancel_reservation()
        self.reservation_repository.update(reservation)

        
        books = self.book_repository.search_by_title(book_name)
        if books and len(books) > 0:
            target_book = books[0]
            target_book.return_book()
            self.book_repository.update(target_book)

        return reservation