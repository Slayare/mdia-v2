"""Event journal: the canonical, append-only record of world truth."""

from mdia.domain.events import ActionResolved


class InMemoryJournal:
    def __init__(self) -> None:
        self._events: list[ActionResolved] = []

    def append(self, event: ActionResolved) -> None:
        self._events.append(event)

    def events(self) -> tuple[ActionResolved, ...]:
        return tuple(self._events)
