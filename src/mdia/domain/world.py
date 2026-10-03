"""World state and action types. The world owns reality; agents only propose actions."""

from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class WorldState:
    stocks: Mapping[str, int]
    """Remaining amount at each resource node, keyed by node id."""
    inventories: Mapping[str, int]
    """Amount each agent carries, keyed by agent id."""


@dataclass(frozen=True)
class Gather:
    agent_id: str
    node_id: str
    amount: int


@dataclass(frozen=True)
class ActionResult:
    accepted: bool
    reason: str | None = None
