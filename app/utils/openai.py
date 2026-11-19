from openai import AsyncOpenAI
from app.config.settings import Settings

settings = Settings()
client = AsyncOpenAI(api_key=settings.OPENAI_KEY)


async def call_openai(prompt: any, model: str = "gpt-4o-mini"):
    responses = await client.responses.create(input=prompt, model=model)
    return responses.output_text
