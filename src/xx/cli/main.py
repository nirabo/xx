"""Main CLI entry point for XX."""

import typer
from rich import print
from rich.console import Console
from rich.panel import Panel

from xx.core.config import Settings
from xx.core.context import CommandContext

app = typer.Typer(
    name="xx",
    help="Intelligent command-line assistant",
    add_completion=False,
)
console = Console()

@app.callback()
def callback() -> None:
    """XX - Intelligent command-line assistant."""
    pass

@app.command()
def main(
    command: str = typer.Argument(None, help="Command to analyze or execute"),
    query: str = typer.Argument(None, help="Natural language query"),
) -> None:
    """Process command and query to provide intelligent assistance."""
    try:
        settings = Settings()
        context = CommandContext()
        
        if not command and not query:
            # Show help if no arguments provided
            console.print(
                Panel.fit(
                    "Welcome to XX! Please provide a command or query.",
                    title="XX CLI",
                    border_style="blue",
                )
            )
            raise typer.Exit()
            
        # TODO: Implement command processing logic
        console.print("[bold blue]Processing your request...[/]")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/] {str(e)}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
