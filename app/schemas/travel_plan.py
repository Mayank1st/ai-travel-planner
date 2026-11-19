from pydantic import BaseModel

from app.models.travel import Status


class TravelPlanRequest(BaseModel):
    destination: str
    days: int
    budget: int


class TripSummary(BaseModel):
    destination: str
    days: int
    budget: int


class TravelResearch(BaseModel):
    hotels: str
    flights: str
    weather: str


class ApprovalDetails(BaseModel):
    required: bool
    threshold: int
    message: str


class TravelPlanResponse(BaseModel):
    trip: TripSummary
    research: TravelResearch
    itinerary: str
    approval: ApprovalDetails
    status: Status
