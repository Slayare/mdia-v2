import pytest

from mdia.cognition.deliberation import Decision, deliberate
from mdia.contracts.actions import AgentAction
from mdia.domain.world import Gather

from fakes import CannedModel


def test_valid_model_output_becomes_a_decision_with_an_intent():
    raw = '{"action": "gather", "node_id": "bush", "amount": 3}'

    decision = deliberate(CannedModel(raw), "luma", "You are Luma.")

    assert decision == Decision(intent=Gather("luma", "bush", 3), raw_output=raw)


@pytest.mark.parametrize(
    "raw",
    [
        "I think I'll gather some berries.",
        '{"action": "fly", "node_id": "bush", "amount": 3}',
        '{"action": "gather", "node_id": "bush", "amount": 3, "agent_id": "bob"}',
    ],
)
def test_unusable_model_output_falls_back_to_no_intent_and_records_why(raw):
    decision = deliberate(CannedModel(raw), "luma", "You are Luma.")

    assert decision.intent is None
    assert decision.raw_output == raw
    assert decision.error


def test_model_is_given_the_action_contract_schema():
    model = CannedModel('{"action": "gather", "node_id": "bush", "amount": 3}')

    deliberate(model, "luma", "You are Luma.")

    assert model.schema == AgentAction.model_json_schema()
