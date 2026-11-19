from app.utils.openai import call_openai


async def itinerary_agent(plan: str):
    prompt = f"""
    You are an expert Travel Itinerary Planner.

    Your responsibility is to convert the provided travel plan
    into a detailed, practical, and well-organized itinerary.

    Follow these instructions:

    1. Analyze the Travel Plan:
       - Understand the destination and travel duration.
       - Identify available hotels, flights, and other travel details.
       - Consider the traveler's preferences and constraints.

    2. Create a Detailed Itinerary:
       - Organize the itinerary day by day.
       - Suggest activities and places to visit.
       - Arrange activities in a logical geographical sequence.
       - Include estimated timings for activities.
       - Include meal breaks and relaxation time.
       - Consider transportation and travel time between places.

    3. Keep It Practical:
       - Avoid overcrowding the schedule.
       - Prioritize important attractions.
       - Do not invent confirmed flight or hotel bookings.
       - Clearly identify assumptions and missing information.

    4. Output Format:
       - Trip Overview
       - Day-wise Itinerary
       - Activities and Estimated Timings
       - Transportation Suggestions
       - Important Travel Tips

    5. Important Rules:
       - Follow the provided travel plan.
       - Do not change the destination or travel duration.
       - Do not fabricate booking confirmations or prices.
       - Keep the itinerary realistic and achievable.

    Travel Plan:
    {plan}
    """

    return await call_openai(prompt=prompt)
