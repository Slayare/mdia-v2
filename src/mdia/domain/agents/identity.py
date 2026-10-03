"""Ontolette identity: who a simulated individual is, kept apart from their mutable state."""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class Ontolette:
    id: str
    name: str
    traits: tuple[str, ...]
    goals: tuple[str, ...]
    beliefs: tuple[str, ...]
    """Subjective claims the Ontolette holds; they may be wrong about the world."""

    def __init__(
        self, id: str, name: str, traits: Iterable[str], goals: Iterable[str], beliefs: Iterable[str]
    ) -> None:
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "traits", tuple(traits))
        object.__setattr__(self, "goals", tuple(goals))
        object.__setattr__(self, "beliefs", tuple(beliefs))
