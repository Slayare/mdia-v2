"""World rules: resolve proposed actions into consequences."""

from mdia.domain.world import ActionResult, Gather, WorldState


def resolve(state: WorldState, action: Gather) -> tuple[WorldState, ActionResult]:
    if action.agent_id in state.dead:
        return state, ActionResult(accepted=False, reason="agent is dead")

    available = state.stocks[action.node_id]
    if not 0 < action.amount <= available:
        return state, ActionResult(accepted=False, reason="amount outside available stock")

    stocks = {**state.stocks, action.node_id: available - action.amount}
    inventories = {
        **state.inventories,
        action.agent_id: state.inventories[action.agent_id] + action.amount,
    }
    return WorldState(stocks=stocks, inventories=inventories), ActionResult(accepted=True)
