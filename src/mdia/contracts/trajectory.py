"""Trajectory contract: one Ontolette's turn as it experienced it, for evals, analytics and training."""

import hashlib

from pydantic import BaseModel, ConfigDict, computed_field

from mdia.contracts.observations import Observation
from mdia.contracts.run import RunContext
from mdia.domain.world import ActionResult, Gather


class TurnRecord(BaseModel):
    model_config = ConfigDict(frozen=True)

    run: RunContext
    tick: int
    agent_id: str
    identity_version: int
    observation: Observation
    prompt: str
    raw_output: str
    latency_s: float
    """Wall-clock seconds the model took to reply; unrelated to simulated time."""
    intent: Gather | None
    """None when the model gave no usable action (the fallback); `error` then says why."""
    result: ActionResult | None
    """The world's verdict, or None when there was no intent to resolve."""
    error: str | None

    @computed_field
    @property
    def prompt_hash(self) -> str:
        """SHA-256 of the UTF-8 prompt, for grouping turns that saw exactly the same prompt."""
        return hashlib.sha256(self.prompt.encode("utf-8")).hexdigest()
