from dataclasses import dataclass
from src.use_cases.interfaces.reservation_repository import ReservationRepository

@dataclass
class DeleteReservationInput:
    reservation_id: str

@dataclass
class DeleteReservationOutput:
    deleted: bool
    message: str

class DeleteReservationUseCase:
    def __init__(self, repository: ReservationRepository) -> None:
        self.repository = repository

    def execute(self, input_data: DeleteReservationInput) -> DeleteReservationOutput:
        deleted = self.repository.delete(input_data.reservation_id)

        if deleted:
            return DeleteReservationOutput(deleted=True, message="Reservation deleted successfully")

        return DeleteReservationOutput(
            deleted=False,
            message=f"Reservation '{input_data.reservation_id}' not found — nothing was deleted"
        )