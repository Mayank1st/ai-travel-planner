from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    OPENAI_KEY: str = Field(
        ...,
        description="OpenAI API key",
        examples=["sk-xxxxxxxx"],
    )

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")
