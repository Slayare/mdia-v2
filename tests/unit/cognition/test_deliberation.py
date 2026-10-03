import pytest

from mdia.cognition.deliberation import deliberate
from mdia.contracts.actions import AgentAction
from mdia.domain.world import Gather

from fakes import CannedModel, SteppingClock


def test_valid_model_output_becomes_a_decision_with_an_intent():
    raw = '{"action": "gather", "node_id": "bush", "amount": 3}'

    decision = deliberate(CannedModel(raw), "luma", "You are Luma.")

    assert (decision.intent, decision.raw_output, decision.error) == (Gather("luma", "bush", 3), raw, None)


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


def test_decision_records_how_long_the_model_took():
    model = CannedModel('{"action": "gather", "node_id": "bush", "amount": 3}')

    decision = deliberate(model, "luma", "You are Luma.", clock=SteppingClock(10.0, 12.5))

    assert decision.latency_s == 2.5
