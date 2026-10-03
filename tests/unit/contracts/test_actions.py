import pytest
from pydantic import ValidationError

from mdia.contracts.actions import AgentAction
from mdia.domain.world import Gather


def test_valid_model_output_becomes_an_intent_for_the_acting_agent():
    proposed = AgentAction.model_validate_json('{"action": "gather", "node_id": "bush", "amount": 3}')

    assert proposed.to_intent("luma") == Gather(agent_id="luma", node_id="bush", amount=3)


def test_model_output_with_fields_outside_the_contract_is_rejected():
    with pytest.raises(ValidationError):
        AgentAction.model_validate_json(
            '{"action": "gather", "node_id": "bush", "amount": 3, "agent_id": "someone_else"}'
        )


@pytest.mark.parametrize("amount", [0, -1])
def test_contract_accepts_amounts_the_world_will_reject(amount):
    """Value checks belong to world rules, so bad decisions get journalled (ADR 0001)."""
    proposed = AgentAction.model_validate_json(f'{{"action": "gather", "node_id": "bush", "amount": {amount}}}')

    assert proposed.amount == amount
