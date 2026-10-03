"""Context: build the bounded package of identity and perception the model decides from.

Prompts are written in-world: the sandbox is the Ontolette's whole reality.
"""

from mdia.contracts.observations import Observation
from mdia.domain.agents.identity import Ontolette


def build_prompt(identity: Ontolette, observation: Observation) -> str:
    sources = "\n".join(f"- {node}: {amount} left" for node, amount in observation.stocks.items())
    return (
        f"You are {identity.name}.\n"
        f"Traits: {', '.join(identity.traits)}\n"
        f"Goals: {', '.join(identity.goals)}\n"
        f"Beliefs: {', '.join(identity.beliefs)}\n"
        f"\n"
        f"You are carrying {observation.inventory}.\n"
        f"Around you:\n{sources}\n"
        f"\n"
        f"Choose one action and reply as JSON."
    )
