"""Command context management."""

from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class CommandContext:
    """Maintains context between commands."""

    last_command: Optional[str] = None
    last_output: Optional[str] = None
    command_history: Dict[str, str] = field(default_factory=dict)
    
    def update_context(self, command: str, output: Optional[str] = None) -> None:
        """Update context with new command and output."""
        self.last_command = command
        if output is not None:
            self.last_output = output
            self.command_history[command] = output
    
    def get_last_output(self) -> Optional[str]:
        """Get the output of the last command."""
        return self.last_output
