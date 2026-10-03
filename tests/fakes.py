"""Shared test doubles."""

from typing import Any


class CannedModel:
    """Fake language model that returns a fixed reply and remembers what it was asked."""

    def __init__(self, reply: str) -> None:
        self.reply = reply
        self.schema: dict[str, Any] | None = None

    def generate(self, prompt: str, schema: dict[str, Any]) -> str:
        self.schema = schema
        return self.reply
