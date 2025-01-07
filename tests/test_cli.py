"""Test the CLI interface."""

from typer.testing import CliRunner

from xx.cli.main import app


def test_cli_help(runner: CliRunner) -> None:
    """Test the CLI help command."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "XX - Intelligent command-line assistant" in result.stdout


def test_cli_no_args(runner: CliRunner) -> None:
    """Test CLI with no arguments."""
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Welcome to XX!" in result.stdout
