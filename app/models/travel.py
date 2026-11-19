from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    PENDING = "pending"
    PENDING_APPROVAL = "pending_approval"
    COMPLETED = "completed"


APPROVAL_THRESHOLD = 30_000


@dataclass
class TravelState:
    destination: str
    days: int
    budget: int
    hotels: str = ""
    flights: str = ""
    weather: str = ""
    itinerary: str = ""
    approval_required: bool = False
    status: Status = Status.PENDING
