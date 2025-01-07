# XX - Intelligent Command-Line Assistant

XX is an intelligent command-line assistant that helps users execute complex commands by understanding their natural language intent. It acts as a safety layer between user intentions and command execution, providing suggestions and validations without direct command execution.

## Features

- Natural language command understanding
- Command proposal and ranking system
- Safety-first approach with no direct command execution
- Intelligent output analysis
- Support for multiple LLM providers
- Context-aware command suggestions

## Installation

```bash
pip install xx-cli
```

## Quick Start

```bash
# Set up your environment variables
export XX_LLM_PROVIDER=openai
export XX_API_KEY=your_api_key

# Run XX with a command
xx tcpdump "show me all HTTP traffic"

# Analyze previous command output
xx "look for malicious activity"
```

## Configuration

XX can be configured using environment variables or a `.env` file:

```env
XX_LLM_PROVIDER=openai|anthropic|ollama
XX_API_KEY=your_api_key
XX_MODEL_NAME=gpt-4|claude-2|llama2
```

## Development

```bash
# Clone the repository
git clone https://github.com/username/xx.git
cd xx

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"
```

## License

MIT License
