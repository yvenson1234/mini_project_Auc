from interfaces.reservation_repository import ReservationRepository

class InMemoryReservationRepository(ReservationRepository):
    def __init__(self):
        self.reservations = {}

    def add(self, reservation):
        self.reservations[reservation.reservation_id] = reservation

    def update(self, reservation):
        if reservation.reservation_id in self.reservations:
            self.reservations[reservation.reservation_id] = reservation

    def get_by_book_name(self, book_name: str):
        for res in self.reservations.values():
            if res.book_name.lower() == book_name.lower():
                return res
        return None

    def delete(self, reservation_id):
        if reservation_id in self.reservations:
            del self.reservations[reservation_id]