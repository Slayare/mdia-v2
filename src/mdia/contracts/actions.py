"""Action contract: the shape a model's proposed action must take at the cognition boundary."""

from typing import Literal

from pydantic import BaseModel, ConfigDict

from mdia.domain.world import Gather


class AgentAction(BaseModel):
    """An action as the model proposes it. Structure only: whether it is possible is for world rules."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    action: Literal["gather"]
    node_id: str
    amount: int

    def to_intent(self, agent_id: str) -> Gather:
        """The acting agent comes from the engine, never from model output."""
        return Gather(agent_id=agent_id, node_id=self.node_id, amount=self.amount)
