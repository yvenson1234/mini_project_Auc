from typing import Optional
from src.entities.reservation import Reservation, ReservationStatus
from src.use_cases.interfaces.reservation_repository import ReservationRepository

class InMemoryReservationRepository(ReservationRepository):
    def __init__(self) -> None:
        self._reservations: dict[str, Reservation] = {}

    def save(self, reservation: Reservation) -> Reservation:
        self._reservations[reservation.id] = reservation
        return reservation

    def update(self, reservation: Reservation) -> Reservation:
        if reservation.id in self._reservations:
            self._reservations[reservation.id] = reservation
        return reservation

    def find_by_id(self, reservation_id: str) -> Optional[Reservation]:
        return self._reservations.get(reservation_id)

    def count_active_by_student_id(self, user_id: int) -> int:
        return sum(
            1 for res in self._reservations.values()
            if res.user_id == user_id and res.status == ReservationStatus.ACTIVE
        )

    def delete(self, reservation_id: str) -> bool:
        if reservation_id in self._reservations:
            del self._reservations[reservation_id]
            return True
        return False
    