from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import uuid

def _now() -> datetime:
    return datetime.now(timezone.utc)

class ReservationStatus(Enum):
    ACTIVE = "ACTIVE"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"

@dataclass
class Reservation:
    book_id: str              
    user_id: int              
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: ReservationStatus = field(default=ReservationStatus.ACTIVE)
    created_at: datetime = field(default_factory=_now)
    updated_at: datetime = field(default_factory=_now)

    def cancel_reservation(self) -> None:
        if self.status != ReservationStatus.ACTIVE:
            raise ValueError(f"Cannot cancel a reservation that is '{self.status.value}'.")
        self.status = ReservationStatus.CANCELED
        self.updated_at = _now()

    def check_reservation_status(self) -> str:
        return self.status.value