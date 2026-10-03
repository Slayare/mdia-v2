"""Command line: run a tiny world with one Ontolette against the local model and watch each turn."""

import argparse
import sys
import uuid
from typing import TextIO

import httpx

from mdia.contracts.run import RunContext
from mdia.domain.agents.identity import Ontolette
from mdia.domain.world import WorldState
from mdia.models.adapters.ollama import OllamaModel
from mdia.models.ports import LanguageModel
from mdia.persistence.journal import InMemoryJournal
from mdia.runtime.display import format_turn
from mdia.simulation.engine import run

LUMA = Ontolette(
    id="luma",
    name="Luma",
    traits=["curious", "cautious"],
    goals=["find food"],
    beliefs=["the tree is barren"],
)
TINY_WORLD = WorldState(stocks={"bush": 5, "tree": 2}, inventories={"luma": 0})


def main(argv: list[str] | None = None, model: LanguageModel | None = None, out: TextIO = sys.stdout) -> int:
    parser = argparse.ArgumentParser(prog="mdia", description=__doc__)
    parser.add_argument("--ticks", type=int, default=5)
    parser.add_argument("--model", default="gpt-oss:20b", help="Ollama model id")
    parser.add_argument("--ollama-url", default="http://localhost:11434")
    parser.add_argument("--seed", type=int, default=0, help="recorded on each turn record")
    args = parser.parse_args(argv)

    if model is None:
        model = OllamaModel(httpx.Client(base_url=args.ollama_url, timeout=300), args.model)
    context = RunContext(run_id=uuid.uuid4().hex[:8], seed=args.seed, model_id=args.model, config_version="dev")

    def show(record):
        print(format_turn(record), file=out, flush=True)

    run(TINY_WORLD, LUMA, model, InMemoryJournal(), args.ticks, context, on_turn=show)
    return 0
