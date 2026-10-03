from typing import Any

import pytest

from mdia.cognition.deliberation import Decision, deliberate
from mdia.contracts.actions import AgentAction
from mdia.domain.world import Gather


class CannedModel:
    """Fake language model that returns a fixed reply and remembers what it was asked."""

    def __init__(self, reply: str) -> None:
        self.reply = reply
        self.schema: dict[str, Any] | None = None

    def generate(self, prompt: str, schema: dict[str, Any]) -> str:
        self.schema = schema
        return self.reply


def test_valid_model_output_becomes_a_decision_with_an_intent():
    raw = '{"action": "gather", "node_id": "bush", "amount": 3}'

    decision = deliberate(CannedModel(raw), "ada", "You are Ada.")

    assert decision == Decision(intent=Gather("ada", "bush", 3), raw_output=raw)


@pytest.mark.parametrize(
    "raw",
    [
        "I think I'll gather some berries.",
        '{"action": "fly", "node_id": "bush", "amount": 3}',
        '{"action": "gather", "node_id": "bush", "amount": 3, "agent_id": "bob"}',
    ],
)
def test_unusable_model_output_falls_back_to_no_intent_and_records_why(raw):
    decision = deliberate(CannedModel(raw), "ada", "You are Ada.")

    assert decision.intent is None
    assert decision.raw_output == raw
    assert decision.error


def test_model_is_given_the_action_contract_schema():
    model = CannedModel('{"action": "gather", "node_id": "bush", "amount": 3}')

    deliberate(model, "ada", "You are Ada.")

    assert model.schema == AgentAction.model_json_schema()
