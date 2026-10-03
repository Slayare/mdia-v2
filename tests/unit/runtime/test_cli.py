import io

from mdia.runtime.cli import main

from fakes import ScriptedModel


def test_cli_runs_the_requested_ticks_and_prints_each_turn():
    gather = '{"action": "gather", "node_id": "bush", "amount": 2}'
    out = io.StringIO()

    exit_code = main(["--ticks", "2"], model=ScriptedModel(gather, gather), out=out)

    lines = out.getvalue().splitlines()
    assert exit_code == 0
    assert [line.split(" | ")[:2] for line in lines] == [["tick 0", "luma"], ["tick 1", "luma"]]
