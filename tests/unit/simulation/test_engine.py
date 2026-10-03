import hashlib

from mdia.cognition.context import build_prompt
from mdia.contracts.observations import Observation
from mdia.contracts.run import RunContext
from mdia.domain.agents.identity import Ontolette
from mdia.domain.events import ActionResolved
from mdia.domain.world import ActionResult, Gather, WorldState
from mdia.persistence.journal import InMemoryJournal
from mdia.simulation.engine import run, take_turn

from fakes import CannedModel, ScriptedModel, SteppingClock

Luma = Ontolette(id="luma", name="Luma", traits=["curious"], goals=["find food"], beliefs=[])
RUN = RunContext(run_id="run-1", seed=7, model_id="gpt-oss:20b", config_version="test")


def _gather(amount: int) -> str:
    return f'{{"action": "gather", "node_id": "bush", "amount": {amount}}}'


def test_run_takes_a_turn_per_tick_each_seeing_the_world_the_last_one_left():
    state = WorldState(stocks={"bush": 5}, inventories={"luma": 0})
    model = ScriptedModel(_gather(3), _gather(3), _gather(2))
    journal = InMemoryJournal()

    final, records = run(state, Luma, model, journal, ticks=3, context=RUN)

    assert final == WorldState(stocks={"bush": 0}, inventories={"luma": 5})
    assert journal.events() == (
        ActionResolved(0, Gather("luma", "bush", 3), ActionResult(accepted=True)),
        ActionResolved(
            1, Gather("luma", "bush", 3), ActionResult(accepted=False, reason="amount outside available stock")
        ),
        ActionResolved(2, Gather("luma", "bush", 2), ActionResult(accepted=True)),
    )
    assert [(r.tick, r.observation.inventory) for r in records] == [(0, 0), (1, 3), (2, 3)]


def test_run_reports_each_turn_before_asking_the_model_about_the_next():
    log: list[str] = []
    scripted = ScriptedModel(_gather(1), _gather(1))

    class LoggingModel:
        def generate(self, prompt, schema):
            log.append("model asked")
            return scripted.generate(prompt, schema)

    state = WorldState(stocks={"bush": 5}, inventories={"luma": 0})

    def report(record):
        log.append(f"tick {record.tick} reported")

    run(state, Luma, LoggingModel(), InMemoryJournal(), ticks=2, context=RUN, on_turn=report)

    assert log == ["model asked", "tick 0 reported", "model asked", "tick 1 reported"]


def test_turn_resolves_a_usable_decision_journals_it_and_records_what_luma_experienced():
    state = WorldState(stocks={"bush": 5}, inventories={"luma": 0})
    raw = '{"action": "gather", "node_id": "bush", "amount": 3}'
    journal = InMemoryJournal()

    new_state, record = take_turn(
        state, Luma, CannedModel(raw), journal, tick=4, run=RUN, clock=SteppingClock(10.0, 12.5)
    )

    gather, accepted = Gather("luma", "bush", 3), ActionResult(accepted=True)
    assert new_state == WorldState(stocks={"bush": 2}, inventories={"luma": 3})
    assert journal.events() == (ActionResolved(4, gather, accepted),)
    observation = Observation(inventory=0, stocks={"bush": 5})
    prompt = build_prompt(Luma, observation)
    assert record.model_dump() == {
        "run": RUN.model_dump(),
        "tick": 4,
        "agent_id": "luma",
        "identity_version": 1,
        "observation": observation.model_dump(),
        "prompt": prompt,
        "prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "raw_output": raw,
        "latency_s": 2.5,
        "intent": {"agent_id": "luma", "node_id": "bush", "amount": 3},
        "result": {"accepted": True, "reason": None},
        "error": None,
    }


def test_turn_with_unusable_output_leaves_the_world_and_journal_untouched_and_records_why():
    state = WorldState(stocks={"bush": 5}, inventories={"luma": 0})
    raw = "I think I'll rest."
    journal = InMemoryJournal()

    new_state, record = take_turn(state, Luma, CannedModel(raw), journal, tick=4, run=RUN)

    assert new_state == state
    assert journal.events() == ()
    assert (record.raw_output, record.intent, record.result) == (raw, None, None)
    assert record.error
