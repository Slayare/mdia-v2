"""Opt-in: needs a local Ollama with gpt-oss:20b. Run with MDIA_OLLAMA_TESTS=1."""

import os

import httpx
import pytest

from mdia.cognition.deliberation import deliberate
from mdia.models.adapters.ollama import OllamaModel

pytestmark = pytest.mark.skipif(
    os.environ.get("MDIA_OLLAMA_TESTS") != "1", reason="set MDIA_OLLAMA_TESTS=1 to call local Ollama"
)


def test_local_model_proposes_an_action_that_satisfies_the_contract():
    client = httpx.Client(base_url="http://localhost:11434", timeout=300)
    prompt = (
        "You are Ada. You are hungry. A berry bush with id 'bush' is in front of you. "
        "Choose one action and reply as JSON."
    )

    decision = deliberate(OllamaModel(client, "gpt-oss:20b"), "ada", prompt)

    assert decision.error is None, decision.raw_output
    assert decision.intent is not None and decision.intent.agent_id == "ada"
