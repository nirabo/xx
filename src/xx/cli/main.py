"""Main CLI application."""

import typer
from rich import print

app = typer.Typer(
    name="xx",
    help="XX - Intelligent command-line assistant",
    add_completion=False,
)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Process command and query to provide intelligent assistance."""
    if ctx.invoked_subcommand is None:
        print("Welcome to XX!")
        print("Type --help for usage information.")


if __name__ == "__main__":
    app()
