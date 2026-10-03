from mdia.contracts.observations import Observation
from mdia.domain.world import WorldState
from mdia.simulation.perception import observe


def test_agent_observes_its_own_inventory_and_stocks_but_not_other_agents_inventories():
    state = WorldState(stocks={"bush": 5, "tree": 2}, inventories={"luma": 3, "bob": 7})

    assert observe(state, "luma") == Observation(inventory=3, stocks={"bush": 5, "tree": 2})
