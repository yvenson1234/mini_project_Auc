from abc import ABC, abstractmethod
from typing import Optional
from src.entities.reservation import Reservation

class ReservationRepository(ABC):    

    @abstractmethod
    def save(self, reservation: Reservation) -> Reservation:
        pass    

    @abstractmethod
    def update(self, reservation: Reservation) -> Reservation:
        pass    

    @abstractmethod
    def find_by_id(self, reservation_id: str) -> Optional[Reservation]:
        pass    

    @abstractmethod
    def count_active_by_student_id(self, user_id: int) -> int:
        pass

    @abstractmethod
    def delete(self, reservation_id: str) -> bool:
        pass