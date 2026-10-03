"""Simulation engine: drives agents' proposed actions through world rules."""

from typing import Protocol

from mdia.domain.events import ActionResolved
from mdia.domain.world import Gather, WorldState
from mdia.simulation.rules import resolve


class Decider(Protocol):
    def decide(self, agent_id: str) -> Gather: ...


class Journal(Protocol):
    def append(self, event: ActionResolved) -> None: ...


def run(state: WorldState, agent_id: str, decider: Decider, journal: Journal, ticks: int) -> WorldState:
    for tick in range(ticks):
        action = decider.decide(agent_id)
        state, result = resolve(state, action)
        journal.append(ActionResolved(tick, action, result))
    return state
