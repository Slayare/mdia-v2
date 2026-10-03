"""Trajectory contract: one Ontolette's turn as it experienced it, for evals, analytics and training."""

from pydantic import BaseModel, ConfigDict

from mdia.contracts.observations import Observation
from mdia.contracts.run import RunContext
from mdia.domain.world import ActionResult, Gather


class TurnRecord(BaseModel):
    model_config = ConfigDict(frozen=True)

    run: RunContext
    tick: int
    agent_id: str
    observation: Observation
    prompt: str
    raw_output: str
    intent: Gather | None
    """None when the model gave no usable action (the fallback); `error` then says why."""
    result: ActionResult | None
    """The world's verdict, or None when there was no intent to resolve."""
    error: str | None
