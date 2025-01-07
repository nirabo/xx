"""Configuration management for the XX CLI."""

from enum import Enum
from typing import Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMProvider(str, Enum):
    """Supported LLM providers."""

    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OLLAMA = "ollama"


class Settings(BaseSettings):
    """Settings for the XX CLI."""

    llm_provider: LLMProvider = Field(default=LLMProvider.OPENAI)
    api_key: Optional[str] = Field(default=None)
    model_name: str = Field(default="gpt-4")
    api_base_url: Optional[str] = Field(default=None)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        env_prefix="XX_",
        protected_namespaces=("settings_",),
    )

    @field_validator("llm_provider", mode="before")
    @classmethod
    def validate_llm_provider(cls, v: str | LLMProvider) -> LLMProvider:
        """Validate LLM provider."""
        if isinstance(v, LLMProvider):
            return v

        v = str(v).lower()
        try:
            return LLMProvider(v)
        except ValueError:
            providers = ", ".join(p.value for p in LLMProvider)
            raise ValueError(f"Invalid LLM provider: {v}. Must be one of: {providers}")
