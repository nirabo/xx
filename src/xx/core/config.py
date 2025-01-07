"""Configuration management for XX."""

from enum import Enum
from typing import Optional

from pydantic import BaseSettings, Field


class LLMProvider(str, Enum):
    """Supported LLM providers."""

    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OLLAMA = "ollama"


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    llm_provider: LLMProvider = Field(
        default=LLMProvider.OPENAI,
        env="XX_LLM_PROVIDER",
        description="LLM provider to use",
    )
    api_key: Optional[str] = Field(
        default=None,
        env="XX_API_KEY",
        description="API key for the LLM provider",
    )
    model_name: str = Field(
        default="gpt-4",
        env="XX_MODEL_NAME",
        description="Model name to use",
    )
    api_base_url: Optional[str] = Field(
        default=None,
        env="XX_API_BASE_URL",
        description="Base URL for API calls",
    )

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
