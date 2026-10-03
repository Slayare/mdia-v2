"""Observation contract: what an Ontolette perceives of the world on a turn."""

from pydantic import BaseModel, ConfigDict


class Observation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    inventory: int
    """Amount the observing agent carries."""
    stocks: dict[str, int]
    """Visible resource nodes and the amount each holds."""
