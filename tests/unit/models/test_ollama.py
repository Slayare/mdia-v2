import json

import httpx
import pytest

from mdia.models.adapters.ollama import OllamaModel

SCHEMA = {"type": "object", "properties": {"action": {"type": "string"}}}


def test_generate_sends_prompt_and_schema_and_returns_the_response_text():
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"model": "gpt-oss:20b", "response": '{"action": "gather"}', "done": True})

    client = httpx.Client(base_url="http://ollama.test", transport=httpx.MockTransport(handler))

    reply = OllamaModel(client, "gpt-oss:20b").generate("You are Ada.", SCHEMA)

    assert reply == '{"action": "gather"}'
    assert requests[0].url.path == "/api/generate"
    assert json.loads(requests[0].content) == {
        "model": "gpt-oss:20b",
        "prompt": "You are Ada.",
        "format": SCHEMA,
        "stream": False,
    }


def test_server_errors_are_raised_rather_than_returned_as_text():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"error": "model 'gpt-oss:20b' not found"})

    client = httpx.Client(base_url="http://ollama.test", transport=httpx.MockTransport(handler))

    with pytest.raises(httpx.HTTPStatusError):
        OllamaModel(client, "gpt-oss:20b").generate("You are Ada.", SCHEMA)
