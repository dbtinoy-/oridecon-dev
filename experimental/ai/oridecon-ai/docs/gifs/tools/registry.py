"""Shared tool definitions and constants for the tool-calling demo."""

OLLAMA_BASE = "http://localhost:11434"
OLLAMA_MODEL = "gemma4:12b"

WEATHER_TOOL = {
    "name": "get_weather",
    "description": "Current weather for a city.",
    "parameters": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"],
    },
}


def p(text):
    """Print and flush stdout."""
    import sys

    print(text)
    sys.stdout.flush()
