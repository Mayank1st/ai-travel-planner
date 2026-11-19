from fastapi import APIRouter
from app.models.travel import APPROVAL_THRESHOLD
from app.schemas.travel_plan import (
    ApprovalDetails,
    TravelPlanRequest,
    TravelPlanResponse,
    TravelResearch,
    TripSummary,
)
from app.services.workflow_engine import execute_workflow

# from app.workflows.travel_workflow import TravelState

router = APIRouter()


@router.post("/travel-plan", response_model=TravelPlanResponse)
async def travel_plan(request: TravelPlanRequest) -> TravelPlanResponse:
    state = await execute_workflow(
        workflow_name="travel",
        payload={
            "destination": request.destination,
            "days": request.days,
            "budget": request.budget,
        },
    )
    approval_message = (
        f"Manual approval is required because the budget ({state.budget}) "
        f"meets or exceeds the threshold ({APPROVAL_THRESHOLD})."
        if state.approval_required
        else f"The budget ({state.budget}) is below the approval threshold "
        f"({APPROVAL_THRESHOLD}); no manual approval is required."
    )
    return TravelPlanResponse(
        trip=TripSummary(
            destination=state.destination,
            days=state.days,
            budget=state.budget,
        ),
        research=TravelResearch(
            hotels=state.hotels,
            flights=state.flights,
            weather=state.weather,
        ),
        itinerary=state.itinerary,
        approval=ApprovalDetails(
            required=state.approval_required,
            threshold=APPROVAL_THRESHOLD,
            message=approval_message,
        ),
        status=state.status,
    )
