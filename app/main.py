from fastapi import FastAPI
from datetime import datetime, timezone
from app.utils.openai import call_openai
from app.routes.travel_planner import router as travel_router

app = FastAPI()


@app.get("/")
def home() -> dict:
    return {
        "name": "AI Travel Planner",
        "version": 1.0,
        "timestamp": datetime.now(timezone.utc),
    }


@app.post("/test-openai")
async def test_openai(model: str = None):
    prompt = f"""
        You are an AI system status assistant.

        Your task is to inform the user whether the OpenAI API is working successfully
        and specify which AI model is currently being used.

        Instructions:
        1. Clearly state whether the OpenAI API is operational.
        2. Mention the AI model currently being used.
        3. If a specific model is provided, mention that model.
        4. If no model is provided, use and mention the default model: gpt-4o-mini.
        5. Keep the response short, simple, and user-friendly.
        6. Do not provide unnecessary technical details.
        7. Do not claim that OpenAI is working unless the API call is successful.

        Current model: {model}
    """
    res = await call_openai(prompt=prompt)
    return res


app.include_router(travel_router, prefix="/travel", tags=["Travle"])
