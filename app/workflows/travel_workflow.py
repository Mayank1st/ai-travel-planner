import asyncio

from app.models.travel import Status, TravelState
from app.utils.openai import call_openai

from app.agents.approval_agent import approval_agent
from app.agents.itinerary_agent import itinerary_agent
from app.agents.planner_agent import planner_agent


# Hotel Research
async def search_hotels(state: TravelState):
    prompt = f"""
    Suggest hotels in :{state.destination}
    Budget : {state.budget}
    """

    return await call_openai(prompt=prompt)


# Hotel Flight
async def search_flights(state: TravelState):
    prompt = f"""
    Suggest flights to :{state.destination}
    """

    return await call_openai(prompt=prompt)


# Hotel Weather
async def search_weathers(state: TravelState):
    prompt = f"""
    Describe weather in :{state.destination}
    """

    return await call_openai(prompt=prompt)


async def run_research(state: TravelState):
    state.hotels, state.flights, state.weather = await asyncio.gather(
        search_hotels(state), search_flights(state), search_weathers(state)
    )
    return state


async def run_travel_workflow(destination: str, days: int, budget: int):
    state = TravelState(destination=destination, days=days, budget=budget)
    state = await run_research(state=state)
    plan = await planner_agent(state=state)
    state.itinerary = await itinerary_agent(plan=plan)
    state.approval_required = await approval_agent(state.budget)
    if state.approval_required:
        state.status = Status.PENDING_APPROVAL
    else:
        state.status = Status.COMPLETED

    return state
