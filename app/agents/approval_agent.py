from app.models.travel import APPROVAL_THRESHOLD


async def approval_agent(budget: int) -> bool:
    return budget >= APPROVAL_THRESHOLD
