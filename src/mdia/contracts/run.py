"""Run contract: what identifies a simulation run and the configuration it ran under."""

from pydantic import BaseModel, ConfigDict


class RunContext(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    run_id: str
    seed: int
    model_id: str
    """The served model, e.g. 'gpt-oss:20b'."""
    config_version: str
