"""Simulation engine: drives agents' proposed actions through world rules."""

from typing import Protocol

from mdia.cognition.context import build_prompt
from mdia.cognition.deliberation import deliberate
from mdia.contracts.run import RunContext
from mdia.contracts.trajectory import TurnRecord
from mdia.domain.agents.identity import Ontolette
from mdia.domain.events import ActionResolved
from mdia.domain.world import Gather, WorldState
from mdia.models.ports import LanguageModel
from mdia.simulation.perception import observe
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


def take_turn(
    state: WorldState,
    identity: Ontolette,
    model: LanguageModel,
    journal: Journal,
    tick: int,
    run: RunContext,
) -> tuple[WorldState, TurnRecord]:
    observation = observe(state, identity.id)
    prompt = build_prompt(identity, observation)
    decision = deliberate(model, identity.id, prompt)
    result = None
    # Fallback: with no usable intent nothing happens in the world, so nothing is journalled.
    if decision.intent is not None:
        state, result = resolve(state, decision.intent)
        journal.append(ActionResolved(tick, decision.intent, result))
    record = TurnRecord(
        run=run,
        tick=tick,
        agent_id=identity.id,
        observation=observation,
        prompt=prompt,
        raw_output=decision.raw_output,
        intent=decision.intent,
        result=result,
        error=decision.error,
    )
    return state, record
