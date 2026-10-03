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


class ScriptedModel:
    """Fake language model that returns the given replies in order, one per call."""

    def __init__(self, *replies: str) -> None:
        self._replies = iter(replies)

    def generate(self, prompt: str, schema: dict[str, Any]) -> str:
        return next(self._replies)


class SteppingClock:
    """Fake clock that returns the given times in order, one per call."""

    def __init__(self, *times: float) -> None:
        self._times = iter(times)

    def __call__(self) -> float:
        return next(self._times)
