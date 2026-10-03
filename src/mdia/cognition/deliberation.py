"""Deliberation: ask the shared model what an Ontolette proposes to do."""

import time
from collections.abc import Callable
from dataclasses import dataclass

from pydantic import ValidationError

from mdia.contracts.actions import AgentAction
from mdia.domain.world import Gather
from mdia.models.ports import LanguageModel


@dataclass(frozen=True)
class Decision:
    intent: Gather | None
    """None when the model gave no usable action (the fallback); `error` then says why."""
    raw_output: str
    latency_s: float
    """Wall-clock seconds the model took to reply; unrelated to simulated time."""
    error: str | None = None


def deliberate(
    model: LanguageModel, agent_id: str, prompt: str, clock: Callable[[], float] = time.perf_counter
) -> Decision:
    started = clock()
    raw = model.generate(prompt, AgentAction.model_json_schema())
    latency_s = clock() - started
    try:
        proposed = AgentAction.model_validate_json(raw)
    except ValidationError as error:
        return Decision(intent=None, raw_output=raw, latency_s=latency_s, error=str(error))
    return Decision(intent=proposed.to_intent(agent_id), raw_output=raw, latency_s=latency_s)
