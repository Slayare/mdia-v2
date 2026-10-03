"""Model ports: what cognition needs from a language model, independent of how it is served."""

from typing import Any, Protocol


class LanguageModel(Protocol):
    def generate(self, prompt: str, schema: dict[str, Any]) -> str:
        """Return raw text for the prompt, constrained to the JSON schema where the server supports it."""
        ...
