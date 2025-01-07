"""Test configuration and fixtures."""

from typing import Any

import pytest
from typer.testing import CliRunner

from xx.cli.main import app
from xx.core.config import Settings
from xx.core.context import CommandContext


@pytest.fixture
def runner() -> CliRunner:
    """Create a CLI runner for testing."""
    return CliRunner()


@pytest.fixture
def cli() -> Any:
    """Get the CLI app for testing."""
    return app


@pytest.fixture
def settings() -> Settings:
    """Create test settings."""
    return Settings(
        llm_provider="openai",
        api_key="test-key",
        model_name="gpt-4",
    )


@pytest.fixture
def command_context() -> CommandContext:
    """Create a test command context."""
    return CommandContext()
