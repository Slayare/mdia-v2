"""Deliberation: ask the shared model what an Ontolette proposes to do."""

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
    error: str | None = None


def deliberate(model: LanguageModel, agent_id: str, prompt: str) -> Decision:
    raw = model.generate(prompt, AgentAction.model_json_schema())
    try:
        proposed = AgentAction.model_validate_json(raw)
    except ValidationError as error:
        return Decision(intent=None, raw_output=raw, error=str(error))
    return Decision(intent=proposed.to_intent(agent_id), raw_output=raw)
