"""Test configuration management."""

import os
from unittest import mock

import pytest

from xx.core.config import LLMProvider, Settings


def test_settings_from_env() -> None:
    """Test loading settings from environment variables."""
    test_env = {
        "XX_LLM_PROVIDER": "ollama",
        "XX_API_KEY": "test-key",
        "XX_MODEL_NAME": "test-model",
        "XX_API_BASE_URL": "http://test.local",
    }
    with mock.patch.dict(os.environ, test_env, clear=True):
        print("Environment variables:", dict(os.environ))
        settings = Settings()
        print("Settings:", settings.model_dump())
        assert settings.llm_provider == LLMProvider.OLLAMA
        assert settings.api_key == "test-key"
        assert settings.model_name == "test-model"
        assert settings.api_base_url == "http://test.local"


def test_settings_validation() -> None:
    """Test settings validation."""
    test_env = {"XX_LLM_PROVIDER": "invalid-provider"}
    with mock.patch.dict(os.environ, test_env, clear=True), pytest.raises(
        ValueError, match="Invalid LLM provider: invalid-provider"
    ):
        Settings()


def test_settings_default_values() -> None:
    """Test settings default values."""
    with mock.patch.dict(os.environ, {}, clear=True):
        settings = Settings()
        assert settings.llm_provider == LLMProvider.OPENAI
        assert settings.api_key is None
        assert settings.model_name == "gpt-4"
        assert settings.api_base_url is None
