from mdia.domain.events import ActionResolved
from mdia.domain.world import ActionResult, Gather
from mdia.persistence.journal import InMemoryJournal


def test_journal_returns_events_in_append_order():
    accepted = ActionResolved(Gather("ada", "bush", 3), ActionResult(accepted=True))
    rejected = ActionResolved(
        Gather("ada", "bush", 9), ActionResult(accepted=False, reason="amount outside available stock")
    )
    journal = InMemoryJournal()

    journal.append(accepted)
    journal.append(rejected)

    assert journal.events() == (accepted, rejected)
