from mdia.contracts.observations import Observation
from mdia.contracts.run import RunContext
from mdia.contracts.trajectory import TurnRecord
from mdia.domain.world import ActionResult, Gather
from mdia.runtime.display import format_turn


def _record(intent: Gather | None, result: ActionResult | None, error: str | None = None) -> TurnRecord:
    return TurnRecord(
        run=RunContext(run_id="run-1", seed=7, model_id="gpt-oss:20b", config_version="test"),
        tick=1,
        agent_id="luma",
        identity_version=1,
        observation=Observation(inventory=5, stocks={"bush": 0, "tree": 2}),
        prompt="You are Luma.",
        raw_output="...",
        latency_s=2.34,
        intent=intent,
        result=result,
        error=error,
    )


def test_accepted_turn_shows_what_was_seen_proposed_and_how_long_it_took():
    line = format_turn(_record(Gather("luma", "tree", 2), ActionResult(accepted=True)))

    assert line == "tick 1 | luma | carrying 5; bush 0, tree 2 | gather 2 from tree | accepted | 2.3s"


def test_rejected_turn_shows_the_world_reason():
    line = format_turn(_record(Gather("luma", "bush", 0), ActionResult(accepted=False, reason="amount outside available stock")))

    assert line == (
        "tick 1 | luma | carrying 5; bush 0, tree 2 | gather 0 from bush"
        " | rejected: amount outside available stock | 2.3s"
    )


def test_fallback_turn_shows_no_usable_action_and_the_first_line_of_the_error():
    line = format_turn(_record(None, None, error="1 validation error for AgentAction\n  Invalid JSON"))

    assert line == (
        "tick 1 | luma | carrying 5; bush 0, tree 2 | no usable action"
        " | 1 validation error for AgentAction | 2.3s"
    )
