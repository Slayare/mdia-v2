from mdia.domain.events import ActionResolved
from mdia.domain.world import ActionResult, Gather, WorldState
from mdia.persistence.journal import InMemoryJournal
from mdia.simulation.engine import run


# TODO: move into a shared test fixtures module once a second test needs it (likely roadmap step 4).
class ScriptedDecider:
    """Fake decider that proposes a fixed sequence of actions, one per tick."""

    def __init__(self, actions: list[Gather]) -> None:
        self._actions = iter(actions)

    def decide(self, agent_id: str) -> Gather:
        return next(self._actions)


def test_run_resolves_each_proposed_action_and_journals_it_by_tick():
    state = WorldState(stocks={"bush": 5}, inventories={"ada": 0})
    first, too_much, rest = Gather("ada", "bush", 3), Gather("ada", "bush", 3), Gather("ada", "bush", 2)
    journal = InMemoryJournal()

    final = run(state, "ada", ScriptedDecider([first, too_much, rest]), journal, ticks=3)

    assert final == WorldState(stocks={"bush": 0}, inventories={"ada": 5})
    assert journal.events() == (
        ActionResolved(0, first, ActionResult(accepted=True)),
        ActionResolved(1, too_much, ActionResult(accepted=False, reason="amount outside available stock")),
        ActionResolved(2, rest, ActionResult(accepted=True)),
    )
