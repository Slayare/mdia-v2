import pytest

from mdia.domain.world import Gather, WorldState
from mdia.simulation.rules import resolve


def test_gather_moves_amount_from_node_to_agent():
    state = WorldState(stocks={"bush": 5}, inventories={"luma": 0})

    new_state, result = resolve(state, Gather(agent_id="luma", node_id="bush", amount=3))

    assert result.accepted
    assert new_state == WorldState(stocks={"bush": 2}, inventories={"luma": 3})


@pytest.mark.parametrize("amount", [6, 0, -1])
def test_gather_outside_available_stock_is_rejected_and_changes_nothing(amount):
    state = WorldState(stocks={"bush": 5}, inventories={"luma": 0})

    new_state, result = resolve(state, Gather(agent_id="luma", node_id="bush", amount=amount))

    assert not result.accepted
    assert new_state == state


def test_dead_agent_cannot_act():
    state = WorldState(stocks={"bush": 5}, inventories={"luma": 0}, dead=frozenset({"luma"}))

    new_state, result = resolve(state, Gather(agent_id="luma", node_id="bush", amount=3))

    assert not result.accepted
    assert new_state == state
