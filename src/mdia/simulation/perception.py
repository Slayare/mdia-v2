"""Perception: the world decides what an agent can observe of it."""

from mdia.contracts.observations import Observation
from mdia.domain.world import WorldState


def observe(state: WorldState, agent_id: str) -> Observation:
    return Observation(inventory=state.inventories[agent_id], stocks=dict(state.stocks))
