"""Events: immutable records of meaningful causal changes in the world."""

from dataclasses import dataclass

from mdia.domain.world import ActionResult, Gather


@dataclass(frozen=True)
class ActionResolved:
    action: Gather
    result: ActionResult
