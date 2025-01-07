"""Test command context management."""

from xx.core.context import CommandContext


def test_command_context_creation() -> None:
    """Test creating a new command context."""
    context = CommandContext()
    assert context is not None
    assert context.command == ""
    assert context.args == []


def test_command_context_with_command() -> None:
    """Test command context with a command."""
    context = CommandContext()
    context.command = "ls"
    context.args = ["-l", "-a"]
    assert context.command == "ls"
    assert context.args == ["-l", "-a"]


def test_command_context_reset() -> None:
    """Test resetting command context."""
    context = CommandContext()
    context.command = "ls"
    context.args = ["-l", "-a"]

    context.reset()
    assert context.command == ""
    assert context.args == []
